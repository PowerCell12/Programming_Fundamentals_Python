happiness = list(map(int, input().split(" ")))
factor  = int(input())
counter = 0
average = 0

for i in range(0, len(happiness)):
    happiness[i] = happiness[i] * factor

    average += happiness[i]
    counter += 1


average = average / counter
counter1 = 0


for i in range(0, len(happiness)):
    if happiness[i] >= average:
        counter1 += 1


if counter1 >= int(len(happiness) / 2):
    print(f"Score: {counter1}/{counter}. Employees are happy!")
else:
    print(f"Score: {counter1}/{counter}. Employees are not happy!")
