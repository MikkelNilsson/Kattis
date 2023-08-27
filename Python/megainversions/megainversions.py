class FenwickTree:

    def __init__(self, n):
        self.A = [0 for _ in range(n + 1)]

    def get(self, i):
        return self.prefix_sum(i) - self.prefix_sum(i - 1)

    def update(self, i, k):
        self.add(i, k - self.get(i))

    def add(self, i, k):
        s = 0
        while i < len(self.A):
            self.A[i] += k
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s

    def query(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)


n = int(input())+1

smallerR = FenwickTree(n)
biggerL = FenwickTree(n)
num = 0

array = map(int, input().split())

for i in array:
    smallerR.add(i, 1)

print(smallerR.A, biggerL.A)

for i in array:
    smallerR.update(i, smallerR.get(i) - 1)
    num += min(smallerR.query(1,i), biggerL(i, n-1))
    biggerL.add(i, biggerL.get(i)+1)


print(num)
print(smallerR.A, biggerL.A)