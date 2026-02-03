#MODULES
import random

#initialise variables
counter = 1

#initialise data structure and stoire the mystery fruits
mysteryFruits = ["apple", "banana", "blueberry", "kiwi", "mango", "orange", "peach", "pineapple", "raspberry", "strawberry"]

#intialise a data structure and store the user's fruit selections
fruitsSelection = []
#get and store valid fruit selections
fruit = str(input("Please enter your fruit: "))
fruitsSelection.append(fruit)
counter = counter + 1


#get and store decision regarding entering aother fruit
decision = str(input("Do you want to enter another fruit? (yes/no): "))

#add 1 to counter
while decision == "yes" and counter < 6:

    #repeat previous
    fruit = str(input("Fruit Selection: "))
    fruitsSelection.append(fruit)
    counter += 1
    decision = str(input("DO you want to enter another fruit? (yes/no): "))


#de
############
number = int(random.randint(0,9))

print("The fruits you entered were.")
#######display all users entered fruit names
for _ in fruitsSelection:
    print(_)

mysteryFruitChosen = str(mysteryFruits[number])
print("The mystery fruit is: " + mysteryFruitChosen)

###################
####LAST PART
#######################

counter +=  1    

if counter < 3:
    print("We recommend a milkshake")
elif counter == 3 or counter == 4:
    print("We recommend a smoothie")
else:
    print("We recommend a fruit juice")