with open("input", "r") as f:
    grid = []
    for line in f.readlines():
        row = []
        line = line.strip()
        for ch in line:
            row.append(ch)
        grid.append(row)


def findTrees(xstep, ystep, grid):
    count = 0
    y = ystep
    x = xstep
    while y < len(grid):
        if grid[y][x % len(grid[0])] == '#':
            count += 1
            print('T')
        else:
            print('N')
        x += xstep
        y += ystep
    print(count)


findTrees(3, 1, grid)
