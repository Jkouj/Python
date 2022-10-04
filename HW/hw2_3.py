#Joseph Koumjian
#due 2/7
#hw2_3.py

rainfall = float(input("Rainfall for month 1: "))

lowest = rainfall
highest = rainfall
i = 1

while i <= 11:
    rainfall = float(input("Rainfall for month " + str(i+1) + ": "))
    if rainfall > highest:
        highest = rainfall

    elif rainfall < lowest:
        lowest = rainfall
    i += 1

print("The highest monthly rainfall was", highest, "inches.")
print("The lowest monthly rainfall was", lowest, "inches.")
