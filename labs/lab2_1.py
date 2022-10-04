#Joey Koumjian, Arthur Souza
#due 2/4
#lab2_1.py

score = 0
star = int(input("Enter star rating: "))
shares = int(input("Enter number of shares: "))


if star > 0 and star < 3:
    if shares < 1000:
        score = star*shares*2
    if shares > 1000:
        score = star*shares
if star > 2 and star < 5:
    if shares < 2500:
        score = star * shares * 3
    if shares > 2500:
        score = star * shares
if star == 5:
    if shares < 5000:
        score = star * shares * 4
    if shares > 5000:
        score = star * shares

print("The score is: ",score)
