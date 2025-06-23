# Create a simple text-based adventure game called "The Mystery Mansion" where players can explore four different locations.

# Your program must demonstrate understanding of 1D arrays, input validation, and string concatenation.

# Your adventure takes place in a mysterious mansion with these four rooms:

# Entrance Hall - "A grand foyer with a crystal chandelier"
# Library - "Dusty bookshelves stretch from floor to ceiling"
# Kitchen - "Copper pots hang above an old stone hearth"
# Garden - "Overgrown vines twist around marble statues"
############################################################
# Technical Requirements
# 1. 1D Arrays

# Location Names Array: Store the four location names
# Location Descriptions Array: Store detailed descriptions for each location
# Available Commands Array: Store valid player commands (N, S, E, W, quit, help)

# 2. Input Validation

# The valid directions are north (N), south (S), east (E) and west (W).
# If the user enters anything that isn’t a valid command or direction, display a helpful error message.

# 3. String concatenation

# You should combine the location name and description when displaying this to the player.
# You should create a personalised welcome message using the player’s name

location_names = ["Entrance Hall", "Library", "Kitchen", "Garden"]
location_descriptions = ["A grand foyer with a crystal chandelier", "Dusty bookshelves stretch from floor to ceiling", "Copper pots hang above an old stone hearth", "Overgrown vines twist around marble statues"]
player_commands = ["N", "S", "E", "W", "quit", "help"]



while True:
    name = input("Please enter your player name: ")
    print("You are in a Mystery Mansion.")

    command = input("where would you like to go?: (N, S, E, W, quit, help)")
    if player_commands.includes(command):
        
    else:
        print("That is not a valid command!")
    

