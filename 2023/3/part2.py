import re

total = 0

with open("input", 'r') as f:
    lines = f.readlines()
    f.seek(0)
    
    line_length = len(lines[0])
    
    partnumbers = []
    for n in re.finditer('\d+', f.read()):
        partnumbers.append((n.start() // line_length, 
                            n.start() % line_length, 
                            n.end() % line_length))
    
    stars: dict[tuple, list[int]] = {}
    for pnum in partnumbers:
        #print(pnum, lines[pnum[0]][pnum[1]:pnum[2]])
        tl = (pnum[0] - 1 if pnum[0] > 0 else pnum[0], 
              pnum[1] - 1 if pnum[1] > 0 else pnum[1])
        br = (pnum[0] + 1 if pnum[0] < len(lines)-1 else pnum[0], 
              pnum[2] + 1 if pnum[2] < line_length-1 else pnum[2])
        part = False
        for y in range(tl[0], br[0]+1):
            for x in range(tl[1], br[1]):
                if lines[y][x] == '*' and (y, x) in stars:
                    stars[(y, x)].append(int(lines[pnum[0]][pnum[1]:pnum[2]]))
                elif lines[y][x] == '*':
                    stars[(y, x)] = [int(lines[pnum[0]][pnum[1]:pnum[2]])]

    for pos, values in stars.items():
        if len(values) == 2:
            total += values[0] * values[1]

print(total)
