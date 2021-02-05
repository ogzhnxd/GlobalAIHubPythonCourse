##################################################
## Global AI Hub Introduction to Python Programming Course
## Day 4 Homework Assignment 1
## Find prime number between "0" and "100"
##################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
##################################################

# Function to check if number is prime
def isPrime(num):
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


def primeNumbers(n):
    # Informing user
    print("Finding prime numbers between 0 and", n)
    # Checking numbers from "0" to "n"
    for i in range(1, n + 1):
        # Checking if "i" is a prime number, if it is printing it
        if isPrime(i):
            print(i)

# Sending "100" to primeNumber function to find prime number between 0-100
primeNumbers(100)
