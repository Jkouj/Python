#Joey Koumjian, Arthur Souza
#due 2/4
#lab2_3.py

i = 0
odd = 0
even = 0

while i < 10:
    number = int(input("Enter integer: "))%2
    if number == 0:
        even = even + 1
    if number == 1:
        odd = odd + 1
    i += 1

print("There are ", even, "even numbers in the list")
print("There are ", odd, "odd numbers in the list")

