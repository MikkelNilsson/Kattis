n = int(input())

for _ in range(n):
    l, a = map(int, input().split())
    stin = input().split()
    while len(stin) < a:
        stin.extend(input().split())

    #print(stin)
    antlist = list(map(int, stin))
    antlist.sort()
    mintime = 0
    for i in antlist:
        mintime = max(mintime, min(i, l-i))
    print(mintime, max(l-antlist[0], antlist[-1]))