#hw5_1
#Joey Koumjian
#Due 3/21/22

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
    shadowList = []
    diffList = []
    inFile = openFile()
    for line in inFile:
        line = line.strip()
        year, shadow, febAv, marAv, diff = line.split(',')
        yearList.append(year)
        shadowList.append(shadow)
        diffList.append(diff)
    inFile.close()
    return yearList, shadowList, diffList


def checkYear():
    goodYear = False;
    while goodYear == False:
        try:
            year = int(input("Enter a year between 1895 and 2016: "))
            if year < 1895 or year > 2016:
                print("Year not in range, try again ... ")
            else:
                goodYear = True
                return year
        except ValueError:
            print("Invalid entry, try again ... ")

def shadowTrend(year, yearList, shadowList):
    percent = 0
    a = 0
    if int(year) > 2012 and year <= 2016:
        return -1, year
    else:
        for i in range(len(yearList)):
            if str(year) == yearList[i]:
                j = 0
                a = i
                while j < 5:
                    if shadowList[a] == 'Full Shadow':
                        percent = percent + 20
                    j = j + 1
                    a = a + 1
        return percent, year

        

def printResults(percent,year):
    if percent == -1:
        print("Five year trend cannot be computed from the given year ",year)
    else:
        print("Phil saw his shadow", float(percent),"% of the five years starting in ",year)


def main():
    yearList, shadowList, diffList = getData()
    year = checkYear()
    percent, year = shadowTrend(year, yearList, shadowList)
    printResults(percent,year)
