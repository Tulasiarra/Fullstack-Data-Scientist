# library.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
if not url or not key:
    print(" Please set SUPABASE_URL and SUPABASE_KEY in .env")
    exit(1)

supabase: Client = create_client(url, key)

# ---------------------------
# CRUD FUNCTIONS
# ---------------------------
def add_member(name, email):
    res = supabase.table("members").insert({"name": name, "email": email}).execute()
    return res.data

def add_book(title, author, category, stock=1):
    res = supabase.table("books").insert(
        {"title": title, "author": author, "category": category, "stock": stock}
    ).execute()
    return res.data

def list_books():
    res = supabase.table("books").select("*").execute()
    return res.data

def search_books(keyword):
    res = supabase.table("books").select("*").ilike("title", f"%{keyword}%").execute()
    return res.data

def update_book_stock(book_id, new_stock):
    res = supabase.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return res.data

def update_member_email(member_id, new_email):
    res = supabase.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    return res.data

def delete_member(member_id):
    res = supabase.table("members").delete().eq("member_id", member_id).execute()
    return res.data

def delete_book(book_id):
    res = supabase.table("books").delete().eq("book_id", book_id).execute()
    return res.data

# ---------------------------
# TRANSACTIONS
# ---------------------------
def borrow_book(member_id, book_id):
    # Check stock
    book = supabase.table("books").select("stock").eq("book_id", book_id).single().execute()
    if not book.data:
        return {"error": "Book not found"}
    if book.data["stock"] <= 0:
        return {"error": "Book not available"}

    # Decrease stock
    supabase.table("books").update({"stock": book.data["stock"] - 1}).eq("book_id", book_id).execute()
    # Insert borrow record
    res = supabase.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()
    return res.data

def return_book(record_id):
    rec = supabase.table("borrow_records").select("*").eq("record_id", record_id).single().execute()
    if not rec.data:
        return {"error": "Record not found"}
    if rec.data["return_date"]:
        return {"error": "Already returned"}

    # Update return date
    supabase.table("borrow_records").update({"return_date": "now()"}).eq("record_id", record_id).execute()
    # Increase stock
    supabase.table("books").update({"stock": 1}).eq("book_id", rec.data["book_id"]).execute()
    return {"success": "Book returned"}

# ---------------------------
# REPORTS
# ---------------------------
def top_borrowed():
    query = """
    SELECT b.title, COUNT(br.record_id) AS borrowed_count
    FROM books b
    JOIN borrow_records br ON b.book_id = br.book_id
    GROUP BY b.title
    ORDER BY borrowed_count DESC
    LIMIT 5;
    """
    res = supabase.rpc("exec_sql", {"sql": query}).execute()
    return res.data if res.data else []

def overdue_members(days=14):
    query = f"""
    SELECT m.name, m.email, b.title, br.borrow_date
    FROM borrow_records br
    JOIN members m ON br.member_id = m.member_id
    JOIN books b ON br.book_id = b.book_id
    WHERE br.return_date IS NULL AND br.borrow_date < NOW() - interval '{days} days';
    """
    res = supabase.rpc("exec_sql", {"sql": query}).execute()
    return res.data if res.data else []

# ---------------------------
# UTILS
# ---------------------------
def pretty(rows):
    if not rows:
        print("No results.")
        return
    if isinstance(rows, dict):
        rows = [rows]
    if isinstance(rows, list) and rows and isinstance(rows[0], dict):
        headers = list(rows[0].keys())
        table = [list(r.values()) for r in rows]
        print(tabulate(table, headers=headers, tablefmt="psql"))
    else:
        print(rows)

# ---------------------------
# CLI
# ---------------------------
def main():
    while True:
        print("""
📚 Library CLI Menu
1. Register Member
2. Add Book
3. List Books
4. Search Books
5. Update Book Stock
6. Update Member Email
7. Delete Member
8. Delete Book
9. Borrow Book
10. Return Book
11. Report: Top 5 Borrowed
12. Report: Overdue Members
0. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            pretty(add_member(name, email))

        elif choice == "2":
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            stock = int(input("Enter stock: "))
            pretty(add_book(title, author, category, stock))

        elif choice == "3":
            pretty(list_books())

        elif choice == "4":
            kw = input("Enter keyword: ")
            pretty(search_books(kw))

        elif choice == "5":
            bid = int(input("Enter book ID: "))
            stock = int(input("Enter new stock: "))
            pretty(update_book_stock(bid, stock))

        elif choice == "6":
            mid = int(input("Enter member ID: "))
            new_email = input("Enter new email: ")
            pretty(update_member_email(mid, new_email))

        elif choice == "7":
            mid = int(input("Enter member ID: "))
            pretty(delete_member(mid))

        elif choice == "8":
            bid = int(input("Enter book ID: "))
            pretty(delete_book(bid))

        elif choice == "9":
            mid = int(input("Enter member ID: "))
            bid = int(input("Enter book ID: "))
            pretty(borrow_book(mid, bid))

        elif choice == "10":
            rid = int(input("Enter record ID: "))
            pretty(return_book(rid))

        elif choice == "11":
            pretty(top_borrowed())

        elif choice == "12":
            pretty(overdue_members())

        elif choice == "0":
            print("👋 Exiting...")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()

