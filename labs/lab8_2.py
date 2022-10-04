#lab8_2.py

def rotateRight(strng):
    newstring = ''
    newstring = newstring + strng[len(strng)-1]
    for i in range(len(strng)-1):
        letter2 = strng[i]
        newstring = newstring+letter2
    return newstring
