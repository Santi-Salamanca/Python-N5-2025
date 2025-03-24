homeScore = [0 for x in range(10)] # creats a list with 10 numbers
awayScore = [0 for x in range(10)]# creats a list with 10 numbers
for x in range(10):
    print(x,":",homeScore[x],"-",awayScore[x]) # prints out the home score and away score 10 times
homeScore[4] = homeScore[4] + 1 # adds a score the scoreboard in the 4th number
homeScore[7] = homeScore[7] + 1 # adds a score the scoreboard in the 7th number
print("-------")
for x in range(10): # prints out the list 10 times with the changes made to the list
    print(x,":",homeScore[x],"-",awayScore[x])
