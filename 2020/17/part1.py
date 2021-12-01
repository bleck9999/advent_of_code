import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import copy

colormap = ListedColormap(["#ff0000", "#00ff00", "#00ffff", "#ffff00"])

sys.setrecursionlimit(999999)  # like it matters anyway past about 12.5k
load = {}
with open("input", "r") as f:
    i = 0
    for line in f.readlines():
        line = line.strip().replace(".", "0")
        line = line.strip().replace("#", "1")
        load[i] = dict(enumerate([int(x) for x in line]))
        i += 1

grid = {0: copy.deepcopy(load)}


class CubeSim:
    m_grid = copy.deepcopy(grid)
    m_newgrid = {}

    def get(self, x, y, z):
        return int(self.m_grid[y][x][z])

    def toggle(self, x, y, z):
        self.m_newgrid[y][x][z] = 0 if self.m_newgrid[y][x][z] == 1 else 1

    def neighbours(self, x, y, z):
        layers = range(y-1, y+2)
        rows = range(x-1, x+2)
        cols = range(z-1, z+2)
        total = 0
        # tempgrid = {}
        for layer in layers:
            if layer not in self.m_grid:
                continue
            # tempgrid[layer] = {}
            for row in rows:
                if row not in self.m_grid[layer]:
                    continue
                # tempgrid[layer][row] = {}
                for col in cols:
                    if col not in self.m_grid[layer][row]:
                        continue
                        #self.m_grid[layer][row][col] = '1' if self.neighbours(row, layer, col) == 3 else '0'
        #            tempgrid[layer][row][col] = self.get(row, layer, col)
                    if layer == y and row == x and col == z:
                        continue
                    total += self.get(row, layer, col)
        #             self.m_grid[layer][row][col] = 3
        # self.m_grid[y][x][z] = 2
        # self.draw_grid()
        # for y in tempgrid:
        #     for x in tempgrid[y]:
        #         for z in tempgrid[y][x]:
        #             self.m_grid[y][x][z] = tempgrid[y][x][z]
        return total

    def cycle(self):
        layers = list(self.m_grid.keys())
        rows = list(self.m_grid[0].keys())
        cols = list(self.m_grid[0][0].keys())
        self.m_grid[layers[0] - 1] = {}.fromkeys(rows)
        self.m_grid[layers[-1] + 1] = {}.fromkeys(rows)
        for layer in self.m_grid:
            self.m_grid[layer][rows[0] - 1] = {}
            self.m_grid[layer][rows[-1] + 1] = {}
            for row in self.m_grid[layer]:
                if self.m_grid[layer][row] is None:
                    self.m_grid[layer][row] = {}
                for col in range(cols[0]-1, cols[-1]+2):  # stop is exclusive
                    if col not in self.m_grid[layer][row]:
                        self.m_grid[layer][row][col] = 0

        self.m_newgrid = copy.deepcopy(self.m_grid)

        self.draw_grid()

        for y in self.m_grid:
            for x in self.m_grid[y]:
                for z in self.m_grid[y][x]:
                    n = self.neighbours(x, y, z)
                    if not self.get(x, y, z) and n == 3:
                        self.toggle(x, y, z)
                    elif self.get(x, y, z) and (n != 2 and n != 3):
                        self.toggle(x, y, z)

        self.m_grid = copy.deepcopy(self.m_newgrid)

        self.draw_grid()
        print("")

    def draw_grid(self):
        for layer in sorted(self.m_grid):
            fig, ax = plt.subplots()
            data = np.array([[self.m_grid[layer][row][col] for col in sorted(self.m_grid[layer][row])]
                             for row in sorted(self.m_grid[layer])])
            psm = ax.pcolormesh(data, cmap=colormap, rasterized=True, vmin=0, vmax=3)
            fig.colorbar(psm, ax=ax)
            plt.show()

    def countActive(self):
        # loop through grid and keep a running total of active cubes
        total = 0
        for layer in self.m_grid:
            for row in self.m_grid[layer]:
                for col in self.m_grid[layer][row]:
                    total += self.get(row, layer, col)
        return total

sim = CubeSim()
for i in range(6):
    sim.cycle()
print(sim.countActive())
