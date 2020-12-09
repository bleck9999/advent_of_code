nums = []
with open("input", "r") as f:
    for line in f.readlines():
        nums.append(int(line.strip()))

for i in range(len(nums)):
    prev25 = nums[i-25:i]

    # do you want
    sum_flag = False
    for num in prev25:
        if (nums[i] - num) in prev25:
            sum_flag = True
    if not sum_flag:
        print(f"Found at position {i}: {nums[i]}")
