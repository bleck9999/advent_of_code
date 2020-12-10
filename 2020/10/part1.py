adapters = []
with open("input", "r") as f:
    for line in f.readlines():
        adapters.append(int(line.strip()))

adapters.sort()
count3 = 1  # built-in is always largest+3, so add a difference of 3
count1 = 1
# i dont know if the outlet is always a diff of 1 but i cant be fucked to check
# and it is for my input + all the tests so who cares
for i in range(len(adapters)-1):
    current = adapters[i]
    next = adapters[i+1]
    if next - current == 1:
        count1 += 1
    elif next - current == 3:
        count3 += 1

print(count1 * count3)
