def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest (%): "))
t = float(input("Enter Time (in years): "))
si = simple_interest(p, r, t)
print("Simple Interest =", si)
