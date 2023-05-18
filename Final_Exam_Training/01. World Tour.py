string = input()

while True:
  commands = input().split(":")


  if "Travel" in commands:
    print(f"Ready for world tour! Planned stops: {string}")
    break


  if commands[0] == "Add Stop":
    if int(commands[1]) < len(string):
      string = string[:int(commands[1])] + commands[2] + string[int(commands[1]):]
      print(string)
    else:
      print(string)

  if commands[0] == "Remove Stop":
    if int(commands[1]) < len(string) and int(commands[2]) < len(string):
      string = string[:int(commands[1])] + string[int(commands[2]) + 1:]
      print(string)
    else:
      print(string)


  if commands[0] == "Switch":
    if commands[1] in string:
      string = string.replace(commands[1], commands[2])
      print(string)
    else:
      print(string)
