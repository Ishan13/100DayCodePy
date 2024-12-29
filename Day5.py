# fruits = ["Apple", "Peach", "Pear"]  # This is a list.
# for i, fruit in enumerate(fruits):  # using enumerate function to get the index and the value in the list.
#     print(f"Index: {i}, Fruit: {fruit}")
#

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# sum_student = 0
# count = 0
# for y in student_heights:
#     sum_student = sum_student + y
#     count += 1
# mid_height = round(sum_student / count)
# print(mid_height)


# student_scores = input("Input a list of student score ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# score_maxvalue = 0
# for score in student_scores:
#     if score_maxvalue < score:
#         score_maxvalue = score
# print(f"The highest score in the class is : {score_maxvalue}")

# value = 0
# for i in range(2, 101):
#     if i % 2 == 0:
#         value += i
# print(value)

# value2 = 0
# for i in range(2, 101, 2):
#     value2 += i
#
# print(value2)


# def fizz_buzz():
#
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
#
# fizz_buzz()

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#  Eazy Level - Order not randomised:
#  e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

#  Hard Level - Order of characters randomised:
#  e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
