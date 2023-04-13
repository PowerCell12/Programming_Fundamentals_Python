Course_Name = {}

while True:
    command = input()

    if command == "end":
        break 

    command = command.split(" : ")


    if command[0] not in Course_Name:
        Course_Name[command[0]] = []
    Course_Name[command[0]].append(command[1])

for key, value in Course_Name.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
