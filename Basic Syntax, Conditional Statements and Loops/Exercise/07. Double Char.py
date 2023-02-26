while True:
    word = str(input())

    if word == "End":
        break

    if word == "SoftUni":
        continue

    repeated_word = ""
    for letter in word:
       repeated_word += letter * 2
    print(repeated_word)
