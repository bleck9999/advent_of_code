






# hey

# i couldnt do day 10




# the solution was made by someone much more competent than me
# posted by tboschi on github
# https://github.com/tboschi/advent-of-code-2020/tree/master/day10/py
# everything after line 48 is not mine
# have a nice day

















adapters = []
with open("input", "r") as f:
    for line in f.readlines():
        adapters.append(int(line.strip()))

adapters.sort()
adapters.insert(0, 0)


# frii theft
# i have no idea how this works
arrangements = [1]
for i in range(1, len(adapters)):
    arrange = arrangements[i-1]
    j = i - 2
    while j >= 0 and adapters[i] - adapters[j] <= 3:
        arrange += arrangements[j];
        j -= 1

    arrangements.append(arrange);


print(f"There are {arrangements[-1]} valid arrangements")