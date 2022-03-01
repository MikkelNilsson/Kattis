i = int(input())

for _ in range(i):
    sum = 1
    for v in list(map(int, input().split()))[1:]:
        sum += v - 1

    print(sum)