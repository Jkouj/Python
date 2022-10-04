#hw5_2
#joey koumjian
#due 3/21/22

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


def getThreshold():
    goodDif = False;
    while goodDif == False:
        try:
            diffThreshold = int(input("Enter a threshold for temperature difference: "))
            return diffThreshold
        except ValueError:
            print("Invalid entry, try again ... ")

def tempDiffFile(diffThreshold, yearList, shadowList, diffList):
    outfile = open('shadow' + str(diffThreshold) + '.0.csv','w')
    i = 1
    outfile.write("year,shadow,temperature difference" + '\n')
    while i < len(diffList):
        if float(diffList[i]) > diffThreshold:
            outfile.write(yearList[i] + ',')
            outfile.write(shadowList[i] + ',')
            outfile.write(diffList[i] + '\n')
        i = i + 1
    outfile.close()
    return

def printResults(diffThreshold):
    print("The results have been written to the output file: "+'shadow'+str(diffThreshold)+'.0.csv')



def main():
    yearList, shadowList, diffList = getData()
    diffThreshold = getThreshold()
    outfile = tempDiffFile(diffThreshold, yearList, shadowList, diffList)
    printResults(diffThreshold)
    

    
