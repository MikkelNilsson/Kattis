#dynamic programming 

t = int(input())
INF = 10**6

def run():
    price = int(input())
    n = int(input())
    coins = [int(input()) for _ in range(n)] #recursive version of dynamic programming

    cache = dict()
    def minimum_coins(p, k):
        #recursive step
        if p == 0:
            return 0
        if p < 0 or k < 0: 
            return  INF
        if (p, k) in cache:
            return cache[(p,k)]
        result = min(minimum_coins(p, k-1), minimum_coins(p-coins[k], k-1) + 1)
        cache[(p,k)] = result
        return result



    for x in range(price, 20000):
        if minimum_coins(x, n-1) < INF:
            print(x, minimum_coins(x, n-1))
            break


for _ in range(t): 
    run()