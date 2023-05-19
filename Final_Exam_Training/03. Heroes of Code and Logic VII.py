numbers_of_heroes = int(input())
dict_heroes = {}

## first is hp and then mp

for i in range(int(numbers_of_heroes)):
  heros = input().split(" ")

  if heros[0] not in dict_heroes:
    dict_heroes[heros[0]] = []
  dict_heroes[heros[0]].append(int(heros[1]))
  dict_heroes[heros[0]].append(int(heros[2]))

  if int(heros[1]) > 100:
    dict_heroes[heros[0]][0] = 100
  
  if  int(heros[2])  > 200:
    dict_heroes[heros[0]][1] = 200


while True:
  commands = input().split(" - ")

  if commands[0] == "End":
    break


  if commands[0] == "CastSpell":
    if dict_heroes[commands[1]][1] >= int(commands[2]):
      dict_heroes[commands[1]][1] -= int(commands[2])
      print(f"{commands[1]} has successfully cast {commands[3]} and now has {dict_heroes[commands[1]][1]} MP!")
    else:
      print(f"{commands[1]} does not have enough MP to cast {commands[3]}!")

  if commands[0] == "TakeDamage":
    dict_heroes[commands[1]][0] -= int(commands[2])

    if dict_heroes[commands[1]][0] <= 0:
      del dict_heroes[commands[1]]
      print(f"{commands[1]} has been killed by {commands[3]}!")
    else:
      print(f"{commands[1]} was hit for {commands[2]} HP by {commands[3]} and now has {dict_heroes[commands[1]][0]} HP left!")


  if commands[0] == "Recharge":
    previos = dict_heroes[commands[1]][1]
    dict_heroes[commands[1]][1] += int(commands[2])
    if dict_heroes[commands[1]][1] > 200:
      dict_heroes[commands[1]][1] = 200

    recovered = dict_heroes[commands[1]][1] - previos
    print(f"{commands[1]} recharged for {recovered} MP!")


  if commands[0] == "Heal":
    previos1 = dict_heroes[commands[1]][0]
    dict_heroes[commands[1]][0] += int(commands[2])
    if dict_heroes[commands[1]][0] > 100:
      dict_heroes[commands[1]][0] = 100

    recovered1 = dict_heroes[commands[1]][0] - previos1
    print(f"{commands[1]} healed for {recovered1} HP!")

for key, value in dict_heroes.items():
  print(key)
  print(f"  HP: {value[0]}")
  print(f"  MP: {value[1]}")
