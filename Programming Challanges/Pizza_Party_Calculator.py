# Write a program that:

# Stores the number of students in the class
# Stores that each pizza serves 8 people
# Calculate how many pizzas are needed (you may need to round up)
# If each pizza costs £12, calculate the total cost
# Display the number of pizzas needed and the total cost
import math
price = 12
pupils = int(input("Please enter the number of students in the class: "))
serving_size = 8
num_of_pizzas = math.ceil(pupils/serving_size)
total_cost = price * num_of_pizzas
print(f"The number of pizzas needed is: {num_of_pizzas}")
print(f"The total cost of the pizzas is: {total_cost}")
