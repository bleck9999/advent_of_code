import re

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
eyecols = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
hair = re.compile("#[a-f0-9]{6}")

def validateyr(yr, min, max):
    try:
        int(yr)
    except ValueError:
        return False
    return max >= int(yr) >= min


def validateheight(hgt):
    try:
        int(hgt[:-2])
    except ValueError:
        return False
    if len(hgt) < 4:
        return False

    if hgt[-2:] == "cm":
        return 193 >= int(hgt[:-2]) >= 150
    elif hgt[-2:] == "in":
        return 76 >= int(hgt[:-2]) >= 59


def validateeye(ecl):
    return ecl in eyecols


def validatehair(hcl):
    return re.match(hair, hcl)


def validatepid(pid):
    try:
        int(pid)
    except ValueError:
        return False
    return len(pid) == 9


for passport in passports:
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys()):
        byr = validateyr(passport["byr"], 1920, 2002)
        iyr = validateyr(passport["iyr"], 2010, 2020)
        eyr = validateyr(passport["eyr"], 2020, 2030)
        hgt = validateheight(passport["hgt"])
        ecl = validateeye(passport["ecl"])
        hcl = bool(validatehair(passport["hcl"]))
        pid = validatepid(passport["pid"])

        if byr and iyr and eyr and hgt and ecl and hcl and pid:
            valid += 1


print(valid)
