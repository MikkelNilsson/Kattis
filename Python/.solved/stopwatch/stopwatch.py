N = int(input())
if N % 2 == 1:
    print("still running")
else:
    sum = 0
    for i in range(int(N/2)):
        sum += -(int(input()) - int(input()))
    print(sum)