ToBuy = {}
final = {}

while True:
  command = input()

  if command == "buy":
    break

  command = command.split(" ")

  
  if command[0] not in ToBuy:
    ToBuy[command[0]] = []
    ToBuy[command[0]].append(float(command[1]))
    ToBuy[command[0]].append(float(command[2]))
  else:
    ToBuy[command[0]][0] = float(command[1])
    ToBuy[command[0]][1] = ToBuy[command[0]][1] + float(command[2])


for key,value in ToBuy.items():
  final[key] = value[0] * value[1]


for name, price in final.items():
  print(f"{name} -> {price:.2f}")
