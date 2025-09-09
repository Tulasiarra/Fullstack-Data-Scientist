from collections import Counter
def find_duplicates(names):
    count = Counter(names) 
    return [name for name, freq in count.items() if freq > 1]
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)
duplicates = find_duplicates(students)
if duplicates:
    print("Duplicate names:", duplicates)
else:
    print("No duplicates found")
