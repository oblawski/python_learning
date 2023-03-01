# exponent challenge
# Write a program called exponent.py that receives
# two numbers from the user and displays the first number
# raised to the power of the second number.


num1 = input("Enter a base: ")
num2 = input("Enter an exponent: ")
result = float(num1) ** float(num2)
print(f"{num1} to the power of {num2} is {result}.")

