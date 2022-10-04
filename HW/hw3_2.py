#HW3_2
#Joseph Koumjian
#Due 2/14

scores =[]
names = []
winner = 0

numGolfers = int(input("How many golfers are in the tournament? "))
i = 0

while i < numGolfers:
    name = input("Enter name of golfer " + str(i+1) + ": ")
    names.append(name)
    score = int(input("Enter score for golfer " + str(i+1) + ": "))
    scores.append(score)
    i = i + 1

for i in range(len(scores)):
    if scores[i] < score:
        winner = scores[i]


print("The current leader of the tournament is" , names[scores.index(winner)] , "with a score of " , winner)
