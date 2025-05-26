#Create a program that asks the user to input 5 
# test scores and calculates the running total after each input.


total = 0
for i in range(5):
    score = float(input("Input yourtest score: "))
    total += score
    print("Your total test score is:",total)

