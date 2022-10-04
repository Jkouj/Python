#List of names and phones to search through
#Find name of that phone number you search for

#Get data and store in two lists
nameList = []
phoneList = []

numPhones = int(input("How many phone numbers? "))

for i in range(numPhones):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    nameList.append(name)
    phoneList.append(phone)

#Get number to search for
searchPhone = input("Enter number to search for: ")
found = False
i = 0
while i < len(phoneList) and found == False:
    if searchPhone == phoneList[i]:
        print(nameList[i])
        found = True
    i = i + 1

if found == False:
    print("No number found ")
