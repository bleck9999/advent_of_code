import re

total = 0
numbers = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
edge_cases = {"twone": '21', "oneight": '18', "sevenine": '79', "fiveight": '58', "nineight": '98', "eightwo": "82", "eighthree": '83'}
for l in open("input", 'r').read().splitlines():
    for death in edge_cases.items():
        l = l.replace(*death)
    for death in numbers.items():
        l = l.replace(*death)
    match = re.findall(r"(\d(.*\d)?)", l)[0][0]
    print(match[0]+match[-1]+'\n')
    total += int(match[0]+match[-1])

print(total)
