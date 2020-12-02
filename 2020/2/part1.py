with open("input","r") as f:
    valid = 0
    for line in f.readlines():
        line = line.strip()
        
        dash = False
        lower = ''
        upper = ''
        for char in line:
            if char == '-':
                dash = True
            elif not dash:
                lower += char
            elif char in ['1','2','3','4','5','6','7','8','9','0'] :
                upper += char
            elif char != ' ':
                polchar = char
                break
        
        lower = int(lower)
        upper = int(upper)
        
        # i could split the string after the colon but i cant be arsed
        count = -1 # exclude the first number as its not part of the password
        for char in line:
            if char == polchar:
                count += 1
        
        if count <= upper and count >= lower:
            valid +=1

    print(valid)
        
