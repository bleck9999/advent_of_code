import copy
import itertools

data = open("input", 'r').read().split('\n')

def gammaepsilon(data: list):
    gamma = ''
    for i in range(len(data[0])):
        gamma += '1' if sum([line[i] == '1' for line in data]) >= len(data)/2 else '0'

    epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])
    return gamma, epsilon


o2rate = ''
co2rate = ''
o2vals = copy.deepcopy(data)
co2vals = copy.deepcopy(data)
i = 0

for n in range(len(data[0])):
    gamma = gammaepsilon(o2vals)[0][i]
    epsilon = gammaepsilon(co2vals)[1][i]
    no2vals, nco2vals = [], []
    for o2val, co2val in itertools.zip_longest(o2vals, co2vals, fillvalue='*'*len(data[0])):
        if o2val[i] == gamma:
            no2vals.append(o2val)
        elif len(o2vals) == 1:
            co2vals = o2vals
        if co2val[i] == epsilon:
            nco2vals.append(co2val)
        elif len(co2vals) == 1:
            nco2vals = co2vals
    o2vals, co2vals = copy.deepcopy(no2vals), copy.deepcopy(nco2vals)
    i += 1

print(int(o2vals[0], 2)*int(co2vals[0], 2))
