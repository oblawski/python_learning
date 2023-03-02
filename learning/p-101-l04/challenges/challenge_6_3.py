# Write a program called temperature.py that defines two functions:

# 1. convert_cel_to_far(), which takes one float parameter representing degrees Celsius
# and returns a float representing the same temperature
# in degrees Fahrenheit using the following formula:
# F = C * 9/5 + 32

# 2. convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit
# and returns a float representing the same temperature
# in degrees Celsius using the following formula:
# C = (F - 32) * 5/9

# The program should do the following:
# 1. Prompt the user to enter a temperature in degrees Fahrenheit
# and then display the temperature converted to Celsius
# 2. Prompt the user to enter a temperature in degrees Celsius
# and then display the temperature converted to Fahrenheit
# 3. Display all converted temperatures rounded to two decimal places

temp_C_to_F_input = float(input("Enter a temperature in degrees C: "))
temp_F_to_C_input = float(input("Enter a temperature in degrees F: "))


def convert_cel_to_far(cel_degrees):
    far_degrees = cel_degrees * 9 / 5 + 32
    return f"{cel_degrees:.2f} degrees C = {far_degrees:.2f} degrees F"


def convert_far_to_cel(far_degrees):
    cel_degrees = (far_degrees - 32) * 5 / 9
    return f"{far_degrees:.2f} degrees F = {cel_degrees:.2f} degrees C"


print(convert_cel_to_far(temp_C_to_F_input))
print(convert_far_to_cel(temp_F_to_C_input))
