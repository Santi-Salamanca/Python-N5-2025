#modules
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
#add 1 to counter
counter += 1

#get and store decision regarding entering aother fruit
decision = str(input("Do you want to enter another fruit? (yes/no): "))

#decision = yes and counter <  6
while decision == "yes" and counter < 6:

    #repeat previous
    fruit = str(input("Please enter your fruit: "))
    fruitsSelection.append(fruit)
    counter += 1
    decision = str(input("DO you want to enter another fruit? (yes/no): "))


############
randomNum = int(random.randint(0,9))

print("The fruits you entered were.")
#######display all users entered fruit names
for _ in fruitsSelection:
    print(_)

mysteryFruitChosen = str(mysteryFruits[randomNum])
print("The myster fruit is: " + mysteryFruitChosen)

###################
####LAST PART
#######################

counter +=  1    

if counter < 3:
    print("We reccomend a milkshake")
elif counter == 3 or counter == 4:
    print("We reccomend a smoothie")
else:
    print("We reccomend a fruit juice")