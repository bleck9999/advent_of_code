start = open("input", "r").readline().strip()

h = 0
for l in start:
    l = int(l)
    if h < l:
        h = l


def recursion_goes_brrr(start, prev, counter):
    if counter == 100:
        print(start.split('1')[1]+start.split('1')[0])
        return
    if prev == 0:
        pos = 0
    else:
        pos = start.index(str(prev))+1
    value = int(start[pos])
    picked_up = start[pos+1:pos+4]
    while True:
        value -= 1
        if value <= 0:
            value = h
        if str(value) not in picked_up:
            break

    target = start.index(str(value))
    new = ''
    for i in start:
        if i not in picked_up:
            new += i

    #if target < pos+1:
    new = new[:new.index(start[target])+1] + picked_up + new[new.index(start[target])+1:]
    #else:

    if pos == len(start)-1:
        nextval = start[0]
    else:
        nextval = start[pos+1]
    recursion_goes_brrr(new, int(nextval), counter+1)
#fuck it
#this wraparound hell is literally driving me insane

recursion_goes_brrr(start, 0, 0)
