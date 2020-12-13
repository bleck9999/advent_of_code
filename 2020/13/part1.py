with open("input", "r") as f:
    timestamp = int(f.readline().strip())
    rawbuses = f.readline().strip().split(sep=',')
buses = []
for bus in rawbuses:
    if bus != 'x':
        buses.append(int(bus))

lowest = 9999999999 # haha maths go brrrr
for bus in buses:
    if bus-(timestamp%bus) < lowest:
        lowest = bus-timestamp%bus
        print((bus - (timestamp % bus)) * bus)
