with open("input", 'r') as f:
    passports = []
    passport = {}
    for line in f.readlines():
        line = line.strip()
        if line != '':
            spline = line.split(sep=' ')
            for item in spline:
                item = item.split(sep=':')
                passport[item[0]] = item[1]
        else:
            passports.append(passport)
            passport = {}

valid = 0
for passport in passports:
    if len(passport) == 8:
        valid += 1
    elif len(passport) == 7 and "cid" not in passport.keys():
        valid += 1

print(valid)
