with open("input","r") as f:
    max = 0
    for line in f.readlines():
        line = line.strip()
        
        num = []
        for ch in line[:7]:
            num.insert(0, 1 if ch == 'B' else 0)
        num = sum(2 ** x for x in range(len(num)) if num[x] == 1)
        
        col = []
        for ch in line[7:]:
            col.insert(0, 1 if ch == 'R' else 0)
        col = sum(2 ** x for x in range(len(col)) if col[x] == 1)
        
        print(line, num, col)
        max = (num*8 + col) if num*8 + col > max else max

    print(max)
