lines = int(input())
dict_cars = {}

## first is mileage then fuel
for i in range(lines):

  cars = input().split("|")


  dict_cars[cars[0]] = []
  dict_cars[cars[0]].append(int(cars[1]))
  dict_cars[cars[0]].append(int(cars[2]))

while True:

  commands = input().split(" : ")

  if commands[0] == "Stop":
    break


  if commands[0] == "Drive":
    if int(commands[3])  > dict_cars[commands[1]][1]:
      print("Not enough fuel to make that ride")
    else:
      dict_cars[commands[1]][0] += int(commands[2])
      dict_cars[commands[1]][1] -= int(commands[3])
      print(f"{commands[1]} driven for {commands[2]} kilometers. {commands[3]} liters of fuel consumed.")

    if dict_cars[commands[1]][0] >= 100000:
      print(f"Time to sell the {commands[1]}!")
      del dict_cars[commands[1]]


  if commands[0] == "Refuel":
    previos = dict_cars[commands[1]][1]
    
    dict_cars[commands[1]][1] += int(commands[2])
    if dict_cars[commands[1]][1] >  75:
      dict_cars[commands[1]][1] = 75

    filled_up = dict_cars[commands[1]][1] - previos
    print(f"{commands[1]} refueled with {filled_up} liters")

  if commands[0] == "Revert":
    dict_cars[commands[1]][0] -= int(commands[2])
    if dict_cars[commands[1]][0] < 10000:
      dict_cars[commands[1]][0] = 10000    
      continue
    print(f"{commands[1]} mileage decreased by {commands[2]} kilometers")


for key,value in dict_cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
