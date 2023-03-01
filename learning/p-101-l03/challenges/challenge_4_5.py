#first letter
#Write a program named first_letter.py that prompts the user for input with the string "Tell me your password:".
# The program should then determine the first letter of the user’s input,
# convert that letter to uppercase, and display it back.

password = input("Tell me your password: ")
print("The first letter you entered is: " + password[0].upper())