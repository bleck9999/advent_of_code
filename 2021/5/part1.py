grid = {}
def addTo(x, y):
    if (x,y) not in grid:
        grid[(x, y)] = 0
    grid[(x, y)] += 1


for l in open("input", 'r').read().splitlines():
    l1, l2 = l.split(sep="->")
    l1 = [int(x) for x in l1.split(sep=',')]
    l2 = [int(x) for x in l2.split(sep=',')]
    if l1[0] == l2[0]:
        pos = l1[0]
        lrange = l1[1] - l2[1]
        for move in range(l1[1] if lrange < 0 else l2[1],
                          l2[1]+1 if lrange < 0 else l1[1]+1):
            addTo(pos, move)
    elif l1[1] == l2[1]:
        pos = l1[1]
        lrange = l1[0] - l2[0]
        for move in range(l1[0] if lrange < 0 else l2[0],
                          (l2[0] + 1) if lrange < 0 else (l1[0] + 1)):
            addTo(move, pos)

positions = []
for pos in grid:
    if grid[pos] >= 2:
        positions.append(pos)

print(len(positions))
