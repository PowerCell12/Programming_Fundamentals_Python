key = input()

while True:
  commands = input().split(">>>")

  if commands[0] == "Generate":
    break

  if commands[0] == "Contains":
    if commands[1] in key:
      print(f"{key} contains {commands[1]}")
    else:
      print("Substring not found!")

  if commands[0] == "Flip":
    if commands[1] == "Upper":
      key1 = key[int(commands[2]):int(commands[3])]
      key1 = key1.upper()
      key = key[:int(commands[2])] + key1 + key[int(commands[3]):]

      print(key)

    if commands[1] == "Lower":
      key1 = key[int(commands[2]):int(commands[3])]
      key1 = key1.lower()
      key = key[:int(commands[2])] + key1 + key[int(commands[3]):]

      print(key)

  if commands[0] == "Slice":
    key = key[:int(commands[1])] + key[int(commands[2]):]

    print(key)

print(f"Your activation key is: {key}")
