HowMany = int(input())
car_owners = {}


for i in range(HowMany):
    commands = input().split()



    if commands[0] == "register":
        key = commands[1]
        value = commands[2]
        if key in car_owners:
            print(f"ERROR: already registered with plate number {value}")
        else:
            print(f"{key} registered {value} successfully")
            car_owners[key] = value
    elif commands[0] == "unregister":
        key = commands[1]
        if  key not in car_owners:
            print(f"ERROR: user {key} not found")
        else:
            print(f"{key} unregistered successfully")
            del car_owners[key]

for key, value in car_owners.items():
    print(f"{key} => {value}")
