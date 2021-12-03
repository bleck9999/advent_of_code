data = open("input", 'r').read().split('\n')

gamma = ''
for i in range(len(data[0])):
    gamma += '1' if sum([line[i] == '1' for line in data]) >= len(data)/2 else '0'

epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])
print(int(epsilon, 2)*int(gamma, 2))
