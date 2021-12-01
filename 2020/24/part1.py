instructions = []
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        instructions.append(line)

black = []
for inst in instructions:
    ewpos = 0
    nspos = 0
    for action in inst:
        if action == 'n':
            nspos += 1
        elif action == 'e':
            ewpos += 1
        elif action == 's':
            nspos -= 1
        elif action == 'w':
            ewpos -= 1
    if [nspos, ewpos] in black:
        black.pop(black.index([nspos, ewpos]))
    else:
        black.append([nspos, ewpos])

print(len(black))
