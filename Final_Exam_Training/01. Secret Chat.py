message = input()

while True:
  command = input().split(":|:")

  if command[0] == "Reveal":
    break

  if command[0] == "InsertSpace":
    message = message[:int(command[1])] + " " + message[int(command[1]):]
    print(message)
  
  if command[0] == "Reverse":
    if command[1] in message:
      message = message.replace(command[1], "", 1)
      message1 = command[1]
      message1 = message1[::-1]
      message = message + message1
      print(message)
    else:
      print("error")


  if command[0] == "ChangeAll":
    message = message.replace(command[1], command[2])
    print(message)

print(f"You have a new text message: {message}")
