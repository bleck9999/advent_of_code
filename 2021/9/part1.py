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

risk = 0
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[y])-1):
        neighbours = [grid[y][x], grid[y][x + 1], grid[y][x - 1], grid[y + 1][x], grid[y - 1][x]]
        if min(neighbours) == grid[y][x] and max(neighbours) != grid[y][x]:
            risk += grid[y][x] + 1

print(risk)
