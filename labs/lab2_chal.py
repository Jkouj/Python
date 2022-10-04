#Joey Koumjian, Arthur Souza
#due 2/4
#lab2_ch1.py

i = 0
summ = 0

n = int(input("Enter the highest number to consider: "))

while i < n:
    if (i % 3) == 0:
        summ = summ + i
    elif (i % 5) == 0:
        summ = summ + i
    i += 1

print("The sum of all multiples of 3 and 5 below ", n, " is", summ)
