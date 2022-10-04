# High Temperature Dates

# Given:  A list of temperatures and a list of dates.
# Find:  The dates when the temperature exceeded a given threshold.

# Function to get the data from user input
# Parameters: None
# Return: List of temperatures (int), list of dates (str)
def getData():
    tempList = []
    dateList = []
    for i in range(7):
        temp = float(input("Enter temperature: "))
        date = input("Enter date in MM/DD/YY format: ")
        tempList.append(temp)
        dateList.append(date)
    return tempList, dateList

# Function to find the indexes of the high temperatures
# Parameters: List of temperatures (int)
# Return: List of indexes of temps in the temp list that exceed threshold (int)
def getHighTemps(tempList):
    threshold = float(input("Enter temperature threshold: "))
    highTempIndexList = []
    for i in range(len(tempList)):
        if tempList[i] > threshold:
            highTempIndexList.append(i)
    return highTempIndexList

# Function to print the results
# Parameters: List of indexes (int), list of temperatures (int), list of dates (str)
# Return: None
def printResults(highTempIndexList, tempList, dateList):
    for i in range(len(highTempIndexList)):
        x = highTempIndexList[i]
        print("On ",dateList[x]," the temperature was ",tempList[x])
    return

# Main function
def main():
    tempList, dateList = getData()
    highTempIndexList = getHighTemps(tempList)
    printResults(highTempIndexList, tempList, dateList)
