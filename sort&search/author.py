#3d - books sold

def getData():
    n = int(input("How many books are there: "))
    booksSold = []
    authors = []
    i = 0
    while i < n:
        author = input("Enter author: ")
        authors.append(author)
        numSold = int(input("Enter number of books sold: "))
        booksSold.append(numSold)
        i = i + 1
    return booksSold, authors

def findMostSold(booksSold, authors):
    author = 0
    mostSold = booksSold[0]
    for i in range(len(booksSold)):
        if booksSold[i] > mostSold:
            mostSold = booksSold[i]
            author = authors[i]
    return author


def findAverage(booksSold):
    total = 0
    average = 0
    for i in range(len(booksSold)):
        total = total + booksSold[i]
        average = total/len(booksSold)
    return average

def printResults(author, average):
    print(author)
    print(average)

def main():
    booksSold, authors = getData()
    author = findMostSold(booksSold,authors)
    average = findAverage(booksSold)
    printResults(author,average)
