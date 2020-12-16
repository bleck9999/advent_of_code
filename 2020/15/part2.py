from tqdm import tqdm
start = []
for x in open("input", "r").readlines():
    x = x.strip().split(sep=',')
    for y in x:
        start.append(int(y.strip()))


def playgaem(start, until):
    seen = start[::-1]
    for _ in tqdm(range(until)):
        last_seen = seen[0]
        if last_seen in seen[1:]:
            last = seen.index(last_seen)
            sndlast = seen.index(last_seen, 1)
            seen.insert(0, sndlast-last)
        else:
            seen.insert(0, 0)

    return seen[until-1]


print(playgaem(start, 30000000))
