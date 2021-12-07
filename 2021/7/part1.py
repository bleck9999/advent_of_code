points = [int(x) for x in open("input", 'r').read().strip().split(sep=',')]
points.sort()
totals = []
for i in range(points[0], points[-1]):
    total = 0
    for p in points:
        total += abs(p-i)
    totals.append(total)

print(min(totals))
