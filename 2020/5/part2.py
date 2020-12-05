with open("input","r") as f:
    ids = []
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
        
        ids.append(num*8 + col)
    
    ids.sort()
    for index in range(len(ids)-1):
        if ids[index+1] != ids[index]+1:
            print(ids[index]+1)
