n = int(input("How many numbers? "))
nums = []
for i in range(n):
    nums.append(int(input(f"Enter number {i+1}: ")))
smallest = nums[0]
largest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("Smallest number:", smallest)
print("Largest number:", largest)
