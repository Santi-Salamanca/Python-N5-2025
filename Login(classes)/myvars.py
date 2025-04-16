class user:
    def __init__ (self, username, password, notes):
        self.username = username
        self.password = password
        self.notes = notes

#example user
person1 = user("John", "John123",["chores",["sweep house", "clean room", "take dog for a walk"]
                                  ,"school",["math homework", "science project"]
                                  ,"work",["finish report", "send email"]])
print(person1.username)
print(person1.password)
print(person1.notes[1][0])
print(person1.notes[1][1])
print(person1.notes[3][0])
print(person1.notes[5][1]) # the chores school and work count as a number for index and are seperate