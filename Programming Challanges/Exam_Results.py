# Create a program that:

# Stores an overall mark for each of 4 different subjects (e.g. English, Maths, Computing, Art & Design)
# Calculates the sum total of all marks entered by the user
# Calculates the average mark
# Displays all results with appropriate labels
total = 0
subjects = 4
marks_dict = {}
for i in range(subjects):
    sub = str(input("Please enter your subject: "))
    mark = int(input("Please enter your mark: "))
    total += mark
    marks_dict.update({sub:mark})
average = total/int(subjects)
for x,y in marks_dict.items():
    counter = 0
    print(f"Your mark for {x} is: {y}")
    counter += 1
print("ypour average marks is: ",average)