l = [int(i) for i in input().split()]

results = [0 for _ in range(l[0]+l[1] + 1)]

for i in range(1, l[0] + 1):
    for j in range(1, l[1] + 1):
        results[i+j] += 1

maxx = 0
maxi = list()
for i in range(2, len(results)):
    if results[i] > maxx:
        maxx = results[i];
        maxi = [i]
    elif results[i] == maxx:
        maxi.append(i)

for i in maxi:
    print(i)

