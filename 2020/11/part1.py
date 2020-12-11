grid = []
with open("input", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        grid.append([ch for ch in line])


while True:
    count = 0
    oldcount = 0
    for row in grid:
        for ch in row:
            if ch == '#':
                oldcount += 1

    newgrid = []
    for i in range(len(grid)):
        row = grid[i]
        newgrid.append([])
        for j in range(len(row)):
            newgrid[i].append('.')
            ch = row[j]
            occupied = 0
            if ch == 'L' or ch == '#':
                i0 = bool(i > 0)
                j0 = bool(j > 0)
                imax = bool(i < len(grid)-1)
                jmax = bool(j < len(row)-1)
                if j0:
                    if grid[i][j-1] == '#':
                        occupied += 1
                    if i0:
                        if j0:
                            if grid[i-1][j-1] == '#':
                                occupied += 1
                        if jmax:
                            if grid[i-1][j+1] == '#':
                                occupied += 1
                    if jmax:
                        if grid[i][j+1] == '#':
                            occupied += 1
                elif jmax:
                    if grid[i][j+1] == '#':
                        occupied += 1
                    if i0:
                        if grid[i-1][j+1] == '#':
                            occupied += 1
                if i0:
                    if grid[i-1][j] == '#':
                        occupied += 1
                    if imax:
                        if j0:
                            if grid[i+1][j-1] == '#':
                                occupied += 1
                        if jmax:
                            if grid[i+1][j+1] == '#':
                                occupied += 1
                        if grid[i+1][j] == '#':
                            occupied += 1
                elif imax:
                    if grid[i+1][j] == '#':
                        occupied += 1
                    if j0:
                        if grid[i + 1][j - 1] == '#':
                            occupied += 1
                    if jmax:
                        if grid[i + 1][j + 1] == '#':
                            occupied += 1

                if occupied == 0 and ch == 'L':
                    newgrid[i][j] = '#'
                elif occupied >= 4 and ch == '#':
                    newgrid[i][j] = 'L'
                else:
                    newgrid[i][j] = ch

    grid = newgrid[:]
    for row in grid:
        for ch in row:
            if ch == '#':
                count += 1

    print(oldcount, "->", count)
    if count == oldcount:
        break

print(count)
