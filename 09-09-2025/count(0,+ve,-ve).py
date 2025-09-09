n = int(input("How many numbers? "))
nums = []
for i in range(n):
    nums.append(int(input(f"Enter number {i+1}: ")))
pos = neg = zero = 0
for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos, "Negative:", neg, "Zero:", zero)
