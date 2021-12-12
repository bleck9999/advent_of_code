pairs = {'[': ']', '{': '}', '<': '>', '(': ')'}
points = {']': 57, '}': 1197, '>': 25137, ')': 3}

stack = []
corrupt = 0
for l in open("input", 'r').read().split(sep='\n'):
    for char in l:
        if char in pairs.keys():
            stack.append(char)
        else:
            if char == pairs[stack[-1]]:
                stack.pop(-1)
            else:
                print(f"Expected {pairs[stack[-1]]}, found {char}")
                corrupt += points[char]
                break

print(corrupt)
