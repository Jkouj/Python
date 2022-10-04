# Given:  A list of grades and a list of student names
# Find:  All students with passing grades
 
# Function to open a file - using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            gradeFile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid filename, please try again ... ")
    return gradeFile
        
 
# Function to get the lists of data - returns two lists
def getData():
    gradeFile = openFile()
 
    gradeList = []
    nameList = []
 
    for line in gradeFile:
        line = line.strip()
        name, grade = line.split(',')
        gradeList.append(int(grade))
        nameList.append(name)
 
    gradeFile.close()
 
    return nameList, gradeList
 
# Function to get a passing grade threshold - using exception handling
def getPassingGrade():
    OK = False
    while OK == False:
        try:
            passingGrade = int(input("Enter passing grade threshold: "))
            OK = True
        except ValueError:
            print("Passing grade must be an integer, please try again...")
    return passingGrade
 
# Function to return the a list of students with a passing grade
def findStudents(gradeList, nameList):
    passingGrade = getPassingGrade()
    passingIndex = []
    for i in range(len(gradeList)):
        if gradeList[i] >= passingGrade:
            passingIndex.append(i)
    return passingIndex
 
# Function to print the list of students with passing grades
def printPassingStudents(passingIndex, nameList, gradeList):
    print("The following students received passing grades: ")
    for i in passingIndex:
        print(nameList[i], gradeList[i])
    return
 
# Main function
def main():
    nameList, gradeList = getData()
    passingIndex = findStudents(gradeList, nameList)
    printPassingStudents(passingIndex, nameList, gradeList)
