l, i, v = map(int, input().split())

i -= 1

b = list(map(int, input().split()))

m = [False] * l

c = 0

while True:
    if b[i] == v:
        print("magic")
        print(c)
        break
    
    if m[i]:
        print("cycle")
        print(c)
        break

    if i + b[i] < 0:
        print("left")
        print(c + 1)
        break

    if i + b[i] >= l:
        print("right")
        print(c + 1)
        break

    m[i] = True
    c += 1
    i += b[i]
