import re
from itertools import zip_longest

total = 0
for l in open("input", 'r').read().splitlines():
    gameid = re.search("(?<=Game )\d+", l).group()
    reds = re.findall("\d+(?= red)", l)
    greens = re.findall("\d+(?= green)", l)
    blues = re.findall("\d+(?= blue)", l)
    for (red, green, blue) in zip_longest(reds, greens, blues, fillvalue='0'):
        if any([int(red) > 12,
                int(green) > 13,
                int(blue) > 14]):
            break
    else:
        total += int(gameid)
print(total)
