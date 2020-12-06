with open("input", 'r') as f:
    total = 0
    group = []
    seen = []
    for line in f.readlines():
        line = line.strip()
        if line != "":
            if not group:
                for ch in line:
                    seen.append(ch)
            group.append(line)
        else:
            for ch in seen:
                count = 0
                for item in group:
                    if ch in item:
                        count += 1
                if count == len(group):
                    total += 1
            seen = []
            group = []

print(total)
