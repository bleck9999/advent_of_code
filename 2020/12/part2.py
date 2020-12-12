instructions = []
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        instructions.append(line)


def rotate(start, amount, direction, x, y):
    if amount == "180":
        return -x, -y
    elif direction == 'R':
        if amount == "90":
            return y, -x
        elif amount == "270":
            return -y, x
    elif direction == 'L':
        if amount == "90":
            return -y, x
        elif amount == "270":
            return y, -x


ewcount = 0
nscount = 0
waypointx = 10
waypointy = 1
facing = 'E'
for inst in instructions:
    action = inst[0]
    amount = inst[1:]
    if action == 'R' or action == 'L':
        waypointx, waypointy = rotate(facing, amount, action, waypointx, waypointy)
        continue
    elif action == 'F':
        ewcount += int(amount) * waypointx
        nscount += int(amount) * waypointy
    if action == 'N':
        waypointy += int(amount)
    elif action == 'E':
        waypointx += int(amount)
    elif action == 'S':
        waypointy -= int(amount)
    elif action == 'W':
        waypointx -= int(amount)

print(abs(nscount) + abs(ewcount))
