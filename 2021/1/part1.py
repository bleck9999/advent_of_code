prev = 0
increased = -1  # account for l1 having nothing to increase from
for l in open("input", 'r').read().splitlines():
    l = int(l)
    if l > prev:
        increased += 1
    prev = l
print(increased)
