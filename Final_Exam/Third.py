
dict_followers = {}

# first is likes and them comments
# !!!!!!!!!!!!!!!!!!1
records = 0
while True:

    commands = input().split(": ")

    if commands[0] == "Log out":
        break

    if commands[0] == "New follower":

        if commands[1] in dict_followers.keys():
            pass
        else:
            dict_followers[commands[1]] = []
            dict_followers[commands[1]].append(0)
            dict_followers[commands[1]].append(0)

    if commands[0] == "Like":

        if commands[1] in dict_followers.keys():
            dict_followers[commands[1]][0] += int(commands[2])
        else:
            dict_followers[commands[1]] = []
            dict_followers[commands[1]].append(0)
            dict_followers[commands[1]].append(0)

            dict_followers[commands[1]][0] += int(commands[2])

    if commands[0] == "Comment":

        if commands[1] in dict_followers.keys():
            dict_followers[commands[1]][1] += 1

        else:
            dict_followers[commands[1]] = []
            dict_followers[commands[1]].append(0)
            dict_followers[commands[1]].append(0)
            dict_followers[commands[1]][1] += 1


    if commands[0] == "Blocked":
    

        if commands[1] in dict_followers.keys():
            del dict_followers[commands[1]]
        else:
            print(f"{commands[1]} doesn't exist.")



print(f"{len(dict_followers)} followers")

for key,value in dict_followers.items():

    print(f"{key}: {sum(value)}")
    
