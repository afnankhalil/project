import random

length = int(input("enter the length of the password: "))

def get_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*<>"
    password = ""
    for x in range(0,length):
        password_characters=random.choice(characters)
        password = password + password_characters
    print("the password is: " +password)
    return
        
get_random_password(length)        