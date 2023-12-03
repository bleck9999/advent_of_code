import re
from itertools import zip_longest

total = 0
for l in open("input", 'r').read().splitlines():
    gameid = re.search("(?<=Game )\d+", l).group()
    reds = [int(x) for x in re.findall("\d+(?= red)", l)]
    greens = [int(x) for x in re.findall("\d+(?= green)", l)]
    blues = [int(x) for x in re.findall("\d+(?= blue)", l)]

    total += max(reds) * max(greens) * max(blues)
print(total)
