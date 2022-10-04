#Joey Koumjian
#Lab 4b-1
#2/25

def getData():
    n = int(input("How many names in the list: "))
    nameList = []
    phoneList = []
    i = 0
    while i < n:
        name = input("Name: ")
        nameList.append(name)
        phone = str(input("Phone: "))
        phoneList.append(phone)
        i = i + 1
    return nameList, phoneList

def search(who,nameList,phoneList):
    name = "hi"
    for i in range(len(phoneList)):
        if who == phoneList[i]:
            name = nameList[i]
            return name
    if who != phoneList[i]:
        return 0

def printResults(name):
    if name == 0:
        print("Phone number not found ")
    else:
        print("Phone number belongs to", name)


def main():
    nameList, phoneList = getData()
    who = str(input("Enter phone number to search for: "))
    name = search(who,nameList,phoneList)
    printResults(name)
