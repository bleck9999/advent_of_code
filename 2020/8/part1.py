code = []
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        code.append(line)

execced = []
i = 0
acc = 0


def next_instruction(i):
    execced.append(i)
    i += 1
    return i


while True:
    if i in execced:
        print(acc)
        exit()
    instruction = code[i].split(sep=' ')[0]
    arg = code[i].split(sep=' ')[1]
    if instruction == "nop":
        i = next_instruction(i)
    elif instruction == "acc":
        acc += int(arg)
        i = next_instruction(i)
    elif instruction == "jmp":
        execced.append(i)
        i += int(arg)
