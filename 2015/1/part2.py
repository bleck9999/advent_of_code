total = 0
a = open("input","r").read()
for i in range(len(a)):
    if a[i] == '(':
        total += 1
    elif a[i] == ')':
        total -= 1
    if total == -1:
        print(i+1)
        exit()

