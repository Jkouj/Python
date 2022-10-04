def getSpeeds():
    speedList = []
    inFile = open('speeds.txt','r') #r = reading
    line = inFile.readline()
    line = line.strip()
    while line != '':
        speed = float(line)
        speedList.append(speed)
        line = inFile.readline()
        line = line.strip()
    inFile.close()
    return speedList

def getSpeeds2():
    speedList = []
    inFile = open('speeds.txt','r')
    for line in inFile
        line = line.strip()
        speed = float(line)
        speedList.append(speed)
    inFile.close()
    return speedList
