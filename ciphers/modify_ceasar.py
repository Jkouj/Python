#modify ceasar

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 

def caesar(plaintext,shift):  
    ciphertext = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        num_in_alphabet = alphabet.index(letter) 
        cipher_num = (num_in_alphabet + shift) % len(alphabet)
        shift = shift + 1
        cipher_letter = alphabet[cipher_num]
        ciphertext = ciphertext + cipher_letter 
    return ciphertext

