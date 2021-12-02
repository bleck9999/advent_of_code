xpos = 0
ypos = 0
for line in open("input", 'r').readlines():
    direction, value = line.strip().split(sep=' ')
    exec(f"{'xpos' if direction == 'forward' else 'ypos'} +=" 
         f" {'-'+value if direction == 'up' else value}")

print(xpos*ypos)
