found = False
index = 2
target = 0

while not found:
    nums = []
    for i in range(1, 7):
        nums.append(sorted(list(str(i*index))))
    
    yes = 0
    for i in nums:
        if nums[0] == i:
            yes += 1
    if yes == len(nums):
        target = index
        found = True
    index += 1

print(target) # 142857

