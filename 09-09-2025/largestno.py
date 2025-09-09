def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
nums = []  
n = int(input("How many numbers? "))
for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    nums.append(value)
print("The largest number is:", find_largest(nums))
