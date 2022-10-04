#relatively_prime.py
#lab7-1

def relativelyPrime(a,m):
    win = True
    i = 2
    while i < m:
        if a%i == 0 and m%i == 0:
            win = False
        i += 1
    return win
    
