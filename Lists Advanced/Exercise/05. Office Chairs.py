rooms = int(input())
counter = 0
chairs_left = 0
boot = True


for i in range(1, rooms + 1):
    counter += 1
    chairs_and_people = input().split()
    chairs = len(chairs_and_people[0])
    people = chairs_and_people[1] 
    people1 = int(people)
    if chairs >= people1:
        chairs_left += chairs - people1
    else:
        chairs_needed = people1 - chairs
        print(f"{chairs_needed} more chairs needed in room {counter}")
        boot = False

if boot:
    print(f"Game On, {chairs_left} free chairs left")
