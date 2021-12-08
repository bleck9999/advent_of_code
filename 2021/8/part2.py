parsed = [x.split(sep=' | ') for x in open("input", 'r').read().split(sep='\n')]
total = 0


def overlay(n1, n2):
    unique1 = ""
    commons = ""
    for ch in n1:
        if ch not in n2:
            unique1 += ch
        else:
            commons += ch
    unique2 = ""
    for ch in n2:
        if ch not in n1:
            unique2 += ch
    return unique1, unique2, commons

for l in parsed:
    pieces = {}
    nums = {}
    seqs = [''.join(sorted(seq.strip())) for seq in l[0].split(sep=' ')]
    for seq in seqs:
        if len(seq) in (3, 2, 7, 4):
            nums[7 if len(seq) == 3 else
                 1 if len(seq) == 2 else
                 8 if len(seq) == 7 else
                 4 if len(seq) == 4 else "fugmachine"] = seq
    pieces["CU"] = overlay(nums[1], nums[7])[1]
    for seq in seqs:
        if len(seq) == 5 and overlay(seq, nums[7])[2] == nums[7]:
            nums[3] = seq

    middles = overlay(nums[3], nums[7])[0]
    pieces["CC"] = overlay(nums[3], nums[4])[2].replace(nums[1][0], '').replace(nums[1][1], '')
    pieces["CL"] = middles[0] if middles[0] != pieces["CC"] else middles[1]

    for seq in seqs:
        if len(seq) == 6:
            if overlay(nums[3], seq)[2] == nums[3]:
                nums[9] = seq
                pieces["LU"] = overlay(nums[3], nums[9])[1]
                pieces["LL"] = overlay(nums[8], nums[9])[0]
    for seq in seqs:
        if len(seq) == 6:
            if overlay(nums[3], seq)[2] != nums[3]:
                if pieces["CC"] not in seq:
                    nums[0] = seq
                    continue
                nums[6] = seq
                pieces["RU"] = overlay(nums[3], nums[6])[0]
                pieces["RL"] = nums[1].replace(pieces["RU"], '')
    nums[5] = ''.join(sorted(pieces["CU"] + pieces["LU"] + pieces["CC"] + pieces["RL"] + pieces["CL"]))
    nums[2] = ''.join(sorted(pieces["CU"] + pieces["RU"] + pieces["CC"] + pieces["LL"] + pieces["CL"]))

    nums = {k: v for v, k in nums.items()}

    for i, val in enumerate(l[1].split(sep=' ')):
        val = ''.join((sorted(val.strip())))
        total += nums[val] * 10**(3-i)

print(total)
