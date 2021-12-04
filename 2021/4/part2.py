boards = []
board = []
nums = ""
for line in open("input", 'r').read().splitlines():
    if line and len(line) != 14:
        nums = line
    elif line:
        board += [line[:2], line[3:5], line[6:8], line[9:11], line[12:14]]
        # "why not use str.split" because sometimes there are two consecutive spaces and shit breaks
    else:
        boards.append(board)
        board = []
boards.pop(0)         # when the hacky workarounds
boards.append(board)  # bottom text

indexes = []
for num in nums.split(sep=','):
    for i, v in enumerate(boards):
        board = v
        # python can we get list.replace?
        # python: we have list.replace at home
        # list.replace at home:
        replaced = str(board).replace(f" {num}" if len(num) == 1 else num, '  ')\
            .replace('[', '').replace(']', '').replace("'", '').split(sep=', ')

        muhflag = False
        for mod in range(5):
            sticky = True
            for mul in range(1, 6):
                # check columns
                if replaced[mul*5 - 1 - mod] == '  ':
                    if sticky and mul == 5:
                        muhflag = True
                else:
                    sticky = False
                # check rows
                if replaced[(mul-1)*5:mul*5] == ["  " for _ in range(5)]:
                    muhflag = True
        if muhflag:
            total = 0
            for x in replaced:
                if x == '  ':
                    pass
                else:
                    total += int(x)
            total *= int(num)
            indexes.append(i)
        boards[i] = replaced
    for i in sorted(indexes)[::-1]:
        boards.pop(i)
    indexes = []
print(total)
