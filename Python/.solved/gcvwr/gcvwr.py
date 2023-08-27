G, T, I = map(int, input().split())

maxweight = (G-T)*0.9
for w in map(int, input().split()):
    maxweight -= w
print(int(maxweight))
