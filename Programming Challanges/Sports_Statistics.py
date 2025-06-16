# Create a program for a football team that:

# Stores overall goals scored, overall goals conceded and number of games played
# Calculates goal difference
# If they played 10 games, calculate the average goals per game
# Display all relevant statistics
import math
scored = int(input("How many goals has the team scored?: "))
conceeded = int(input("How many goals has the team conceeded?: "))
played = int(input("How many games has the team played?: "))
difference = scored - conceeded
difference = difference ** 2
difference = math.sqrt(difference)
average = scored/played
print(f"The team has scored on average: {average} goals per game")
print(f"The team has a goal difference of: {difference} goals")
