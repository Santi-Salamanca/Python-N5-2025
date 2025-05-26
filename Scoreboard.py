home = 0
away = 0
period = 1
banana = True
print("Home: ", home, "   Away: ",away)
print("period:", period)
while banana == True:
    Hscored = str(input("has the Home Team Scored: "))
    Ascored = str(input("Has the Away team scored: "))
    period = int(input("What is the period: "))
    if Hscored == "yes":
        home = home + 1
    if Ascored == "yes":
        away = away + 1
    while period < 3:
        print("Home: ", home, "   Away: ",away)
        print("period:", period)
        Hscored = str(input("has the Home Team Scored: "))
        Ascored = str(input("Has the Away team scored: "))
        period = int(input("What is the period: "))
        if Hscored == "yes":
            home = home + 1
        if Ascored == "yes":
            away = away + 1

