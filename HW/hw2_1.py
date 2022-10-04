#Joseph Koumjian
#due 2/7
#hw2_2.py

sale = float(input("Enter amount of sale $"))

if sale <= 100:
    finalSale = sale - (sale*0.05)
    print("The final sale amount is $", "{:,.2f}".format(finalSale))

elif sale <= 300:
    finalSale = sale - (sale*0.1)
    print("The final sale amount is $", "{:,.2f}".format(finalSale))

elif sale <= 600:
    finalSale = sale - (sale*0.2)
    print("The final sale amount is $", "{:,.2f}".format(finalSale))

elif sale <= 900:
    finalSale = sale - (sale*0.3)
    print("The final sale amount is $", "{:,.2f}".format(finalSale))



