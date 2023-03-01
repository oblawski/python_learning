# #exercise 4.1.1
# first_string = "An example of string with \"quotation marks inside\""
# print(first_string)
#
# #exercise 4.1.2
# second_string = "Another example of 'string with quotation marks inside'"
# print(second_string)
#
# #exercise 4.1.3
# third_string = """So far in this book we have concentrated on a number of introductory ideas,
# mainly concerned with programming. We are now going to change tack and look at some mathematics,
# although we will present some programs later."""
# print(third_string)
#
# #exercise 4.1.4
# fourth_string = "So far in this book we have concentrated on a number of introductory ideas, " \
#                "mainly concerned with programming. We are now going to change tack and look at some mathematics, " \
#                "although we will present some programs later."
# print(fourth_string)

# #exercise 4.2.1
# name = "Bartosz"
# print(len(name))
#
# #exercise 4.2.2
# name = "Bartosz"
# surname = "Obławski"
# print(name + surname)
#
# #exercise 4.2.3
# name = "Bartosz"
# surname = "Obławski"
# print(name + " " + surname)
#
# #exercise 4.2.4
# print("bazinga"[2:6])
#
# name = "Bartosz Obławski    "
# print(name.rstrip())

# #exercise 4.3.1
# string_one = "Animals"
# string_two = "Badger"
# string_three = "Honey Bee"
# string_four = "Honey Badger"
#
# print(string_one.lower())
# print(string_two.lower())
# print(string_three.lower())
# print(string_four.lower())
#
# #exercise 4.3.2
# print(string_one.upper())
# print(string_two.upper())
# print(string_three.upper())
# print(string_four.upper())
#
# #exercise 4.3.3
# string1 = "    Filet Mignon"
# string2 = "Brisket    "
# string3 = "  Cheeseburger   "
#
# print(string1.lstrip())
# print(string2.rstrip())
# print(string3.strip())
#
# #exercise 4.3.4
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = "bEautiful"
#
# print(string1.startswith("be"))
# print(string2.startswith("be"))
# print(string3.startswith("be"))
# print(string4.startswith("be"))

# #exercise 4.4.1
# name = input("Tell me your name. ")
# print("Hi, " + name + ".")
#
# #exercise 4.4.2
# x = input("Write something in uppercase, please.")
# print(x.lower())
#
# #exercise 4.4.3
# y = input()
# print(len(y))
#
# number = input("Type some number: ")
# print(float(number))
#
# num1 = 10
# num2 = 5
# print("Im going to eat " + str(num1) + " pancakes.")
# print("Im going to eat " + str(num1 - num2) + " pancakes.")
#
# #exercise 4.6.1
# string = "2"
# print(int(string))
#
# #exercise 4.6.2
# string = "2.0"
# print(float(string))
#
# #exercise 4.6.3
# string = "2"
# number = 3
# print(string + str(number))
#
# #exercise 4.6.4
# num1 = input("First number: ")
# num2 = input("Second number: ")
# result = float(num1) * float(num2)
# print(result)
#
# name = "Zaphod"
# heads = 2
# arms = 3
# print(f"{name} has {heads} heads and {arms} arms.")
# print("{} has {} heads and {} arms.".format(name, heads, arms))
#
# n = 2
# m = 3
# print(f"{n} times {m} is {n*m}")
#
# #exercise 4.7.1
# weight = 0.2
# animal = "newt"
# print(str(weight) + " kg is the weight of the " + animal)
#
# #exercise 4.7.2
# print("{} kg is the weight of the {}".format(weight, animal))
#
# #exercise 4.7.3
# print(f"{weight} kg is the weight of the {animal}")
#
# phrase = "the surprise is in here somewhere"
# print(phrase.find("surprise"))
# print(phrase.find("eloelo"))
# print("the surprise is in here somewhere".find("SURPRISE"))
#
# print("I put a string in your string".find("string"))
# # returns the index of first appearance, starting from begining.
#
# print("My number is: 668-834-044.".find("8"))
# # .find() accepts only strings
#
# my_story = "I'm telling you the truth; nothing but the truth!"
# print(my_story.replace("the truth", "lies"))
#
# #exercise 4.8.1
# print("AAA".find("a"))
#
# #exercise 4.8.2
# string = "Somebody said something to Samantha."
# print(string.replace("s", "x"))
#
# #exercise 4.8.3
# name = input("Your name is: ")
# print(name.find("s"))


