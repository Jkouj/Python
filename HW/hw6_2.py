#Joey Koumjian
#HW 6-2
#due 3/28

# Open the data file
def openFile():
    goodFile = False;
    while goodFile == False:
        fname = input("Please enter the name of the data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name, try again... ")
    return inFile

def getData():
    yearList = []
    awardList = []
    inFile = openFile()
    next(inFile)
    for line in inFile:
        line = line.strip()
        year, award = line.split(',')
        yearList.append(year)
        awardList.append(award)
    inFile.close()
    return yearList, awardList

def get_aORd():
    aORd = input("Enter A for ascending, D for descending: ")
    while True:
        if aORd == "A":
            return "asc"
        elif aORd == "D":
            return "desc"
        else:
            aORd = str(input("Invalid input -- A or D: "))  

def outFile(yearList, awardList, aORd):
    outfile = open('sorted-tony-' + aORd + '.csv','w')
    i = 0
    outfile.write("year,tony" + '\n')
    while i < len(awardList):
        outfile.write(yearList[i] + ',')
        outfile.write(awardList[i] + '\n')
        i = i + 1
    outfile.close()

def dualSelectionSort(yearList, awardList, aORd):
    for i in range(0, len(awardList)):            
        swap = i
        for j in range(i + 1, len(awardList)):
            if aORd == "asc":
            # comparison
                if awardList[j] < awardList[swap]:
                    swap = j
            else:
                if awardList[j] > awardList[swap]:
                    swap = j
                
        # swap
        yearList[i], yearList[swap] = yearList[swap], yearList[i]
        awardList[i], awardList[swap] = awardList[swap], awardList[i]
    return yearList, awardList

def main():
    yearList, awardList = getData()
    aORd = get_aORd()
    yearList, awardList = dualSelectionSort(yearList, awardList, aORd)
    outFile(yearList, awardList, aORd)
    print("Sorted data has been written to the file sorted-tony-"+aORd+".csv")

    
        
    

