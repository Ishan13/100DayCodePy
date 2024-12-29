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


def fizz_buzz():

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()
