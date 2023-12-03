import math


def recursiontime(i, f, days):
    newfish = math.floor((days - 7*i - f - 3) / 7)
    if newfish <= 0:
        return 0
    for m in range(i+1, newfish+1):
        newfish += recursiontime(m, f, days)
    return newfish

days = 18
fish = []
for f in open("input", 'r').read().strip().split(sep=','):
    fish.append(int(f))

total = len(fish)
for f in fish:
    # we do a little maths
    newfish = math.floor((days-f) / 7) + 1
    for i in range(newfish):
        newfish += recursiontime(i, f, days)
    total += newfish

print(total)
