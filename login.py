
accepted = bool(False)
while accepted == False:
    username = input("Please enter your username")
    password = input("Please enter your password")
    if username == "Santi" and password == "themanwhoknocks":
        print("login accepted")
        accepted = bool(True)
    else:
        print("login rejected")