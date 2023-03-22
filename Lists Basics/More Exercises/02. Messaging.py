numbers = input().split(' ')
string = input()
message = ""

for number in numbers:
    index = 0
  
    for chrs in number:
      index += int(chrs)


    while index >= len(string):
      index -= len(string)

    final = string[index]

    message += final

  ## can give an error
    string = string[:index] +  string[index + 1:]

print(message)
