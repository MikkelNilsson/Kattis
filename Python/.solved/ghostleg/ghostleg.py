
n, m = map(int, input().split())
ghost_legs = list()

for _ in range(m):
    ghost_legs.append(int(input()))

output = [0] * (n + 1)

for pind in range(1, n+1):
    pindvalue = pind
    for leg in ghost_legs:
        if pindvalue == leg:
            pindvalue += 1
        elif pindvalue == leg+1:
            pindvalue -= 1
        else:
            pass
    output[pindvalue] = pind


[print(v) for v in output[1:]]