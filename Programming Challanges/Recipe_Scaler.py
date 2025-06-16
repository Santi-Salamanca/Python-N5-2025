# Write a program that:

# Stores ingredients for a chocolate chip cookie recipe that serves 4 people (flour in grams, butter in grams, sugar in grams, number of eggs, chocolate chips in grams, vanilla in teaspoons)
# Work out the scaling factor as the user wants to cook for 6 people instead
# Scale all ingredients proportionally using the calculated factor
# Display the new ingredient amounts
ingredients_dict = {}
exited = False
while exited == False:
    print("Enter Your recipe for a chocolate chip cookie recipe, that serves 4 people.")
    ingredient = str(input("Please enter an ingredient for the chocolate chip cookie recipe: "))
    measurement = str(input("What measurement would you like to store this ingredient with?: "))
    ingredients_dict[ingredient] = measurement
    exit = input("Would you like to continue adding ingredients to the recipe? (q to exit): ")
    if exit == "q":
        exited = True
    else:
        exited = False


