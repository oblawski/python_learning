# def multiply(x, y):  # function signature
#     # function body
#     """Return the product of two numbers x and y"""
#     product = x * y
#     return product
#
#
# num = multiply(2, 4)
# print(num)
#
#
# def greet(name):
#     print(f"Hi, {name}!")
#
#
# greet("Bartek")
#
# help(multiply)
#
#
# # exercise 6.3.1
# def cube(x):
#     num = x ** 3
#     return num
#
#
# print(cube(3))
#
#
# # exercise 6.3.2
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet("Bartek")

total = 0


def add_to_total(n):
    global total
    total = total + n


add_to_total(5)
print(total)

"""you cant use variable if its not assigned to anything in global scope"""


# x = 5


# def outer_func():
#     y = 2
#
#     def inner_func():
#         z = x + y
#         return z
#
#     return inner_func()
#
#
# print(outer_func())
