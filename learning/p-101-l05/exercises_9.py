from __future__ import print_function
import copy

# """TUPLES"""

# my_first_tuple = (1, 2, 3, 4, 5, 6)
#
# print(my_first_tuple[0:5])
# x = tuple("Python")
# print(x)
# print(x[2])
#
# coordinates = 4.21, 9.29
# x, y = coordinates
# print(coordinates)
#
# name, age, work = "Bartosz", 28, "dega sadge"
# print(name)
# print(age, work)
#
# vowels = ("a", "e", "i", "o", "u")
# print("a" in vowels)
#
#
# def adder_subtractor(num1, num2):
#     return (num1 + num2, num1 - num2)
#
#
# print(adder_subtractor(3, 2))
#
# # exercise 9.1.1
# cardinal_numbers = "first", "second", "third"
# print(cardinal_numbers)
#
# # exercise 9.1.2
# print(cardinal_numbers[1])
#
# # exercise 9.1.3
# position1, position2, position3 = cardinal_numbers
# print(position1)
# print(position2)
# print(position3)
#
# # exercise 9.1.4
# my_name = tuple("Bartosz")
# print(my_name)
#
# # exercise 9.1.5
# print("x" in my_name)
#
# # exercise 9.1.6
# new_tuple = my_name[1:]
# print(new_tuple)

# """LISTS"""
#
# n = list(input())
# print(n)
#
# colors = ["red", "yellow", "green", "blue"]
# colors.insert(1, "violet")
# print(colors)
# colors.pop(0)
# print(colors)
# colors.append("lagoon")
# print(colors)

# n = [1, 2, 3, 4, 5]
# suma = 0
# for numbers in n:
#     suma += numbers
# print(suma)
#
# print(sum(n))
# print(min(n))
# print(max(n))
#
# numbers = [1,2,3,4,5]
# squares = [num**2 for num in numbers]
# print(squares)
#
# # exercise 9.2.1
# food = ["rice", "beans"]
# print(food)
#
# # exercise 9.2.2
# food.append("broccoli")
# print(food)
#
# # exercise 9.2.3
# food.extend(("bread", "pizza"))
# print(food)
#
# # exercise 9.2.4
# print(food[0:2])
#
# # exercise 9.2.5
# print(food[-1])
#
# # exercise 9.2.6
# breakfast = "eggs,fruit,orange juice".split(",")
# print(breakfast)
#
# # exercise 9.2.7
# print(len(breakfast) == 3)
#
# # exercise 9.2.8
# lengths = [len(word) for word in breakfast]
# print(lengths)

# TODO: Implement this part of code in future project
# def board_size(height, width):
#     game_board = []
#     for i in range(height):
#         game_board.append(width * ['-'])
#     return game_board
#
#
# board = board_size(3, 3)
# for element in board:
#     print(' '.join(element))
# TODO: make a function to replace any element in a board and then print it

# """copying a list"""

# animals = ["lion", "tiger", "cat"]
# large_cats = animals
# large_cats.append("Tiger")
# print(animals)
#
# """original list has also been changed"""
#
# animals = ["lion", "tiger", "cat"]
# large_cats = animals[:]
# large_cats.append("leopard")
# print(large_cats)
# print(animals)
#
# """copying list of lists"""
# matrix1 = [[1, 2], [3, 4]]
# matrix2 = matrix1[:]
# matrix2[0] = [5, 6]
# print(matrix1)
# print(matrix2)
#
# """when you try to change 1st element in 2nd list in matrix:"""
# matrix2[1][0] = 1
# print(matrix2)
# print(matrix1)
# # both matrixes changed 2nd list's value # SHALLOW COPY - PŁYTKIE KOPIOWANIE (?)
#
# """To copy lists and all its elements - deep copy"""
# # import copy !!!
# matrix3 = copy.deepcopy(matrix1)
# matrix3[1][0] = 3
# print(matrix1)
# print(matrix3)

"""SORTING LISTS"""
# .sort() method - by default, the list is sorted in alphabetical or numerical order

colors = ["red", "blue", "yellow", "green"]
colors.sort()
print(colors)

numbers = [5, 3, 7, 31, 2]
numbers.sort()
print(numbers)

colors.sort(key=len)
print(colors)


def get_second_element(item):
    return item[1]


items = [[4, 1], [1, 2], [-9, 0]]
items.sort(key=get_second_element)
print(items)

# exercise 9.4.1
data = ((1, 2), (3, 4))

# exercise 9.4.2
count = 1
for i in data:
    print(f"Row {count} sum: {sum(i)}")
    count += 1

# exercise 9.4.3
numbers = [4, 3, 2, 1]

# exercise 9.4.4
number1 = numbers[:]

#exercise 9.4.5
numbers.sort()
print(numbers)
