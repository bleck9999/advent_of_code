import pyautogui as pg
import time

# ok so what we're doing here is getting the input
lines = open("input", 'r').readlines()
time.sleep(3)
# and turning it into "COPY {num} F"
# the idea is we've already created a file and are just dumping input into it
for l in lines:
    # however, there's an instruction limit of 1000 lines per exa (and a file size limit aswell)
    # so to 'resume' where we left off we just check for current input line being > the the last value we entered
    if int(l) > 9073:
        pg.typewrite(f"COPY {l.strip()} F")
        pg.typewrite(["enter"])

# Exapunks code available in a seperate file exahell.txt (only the logic exa, file slaves not included)
# it expects the input across 3 files, but could be fairly easily modified for fewer/more by altering the rep numbers.
