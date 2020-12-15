from iteration_utilities import deepflatten
def maskedmán(mask: str, addr: str, memory):
    oaddr = addr
    addr = list(addr)
    returnval = []
    for bit in enumerate(addr):
        tmask = list(mask)
        if mask[bit[0]] == 'X':
            tmask[bit[0]] = '0'
            addr[bit[0]] = '1'
            returnval.append(maskedmán(tmask, addr, memory))
            addr[bit[0]] = '0'
            returnval.append(maskedmán(tmask, addr, memory))
            addr = oaddr[:]
            break
    else:
        fval = ''
        for maskbit, valbit in zip(mask, addr):
            if maskbit == '0':
                fval += valbit
            elif maskbit == '1':
                fval += maskbit
        returnval.append(int(fval, 2))
    return returnval


with open("input", "r") as f:
    memory = {}
    for line in f.readlines():
        line = line.strip()
        if line.startswith("mask"):
            mask = line.split(sep='=')[1].strip()
        else:
            line = line.split(sep='=')
            val = line[1].strip()
            addresses = maskedmán(mask, bin(int(line[0][line[0].index("[")+1:line[0].index("]")]))[2:].zfill(36), memory)
            for addr in deepflatten(addresses):
                memory[addr] = val

total = 0
for addr in memory:
    total += int(memory[addr])
print(total)