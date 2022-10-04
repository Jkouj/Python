#lab3_2
#11 February 2022
#Joey Koumjian, Jakob Porto

stocks = ['IBM','AAPL','GOOG','FB','SMSN','INTC','MCD','TWTR']
stockPrices = [23.4,24.5,25.3,56.7,89.4,45.3,43.6,67.4]

name = input("Enter the name of the stock: ")
percent = float(input("Enter the percentage increase: "))
i=0
real=False
while i < len(stocks):
    if name==stocks[i]:
        real=True
    i=i+1
if real==True:
    num = stocks.index(name)
    stockPrices[num] = round(stockPrices[num] * (1+percent/100),3)
    print("Updated Price List: ")
    print(stockPrices)
else:
    print("Stock not found")
