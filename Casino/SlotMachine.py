#modules

import random
import time
from colorama import Fore

MAX_LINES = 3 #constant line
MAX_BET = 1000 #constant line accessible anywhere
MINIMUM_BET = 10

ROWS = 3
COLS = 3

symbol_count = { #creates the chances for the symbols on the slot machine
    "A": 2,
    "B": 4,
    "C": 6,
    "D":8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#creates the chances for the machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): #when u want to loop throguh something but dont care about the 
            all_symbols.append(symbol) #iteration u can just use _ and u wont have an unused variable
    columns = []
    for _ in range(cols): #loops this the amount of columns
        column = []
        current_symbols = all_symbols[:] #: creates a copy
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(Fore.GREEN + f"{column[row]}", end=" | " + Fore.WHITE)
            else:
                print(Fore.GREEN + f"{column[row]}", end="" + Fore.WHITE)
        print()
        time.sleep(0.5)

#this function responsible for collecting users deposit
def deposit():
    while True:
        amount = input(Fore.CYAN + "How much money would you like to depost?: £" + Fore.WHITE)
        if amount.isdigit(): #this checks if the input is a number
            amount = int(amount) #this turns the amount into an integer as it is a string as default
            if amount > 0:
                break #ends the while loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


#get lines function
def get_number_of_lines():
    while True:
        lines = input(Fore.CYAN + "Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")?: " + Fore.WHITE)
        if lines.isdigit(): #this checks if the input is a number
            lines = int(lines) #this turns the amount into an integer as it is a string as default
            if 1<= lines <= MAX_LINES:
                break #ends the while loop
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

#function to get the betting amount
def getBet():
    while True:
        amount = input(Fore.CYAN + f"Enter how much do you want to bet on each line? (£{MINIMUM_BET}-£{MAX_BET}): £" + Fore.WHITE)
        if amount.isdigit(): #this checks if the input is a number
            amount = int(amount) #this turns the amount into an integer as it is a string as default
            if MINIMUM_BET<= amount <= MAX_BET:
                break #ends the while loop
            else:
                print(f"Amount must be between £{MINIMUM_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = getBet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

###main lines
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")



main()