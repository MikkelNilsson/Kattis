n = int(input())

for s in range(n):
    b, p = map(float, input().split())
    BPM = "%0.4f" % round(60*b/p, 4)
    minAbpm = "%0.4f" % round(60/(p/(b-1)), 4)
    maxAbpm = "%0.4f" % round(60/((p)/(b+1)),4)

    print(minAbpm,BPM, maxAbpm)
