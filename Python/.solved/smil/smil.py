from re import I


v = input()

start = 0
insmile = False

for i, c in enumerate(v):
    if c == ':' or c == ';':
        start = i
        insmile = True
    elif insmile and c == ')':
        print(start)
        insmile = False
    elif insmile and c == '-':
        pass
    else:
        insmile = False
