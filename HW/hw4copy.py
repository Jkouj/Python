#hw4_copy
# Andrew Federico
# Homework #4 Working with Python Functions

def getToys():

    num_toys = int(input("How many toys are in your catalog? "))
        
    toyNames=[]
    toyPrices=[]    
    numSold=[]
    for i in range (num_toys):
            toy = input("Enter toy name: ")
            toyNames.append(toy)
            price = input("Enter toy price: ")
            toyPrices.append(price)
            sold = input("Enter number sold: ")
            numSold.append(sold)
    return toyNames, toyPrices, numSold 

toyNames = []
toyList = []

def searchToy(toyNames, toyList):
    toyList = input("Enter a toy to find the price of: ")
    searchToy = toyList[0]
    i = 0
    found = 0

    while i < len(toyList):
        if toyList[i] == searchToy:
            found = 1
            toyIndex = i
        i=i+1
    if found == 1:
        
        return -1
        
    

def soldMore(toyNames, numSold, toyIndex):
    i = 0
    if numSold > i:
        i = i + 1
    return toyNames


def printResults(toyIndex, toyList, toyPrices, numSold):
    print("The toys that have more sold than " , " are: ",toyPrice[high])
    if found == 0:
        print("The toy name you entered is not in our catalog")
    else:
        print("The price is ", "{:,.2f}".format(price))        


def main():
    toyNames, toyPrices, numSold = getToys()
    high = searchToy(toyNames, toyList)
    printResults(high, toyNames, toyPrices)
    
