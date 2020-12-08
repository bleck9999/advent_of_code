code = []
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        code.append(line)


def doesItInfinite(code):
    i = 0
    acc = 0
    execced = []
    while True:
        if i >= len(code):
            print(acc)
            return True
        elif i in execced:
            return False
        instruction = code[i].split(sep=' ')[0]
        arg = code[i].split(sep=' ')[1]
        if instruction == "nop":
            execced.append(i)
            i += 1
        elif instruction == "acc":
            acc += int(arg)
            execced.append(i)
            i += 1
        elif instruction == "jmp":
            execced.append(i)
            i += int(arg)


# bruteforcing gun gooooo
for ln in range(len(code)):
    if code[ln].split()[0] == "nop":
        code[ln] = code[ln].replace("nop", "jmp")
        doesItInfinite(code)
        code[ln] = code[ln].replace("jmp", "nop")

for ln in range(len(code)):
    if code[ln].split()[0] == "jmp":
        code[ln] = code[ln].replace("jmp", "nop")
        doesItInfinite(code)
        code[ln] = code[ln].replace("nop", "jmp")
