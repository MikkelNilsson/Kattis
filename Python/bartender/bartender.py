n, r, t = map(int, input().split())

print(n, r, t)

drinks = dict()

for _ in range(n):
    drink, s, g = input().split()
    drinks[drink] = (int(s), int(g))

print(drinks)