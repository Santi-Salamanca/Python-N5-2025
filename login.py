numoftries = int(3) #adds an maximum amount of tries variable
accepted = bool(False) #true or false value for loop
while accepted == False and numoftries >= 1: # this will make the program repeat until the right username and password has been entered under the maximum amount of tries
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == "santi" and password == "themanwhoknocks": #this is an if statement
        print("login accepted")
        accepted = bool(True) # this will make the program stop repeating when the right username and passwrod is entered
    else:
        print("login rejected")

        numoftries = numoftries - 1 # adds an try used
        if numoftries >=1: #this makes it so it whill only display this message if they have tries left
            print("")
            print("You have " + str(numoftries) + " tries left, use them carefully.")