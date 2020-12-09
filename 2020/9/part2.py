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
        target = nums[i]


def yeyRecursion(start, target, nums):
    if nums[start] > target:
        return
    total = nums[start]
    numrange = [nums[start]]
    for it in range(1, len(nums)-start):
        total += nums[start+it]
        numrange.append(nums[start+it])
        if total > target:
            yeyRecursion(start+1, target, nums)
            return
        elif total == target:
            numrange.sort()
            print(f"Range found: {start}-{start+it}, L+H {numrange[0] + numrange[len(numrange)-1]}")
            return


yeyRecursion(0, target, nums)
