with open("input", 'r') as f:
    total = 0
    seen = []
    for line in f.readlines():
        line = line.strip()
        if line != '':
            for ch in line:
                if ch not in seen:
                    seen.append(ch)

        else:
            total += len(seen)
            seen = []

print(total)
