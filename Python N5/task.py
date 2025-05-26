mileage = input("Enter the mileage of the car: ")
rating = input("Enter the Kw rating for current charging station of the car: ")
if rating == 7:
    priceper = 0
elif rating == 22:
    priceper = 0.005
else:
    priceper = 0.01
miles = input("enter the miles travelled: ")
newmiles = int(miles) - int(mileage)
cost = newmiles * priceper
print("The cost of charging the car is: £" + str(round(cost, 2)))