valid = [1, 1, 2, 2, 2, 8]
inp = [i for i in input().split()]

for i, v in enumerate(valid):
    inp[i] = str(v - int(inp[i]))

print(" ".join(inp))