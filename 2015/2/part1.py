with open("input","r") as f:
    total = 0
    for line in f.readlines():
        dimensions = line.strip().split(sep='x')
        dimensions[0] = int(dimensions[0])
        dimensions[1] = int(dimensions[1])
        dimensions[2] = int(dimensions[2])

        face1 = dimensions[0] * dimensions[1]
        face2 = dimensions[0] * dimensions[2]
        face3 = dimensions[1] * dimensions[2]
    
        total += (face1*2) + (face2*2) + (face3*2)

        dimensions.sort()
        slack = dimensions[0] * dimensions[1]

        print(dimensions, slack)

        total += slack

    print(total)


