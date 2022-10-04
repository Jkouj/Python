#lab 7_4.py

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 


def relativelyPrime(a,m):
    win = True
    i = 2
    while i < m:
        if a%i == 0 and m%i == 0:
            win = False
        i += 1
    return win

def modInverse(a,m):
    x = 0
    boole = False
    while boole == False and x < m:
        if (a*x)%m == 1:
            boole = True
        else:
            x += 1
    if boole == True:
        return x
    elif boole == False:
        return -1

def unAffine(a,b,m,plaintext):
    ciphertext = ""
    if modInverse(a,m) == -1:
        return ""
    else:
        for i in range(len(plaintext)):
            letter = plaintext[i]
            num = alphabet.index(letter)
            x = modInverse(a,m)
            p = (x*(num-b)%m)
            cipher_letter = alphabet[p]
            ciphertext = ciphertext + cipher_letter
        return ciphertext

