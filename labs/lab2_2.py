#Joey Koumjian, Arthur Souza
#due 2/4
#lab2_2.py

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

final = 1
i = 0

while i < b:

    final = (final * a)
    i += 1

print(a , "**" , b, "=", final)
