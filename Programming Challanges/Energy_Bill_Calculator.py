# Create a program that calculates an electricity bill:

# Store that each unit costs £0.15
# Store the meter reading at the start and end of the month
# Calculate units used (i.e end reading - start reading)
# Calculate the cost of the units used
# Add a standing charge of £12 to the total cost
# Calculate and display the total bill
unit = 0.15
start = input("Enter the starting meter reading for the month: ")
end = input("Enter the meter reading at the end of the month: ")
units_used = int(end) - int(start)
cost = unit * units_used
total = cost + 12
print(f"The total bill is £{total}")