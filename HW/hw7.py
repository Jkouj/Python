#hw7
#Joey Koumjian
#Due 4/1/22

import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

def caesarRandom(plaintext, seedIn):
    ciphertext = ""
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()
    random.seed(seedIn)
    for i in range(len(plaintext)):
        letter = plaintext[i]
        alphabetNum = alphabet.index(letter)
        num = random.randint(0,25)
        alphabetNum = alphabetNum + num
        cipherValue = alphabetNum % 26
        cipherLetter = alphabet[cipherValue]
        ciphertext = ciphertext + cipherLetter
    return ciphertext

def unCaesarRandom(plaintext, seedIn):
    ciphertext = ""
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()
    random.seed(seedIn)
    for i in range(len(plaintext)):
        letter = plaintext[i]
        alphabetNum = alphabet.index(letter)
        num = random.randint(0,25)
        alphabetNum = alphabetNum - num
        cipherValue = alphabetNum % 26
        cipherLetter = alphabet[cipherValue]
        ciphertext = ciphertext + cipherLetter
    return ciphertext
