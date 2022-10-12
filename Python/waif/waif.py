n, m, p = map(int, input().split())


l = dict([(i, dict()) for i in range(n+m+p+2)])
l[0] = dict([(i+1, 1) for i in range(n)])

for i in range(1, n+1):
    l[i] = dict([(n+int(j), 1) for j in input().split()[1:]])

# residual graph
for i in range(1, n+1):
    l[i][0] = 0

s = set(range(1, m+1))
for i in range(1,p+1):
    c = input().split()
    for t in c[1:-1]:
        s.remove(int(t))
        l[n+int(t)][n+m+i] = 1
        # residual graph
        l[n+m+i][n+int(t)] = 0
    l[n+m+i][n+m+p+1] = int(c[-1])
    # residual graph
    l[n+m+p+1][n+m+i] = 0

for i in s:
    l[n+i][n+m+p+1] = 1



print(l)