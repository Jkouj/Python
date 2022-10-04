# Jakob Porto and Joey Koumjian
# 11 February 2022
# lab3_ch2

i=0
j=0
l1=[1,4,6,7,9,11,15]
l2=[2,3,4,5,10,11,12]
sort=[]
while i<len(l1) or j<len(l2):
    if i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            sort.append(l1[i])
            i=i+1
        elif l1[i]>l2[j]:
            sort.append(l2[j])
            j=j+1
        elif l1[i]==l2[j]:
            sort.append(l2[j])
            j=j+1
            sort.append(l1[i])
            i=i+1
    elif i==len(l1):
        
        sort.append(l2[j])
        j=j+1
    elif j==len(l2):
        
        sort.append(l1[i])
        i=i+1
        
print(sort)
