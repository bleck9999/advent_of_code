with open("input", "r") as f:
    state = 0
    tickets = []
    fields = {}
    my_ticket = []
    for line in f.readlines():
        line = line.strip()
        if line == '':
            state += 1
            continue
        elif state == 0:  # reading fields
            line = line.split(sep=':')
            fields[line[0]] = line[1].split(sep=" or ")
        elif state == 1:  # my ticket
            my_ticket = line.split(sep=',')
        elif state == 2:  # nearby tickets
            if line == "nearby tickets:":
                continue
            tickets.append(line.split(sep=','))

minAll, maxAll = 999, 0
for key in fields:
    field = fields[key]
    lower = field[0].split(sep='-')
    upper = field[1].split(sep='-')
    if int(lower[0]) < minAll:
        minAll = int(lower[0])
    elif int(upper[1]) > maxAll:
        maxAll = int(upper[1])

positions = {}
for ticket in enumerate(tickets):
    for val in ticket[1]:
        val = int(val)
        if val < minAll or val > maxAll:
            tickets.pop(ticket[0])


