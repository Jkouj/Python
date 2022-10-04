# Given:  A list of car speeds and a speed limit 
# Find: The percentage of cars that exceed the speed limit

# Open the data file
def openFile():
    goodFile = False;
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            speedFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again...")
    return speedFile
 
# Get the speeds from user input
def getSpeeds():
    
    speedList = []
 
    infile = openFile()
 
    line = infile.readline()
    line = line.strip()
    while line != "":
        speed = float(line)
        speedList.append(speed)
        line = infile.readline()
        line = line.strip()
 
    return speedList

# Function to get the speed limit
def getSpeedLimit():
    OK = False
    while OK == False:
        try:
            speedLimit = float(input("Enter speed limit: "))
            OK = True
        except ValueError:
            print("Speed limit must be float, please try again...")
    return speedLimit
 
# Count the number of speeds that exceed the speed limit
def countAboveLimit(speedList):
    limit = getSpeedLimit()
 
    total = 0
 
    for i in range(len(speedList)):
        if speedList[i] > limit:
            total = total + 1
 
    return total
 
# Main function
def main():
    speedList = getSpeeds()
    totalAbove = countAboveLimit(speedList)
    percentAbove = totalAbove/len(speedList) * 100
    print("The percentage of cars that exceed the speed limit is " + str(percentAbove) + "%")
 
    
