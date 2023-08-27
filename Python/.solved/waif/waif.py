n, m, p = map(int, input().split())

sink = n+m+p+1

l = dict([(i, dict()) for i in range(n+m+p+2)])
l[0] = dict([(i+1, 1) for i in range(n)])

# residual graph
for i in range(1, n+1):
    l[i][0] = 0



for i in range(1, n+1):
    for j in input().split()[1:]:
        l[i][n + int(j)] = 1
        # residual graph
        l[n + int(j)][i] = 0


s = set(range(1, m+1))
for i in range(1,p+1):
    c = input().split()
    for t in c[1:-1]:
        s.remove(int(t))
        l[n+int(t)][n+m+i] = 1
        # residual graph
        l[n+m+i][n+int(t)] = 0
    l[n+m+i][sink] = int(c[-1])
    # residual graph
    l[sink][n+m+i] = 0

for i in s:
    l[n+i][sink] = 1
    l[sink][n+i] = 0


def bfs(parent):

    visited = [False] * (sink + 1)

    queue = []

    queue.append(0)
    visited[0] = True

    while queue:
        v = queue.pop()

        for i, c in l[v].items():
            if not visited[i] and c > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = v
                if i == sink:
                    return True
    
    return False

def run_ff_bfs():
    parent = [-1] * (sink + 1)
    maxflow = 0

    while bfs(parent):
        pathflow = INF
        s = sink
        while s != 0:
            pathflow = min(pathflow, l[parent[s]][s])
            s = parent[s]

        maxflow += pathflow
        
        v = sink
        while(v != 0):
            u = parent[v]
            l[u][v] -= pathflow
            l[v][u] += pathflow
            v = u

    return maxflow

# def dfs(node: int, max_weight: int, seen) -> int:
#     for next in l[node].keys():
#         #print(next, seen)
#         if next in seen or l[node][next] < 1:
#             #print("Seen")
#             continue

#         if next == sink:
#             weight = min(max_weight, l[node][next])
#             l[node][next] -= weight
#             return weight

#         seen1 = set(seen)
#         seen1.add(node)
#         res_weight = dfs(next, min(max_weight, l[node][next]), seen1)
#         if res_weight > 0:
#             #print(node, next)
#             l[node][next] -= res_weight
#             l[next][node] += res_weight
#             return res_weight
#     return -1
    

INF = 10**6

flow = run_ff_bfs()


# Run with DFS (Too slow)
# cur_flow = 0
# flow = 0
# while (cur_flow != -1):
#     flow += cur_flow
#     cur_flow = dfs(0, INF, set())
#     #print("---------------Done:", cur_flow)

print(flow)
