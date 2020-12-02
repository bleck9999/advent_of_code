total = 0
for i in open("input","r").read():
    if i == '(':
        total += 1
    elif i == ')':
        total -= 1
print(total)
