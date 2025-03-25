temperatures = []

print("")
for i in range (5):
    while True:
        temperature = int(input("Please input a temperature: "))
        if temperature >= -20 and temperature <= 50:
            temperatures.append(temperature)
            break
        else:
            print("temperature must be between -20 and 50")
print("Here are all the temperatures: "+temperatures)
total = 0
for x in range(len(temperatures)):
    total += temperatures[x]
print(f"The average temperature is: {round(total/5, 1)}")



    