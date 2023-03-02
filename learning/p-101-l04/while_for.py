# WHILE LOOP
# n = 1
# while n < 5:
#     print(n)
#     n += 1
#
# num = float(input("Enter a positive number: "))
# count = 0
# while num <= 0:
#     print("Invalid number!")
#     num = float(input("Enter a positive number: "))
#

# FOR LOOP
# for letter in "Python":
#     print(letter)
#
# for i in range(3):
#     print("Python")
#
# for n in range(10, 20):
#     print(n*n)
#
# amount = float(input("Enter an amount: "))
#
# for num_people in range(2, 6):
#     print(f"{num_people} people: ${amount / num_people:,.2f} each")
#
# for n in range(1, 4):
#     for j in range(4, 7):
#         print(f"n = {n} and j = {j}")
#
#
# # exercise 6.4.1
# for i in range(2, 11):
#     print(i)
#
# # exercise 6.4.2
# n = 1
# while n < 10:
#     n += 1
#     print(n)
#

# exercise 6.4.3
def doubles(num):
    return num * 2


n = int(input("Enter your number: "))
for i in range(0, 3):
    n = doubles(n)
    print(n)
