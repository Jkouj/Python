#Joey Koumjian
#2/21/22
#HW4_1

def getToys():
    names = []
    prices = []
    sold = []
    
    numToys = int(input("How many toys are in your catalog? "))
    i = 0
    while i < numToys:
        name = str(input("Enter toy name: "))
        names.append(name)
        price = float(input("Enter toy price: "))
        prices.append(price)
        amntSold = int(input("Enter number sold: "))
        sold.append(amntSold)
        i = i + 1
    return names,prices,sold

def searchToy(names,toy):
    i = 0
    while i < len(names):
        if toy == names[i]:
            return i
        i = i + 1
    print("The toy name you entered is not in our catalog. ")
    return -1


def soldMore(names,sold,a):
    haveSold = []
    i = 0
    while i < len(sold):
        if sold[i] > sold[a]:
            haveSold.append(names[i])
        i = i + 1
    return haveSold

def printResults(a,names,prices,haveSold):
    print("The price of ", names[a], " is $ ","{:,.2f}".format(prices[a]))
    if len(haveSold) > 0:
        print("The toys that have more sold than ",names[a], " are: ")
        for i in range(len(haveSold)):
            print(haveSold[i])
    elif len(haveSold) == 0:
        print("No toys have sold more than ",names[a])

def main():
    names,prices,sold = getToys()
    print()
    toy = str(input("Enter a toy to find the price of: "))
    a = searchToy(names,toy)
    if a == -1:
        return
    haveSold = soldMore(names,sold,a)
    printResults(a,names,prices,haveSold)
    
