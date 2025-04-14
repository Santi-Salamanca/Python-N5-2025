# Program 4 - Investigate and modify
age = float(input("Please enter your age: "))
if age < 0.0:
  print("Not possible! You have to be at least 0 years old.")
elif age < 18.0:
  print("You cannot drive a car yet.")
else:
  print("You can drive a car.")


