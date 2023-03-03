people = int(input())
capasity = int(input())
counter = 0
people1 = 0

while True:
 if people <= capasity:
    counter = 1
    print(counter)
    break

 if people > capasity:
    final = people / capasity
    people1 = people
    counter +=  1
    if counter == 1:
      final2 = people1 - capasity
    if counter > 1:
     final2 = people2 - capasity
    people2 = final2
    final2 = people2


    if final2 < capasity:
      if final2 > 0:
         counter += 1 
         print(counter)
         break
      print(counter)
      break
