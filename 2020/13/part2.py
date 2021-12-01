import numpy as np
from numba import cuda
import math

with open("input", "r") as f:
    timestamp = int(f.readline().strip()) # we dont need this anymore but i cant be fucked to change it
    rawbuses = f.readline().strip().split(sep=',')
for i in range(len(rawbuses)):
    if rawbuses[i] != 'x':
        rawbuses[i] = int(rawbuses[i])
    else:
        rawbuses[i] = 1


@cuda.jit
def aaaaaa(start, rawbuses):
    i = cuda.grid(1) + start
    termd = False
    for bus in enumerate(rawbuses):
        if bus[1] == 1:
            continue
        elif (i+bus[0]) % bus[1] == 0:
            continue
        else:
            termd = True
            return
    if not termd:
        print("Hit at", i)
        return


buses = np.array(rawbuses, dtype=np.uint64)
# #lower = 100000000000000
lower = 0
while True:
    array = np.arange(lower, lower + 880000000, 1, np.uint64)
    # the amount you increment lower by is limited by the amount of RAM you have
    # oh also the values need to be reachable you gigantic melon
    print(1202161486 in array)
    array = cuda.to_device(array)
    bpg = 128
    tpb = 512
    for n in range(math.ceil(880000000/(bpg * tpb))):
        aaaaaa[bpg, tpb](bpg * tpb * n, buses)
        cuda.syncthreads
    lower += 880000000  # this number and the number added to lower above should be the same

# yes i would rather make a bad solution work better than make a good solution in the first place
# also ive never used cuda before so this is bad in literally every way
