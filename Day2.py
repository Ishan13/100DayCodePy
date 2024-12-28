# print("Hello"[-1])

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# print(type(num_char))

# two_digit_number = input("Type a two digit number: ")
# # print(type(two_digit_number))
# first_num = int(two_digit_number[0])
# second_num = int(two_digit_number[1])
# add_num = first_num + second_num
# # print(type(first_num))
# print(add_num)

# PEMDASLR
# ()
# **
# */
# +-

# print(3*(3+3)/3-3)

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = float(weight)/float(height) ** 2
# print(int(bmi))

# print(round(8/3))

# score = 0
# height = 1.8
# isWinning = True
# #f-String
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}.")

# age = input("What is your current age? ")
# age_full = 90 - int(age)
# age_day = 365 * age_full
# age_week = 52 * age_full
# age_month = 12 * age_full
#
# print(f"You have {age_day} days, {age_week} weeks, {age_month} months left.")

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
# print(type(total_bill))
tip_percentage = 1 + (int(input("What percentage tip would you like to give? 10, 12, or 15? "))/100)
split_qty = int(input("How many people to split the bill? "))
# print(tip_percentage)
each_payment = round(((total_bill * tip_percentage) / split_qty), 2)
final_payment = "{:.2f}".format(each_payment)
print(f"Each person should pay: ${final_payment}")
