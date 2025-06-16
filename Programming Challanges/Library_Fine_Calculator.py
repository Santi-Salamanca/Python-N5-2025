# Write a program that:

# Stores the number of days a book is overdue
# The fine is £0.50 per day
# If the fine exceeds £5, add an additional £2 processing fee
# Calculate and display the total fine
days = int(input("How many days is the book overdue?: "))
fine = 0.5
total = fine * days
if total > 5:
    total += 2
print(f"The total fine is: £{total}")