import random
Endings = ["ing","end","axe","gex","goh"]
num_of_Students = int(input("Enter number of students: "))
for student in range (0, num_of_Students):
    student_name = input("Enter the first 3 letters of the student's name: ")
    while len(student_name) != 3:
        print("Error student's name is not 3 letters long")
        student_name = input("Enter the first 3 letters of the student's name: ")
    ran_num = random.randint(0,4)#5
    ending_chosen = Endings[ran_num]#6
    generated_username = student_name + ending_chosen#6
    print(generated_username)