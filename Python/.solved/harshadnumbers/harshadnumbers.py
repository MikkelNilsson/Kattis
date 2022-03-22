inp = input()
i = int(inp)

while(True):
    if i % sum([int(c) for c in inp]) == 0:
        break
    i += 1
    inp = str(i)

print(i)