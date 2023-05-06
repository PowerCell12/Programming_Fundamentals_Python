## For 30 days 
food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
food1 = food
counter = 0

weight = float(input()) * 1000
success = True

for i in range(1, 31):
    counter  += 1
    food = food1 - 300
    food1 = food

    if counter % 2 == 0:
      needed_hay = food * 0.05
      hay = hay - needed_hay

    if counter % 3 == 0:
        cover_needed = weight * (1 / 3)
        cover = cover - cover_needed

    if cover < 1 or hay < 1 or food < 1:
        print("Merry must go to the pet store!")
        success = False
        break

if success:
    food_left = food  / 1000
    hay_left = hay / 1000
    cover_left = cover / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_left:.2f}, Hay: {hay_left:.2f}, Cover: {cover_left:.2f}.")
