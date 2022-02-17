import sys

s = input()

t = set()
for c in s:
    if c in t:
        print(0)
        sys.exit()
    else:
        t.add(c)

print(1)