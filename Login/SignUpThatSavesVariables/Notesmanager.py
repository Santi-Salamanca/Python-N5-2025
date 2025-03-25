#1. Personal Notes Manager
#Description: Allow users to create, view, edit, and delete personal notes after logging in.
#Features:
#Each user has their own set of notes stored in a file or database.
#Users can search for notes by title or content.
#Notes are saved and loaded automatically when the user logs in.

Notes = [
    [[]]
]
def Noteadd():
    note = str(input("Please enter a new Note: "))
    name_of_note = str(input("Please enter the name of this Note: "))
    def skibidi(note, name_of_note):
        Notes[[]].append(note)
        Notes[[]].append(name_of_note)

