
class FenwickTree:
    A = []
    N = 0

    def __init__(self, n):
        self.A = [0 for _ in range(n + 1)]
        self.N = n + 1

    def flip(self, i):
        add = -1 if self.get(i) > 0 else 1
        while i < N:
            self.A[i] += add
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s

    def get(self, i):
        return self.prefix_sum(i) - self.prefix_sum(i - 1)

    def query(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

N, K = map(int, input().split())

tree = FenwickTree(N)

for _ in range(K):
    inp = input()
    if inp.startswith("F"):
        tree.flip(int(inp.split()[1]))
    else:
        print(str(tree.query(int(inp.split()[1]), int(inp.split()[2]))))
