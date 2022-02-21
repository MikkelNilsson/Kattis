distinct = set()

for i in range(10):
    distinct.add(int(input()) % 42)

print(len(distinct))