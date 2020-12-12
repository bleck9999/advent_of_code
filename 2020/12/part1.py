instructions = []
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        instructions.append(line)


def rotate(start, amount, direction):
    r90 = {
        'E': 'S',
        'S': 'W',
        'W': 'N',
        'N': 'E'
    }
    rl180 = {
        'E': 'W',
        'W': 'E',
        'N': 'S',
        'S': 'N'
    }
    l90 = {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E'
    }
    if amount == "180":
        return rl180[start]
    elif direction == 'R':
        if amount == "90":
            return r90[start]
        elif amount == "270":
            return l90[start]
    elif direction == 'L':
        if amount == "90":
            return l90[start]
        elif amount == "270":
            return r90[start]


ewcount = 0
nscount = 0
facing = 'E'
for inst in instructions:
    action = inst[0]
    amount = inst[1:]
    if action == 'R' or action == 'L':
        facing = rotate(facing, amount, action)
        continue
    elif action == 'F':
        action = facing
    if action == 'N':
        nscount += int(amount)
    elif action == 'E':
        ewcount += int(amount)
    elif action == 'S':
        nscount -= int(amount)
    elif action == 'W':
        ewcount -= int(amount)
    print(nscount, ewcount)

print(abs(nscount) + abs(ewcount))
