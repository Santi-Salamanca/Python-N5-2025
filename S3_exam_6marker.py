testscores = []
for index in range(20):
    score = int(input("Enter a test score: "))
    while score<100 or score<0:
        print("error")
        score = int(input("Enter a test score: "))
    testscores.append(score)