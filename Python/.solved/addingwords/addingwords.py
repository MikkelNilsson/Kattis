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
    var = ""
    unknown = False
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-' or s[i] == '=':
            val = findval(var)
            if val > 1000:
                unknown = True
                break
            if op == "-" :
                sum -= val
            else:
                sum += val
            op = s[i]
            var = ""
        else:
            var += s[i]

    s = s.replace("+", " + ").replace("-", " - ").replace("=", " = ")
    if unknown:
        s += "unknown"
        return s
    else:
        return s + findvar(sum)




for line in sys.stdin:
    l = line.split()
    if l[0] == "def":
        d.update({l[1]: int(l[2])})
    elif l[0] == "calc":
        s = ''.join(l[1:])
        print(calc(s))
    elif l[0] == "clear":
        d = dict()