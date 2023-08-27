l = [11, 4, 3, 2, 10]
N, B = input().split()

sum = 0

for _ in range(int(N)*4):

    inp = input()
    if 'A' in inp:
        sum += 11
    if 'K' in inp:
        sum += 4
    if 'Q' in inp:
        sum += 3
    if 'J' in inp:
        if B in inp:
            sum += 20
        else:
            sum += 2
    if 'T' in inp:
        sum += 10
    if '9' in inp:
        if B in inp:
            sum += 14

print(sum)

