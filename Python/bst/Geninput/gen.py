import random

with open("bst.large.in", "w") as f:
    N = 100000
    f.write(str(N) + "\n")

    Nlist = [i for i in range(1,N+1)]
    random.shuffle(Nlist)
    
    for i in Nlist:
        f.write(str(i) + "\n")
