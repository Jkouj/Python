#HW3_3
#Joseph Koumjian
#Due 2/14

scores = []
sampleScores = []

numScores = int(input("How many golf scores have you collected? "))

i = 0
while i < numScores:
    score = int(input("Enter score: "))
    scores.append(score)
    i = i + 1

sample = int(input("Enter sample rate (k): "))

j = 0
while j < len(scores):
    sampleScores.append(scores[j])
    j = j + sample

print("The sampled scores are: ")
print(sampleScores)
