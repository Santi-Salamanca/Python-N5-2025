# Write a program that:

# Stores a temperature in Celsius in a variable
# Converts it to Fahrenheit using the formula: F = (C × 9/5) + 32
# Displays both temperatures with appropriate labels
temperature = int(input("Please input the temperature in celcuius: "))
farenheit = (int(temperature) * 9/5) + 32
print(f"The temperature in clecius is: {temperature}")
print(f"The temperature in farenheit is: {farenheit}")