nums = []
for i in range(3):
    nums.append(int(input(f"Enter number {i+1}: ")))
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest number is:", largest)
