# start = []
# for x in open("input", "r").readlines():
#     x = x.strip().split(sep=',')
#     for y in x:
#         start.append(int(y.strip()))
#
#
#
# def playgaem(start, until):
#     seen = start[:]
#     while True:
#         last_seen = seen[-1]
#         if last_seen in seen[:-1]:
#             last = len(seen) - seen.index(last_seen)
#             sndlast = len(seen) - seen.index(last_seen )
#             seen.insert(len(seen), last-sndlast)
#         else:
#             seen.append(0)
#         if len(seen) == until:
#             return seen[until-1]
#
#
# # ok nevermind this takes a day to run
# print(playgaem(start, 30000000))

# aa