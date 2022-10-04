#Lab 3_ch2

oList=[]
rList=[]
length=int(input("Enter the size of the list: "))
i=0
for i in range(length):
    add=int(input("Enter a number: "))
    oList.append(add)
i=0
for i in range(length):
    rList.append(oList[length-1-i])
print("The original list is: ")
print(oList)
print("The reversed list is: ")
print(rList)
