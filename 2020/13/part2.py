with open("input", "r") as f:
    timestamp = int(f.readline().strip()) # we dont need this anymore but i cant be fucked to change it
    buses = f.readline().strip().split(sep=',')
for i in range(len(buses)):
    buses[i] = int(buses[i]) if buses[i] != 'x' else buses[i]


t = 0
step = 1
maxstate = -1
while True:
    flag = False
    for bus in enumerate(buses):
        if bus[1] == 'x':
            continue
        elif (t+bus[0]) % bus[1] == 0:
            if maxstate < bus[0]:
                maxstate = bus[0]
                step *= bus[1]
            continue
        else:
            flag = True
            break
    if not flag:
        print("Hit at", t)
        exit()
    t += step
