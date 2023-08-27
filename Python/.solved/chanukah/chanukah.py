N = int(input())

for _ in range(N):
    k, d = map(int, input().split())
    print(k, (sum(range(1,d)) + d + d))