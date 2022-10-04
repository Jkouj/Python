#Find fastest of 10 calculated speeds
time = float(input("Enter time: "))
distance = float(input("Enter distance: "))
fastest = distance/time

i = 1
while i < 10:
    time = float(input("Enter time: "))
    distance = float(input("Enter distance: "))
    speed = distance/time

    if speed > fastest:
        fastest = speed

print("The fastest speed is: ", fastest)
