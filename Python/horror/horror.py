import imp
import sys
from collections import defaultdict

seen = set()
hindecies = defaultdict(list)
maxhi = 1


def DFS(G, node, hi):
    
    mhi = hi
    # create dfs...
    for v in G[node]:
        if v not in seen or hindecies[v] > hi:
            seen.add(v)
            mhi = hi + 1
            hindecies[mhi].append(v)
            mhi = max(mhi, DFS(G, v, mhi))

    return mhi
    


N, H, L = map(int, input().split())

hlist = set(map(int, input().split()))

G = dict([(i, []) for i in range(N)])

for _ in range(L):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for h in hlist:
    seen.add(h)
    hindecies[0] = h
    for v in G[h]:
        if v not in hindecies.keys() or hindecies[v] > 1:
            seen.add(v)
            hindecies[1] =  v
        maxhi = DFS(G, v, 0)

for v in range(N):
    if v not in seen:
        print(v, end="")
        sys.exit(0)
l = sorted(hindecies[maxhi], key=lambda x: x[1])[0]
print(l)

