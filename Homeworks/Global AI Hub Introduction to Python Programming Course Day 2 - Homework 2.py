###############################################################
## Global AI Hub Introduction to Python Programming Course
## Day 2 Homework Assignment 2
## Printing out even numbers that in the length of user input
###############################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###############################################################

# Initiating variables
n = 0
evenNumber = 0

# Infinite loop
while True:

    # Getting input from user
    n = int(input("Enter a natural number between 0-10 (not including 10) : "))

    # Rejecting input if input is not between 0-10
    if not (0 <= n < 10):
        print("The number you have entered is not between 1-10 please try again")
        continue

    # Calculating even numbers until input if input is between 0-10
    elif 0 < n < 10:
        # For loop for calculating even numbers
        for i in range(1, n + 1):
            # Printing even number
            print(evenNumber)
            # Adding 2 to it for next even number
            evenNumber = evenNumber + 2
            # Breaking out of for loop if we exceed user input
            if evenNumber > n:
                break
        # Breaking out of infinite loop if we exceed user input
        break

    # Printing "0" and getting out of infinite loop if the input is "0"
    else:
        print(0)
        break
