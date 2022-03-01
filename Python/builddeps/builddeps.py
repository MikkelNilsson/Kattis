d = dict()
nonmarked = set()

for _ in range(int(input())):
    deps = input().split(":")
    d[deps[0]] = list()
    nonmarked.add(deps[0])
    if deps[1] != "":
        tmp = deps[1].strip()
        tmp1 = tmp.split()
        for v in tmp1:
            if v not in d.keys():
                d[v] = list()

            d[v].append(deps[0])

l = list()
perm = set()

def visit(i):
    if i in perm:
        return

    for n in d[i]:
        visit(n)

    perm.add(i)
    nonmarked.remove(i)
    l.append(i)


while nonmarked:
    node = nonmarked.pop()
    nonmarked.add(node)
    visit(node)


for i in l:
    print(i)

