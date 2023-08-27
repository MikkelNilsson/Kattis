inp = input()

out = str(inp[0])
prevc = str(inp[0])
for c in [str(inp[i]) for i in range(1, len(inp))]:
    if prevc == c:
        continue
    else:
        out += c
        prevc = c
print(out)
