#Joey Koumjian
#Hw 6-1
#Due 3/27

# Open the data file
def openFile():
    goodFile = False;
    while goodFile == False:
        fname = input("Please enter the name of the data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name, try again...")
    return inFile

def getData():
    yearList = []
    awardList = []
    inFile = openFile()
    for line in inFile:
        line = line.strip()
        year, award = line.split(',')
        yearList.append(year)
        awardList.append(award)
    inFile.close()
    return yearList, awardList

def checkYear():
    goodYear = False;
    while goodYear == False:
        try:
            year = str(input("Enter a year: "))
            if int(year) < 1949 or int(year) > 2020:
                print("Year not in range, try again ... ")
            else:
                goodYear = True
                return year
        except ValueError:
            print("Invalid entry, try again ... ")

def getYearLinear(yearList, year):
    count = 0
    found = 0
    linearIndex = -1
    if found == 0:
        count = count + 1
        for i in range(len(yearList)):
            count = count + 1
            if year == yearList[i]:
                linearIndex = i
                found = 1
    count = count + 1
    
    if found == 0:
        return linearIndex
    else:
        print("Linear Search: comps = ",count)
        return linearIndex
        

def getYearBinary(yearList, year):
    counter = 0
    binaryIndex = -1
    left = 0    
    right = len(yearList) - 1
    found = 0
    while right >= left and found == 0:
        counter = counter + 1
        m = (left + right) // 2
        if yearList[m] == year:
            binaryIndex = m
            found = 1
        elif yearList[m] < year:
            left = m + 1
        else:
            right = m - 1

    if found == 0:
        return binaryIndex
    else:
        print("\n"+"Binary Search: comps = ",counter ,"\n")
        return binaryIndex

def printResults(year, awardList, a):
    print("In " ,year, "the winner of the Tony Award for Best Musical was",awardList[a])
    
def main():
    yearList, awardList = getData()
    year = checkYear()
    b = getYearBinary(yearList, year)
    a = getYearLinear(yearList, year)
    printResults(year, awardList, a)
    
#The worst case input for linear search would be year 2020 because it is the
#last element in the list so it has to search every element before reaching the final
#The best case input for linear search would be the first element in the list
#(1949) because it only has to loop through once to find its answer

#The worst case input for binary search would be either 2020 or 1949
#Because these inputs are farthest from the middle of the list
#The best case input for binary search would be the direct middle of the list
#Because the program starts by checking if the middle of the list is correct
#so it only has to loop through once.

#linear is better for elements closer to the start of the list
#binary is better for elements closer to the middle of the list
#By this logic, binary search in most cases is better for larger sized lists
