message = input()

while True:
  commands = input().split("|")


  if commands[0] == "Decode":
    break


  if commands[0] == "Move":
      to_move = int(commands[1])

      message2 =  message[:to_move]
      message = message[to_move:]
      message = message + message2

  if commands[0] == "Insert":
      message = message[:int(commands[1])] + commands[2] + message[int(commands[1]):]

  if commands[0] == "ChangeAll":
    message = message.replace(commands[1], commands[2])


print(f"The decrypted message is: {message}")
