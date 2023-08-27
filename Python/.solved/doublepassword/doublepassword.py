pass1 = input()
pass2 = input()
diff = 0
for i in range(4):
    if pass1[i] != pass2[i]:
        diff += 1

print(2**diff)