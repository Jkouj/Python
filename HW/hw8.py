#hw8
#Joey Koumjian
#Due 4/11

def k_Fletcher32(string,k):
    # This function calculates the checksum of the given string
    # string: the input being tested
    # k: the amount of times we are summing through the list
    aList = []
    kList = []
    checksum = 0
    # building the aList
    for i in range(len(string)):
        aList.append(ord(string[i]))
    kList = aList
    # building the list k amount of times
    while k > 0:
        kList = listSum(kList)
        k = k - 1
    # finding the checksum
    for i in range(len(kList)):
        checksum = checksum + kList[i]
    return checksum % 65535
    
def listSum(lst):
    # building the kList
    # lst: the kList
    kList = [0]
    k = 0
    for i in range(len(lst)):
        k = k + lst[i]
        kList.append(k)
    return kList
