items_others = {}
name = " "
key_items = {}
number_shards = 0
number_motes = 0
number_fragments = 0

while True:
  Items_Quantity = input().split(" ")

  for i in range(1, len(Items_Quantity) + 1, 2):
      current = Items_Quantity[i].lower()

      if current == "shards" or current == "fragments" or current == "motes":
        if current not in key_items:
          key_items[current] = int(Items_Quantity[i - 1])
        else:
          key_items[current] = int(key_items[current] + int(Items_Quantity[i - 1]))
      else:
        if current not in items_others:
          items_others[current] = int(Items_Quantity[i - 1])
        else:
          items_others[current] = int(items_others[current] + int(Items_Quantity[i - 1]))

      if current == "shards" or current == "fragments" or current == "motes":
        if key_items[current] >= 250:
          if current == "shards":
            name = "Shadowmourne"
          elif current == "fragments":
            name = "Valanyr"
          elif current == "motes":
            name = "Dragonwrath"

          key_items[current] = key_items[current] - 250
          
          for key, value in key_items.items():
            if key == "shards":
              number_shards = value
            if key == "fragments":
              number_fragments = value
            if key == "motes":
              number_motes = value

          
          print(f'{name} obtained!')
          print(f"shards: {number_shards}")
          print(f'fragments: {number_fragments}')  
          print(f'motes: {number_motes}')

          for final, final1 in items_others.items():
            print(f'{final}: {final1}')


          quit()
