#Joseph Koumjian
#HW 3_1
#Due 2/14

scores = []
total = 0

numGolfers = int(input("How many golfers are in the tournament? "))
i = 0

while i < numGolfers:
    score = int(input("Enter two-day score for golfer " + str(i+1) + ": "))
    scores.append(score)
    i = i + 1

cutoff = int(input("Enter the cut-off score: "))

j = 0
while j < len(scores):
    if scores[j] < cutoff:
        total = total + 1
    j = j + 1
        

final = (total / numGolfers) * 100

print("The percent of golfers that made the cut is", round(final, 1), "%. ")
