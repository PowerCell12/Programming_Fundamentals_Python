
import math

cards = str(input())
cards = cards.split()
number_of_shuffles = int(input())

while True:
    number_of_shuffles -= 1
    if number_of_shuffles == -1:
        break

    middle_index = len(cards) / 2
    middle_index = math.trunc(middle_index)

    first_half = cards[:middle_index].copy()
    second_half = cards[middle_index:].copy()
    cards = []
    index = 0
    while len(first_half) > 0 and len(second_half) > 0:
        current_fist_card = first_half.pop(index)
        current_second_card = second_half.pop(index)
        cards.append(current_fist_card)
        cards.append(current_second_card)

print(cards)
