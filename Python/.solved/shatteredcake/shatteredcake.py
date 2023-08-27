w = int(input())

n = int(input())

area = 0
for _ in range(n):
    wi, l = map(int, input().split())
    area += wi * l
    
print(int(area / w))