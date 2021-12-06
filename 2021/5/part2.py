import itertools

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

colormap = ListedColormap(["#000000", "#00ffff", "#ffff00", "#00ff00"])

grid = {}
def addTo(x, y):
    if (x,y) not in grid:
        grid[(x, y)] = 0
    grid[(x, y)] += 1


for l in open("input", 'r').read().splitlines():
    l1, l2 = l.split(sep="->")
    # we shift positions up by one so the grid starts at 1,1 in the next line.
    # we do this because we take movement being 0 to mean the line isnt diagonal and if we let 0 be a valid position
    # then in the case of a line going to x,0 or 0,y it would put the wrong coordinate
    # to see how it breaks try the example input without the +1s on the below 2 lines and have a look at 6,4->2,0
    l1 = [int(x)+1 for x in l1.split(sep=',')]
    l2 = [int(x)+1 for x in l2.split(sep=',')]
    xrange = l1[0] - l2[0]
    yrange = l1[1] - l2[1]
    for xmove, ymove in itertools.zip_longest(range(l1[0], l2[0] - (1 if xrange > 0 else -1), -1 if xrange > 0 else 1),
                                              range(l1[1], l2[1] - (1 if yrange > 0 else -1), -1 if yrange > 0 else 1)):
        addTo(xmove if xmove else l1[0],
              ymove if ymove else l1[1])

fig, ax = plt.subplots()
data = np.array([[grid[(x, y)] if (x, y) in grid else 0 for x in range(1, 1001)] for y in range(1, 1001)])
psm = ax.pcolormesh(data, cmap=colormap, rasterized=True, vmin=0, vmax=3)
fig.colorbar(psm, ax=ax)
plt.savefig("graph.png", format="png", dpi=150)
plt.show()

positions = []
for pos in grid:
    if grid[pos] >= 2:
        positions.append(pos)

print(len(positions))
