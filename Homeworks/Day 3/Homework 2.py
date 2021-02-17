###############################################################
## Global AI Hub Introduction to Python Programming Course
## Day 3 Homework Assignment 1
## Username Password Interface
###############################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###############################################################

# Initializing variables
studentGrades = []
studentNames = []
studentAverages = []
gradeSum = 0
info = {}

# Getting student information from user
for i in range(5):
    studentName = input("Enter student's name : ")
    studentSurname = input("Enter student's surname : ")
    temp = [studentName, studentSurname]
    studentNames.append(temp)
    studentMidTermGrade = int(input("Enter student's mid term grade : "))
    studentFinalGrade = int(input("Enter student's mid term grade : "))
    studentHomeworkGrade = int(input("Enter student's mid term grade : "))
    temp = [studentMidTermGrade, studentFinalGrade, studentHomeworkGrade]
    studentGrades.append(temp)

# Printing student info
print(studentNames)
print(studentGrades)

# From grades generating an average score for all students
for grades in studentGrades:
    for grade in grades:
        gradeSum += grade
        gradeAvg = gradeSum / 3
        # Rounding the value
        gradeAvg = round(gradeAvg, 2)

    studentAverages.append(gradeAvg)
    gradeSum = 0

# Printing average scores
print(studentAverages)

# Sorting all info lists using selection sort
for i in range(len(studentAverages)):
    # Selecting the first index value as minimum
    minimum = i

    # Iterating over the list to find smallest value
    for j in range(i + 1, len(studentAverages)):
        # Selecting the smallest value
        if studentAverages[j] < studentAverages[minimum]:
            minimum = j

    # Placing it at the front of the sorted end of the array
    studentNames[minimum], studentNames[i] = studentNames[i], studentNames[minimum]

    # Applying the same change to the other lists
    studentGrades[minimum], studentGrades[i] = studentGrades[i], studentGrades[minimum]
    studentAverages[minimum], studentAverages[i] = studentAverages[i], studentAverages[minimum]

# Reversing all of the list to get descending order
studentNames.reverse()
studentGrades.reverse()
studentAverages.reverse()

# Generating info dictionary using sorted lists
for i in range(5):
    temp = [studentGrades[i], studentAverages[i]]
    info[f"{studentNames[i][0]} {studentNames[i][1]}"] = temp

# Printing info dictionary
print(info)

# Congratulating the student with highest average score
print("Congratulations {} {} you have the highest score of all the students".format(studentNames[0][0], studentNames[0][1]))
