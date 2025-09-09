n = int(input("Enter number of items: "))
items = {}
for i in range(n):
    name = input(f"Enter name of item {i+1}: ")
    price = float(input(f"Enter price of {name}: "))
    items[name] = price
total = sum(items.values())
print("Items:", items)
print("Total bill: ₹", total)
