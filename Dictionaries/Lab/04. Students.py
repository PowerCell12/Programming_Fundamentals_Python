students = {}
command = []
list1 =[]

while True:
  command = input()

  if ":" not in command:
    break
  else:
    command = command.split(":")

  name, id = command[0], command[1]

  list1.append(command[2])
  students[name] = id

counter =0
if command == "programming_basics":
  command = "programming basics"


for key, value in students.items():
  if list1[counter] == command:
      print(f"{key} - {value}")
  counter += 1
