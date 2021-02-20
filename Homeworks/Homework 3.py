##################################################
## Global AI Hub Introduction to Python Programming Course
## Day 4 Homework Assignment 1
## Find prime number between "0" and "1000"
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

# Function to check if number is prime
def prime_first(num):
    # Returning False if number is "1"
    if num == 1:
        return False

    # Checking is number is prime
    for i in range(2, num):
        # If number is divisible with any number other than itself returning false
        if num % i == 0:
            return False
        # If number isn't divisible with "i" keep trying other numbers
        else:
            continue
    # If number wasn't divisible with none of the "i"s that mean it's a prime number returning true
    return True


def prime_second(num):
    # Returning False if number is "1"
    if num == 1:
        return False

    # Checking is number is prime
    for i in range(2, num):
        # If number is divisible with any number other than itself returning false
        if num % i == 0:
            return False
        # If number isn't divisible with "i" keep trying other numbers
        else:
            continue
    # If number wasn't divisible with none of the "i"s that mean it's a prime number returning true
    return True


endValue = 1000
# Informing user
print("Finding prime numbers between 0 and", endValue + 1)
# Checking numbers from "0" to "n"
for i in range(1, endValue + 1):
    # Checking if "i" is a prime number and is between 0 and 500, if it is printing it
    if prime_first(i) and 0 < i < 500:
        print(i)
    # Checking if "i" is a prime number and is between 500 and 1000, if it is printing it
    elif prime_second(i) and 500 < i < 1000:
        print(i)
