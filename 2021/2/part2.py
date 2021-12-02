xpos = 0
ypos = 0
aim = 0
for line in open("input", 'r').readlines():
    direction, value = line.strip().split(sep=' ')
    if direction == "forward":
        xpos += int(value)
        ypos += int(value)*aim
    else:
        aim += eval(f"{'-' if direction == 'up' else ''}{value}")


print(xpos*ypos)
