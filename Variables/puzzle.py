homeHT = int(input("Enter the half time score for the home team: "))
awayHT = int(input("Enter the half time score for the away team: "))
print()
awayFT = int(input("Enter the full time score for the away team: "))
homeFT = int(input("Enter the full time score for the home team: "))
print()
noGoalsScored = (homeFT + awayFT) - (homeHT + awayHT)
print("The number of goals scored after the half time break was: "+str(noGoalsScored))




heightOfTower = int(input("Enter the height of the stacked pair tower: "))
heightOfChair = int(input("Enter the height of one chair: "))
noChairLegs = ((heightOfTower / heightOfChair) * 2) * 4
print("The total number of chair legs in the tower is: "+str(noChairLegs))




weekday = input("Enter the week day for January 1st (MO/TU/WE/TH/FR/SA/SU): ")
leapyear = input("Is it a leap year? (y/n): ")
if weekday == "SA":
    noSaturdays = 53
elif weekday == "FR" and leapyear == "y":
    noSaturdays = 53
else:
  noSaturdays = 52
print("There are",noSaturdays,"Saturdays this year.")



lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
specialOffer = input("Is a special offer running? (y/n): ")
additionalRows = int(input("Please enter the number of additional rows included for free: "))
if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
    widthOfSquarePacks = lengthOfSquarePacks
if specialOffer == "y":
    widthOfSquarePacks = widthOfSquarePacks + additionalRows
totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
print("The number of cans in the pack is: "+str(totalNumberOfCans))
