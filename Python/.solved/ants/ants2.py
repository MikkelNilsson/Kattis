n = int(input())

for _ in range(n):
    l, a = map(int, input().split())
    stin = input().split()
    while len(stin) < a:
        stin.extend(input().split())

    #print(stin)
    antlist = list(map(int, stin))
    mintime = 0
    maxtime = 0
    for i in antlist:
        maxtime = max(maxtime, max(l-i, i))
        mintime = max(mintime, min(i, l-i))
    print(mintime, maxtime)
