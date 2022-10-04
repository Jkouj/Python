#Given two positive integers make a function to
#Compute the product of the two without using *

def computeProduct(a,b):
    product = 0
    i = 0
    while i < b:
        product = product + a
        i = i + 1
    return product
