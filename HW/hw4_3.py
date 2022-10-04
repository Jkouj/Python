#Joey Koumjian
#HW4_2
#2/21/22

def sumKDigits(n,k):
    a = str(n)
    i = 0
    total = 0
    if k <= len(a):
        while i < k:
            total = total + int(a[i])
            i = i + 1
    return total
    if k > len(a):
        return 0

def allSumKDigits(new):
    lst = []
    b = str(new)
    i = 1
    while i <= len(b):
        lst.append(sumKDigits(new,i))
        i = i + 1
    return lst

