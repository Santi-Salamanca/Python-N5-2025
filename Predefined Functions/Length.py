# Program 3 - Investigate and modify
password = input("Please enter your password: ")
while len(password) < 8:
    print("Error, your Password is not long enough try again.")
    password = input("Please enter your password: ")
print("Password accepted.")
