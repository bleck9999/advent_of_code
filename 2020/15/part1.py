start = []
for x in open("input", "r").readlines():
    x = x.strip().split(sep=',')
    for y in x:
        start.append(int(y.strip()))



def playgaem(start, until):
    seen = start[:]
    while True:
        last_seen = seen[-1]
        if last_seen in seen[:-1]:
            oldseen = seen[:]
            seen = seen[::-1]
            last = len(seen) - seen.index(last_seen)
            seen.remove(last_seen)
            sndlast = len(seen) - seen.index(last_seen)
            seen = oldseen[:]
            seen.append(last - sndlast)
        else:
            seen.append(0)
        if len(seen) == until:
            return seen[until-1]


print(playgaem(start, 2020))
