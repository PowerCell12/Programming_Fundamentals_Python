path = input()


for chrs in path:
    if chrs == ".":
        index = path.index(chrs) + 1

extention = path[index :]

final =  path.rindex("\\")

name = path[final + 1:index - 1]

print(f"File name: {name}")
print(f"File extension: {extention}")
