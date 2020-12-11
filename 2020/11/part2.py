from math import isqrt
grid = []
with open("input", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        grid.append([ch for ch in line])


max_length = isqrt((len(grid[0])) ** 2 + (len(grid)) ** 2) - 1
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
                    # apparently recursion is bad
                    # so have some iteration
                    # not that i thought about doing this with recursion anyway
                    for it in range(1, max_length):
                        y = i
                        x = j-it
                        if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                            break
                        elif grid[y][x] == '#':
                            occupied += 1
                            break
                        elif grid[y][x] == 'L':
                            break
                    if i0:
                        if j0:
                            for it in range(1, max_length):
                                y = i - it
                                x = j - it
                                if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                    break
                                elif grid[y][x] == '#':
                                    occupied += 1
                                    break
                                elif grid[y][x] == 'L':
                                    break
                        if jmax:
                            for it in range(1, max_length):
                                y = i - it
                                x = j + it
                                if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                    break
                                elif grid[y][x] == '#':
                                    occupied += 1
                                    break
                                elif grid[y][x] == 'L':
                                    break
                    if jmax:
                        for it in range(1, max_length):
                            y = i
                            x = j + it
                            if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                break
                            elif grid[y][x] == '#':
                                occupied += 1
                                break
                            elif grid[y][x] == 'L':
                                break
                elif jmax:
                    for it in range(1, max_length):
                        y = i
                        x = j + it
                        if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                            break
                        elif grid[y][x] == '#':
                            occupied += 1
                            break
                        elif grid[y][x] == 'L':
                            break
                    if i0:
                        for it in range(1, max_length):
                            y = i - it
                            x = j + it
                            if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                break
                            elif grid[y][x] == '#':
                                occupied += 1
                                break
                            elif grid[y][x] == 'L':
                                break
                if i0:
                    for it in range(1, max_length):
                        y = i - it
                        x = j
                        if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                            break
                        elif grid[y][x] == '#':
                            occupied += 1
                            break
                        elif grid[y][x] == 'L':
                            break
                    if imax:
                        if j0:
                            for it in range(1, max_length):
                                y = i + it
                                x = j - it
                                if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                    break
                                elif grid[y][x] == '#':
                                    occupied += 1
                                    break
                                elif grid[y][x] == 'L':
                                    break
                        if jmax:
                            for it in range(1, max_length):
                                y = i + it
                                x = j + it
                                if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                    break
                                elif grid[y][x] == '#':
                                    occupied += 1
                                    break
                                elif grid[y][x] == 'L':
                                    break
                        for it in range(1, max_length):
                            y = i + it
                            x = j
                            if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                break
                            elif grid[y][x] == '#':
                                occupied += 1
                                break
                            elif grid[y][x] == 'L':
                                break
                elif imax:
                    for it in range(1, max_length):
                        y = i + it
                        x = j
                        if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                            break
                        elif grid[y][x] == '#':
                            occupied += 1
                            break
                        elif grid[y][x] == 'L':
                            break
                    if j0:
                        for it in range(1, max_length):
                            y = i + it
                            x = j - it
                            if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                break
                            elif grid[y][x] == '#':
                                occupied += 1
                                break
                            elif grid[y][x] == 'L':
                                break
                    if jmax:
                        for it in range(1, max_length):
                            y = i + it
                            x = j + it
                            if (y >= len(grid) or x >= len(row)) or (y < 0 or x < 0):
                                break
                            elif grid[y][x] == '#':
                                occupied += 1
                                break
                            elif grid[y][x] == 'L':
                                break

                if occupied == 0 and ch == 'L':
                    newgrid[i][j] = '#'
                elif occupied >= 5 and ch == '#':
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
