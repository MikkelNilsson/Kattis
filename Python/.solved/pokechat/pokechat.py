s = input()

code = input()

message = ""
for i in range(0, len(code), 3):
    message += s[int(code[i:i+3]) - 1]

print(message)