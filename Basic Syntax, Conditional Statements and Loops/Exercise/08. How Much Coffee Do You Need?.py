coffess = 0

while True:
    thingstodo = str(input())
 
    if thingstodo == "END":
        if coffess > 5:
            print("You need extra sleep")
            break
        print(coffess)
        break

    if thingstodo.islower():    
       if thingstodo == "coding" or thingstodo == "dog" or thingstodo == "cat" or thingstodo == "movie":
          coffess += 1
       

    if thingstodo.isupper():
     if thingstodo == "CODING" or thingstodo == "DOG" or thingstodo == "CAT" or thingstodo == "MOVIE":
        coffess += 2
