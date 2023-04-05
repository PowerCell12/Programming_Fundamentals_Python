lessons = input().split(", ")
with_exercises = []
index_exercises = 0

while True:

    commands = input().split(":")
    boolean  = False

    if commands[0] == "course start":
        break

    if commands[0] == "Add":
        if commands[1] not in lessons:
            lessons.append(commands[1])

    if commands[0] == "Insert":
        if commands[1] not in lessons:
            lessons.insert(int(commands[2]), commands[1])

    if commands[0] == "Remove":
        if commands[1] in lessons:
    
            if commands[1] in with_exercises:
                index = lessons.index(commands[1])
                lessons.remove(commands[1])
                lessons.pop(index)
                with_exercises.remove(commands[1])
            else:
                lessons.remove(commands[1])

    if commands[0] == "Swap":
        if commands[1] in lessons and commands[2] in lessons:

            if commands[1] in with_exercises or commands[2] in with_exercises:
                if commands[1] in with_exercises:
                    index  = lessons.index(commands[1])
                    index_exercises = index + 1
                    index1 = lessons.index(commands[2])
                    
                    lessons[index], lessons[index1] = lessons[index1], lessons[index]
                    final = lessons.pop(index_exercises)
                    lessons.insert(index1 + 1, final)
                
                elif commands[2] in with_exercises:
                    index = lessons.index(commands[2])
                    index_exercises = index + 1
                    index1 = lessons.index(commands[1])

                    lessons[index], lessons[index1] = lessons[index1], lessons[index]
                    final = lessons.pop(index_exercises)
                    lessons.insert(index1 + 1, final)

            else:
                index1 = lessons.index(commands[1])
                index2 = lessons.index(commands[2])

                lessons[index1], lessons[index2] = lessons[index2], lessons[index1]

    if commands[0] == "Exercise":

        ## there is an error here (in exercise)

        if commands[1] in lessons:
                index3  = lessons.index(commands[1]) + 1

                lesssons = lessons.insert(index3, f"{commands[1]}-Exercise")
                with_exercises.append(commands[1])             
        elif commands[1] not in lessons:
            lessons.append(commands[1])
            lessons.insert(len(lessons), f"{commands[1]}-Exercise")
            with_exercises.append(commands[1])


for j in range(len(lessons)):
    index = j + 1
    print(f"{index}.{lessons[j]}", end="\n")
