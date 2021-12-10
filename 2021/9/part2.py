grid = []
row = []
for i in open("input", 'r').read():
    if i == '\n':
        grid.append(row)
        row = []
    else:
        row.append(int(i))
grid.append(row)

for y in range(len(grid)):
    grid[y].append(9)
    grid[y].insert(0, 9)
grid.append([9]*len(grid[0]))
grid.insert(0, [9]*len(grid[0]))

def youknowwhattimeitis(y, x, start, seen):
    size = 0
    if grid[y][x] < start or grid[y][x] == 9:
        return size, (0, 0)
    if grid[y][x] - start == 1:
        size = 0 if (y, x) in seen else 1
        res = youknowwhattimeitis(y, x + 1, grid[y][x], seen)
        size += res[0]; seen.append(res[1])
        res = youknowwhattimeitis(y, x - 1, grid[y][x], seen)
        size += res[0]; seen.append(res[1])
        res = youknowwhattimeitis(y + 1, x, grid[y][x], seen)
        size += res[0]; seen.append(res[1])
        res = youknowwhattimeitis(y - 1, x, grid[y][x], seen)
        size += res[0]; seen.append(res[1])
    return size, (y, x) if size else (0, 0)

basins = []
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[y])-1):
        neighbours = [grid[y][x], grid[y][x + 1], grid[y][x - 1], grid[y + 1][x], grid[y - 1][x]]
        if min(neighbours) == grid[y][x] and max(neighbours) != grid[y][x]:
            size = 1
            seen = [(y, x)]
            res = youknowwhattimeitis(y, x + 1, grid[y][x], seen)
            size += res[0]; seen.append(res[1])
            res = youknowwhattimeitis(y, x - 1, grid[y][x], seen)
            size += res[0]; seen.append(res[1])
            res = youknowwhattimeitis(y + 1, x, grid[y][x], seen)
            size += res[0]; seen.append(res[1])
            res = youknowwhattimeitis(y - 1, x, grid[y][x], seen)
            size += res[0]; seen.append(res[1])
            basins.append(size)

basins.sort()
print(basins[-3]*basins[-2]*basins[-1])
