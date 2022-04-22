# Task-1:
# Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.

temperature_1 = float(input("Please enter a Celcius temperature: "))
temperature_2 = temperature_1 * 1.8 + 32
print((f"{temperature_1} Celcius is equal to {temperature_2} Fahrenheit."), "\n")

# Task-2:
# Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result.

distance_1 = int(input("Please enter a distance in km: "))
distance_2 = distance_1 / 1.609344
print(f"{distance_1} km is equal to {distance_2} mil.")
