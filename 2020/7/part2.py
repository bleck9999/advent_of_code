colours = {}
with open("input", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split(sep="contain")
        bagCol = line[0]
        contains = line[1].split(sep=',')
        for i in range(len(contains)):
            contains[i] = contains[i].strip()
            # gdi now i need to use the numbers
            if contains[i][-1] == '.':
                contains[i] = contains[i][:-1]
            if contains[i][-1] == 'g':
                contains[i] = contains[i] + 's'  # this is absolutely horrible and i hate it

        colours[bagCol.strip()] = contains


def countBags(colour):
    total = 0
    for col in colours[colour[2:]]:
        if col == "no other bags":
            return 1
        else:
            total += countBags(col) * int(col[0])
    return total+1


print(countBags("1 shiny gold bags")-1)
