scores = [12, 14, 42, 82, 167, 75]
highscore = scores[0]
for index in range(scores):
    if scores[index] > highscore:
        highscore = scores[index]
print("The highest score is: " + highscore)