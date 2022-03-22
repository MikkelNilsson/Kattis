a, b, h = map(int, input().split())
climbs = 0
while True:
    h -= a
    climbs += 1
    if h<=0:
        break;
    h += b

print(climbs)
