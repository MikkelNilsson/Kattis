
x, y, z = map(int, input().split())

# 0 = +
# 1 = -
# 2 = *
# 3 = /
def ope(a, b, o):
    if o == 0:
        return a + b
    if o == 1:
        return a - b
    if o == 2:
        return a * b
    if o == 3:
        return a / b

curmin = 10**6
for o1 in range(4):
    if o1 == 3 and x % y != 0:
        continue
    v1 = ope(x, y, o1)
    for o2 in range(4):
        if o2 == 3 and v1 % z != 0:
            continue
        
        cal_val = ope(v1, z, o2)

        if cal_val < curmin and cal_val >= 0:
            curmin = cal_val


print(int(curmin))
