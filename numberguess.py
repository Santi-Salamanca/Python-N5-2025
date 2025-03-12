# Program 4 - Investigate and modify
rightnumber = 8
guess = 1
number = int(input("Guess a number: "))
if number == rightnumber:
  print("Well done, you guessed the right number!")
else:
    while (guess < 5) and (number != rightnumber):
        print("Not right. Try again.")
        number = int(input("Guess a number: "))
        guess = guess + 1
