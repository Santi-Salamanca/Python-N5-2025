list_of_users = []
logged_in = False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def signUp():
    user = input("What would you like your username to be?: ")
    passw = input("What would you like your password to be?: ")
    p1 = User(user, passw)
    list_of_users.append(p1)
    ###delete after testing is done
    for i in list_of_users:
        print(i.username)
        print(i.password)

def login():
    global logged_in
    username = input("Enter your username:")
    user_password = input("Enter your password: ")
    for i in list_of_users:
        if username == i.username and user_password == i.password:
            
            logged_in = True
        else:
            logged_in = False
    if logged_in == True:
        print("You are logged in!")
    else:
        again = input("Your login info was not found. Would you like to try again(e) or extit back to menu?(q): ")
        while True:
            if again == "e":
               login()

            elif again == "q":
                break
            else:
                print("Invalid input try again!")

while True:
    signUp()
    login()
    