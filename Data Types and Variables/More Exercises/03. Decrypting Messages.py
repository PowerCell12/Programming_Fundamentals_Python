key = int(input())
lines = int(input())
message  = []


for i in range(lines):
    letter = input()
    letter = ord(letter)
    final = letter + key
    final = chr(final)
    message.append(final)


print(''.join(message))
