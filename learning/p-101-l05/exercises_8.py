import random


# # exercise 8.1.1
# print(1 <= 1)  # true
# print(1 != 1)  # false
# print(1 != 2)  # true
# print("good" != "bad")  # true
# print("good" != "Good")  # true
# print(123 == "123") # false

# # exercise 8.1.2
# print(3 != 4)
# print(10 > 5)
# print("jack" != "jill")
# print(42 != "42")

# # exercise 8.2.1
# print((1 <= 1) and (1 != 1))  # false
# print(not(1 != 2))  # false
# print(("good" != "bad") or False)  # true
# print(("good" != "Good") and not (1 == 1))  # false

# # exercise 8.2.2
# print(False == (not True))
# print((True and False) == (True and False))
# print(not (True and "A" == "B"))

# exercise 8.3.1
# word = input("Enter a word: ")
#
# if len(word) < 5:
#     print("Your input is less than 5 characters long.")
# elif len(word) > 5:
#     print("Your input is greater than 5 characters long.")
# else:
#     print("Your input is 5 characters long.")

# # exercise 8.3.2
# number = input("I am thinking of a number between 1 and 10. Guess which one.")
# if number == "3":
#     print("You win!")
# else:
#     print("You lose!")

# for n in range(3):
#     password = input("Password: ")
#     if password == "7947":
#         print("Good password.")
#         break
#     print("Password is incorrect.")
# else:
#     print("Suspicious activity. The authorities have been alerted.")

# # exercise 8.5.1
# while True:
#     n = input("Enter a password: ")
#     if n.upper() == "Q":
#         break

# # exercise 8.5.2
# for i in range(1, 51):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i)

# try:
#     number = int(input("Enter an int: "))
# except ValueError:
#     print("That was not an integer!")
#
#
# def divide(num1, num2):
#     try:
#         print(num1 / num2)
#     except(TypeError, ZeroDivisionError):
#         print("Encountered a problem")

# # exercise 8.6.1
# while True:
#     try:
#         number = int(input("Enter an integer: "))
#         print(number)
#     except ValueError:
#         print("Your input is not an integer!")
#         break

# exercise 8.6.2
# some_string = input("Enter a string: ")
# try:
#     n = int(input("Enter an integer: "))
#     print(some_string[n])
# except ValueError:
#     print("Your input is not an integer!")
# except IndexError:
#     print("Your string is out of bounds!")

# def coin_flip():
#     if random.randint(0, 1) == 0:
#         return "heads"
#     else:
#         return "tails"
#
#
# def unfair_coin_flip(probability_of_tails):
#     if random.random() < probability_of_tails:
#         return "tails"
#     else:
#         return "heads"
#
#
# heads_tally = 0
# tails_tally = 0
#
# for trial in range(10_000):
#     if unfair_coin_flip(.7) == "heads":
#         heads_tally += 1
#     else:
#         tails_tally += 1
# print(heads_tally)
# print(tails_tally)
# print(f"The ratio of heads to tails is: {heads_tally / tails_tally}")

# # exercise 8.7.1
# def roll():
#     return f"Your roll is: {random.randint(1, 6)}"
#
#
# print(roll())

# # exercise 8.7.2
# sum_of_rolls = 0
# for i in range(10_000):
#     sum_of_rolls += random.randint(1, 6)
#
# print(f"Average roll is: {int(sum_of_rolls/10_000)}")


