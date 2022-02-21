n = int(input())

for s in range(n):
    b, p = map(float, input().split())
    BPM = 60*b/p
    minAbpm = 60/(p/b)
    maxAbpm = 60/((p+1)/b)
    print(minAbpm,BPM, maxAbpm)
