ssum = 0

for s in input().split(";"):
    if "-" in s:
        mn, mx = map(int, s.split("-"))
        ssum += mx-mn + 1
    else:
        ssum += 1

print(ssum)