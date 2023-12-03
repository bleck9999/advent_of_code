import re

symbols = "=-*/+$&%#@"
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
    
    for pnum in partnumbers:
        #print(pnum, lines[pnum[0]][pnum[1]:pnum[2]])
        tl = (pnum[0] - 1 if pnum[0] > 0 else pnum[0], 
              pnum[1] - 1 if pnum[1] > 0 else pnum[1])
        br = (pnum[0] + 1 if pnum[0] < len(lines)-1 else pnum[0], 
              pnum[2] + 1 if pnum[2] < line_length-1 else pnum[2])
        part = False
        for y in range(tl[0], br[0]+1):
            for x in range(tl[1], br[1]):
                if lines[y][x] in symbols:
                    part = True
        if part:
            total += int(lines[pnum[0]][pnum[1]:pnum[2]])

print(total)
