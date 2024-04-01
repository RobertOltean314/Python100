import random

# Exercise 1: Average Height

# student_heights = [180, 124, 165, 173, 189, 169, 146]
# sum = 0
#
# for student_height in student_heights:
#     sum += student_height
#
# print(f"The average student height in this class is: {sum / len(student_heights)}")

# ----------------------------------------------------------------------------------------------- #

# Exercise 2: Highest Score

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest_score = 0
#
# for student_score in student_scores:
#     if student_score > highest_score:
#         highest_score = student_score
#
# print(f"The highest score in the class is: {highest_score}")

# ----------------------------------------------------------------------------------------------- #

# Exercise 3: Adding Even Numbers

# def sum_of_even_numbers(x):
#     sum = 0
#     for i in range(1, x + 1):
#         if i % 2 == 0:
#             sum += i
#     return sum
#
#
# print(f"The sum of even numbers from 1 to 100 is: {sum_of_even_numbers(100)}")

# ----------------------------------------------------------------------------------------------- #

# Exercise 4: FizzBuzz

# for i in range(1, 101):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# ----------------------------------------------------------------------------------------------- #

# Exercise 5: Random Password Generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")
