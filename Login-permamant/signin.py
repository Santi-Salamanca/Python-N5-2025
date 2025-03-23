# Import the users list from myvars.py
from myvars import users
import os, time  # Import os to handle file paths and clear the console

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' for Windows, 'clear' for Linux/Mac

# Call the function to clear the console at the start of the program
clear_console()

# Ensure users is initialized as a list if not already
if not isinstance(users, list):
    users = []

# Function to save the updated users to myvars.py
def save_to_myvars():
    myvars_path = os.path.join(os.path.dirname(__file__), "myvars.py")
    with open(myvars_path, "w") as f:
        f.write(f"users = {users}\n")
    print("Users saved successfully!")
    time.sleep(2)  # Wait for 2 seconds before clearing the console
    clear_console()

# Main program loop
while True:
    # Ask the user if they want to sign in or sign up
    signQ = input("Do you want to sign in (y/n): ").strip().lower()
    clear_console()  # Clear the console after input

    if signQ == "y":  # If the user wants to sign in
        username = input("Please enter your username: ").strip()
        if username in [user[0] for user in users]:  # Check if the username exists
            password = input("Please enter your password: ").strip()
            if any(user[0] == username and user[1] == password for user in users):  # Check if the password matches
                print(f"Login successful! Welcome, {username}.")
                time.sleep(2)  # Wait for 2 seconds before clearing the console
                clear_console()
                break  # Exit the program after successful login
            else:
                print("Incorrect password. Please try again.")
                time.sleep(2)  # Wait for 2 seconds before clearing the console
                clear_console()
        else:
            print("Username not found. Please try again or sign up.")
            time.sleep(2)  # Wait for 2 seconds before clearing the console
            clear_console()

    elif signQ == "n":  # If the user doesn't want to sign in
        # Ask if the user wants to sign up
        upQ = input("Would you like to sign up (y/n): ").strip().lower()
        clear_console()
        if upQ == "y":  # If the user wants to sign up
            while True:
                new_user = input("Please enter a username to sign up: ").strip()
                if not new_user:  # Check if the username is empty
                    print("Username cannot be empty. Please try again.")
                    time.sleep(1)  # Wait for 1 seconds before clearing the console
                    clear_console()
                elif new_user in [user[0] for user in users]:  # Check if the username already exists
                    print("This username already exists. Please try again.")
                    time.sleep(1)  # Wait for 1 seconds before clearing the console
                    clear_console()
                else:
                    new_password = input("Please enter a password: ").strip()
                    clear_console()  # Clear the console after input
                    users.append((new_user, new_password))  # Add the new username and password as a tuple

                    # Save the updated users list to myvars.py
                    save_to_myvars()

                    print("Sign-up successful! You can now sign in.")
                    time.sleep(2)  # Wait for 2 seconds before clearing the console
                    clear_console()
                    break  # Exit the sign-up loop
        else:
            print("Goodbye!")  # If the user doesn't want to sign up, exit the program
            time.sleep(2)  # Wait for 2 seconds before clearing the console
            clear_console()
            break  # Exit the main loop

    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        time.sleep(2)  # Wait for 2 seconds before clearing the console
        clear_console()