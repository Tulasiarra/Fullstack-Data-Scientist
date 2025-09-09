def calculator(a, b, op):
    if op == '+': 
        return a + b
    if op == '-': 
        return a - b
    if op == '*': 
        return a * b
    if op == '/': 
        if b!=0:
            return a/b
        else:
            return "cannot divide by zero"
    else:
        "invalid operation"
print(calculator(1,2,"+"))
print(calculator(10,5,"-"))
print(calculator(1,2,"*"))
print(calculator(20,0,"/"))
print(calculator(20,2,"/"))

