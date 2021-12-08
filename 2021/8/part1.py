parsed = [x.split(sep=' | ') for x in open("input", 'r').read().split(sep='\n')]
total = 0
for l in parsed:
    nums = {}
    for seq in l[0].split(sep=' '):
        seq = ''.join(sorted(seq.strip()))
        nums[seq] = '7' if len(seq) == 3 else \
            '1' if len(seq) == 2 else \
            '8' if len(seq) == 7 else \
            '4' if len(seq) == 4 else "?"

    for val in l[1].split(sep=' '):
        val = ''.join((sorted(val.strip())))
        if nums[val] != '?':
            total += 1

print(total)
