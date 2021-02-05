###############################################################
## Global AI Hub Introduction to Python Programming Course
## Day 3 Homework Assignment 1
## Username Password Interface but with Dictionaries
###############################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###############################################################

# Defining username and password
defUserInfo = { "username": "aCoolUsername",
                "password": "aCoolPassword"}

# Taking username and password from user as inputs
username = input("Enter your username : ")
password = input("Enter your password : ")

# Looping until user enters his username and password correctly
while defUserInfo["username"] != username and defUserInfo["password"] != password:

    # If password is wrong inform user and ask user for username and password again
    if defUserInfo["username"] == username and defUserInfo["password"] != password:
        print("Username isn't correct please try again")
        username = input("Enter your username : ")
        password = input("Enter your password : ")
    # If username is wrong inform user and ask user for username and password again
    elif defUserInfo["username"] != username and defUserInfo["password"] == password:
        print("Username isn't correct please try again")
        username = input("Enter your username : ")
        password = input("Enter your password : ")
    # If both username and password is wrong inform user and ask user for username and password again
    else:
        print("Username or password isn't correct please try again")
        username = input("Enter your username : ")
        password = input("Enter your password : ")

# If both username and password is correct inform user and finish program
if defUserInfo["username"] == username and defUserInfo["password"] == password:
    print("Welcome,", defUserInfo["username"])
