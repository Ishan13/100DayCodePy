# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# number = int(input("Which number do you want to check? "))
# modulo = number % 2
#
# if modulo == 0:
#     print("This is an even number !")
# else:
#     print("This is an odd number !")

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / (height ** 2))
#
# if bmi < 18.5:
#     print(f"your bmi is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"your bmi is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"your bmi is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"your bmi is {bmi}, you are obese.")
# else:
#     print(f"your bmi is {bmi}, you are clinically obese.")

# year = int(input("Which year do you want to check? "))
# modulo4 = year % 4
# modulo100 = year % 100
# modulo400 = year % 400
#
# if (modulo4 == 0 and modulo100 != 0) or (modulo4 == 0 and modulo100 == 0 and modulo400 == 0):
#     print("Leap Year !")
# elif modulo4 == 0 and modulo100 == 0 and modulo400 == 0:
#     print("Leap Year !")
# else:
#     print("Not a Leap Year !")

# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap Year.")
# else:
#     print("Not a Leap Year.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y" and extra_cheese == "N":
#         bill += 2
#     elif add_pepperoni == "Y" and extra_cheese == "Y":
#         bill += 3
#     elif add_pepperoni == "N" and extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y" and extra_cheese == "N":
#         bill += 3
#     elif add_pepperoni == "Y" and extra_cheese == "Y":
#         bill += 4
#     elif add_pepperoni == "N" and extra_cheese == "Y":
#         bill += 1
# else:
#     bill += 25
#     if add_pepperoni == "Y" and extra_cheese == "N":
#         bill += 3
#     elif add_pepperoni == "Y" and extra_cheese == "Y":
#         bill += 4
#     elif add_pepperoni == "N" and extra_cheese == "Y":
#         bill += 1
#
# print(f"Your final bill is $ {bill}.")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n ")
# name2 = input("What is their name? \n ")
#
# name = name1 + name2
# # print(name)
# lower_case_name = name.lower()
#
# t_name_count = lower_case_name.count("t")
# r_name_count = lower_case_name.count("r")
# u_name_count = lower_case_name.count("u")
# e_name_count = lower_case_name.count("e")
#
# l_name_count = lower_case_name.count("l")
# o_name_count = lower_case_name.count("o")
# v_name_count = lower_case_name.count("v")
#
# true_count_name = t_name_count + r_name_count + u_name_count + e_name_count
# love_count_name = l_name_count + o_name_count + v_name_count + e_name_count

# total_percent = (true_count_name * 10) + love_count_name
# total_percent = int(str(true_count_name)+str(love_count_name))
# total_percent: int = 63

# if total_percent < 10 or total_percent > 90:
#     print(f"Your score is {total_percent}%, you go together like code and mentos.")
# elif (total_percent >= 40) or (total_percent <= 50):
#     print(f"Your score is {total_percent}%, you are alright together.")
# else:
#     print(f"Your score is {total_percent}%.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")