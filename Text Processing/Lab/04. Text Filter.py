banned = input().split(", ")
text = input()

for word in banned:

    while word in text:
        final = len(word)  * '*'
        text = text.replace(word, final)


print(text)
