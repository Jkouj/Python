#Sequence match function

def match(str1,str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            counter += 1
    return counter
    
