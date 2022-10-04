#lab7_3

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
