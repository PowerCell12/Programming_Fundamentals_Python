string = input()

while True:
    commands = input().split(" ")
    new_pass = ""
    to_cut = ""
  
    if commands[0] == "Done":
        print(f"Your password is: {string}")
        break

    if commands[0] == "TakeOdd":
        for i in range(1, len(string), 2):
            new_pass += string[i]
        string = new_pass
        print(new_pass)
  
    if commands[0] == "Cut":
      to_cut = string[int(commands[1]):int(commands[1]) + int(commands[2])]
      string = string.replace(to_cut, "", 1)

      print(string)

    if commands[0] == "Substitute":
      if commands[1] in string:
        string = string.replace(commands[1], commands[2])
        print(string)
      else:
        print("Nothing to replace!")
