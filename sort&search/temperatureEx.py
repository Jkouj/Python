def getData():
    tempList = []
    dateList = []
    for i in range(7):
        date = input("Enter date in mm/dd/yy format: ")
        temp = float(input("Enter temp on that date: "))
        tempList.append(temp)
        dateList.append(date)
    return tempList, dateList

def getHighTempIndexes(tempList):
    tempThreshold = float(input("Enter temp threshold: "))
    highTempIndexList  = []
    for i in range(len(tempList)):
        if tempList[i] > tempThreshold:
            highTempIndexList.append(i)
    return highTempIndexList

def printResults(highTempIndexList, tempList, dateList):
    print("The dates and temperatures for temperatures that exceed the threshold are: ")
    for i in range(len(highTempIndexList)):
        x = highTempIndexList[i]
        print("Date: ", dateList[x], "Temp: ", tempList[x])


def main():
    tempList, dateList = getData()
    highTempIndexList = getHighTempIndexes(tempList)
    printResults(highTempIndexList, tempList, dateList)
