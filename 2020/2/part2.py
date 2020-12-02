with open("input","r") as f:
    valid = 0
    for line in f.readlines():
        line = line.strip()
        
        dash = False
        pos1 = ''
        pos2 = ''
        for char in line:
            if char == '-':
                dash = True
            elif not dash:
                pos1 += char
            elif char in ['1','2','3','4','5','6','7','8','9','0'] :
                pos2 += char
            elif char != ' ':
                polchar = char
                break
        
        pos1 = int(pos1)
        pos2 = int(pos2)
        
        # fuck guess i have to now
        passwd = line.split(sep=':')[1].strip()  
        if (passwd[pos1-1] == polchar) ^ (passwd[pos2-1] == polchar):
            valid += 1

    print(valid)
        
