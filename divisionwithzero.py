try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero ")
except ValueError:
    print("Error: Invalid input ")
else:
    print(f"{a} / {b} = {result}")
