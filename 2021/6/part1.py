fish = []
for f in open("input", 'r').read().strip().split(sep=','):
    fish.append(int(f))

max_days = 256
to_add = 0
for d in range(max_days):
    [fish.append(9) for _ in range(to_add)]
    to_add = 0
    for i, f in enumerate(fish):
        if f == 1:
            to_add += 1
        elif not f:
            f = 7
        f -= 1
        fish[i] = f
    #print(fish)

print(len(fish))
