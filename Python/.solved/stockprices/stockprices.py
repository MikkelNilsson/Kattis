
class Heap:
    def __init__(self, comparefunction):
        self.compare = comparefunction
        self.A = [(-1, -1)] * 1000
        self.N = 0

    def insert(self, num):
        self.A[self.N] = num
        self.N += 1
        self.bubble(self.N-1)

    def bubble(self, index):
        if index <= 0:
            return
        parent = int((index - (2 - (index % 2)))/2)
        if self.compare(self.A[index], self.A[parent]):
            tmp = self.A[parent]
            self.A[parent] = self.A[index]
            self.A[index] = tmp
            self.bubble(parent)

    def pop(self):
        self.N -= 1
        res = self.A[0]
        self.A[0] = self.A[self.N]
        self.A[self.N] = (-1, -1)
        
        self.sink(0)
        return res

    def peak(self):
        return self.A[0]


    def sink(self, index):
        c1 = index * 2 + 1
        c2 = index * 2 + 2
        if c1 <= self.N-1 and c2 <= self.N-1 and self.compare(self.A[c2], self.A[c1]):
            if self.compare(self.A[c2], self.A[index]):
                tmp = self.A[c2]
                self.A[c2] = self.A[index]
                self.A[index] = tmp
                self.sink(c2)
        elif c1 <= self.N-1 and self.compare(self.A[c1], self.A[index]):
            tmp = self.A[c1]
            self.A[c1] = self.A[index]
            self.A[index] = tmp
            self.sink(c1)
        elif c2 <= self.N-1 and self.compare(self.A[c2], self.A[index]):
            tmp = self.A[c2]
            self.A[c2] = self.A[index]
            self.A[index] = tmp
            self.sink(c2)




def max(i1, i2):
    return i1[0] > i2[0]

def min(i1, i2):
    return i1[0] < i2[0]



N = int(input())

for _ in range(N):

    ask = Heap(min)
    bid = Heap(max)
    latest_buy_price = "-"

    T = int(input())

    for _ in range(T):
        inp = input().split()
        transaction = (inp[0] == "sell", int(inp[1]), int(inp[4]))
        if transaction[0]:
            ask.insert((transaction[2], transaction[1]))
        else:
            bid.insert((transaction[2], transaction[1]))

        madedeal = True
        while madedeal:
            madedeal = False
            if ask.N > 0 and bid.peak()[0] >= ask.peak()[0]:
                if ask.peak()[1] > bid.peak()[1]:
                    ask.A[0] = (ask.peak()[0], ask.peak()[1] - bid.peak()[1])
                    latest_buy_price = ask.peak()[0]
                    bid.pop()
                    madedeal = True
                elif ask.peak()[1] < bid.peak()[1]:
                    bid.A[0] = (bid.peak()[0], bid.peak()[1] - ask.peak()[1])
                    latest_buy_price = ask.pop()[0]
                    madedeal = True
                else:
                    bid.pop()
                    latest_buy_price = ask.pop()[0]
                    madedeal = True
        
        print(ask.peak()[0] if ask.peak()[0] > -1 else "-", bid.peak()[0] if bid.peak()[0] > -1 else "-", latest_buy_price)





        

