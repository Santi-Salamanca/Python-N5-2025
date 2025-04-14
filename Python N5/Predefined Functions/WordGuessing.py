# PROJECT
import random
words = ["python", "function", "random", "length", "computer", "program", "variable"]
des = 5
secret_word = random.choice(words)
print(str(secret_word))
guess = input(str("Input your guess: "))
while des > 1:
    if guess == secret_word:
        print("good job, you have guessed correctly!")
        print("The secret word was: "+secret_word)
        des = 0
    else:
        des -= 1
        print("Incorrect guess, you have "+str(des)+" guesses left")
        guess = input(str("Input your guess: "))
