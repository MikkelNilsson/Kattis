l = [int(i) for i in input().split()]

results = [0 for _ in range(l[0]+l[1])]

for i in range(1, l[0]):
    for j in range(1, l[1]):
        results[i+j] += 1

maxx = 0
maxi = list()
for i in range(2, len(results)):
    if i > maxx:
        maxx = i;
        maxi = [results[i]]
    elif i == maxx:
        maxi.append(results[i])

for i in maxi:
    print(i + "\n")

