# Program 3 - Investigate and Modify
price = [3.99, 5.25, 10.50]
total = 0
for x in range(len(price)):
    total += price[x]
print('The total cost is: £' + str(round(total, 2)) )