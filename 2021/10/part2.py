pairs = {'[': ']', '{': '}', '<': '>', '(': ')'}
points = {']': 2, '}': 3, '>': 4, ')': 1}

fstrs = []
lines = open("input", 'r').read().split(sep='\n')
for l in lines:
    stack = []
    for char in l:
        if char in pairs.keys():
            stack.append(char)
        else:
            if char == pairs[stack[-1]]:
                stack.pop(-1)
            else:
                print(f"Expected {pairs[stack[-1]]}, found {char}")
                break
    else:
        fstr = ''.join(pairs[x] for x in reversed(stack))
        print(f"Completing line {l} with {fstr}")
        fstrs.append(fstr)

scores = []
for completion in fstrs:
    score = 0
    for ch in completion:
        score *= 5
        score += points[ch]
    scores.append(score)
scores.sort()

print(scores[(1+len(scores)//2)-1])
