stack = []
seennodes = set()

def DFSstart(G, v_set):
    while v_set:
        start = v_set.pop()
        seennodes = set(start)
        path = [start]
        for v in G[start].keys():   
                stack.append(v)
        
        DFS(G, v_set, path)

def checkArbitrage(G, path, start, stop):
    sum = G[start][stop]
    prevnode = path.pop()
    node = path.pop()
    while node != stop:
        sum *= G[node][prevnode]
        prevnode = node
        node = path.pop()
    if sum * G[node][prevnode] != 1:
        return False
    return True



def DFS(G, v_set, path):
    while stack:
        node = stack.pop()
        path.append(node)
        seennodes.add(node)
        for v in G[node].keys():
            if v in path:
                if not checkArbitrage(G, path, node, v):





i = int(input())


while i != 0:
    stack.clear()
    nodes = set(input().split())
    G = dict([(n, dict()) for n in nodes])

    j = int(input())
    for _ in range(j):
        inp = input().split()
        G[inp[0]][inp[1]] = (int(inp[2].split(":")[1])/ int(inp[2].split(":")[0]))
    
    DFS(G, nodes)

    i = int(input())
