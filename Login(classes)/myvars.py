class user:
    def __init__ (self, username, password, notes):
        self.username = username
        self.password = password
        self.notes = notes
        notes = [[]]

#example user
person1 = user("John", "John123",["chores",["sweep house", "clean room", "take dog for a walk"]] )
print(person1.username)
print(person1.password)
print(person1.notes[0][1])