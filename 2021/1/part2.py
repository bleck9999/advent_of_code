prev = []
lines = []
for l in open("input", 'r').read().splitlines():
    prev.append(int(l))
    if len(prev) < 3:
        continue
    elif len(prev) == 3:
        lines.append(sum(prev))
        prev.pop(0)
    else:
        raise Exception("fug")

prev = 0
increased = -1  # account for l1 having nothing to increase from
for l in lines:
    l = int(l)
    if l > prev:
        increased += 1
    prev = l
print(increased)
