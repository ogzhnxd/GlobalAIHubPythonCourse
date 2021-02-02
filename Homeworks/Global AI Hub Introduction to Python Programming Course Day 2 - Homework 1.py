###########################################################
## Global AI Hub Introduction to Python Programming Course
## Day 2 Homework Assignment 1
## Split Lists from half and add them together in reverse
###########################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###########################################################

# Creating list
myList = list(range(10))

print("Your List : ", myList)

# Finding the lenght of list
n = len(myList)

# Finding the half of list length for indexing later
half = int((n-1)/2)

# Creating two empty lists
listPart1 = []
listPart2 = []

# Loop for splitting list into two parts
for i in range(0, half+1):

    # Generating first half of the list
    listPart1.append(i)
    # Generating second half of the list
    listPart2.append(i+half+1)

# Adding the second part of the list to first half to get new reversed list
newList = listPart2 + listPart1

# Printing the new reversed list
print(" New list : ", newList)
