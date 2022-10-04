#

def bin_to_dec(binary):
    decimal = 0
    binary = str(binary)
    current = len(str(binary)) - 1
    exp = 0
    while current >= 0:
        if binary[current] == '1':
            decimal = decimal + 2**exp
        current = current - 1
        exp = exp + 1
    return decimal

def rotateRight(strng):
    newstring = ''
    newstring = newstring + strng[len(strng)-1]
    for i in range(len(strng)-1):
        letter2 = strng[i]
        newstring = newstring+letter2
    return newstring
            
def dec_to_bin(num):
    binary = ''
    found = False
    while found == False:
        if num <= 1:
            binary = str(num) + binary
            found = True
        elif num % 2 == 1:
            binary = '1' + binary
        else:
            binary = '0' + binary
        num = num // 2
    return binary

