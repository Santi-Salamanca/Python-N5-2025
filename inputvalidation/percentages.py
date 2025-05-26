#Get user input
list = [] # creates a array
while True:
    percentage = int(input("Enter Percentage:"))
    bum = True
    #Validate between 0 and 100

    while percentage < 0 or percentage > 100: # loops program till valid input is entered
        print("Error, % must be between 0 and 100")
        percentage = int(input("Please enter a valid percentage: "))
        list.append(percentage) # adds percentage to array
        print(list)