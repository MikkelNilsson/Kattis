inp = input()
vowels = 0
for c in inp:
    if c.lower() in ['a', 'e', 'o', 'u', 'i']:
        vowels += 1
print(vowels)