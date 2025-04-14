home = 0
away = 0
period = 1
print("enter (h) if the home team has scored, enter (a) if the away team has scored, enter (x) if the current period has ended: ")
while period < 4:
    thing = str(input("Input letter: "))
    if thing == "a":
        home = home + 1
    elif thing == "h":
        away = away + 1
    elif thing == "x":
        period += 1
print("Home: " + str(home) + " / Away: " + str(away))
print("Period: 4 over")