password = input()
key1 = False
key2 = False
key3 = False


if len(password) < 6 or len(password) > 10:
    print("Password must be between 6 and 10 characters")
else:  
    key1 = True


import re



if re.match("^[A-Za-z0-9_-]*$", password):
    key3 = True
else:
    print("Password must consist only of letters and digits")


new_string = ''.join(filter(lambda x:  x.isdigit(), password))

if len(new_string) < 2:
    print("Password must have at least 2 digits")
else:
    key2 = True



if key3 and key2 and key1:
    print("Password is valid")
