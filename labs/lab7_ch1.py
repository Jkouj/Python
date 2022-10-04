#lab 7_ch1.py


def findPrimeFactors(n):
    i = 2
    while i * i < n:
         while n % i == 0:
             n = n / i
         i = i + 1
    return n

