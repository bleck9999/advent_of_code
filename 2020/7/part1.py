colours = {}
with open("input", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split(sep="contain")
        bagCol = line[0]
        contains = line[1].split(sep=',')
        for i in range(len(contains)):
            contains[i] = contains[i].strip()
            contains[i] = contains[i][2:]       # fuck numbers all my homies hate numbers
            if contains[i][-1] == '.':
                contains[i] = contains[i][:-1]
            if contains[i][-1] == 'g':
                contains[i] = contains[i]+'s'   # this is absolutely horrible and i hate it

        colours[bagCol.strip()] = contains

valid = []


def validateColour(colour):
    if colour == " other bags":
        return
    if "shiny gold bags" in colours[colour] and colour not in valid:
        valid.append(colour)
    for col in colours[colour]:
        validateColour(col)


def validateAgainstExisting(colour):
    for v in valid:
        if v in colours[colour] and colour not in valid:
            valid.append(colour)


for colour in colours.keys():
    validateColour(colour)

# prepare your eyes
for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

for colour in colours.keys():
    validateAgainstExisting(colour)

print(len(valid))
