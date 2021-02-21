###########################################################
## Global AI Hub Introduction to Python Programming Course
## Day 2 Homework Assignment 1
## 3x3 Matrix with Random Prime Numbers
###########################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###########################################################

# Importing needed module
import random as rand

# Initialising 3x3 matrix and variables
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
alreadyInMatrix = []
randStart, randEnd = 0, 100
# Nested for loop for assigning random prime numbers to the matrix
for i in range(3):
    for j in range(3):
        # A while loop to check if random number is prime
        while True:
            # Generating a random number
            randomNumber = rand.randint(randStart, randEnd)
            check = True
            # Returning False if number is "1"
            if randomNumber == 1 or randomNumber == 0:
                check = False
            # Checking is number is prime
            for k in range(2, randomNumber):
                # If number is divisible with any number other than itself returning false
                if randomNumber % k == 0:
                    check = False
                # If number isn't divisible with "k" keep trying other numbers
                else:
                    continue
            # If random number is prime and it's not already in the matrix assigning it to the matrix
            if check and randomNumber not in alreadyInMatrix:
                matrix[i][j] = randomNumber
                alreadyInMatrix.append(randomNumber)
                break
            # Else generating a new random number
            else:
                continue

# Printing the generated 3x3 Matrix
print("{}\n".format(matrix))

for i in matrix:
    print(i)
