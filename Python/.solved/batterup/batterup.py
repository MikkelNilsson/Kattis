N = int(input())
sum = 0

for i in map(int, input().split()):
    if i < 0:
        N -= 1
    else:
        sum += i

print(sum/N)