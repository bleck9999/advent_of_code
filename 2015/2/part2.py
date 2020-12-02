with open("input","r") as f:
    total = 0
    for line in f.readlines():
        dimensions = line.strip().split(sep='x')
        dimensions[0] = int(dimensions[0])
        dimensions[1] = int(dimensions[1])
        dimensions[2] = int(dimensions[2])

        dimensions.sort()

        total += dimensions[0]*dimensions[1]*dimensions[2]  # bow
        total += dimensions[0]*2 + dimensions[1]*2          # smallest perimeter 

    print(total)


