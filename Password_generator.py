import random
import string
def passwordGenerator(length=8, use_upper=True, use_lower=True, use_numbers=True, use_special=True):
    
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        # characters += string.punctuation
        characters += '@!?#&*$=/'
    if characters == '':
        print('Error: No character types selected.')
        return 
    password = ''.join(random.choice(characters) for i in range(length))
    return password
copy_of_password = passwordGenerator(12)
# passwordList = list(copy_of_password)

with open("password.txt", "w") as f:
    # f.write(str(passwordList))
    f.write(copy_of_password+"\n")
print(copy_of_password)