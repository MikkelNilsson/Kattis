import sys

d = dict()

def findval(s):
    return d.get(s, 1004)

def findvar(v):
    for p in d.items():
        if p[1] == v:
            return p[0]

    return "unknown"


def calc(s):
    sum = 0
    op = ""
    val = 0
    unknown = False
    for c in s:
        if c == '+' or c == '-' or c == '=':
            if op == "-" :
                sum -= val
            else:
                sum += val
            op = c
        else:
            val = findval(c)
            if val > 1000:
                unknown = True
                break

    res = " ".join(s) + " "
    if unknown:
        res += "unknown"
        return res
    else:
        return res + findvar(sum)




for line in sys.stdin:
    l = line.split()
    if l[0] == "def":
        d.update({l[1]: int(l[2])})
    elif l[0] == "calc":
        s = l[1:]
        print(calc(s))
    elif l[0] == "clear":
        d = dict()