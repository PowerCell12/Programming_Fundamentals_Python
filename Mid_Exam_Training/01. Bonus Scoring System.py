how_many = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
highest = 0
highest_attendenteice = 0

for i in range(0, how_many):
    lectures_went_to = int(input())

    total_bonus = (lectures_went_to / number_of_lectures) * (5 + additional_bonus)
    if total_bonus > highest:
        highest = total_bonus
        highest_attendenteice = lectures_went_to


print(f"Max Bonus: {highest:.0f}.")
print(f"The student has attended {highest_attendenteice:.0f} lectures.")
    
