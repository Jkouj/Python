#2/8 Example

#Given List of 10 grades
#Find average of all failing grades

gradeList = []

#while loop
#        i = 0
#        while i < 10:
#            grade = float(input("Enter grade: "))
#            gradeList.append(grade)
#            i = i + 1
#


#range(0,10) or range(10) starts at 0 and goes up to but not including 10
#for loop
for i in range(10):
    grade = float(input("Enter grade: "))
    gradeList.append(grade)

#Get failing threshold
threshold = float(input("Enter failing threshold: "))

#initialize number of failing grades
numFailing = 0

#initialize total
total = 0

for grade in gradeList:
    if grade < threshold:
        total = total + grade
        numFailing = numFailing + 1

#compute average
        if numFailing > 0
        average = total/numFailing
        print(" ")
        else:
            print(" ")

print(gradeList)
