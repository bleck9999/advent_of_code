with open("input", "r") as f:
    memory = {}
    for line in f.readlines():
        line = line.strip()
        if line.startswith("mask"):
            mask = line.split(sep='=')[1].strip()
        else:
            line = line.split(sep='=')
            val = bin(int(line[1].strip()))[2:].zfill(36)
            fval = ''
            for maskbit, valbit in zip(mask, val):
                if maskbit == 'X':
                    fval += str(valbit)
                else:
                    fval += str(maskbit)

            memory[line[0][line[0].index("[")+1:line[0].index("]")]] = fval

total = 0
for addr in memory:
    total += int(memory[addr], 2)
print(total)