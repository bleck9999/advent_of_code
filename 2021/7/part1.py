points = [int(x) for x in open("input", 'r').read().strip().split(sep=',')]
points.sort()
totals = []
for i in range(points[0], points[-1]):
    total = 0
    for p in points:
        total += sum(x for x in range(1, abs(p-i)+1))
    totals.append(total)

print(min(totals))
