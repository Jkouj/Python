#lab7_2.py

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

def relativelyPrime(a,m):
    win = True
    i = 2
    while i < m:
        if a%i == 0 and m%i == 0:
            win = False
        i += 1
    return win


def affine(a,b,m,plaintext):
    ciphertext = ""
    plaintext = str(plaintext)
    for i in range(len(plaintext)):
        letter = plaintext[i]
        num_in_alphabet = alphabet.index(letter)
        c = (a*num_in_alphabet+b)%m
        cipher_letter = alphabet[c]
        ciphertext = ciphertext + cipher_letter
    if relativelyPrime(a,m) == False:
        return ""
    else:
        return ciphertext
    
