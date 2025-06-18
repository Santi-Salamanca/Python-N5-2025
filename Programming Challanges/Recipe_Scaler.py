# Write a program that:

# Stores ingredients for a chocolate chip cookie recipe that serves 4 people (flour in grams, butter in grams, sugar in grams, number of eggs, chocolate chips in grams, vanilla in teaspoons)
# Work out the scaling factor as the user wants to cook for 6 people instead
# Scale all ingredients proportionally using the calculated factor
# Display the new ingredient amounts
from colorama import Fore
from dataclasses import dataclass
#####
exited = False
ingredients_list = []
########
@dataclass
class Ingredient:
    name : str = ""
    measurement : str = ""
    amount : float = 0.0
####################
########################
print(Fore.LIGHTRED_EX + "Enter Your recipe for a chocolate chip cookie recipe, that serves 4 people." + Fore.WHITE)
###########
while exited == False:
    p1 = Ingredient()
    p1.name = str(input("Please enter an ingredient: "))
    p1.measurement = str(input("What measurement would you like to store this ingredient with?: "))
    p1.amount = float(input("How much quantity would you like to store of this ingredient?: "))
    ingredients_list.append(p1)
    exit = input(Fore.RED +"Would you like to continue adding ingredients to the recipe? (q to exit): "+ Fore.WHITE)
    if exit == "q":
        exited = True
    else:
        exited = False

def Scale(num):
    for object in ingredients_list:
        object.amount = float(object.amount/4)
        object.amount = object.amount * num

randy = int(input(Fore.GREEN +"For how many people would you like this recipe to be scale up to?: "+Fore.WHITE))
Scale(randy)
###############output of recipe scaled
for object in ingredients_list:

    print(f"{str(object.name), str(object.amount) + str(object.measurement)}")

