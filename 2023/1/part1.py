import re

total = 0
for l in open("input", 'r').read().splitlines():
    match = re.findall(r"(\d(.*\d)?)", l)[0][0]
    total += int(match[0]+match[-1])

print(total)
