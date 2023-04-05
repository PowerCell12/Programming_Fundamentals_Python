population = list(map(int, input().split(", ")))
minimum = int(input())
biggest = 0
counter = 0

for i in range(0, len(population)):
    for j in range(0, len(population)):
        if population[j] > biggest:
            biggest = population[j]
            index = j
    if biggest - (minimum - population[i]) < minimum:
        print("No equal distribution possible")
        counter += 1
        break
    if population[i] < minimum and biggest - (minimum - population[i]) >= minimum:
         population[index] = population[index] - (minimum - population[i])
         population[i] = minimum

    biggest = 0

if counter == 0:
    print(population)
