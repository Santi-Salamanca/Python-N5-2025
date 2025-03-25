class character: #creates a class called character
    #the self, is the main thing that makes this work as self is the variable that will be acted upon
    #the health and damage and speed; are attribuytes that get given to whatever variable this is being assigned to
    def __init__(self, health, damage, speed): # the init line iunitializes the class
        self.health = health
        self.damage = damage
        self.speed = speed


Voltron = character(100,20,25) #this uses the class to create a variable called Voltron which has certain characteristics of speed health and damage
print(Voltron.health)
print(Voltron.damage)
print(Voltron.speed)