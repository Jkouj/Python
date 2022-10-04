# Given:  A list of car speeds and a speed limit
# Find: The percentage of cars that exceed the speed limit
 
# Get the speeds from user input
def getSpeeds():
    speedList = []
    inFile = open('speeds.txt','r')
    for line in inFile:
        line = line.strip()
        speed = float(line)
        speedList.append(speed)
    inFile.close()
    return speedList
 
# Count the number of speeds that exceed the speed limit
def countAboveLimit(speedList):
    limit = float(input("Enter the speed limit: "))
 
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
