def find_defaulters(attendance):
    defaulters = [name for name, percent in attendance.items() if percent < 75]
    return defaulters
n = int(input("Enter number of students: "))
attendance = {}
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    percent = float(input(f"Enter attendance % for {name}: "))
    attendance[name] = percent
defaulters = find_defaulters(attendance)
if defaulters:
    print("Defaulters (attendance < 75%):", defaulters)
else:
    print("No defaulters!")
