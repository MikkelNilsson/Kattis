import sys
from collections import defaultdict
import time
sys.setrecursionlimit(10**6)

start = time.time()
input = sys.stdin.readline

table = dict()



#red black search tree
class red_black_node:
    def __init__(self, value, color, left, right):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
    
    def isRed(self):
        return self.color

    def compare(self, num):
        return self.value.compare(num)

    def split(self, num, depth):
        (i1, i2) = self.value.split(num)
        if i1 is not None and i2 is not None:
            less = red_black_node(i1, True, self.left, None)
            table[str(less.value)] = depth + 1
            larger = red_black_node(i2, self.color, less, self.right)
            table[str(larger.value)] = depth + 1
        elif i1 is None and i2 is not None:
            larger = red_black_node(i2, self.color, self.left, self.right)
            table[str(larger.value)] = depth + 1
        elif i1 is not None and i2 is None:
            less = red_black_node(i1, self.color, self.left, self.right)
            larger = less
            table[str(larger.value)] = depth + 1
        elif self.left is not None or self.right is not None:
            larger = self
        else:
            larger = None

        return larger

    def rotate_right(self):
        x = self.left
        self.left = x.right
        x.right = self
        x.color = self.color
        self.color = True
        return x


    def flip_colors(self):
        self.left.color = not self.left.color
        self.right.color = not self.right.color
        self.color = not self.color
        
    def rotate_left(self):
        x = self.right
        self.right = x.left
        x.left = self
        x.color = self.color
        self.color = True
        return x


class red_black_tree:
    def __init__(self, N):
        self.root = red_black_node(interval(1, N), "black", None, None)
        self.N = N
        table[str(self.root.value)] = 0

    def insert(self, num):
        (self.root, c) = insertrec(self.root, num)
        if self.root is not None:
            self.root.color = False
        return c
        """try:
            (self.root, c) = insertrec(self.root, num)
            self.root.color = False
            return c
        except:
            print(table)
            return 0"""

    def print(self):
        queue = []
        queue.append((self.root if self.root is not None else (red_black_node("empty", True, None, None)),0))
        l = defaultdict(str)
        depth = 0
        while len(queue) > 0:
            elem = queue.pop(0)
            l[elem[1]] += str(elem[0].value) + "  |  "
            if not (elem[0].left == None and elem[0].right == None and elem[0].value == "empty"):
                if elem[0].left == None:
                    queue.append((red_black_node("empty", True, None, None), elem[1] + 1))
                else:
                    queue.append((elem[0].left, elem[1] + 1))

                if elem[0].right == None:
                    queue.append((red_black_node("empty", True, None, None), elem[1] + 1))
                else:
                    queue.append((elem[0].right, elem[1] + 1))

        print("\n".join([str(i) + ":  " + v for i, v in enumerate(l.values())]), "\n")






def insertrec(node, num):
    c = -1
    compare = node.compare(num)
    if compare < 0:
        (node.left, c) = insertrec(node.left, num)
    elif compare > 0:
        (node.right, c) = insertrec(node.right, num)
    elif compare == 0:
        depth = table[str(node.value)]
        c = depth
        node = node.split(num, depth)

    if node is None:
        return (node, c)

    if (node.right is not None and node.right.isRed()) and (node.left is not None and not node.left.isRed()):
        node = node.rotate_left()
    if (node.left is not None and node.left.isRed()) and (node.left.left is not None and node.left.left.isRed):
        node = node.rotate_right()
    if (node.left is not None and node.left.isRed()) and (node.right is not None and node.right.isRed()):
        node.flip_colors()

    return (node, c)





class interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
    def compare(self, num):
        if self.low > num:
            return -1
        elif self.high < num:
            return 1
        else:
            return 0

    def split(self, num):
        return ((interval(self.low, num-1) if (num - 1) - self.low >= 0 else None), (interval(num + 1, self.high) if self.high - (num + 1) >= 0 else None))

    def __str__(self):
        return str(self.low) + "-" + str(self.high)
        
        
fin = open("Geninput/bst.large.in")
count = 0
N = int(input())
N = int(fin.readline())
print(N)
maxinsert = 0
t = red_black_tree(N)
output = ""

for i in range(N):
    #inp = int(input())
    inp = int(fin.readline())
    #print(str(i) + ": ", str(inp), "\n_____________________\n")
    t.print()
    #maxinsert = max(maxinsert, t.insert(inp))
    count += t.insert(inp)
    output += str(count) + "\n"
    #print(i)

#print(output.strip("\n"))
print(time.time()-start)
f = open("Geninput/bst.large2.ans", "w")
f.write(output.strip("\n"))

#t.print()
#print(maxinsert)


"""count += t.insert(3)
print(count)
count += t.insert(2)
print(count)
count += t.insert(4)
print(count)
count += t.insert(5)
print(count)
count += t.insert(1)
print(count)

print(table)"""