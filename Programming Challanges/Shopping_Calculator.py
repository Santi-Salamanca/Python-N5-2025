# Create a program that calculates the total cost of shopping items:
#---------------------------------------------------------------------
# Store the price of 3 different items in variables
# Store the quantity of each item purchased
# Calculate and display the total cost for each item
# Calculate and display the grand total
#---------------------------------------------------------------------
total = 0
cart = []
for i in range(3):
    price = int(input("Please enter the price of your item: £"))
    total += price
print("The grand total is: £",total)