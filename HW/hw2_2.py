#Joseph Koumjian
#due 2/7
#hw2_2.py

toys = float(input("How many toys are in the catalog? "))
i = 1
total = 0
while i <= toys:
    price = float(input("Enter toy price $"))
    total = total + price
    i += 1

averagePrice = total/toys
print("The average price of toys in the catalog is: $ ", round(averagePrice, 2))
