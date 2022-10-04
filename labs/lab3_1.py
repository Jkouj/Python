# Jakob Porto and Joey Koumjian
# 11 February 2022
# lab3_1

read=[]
dan=[]
safe=[]
warning=[]
i=0
while i!=-1:
    add=float(input("Enter vibration value (-1 to quit): "))
    i=add
    if i!=-1:
        read.append(add)
        
warn=float(input("Enter threshold for warning values: "))
dang=float(input("Enter threshold for danger values: "))
i=0
for i in range(len(read)):
    if read[i]<warn:
        safe.append(read[i])
    elif read[i]>=warn and read[i]<dang:
        warning.append(read[i])
    elif read[i]>=dang:
        dan.append(read[i])
print("There are " , str(len(safe)) , " safe readings:")
print(safe)
print("There are " , str(len(warning)) , " warning readings:")
print(warning)
print("There are " , str(len(dan)) , " danger readings:")
print(dan)
