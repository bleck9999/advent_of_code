from numba import cuda
import numpy as np

tiles = {}
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if "Tile" in line:
            tile = []
            id = int(line[4:-1])
        elif line == '':
            tiles[id] = tile
        else:
            binline = ''
            for ch in line:
                if ch == '.':
                    binline += '0'
                elif ch == '#':
                    binline += '1'
            tile.append(binline)


