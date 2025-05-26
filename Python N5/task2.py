caker = input("Do you want a cake: ")
if caker == "yes":
    cake = 15
else:
    cake = 0
adults = int(input("Enter the number of adults: "))
children = int(input("Enter the number of children: "))
diet = []
for i in range(children):
    ransd = (input("Enter the dietary requirements of the children: "))
    diet.append(ransd)
print("The dietary requirements of the children are: ", diet)
if (adults + children) > 20:
    venue = 0
else:
    venue = 50
cost = (children * 2) + cake + venue
print("The final cost for the buffet is: £", round(cost,2))