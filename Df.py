# Cтворіть консольного чат-бота:
#
# 1. Бот повинен привітатися і запитати ім'я користувача
#
# 2. У відповідь привітатися додавши ім'я користувача у привітання
# (ім'я користувача має бути обов'язково з великої літери, навіть якщо користувач вказав ім'я з маленької літери).
# Одразу запитайте вік користувача.
#
# 3. Після отриманння віку користувача, запитайте як справи. Сформуйте фразу в залежності від вказаного віку.
#
# 4. Після запропонуйте 3 теми до обговорення, на ваш вибір.
#
# 5. В залежності від вибраної користувачем теми сформуйте відповідь на данну тему.
#
# 6. В будь-який момент користувач повинен мати можливість вийти із чату вказавши q
#
# 7. Можете розширити діалог як забажаєте. Додайте власну фантазію.

import random
from pprint import pprint
import collections

# block_of_themes = {'theme_1 ': 'answer_1',
#                    'theme_2': 'answer_2',
#                    'theme_3': 'answer_3',
#                    'theme_4': 'answer_4',
#                    'theme_5': 'answer_5',
#                    'theme_6': 'answer_6',
#                    'theme_7': 'answer_7',
#                    'theme_8': 'answer_8',
#                    'theme_9': 'answer_9',
#                    'theme_10': 'answer_10'
#                    }
# while True:
#
#     name = input("Hello and welcome to chatBot, What is your name? (use 'q' to exit)\n:")
#
#     if name == "q":
#         break
#
#     elif name.isalpha():
#
#         if len(name) > 18:
#             print("Too long version, can you use shorter form?")
#             continue
#
#         else:
#             print(f'Nice to meet you, {name.capitalize()}')
#
#             while True:
#
#                 age = input('And now, pls, tell me your age.\n:')
#
#                 if age == "q":
#                     quit()
#
#                 elif age.isdigit():
#
#                     if int(age) <= 15:
#                         print(f'You have to wait at least{16-int(age) } years, young man')
#                         quit()
#
#                     elif int(age) <= 30:
#                         print(f"{int(age)}'s is the best age! ")
#                     else:
#                         print('No Country for Old Men')
#
#                     print('Lets talk about smth?')
#
#                     themes = {}
#
#                     for i in range(1, 4):
#                         themes[i] = random.choice(list(block_of_themes.keys()))
#
#                     while True:
#
#                         pprint(themes)
#
#                         conversation_theme = input('You can choose theme of conversation press [1-3]\n:')
#                         if conversation_theme == "q":
#                             quit()
#                         elif not conversation_theme.isdigit():
#                             print("Use some letters, pls!")
#                             continue
#                         elif int(conversation_theme) not in range(1, 4):
#                             print('No such theme in the pool')
#                             continue
#                         elif int(conversation_theme) in range(1, 4):
#                             print(f'Okay, good choise {(chosen:= themes[int(conversation_theme)])}\n'
#                                   f'{block_of_themes.get(chosen)}')
#
#                 else:
#                     print("Use numbers, for this action !")
#                     continue
#
#     else:
#         print("Wrong answer! Pls type your real name!")
#         continue
#

# Homework_3

# Task 1
#
# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

# while True:
#     my_string = input('input:\n')
#
#     if len(my_string) < 2:
#         print(None)
#     else:
#         print(my_string[:2] + my_string[-2:])


#  Task 2

# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number. The program should check that the
# string contains only numerical characters and is only 10 characters long. Print a suitable message depending
# on the outcome of the string evaluation.

# while True:
#     number = input('Please enter you phone number below:\n+38 ')
#     if number.isdigit():
#         if len(number) == 10:
#             print('validation succeed')
#             break
#         else:
#             print('Mobile number consist from 10 symbols, try type it again ')
#             continue
#     else:
#         print("Only digits allowed!!")


# Task 3
#
# The math quiz program.
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and
# then responds with a message accordingly.
# symbols = [
#      '+',
#      '-',
#      '*',
#      '/'
# ]
# counter = 0
#
# while counter < 10:
#     a = random.randint(-10, 10)
#     b = random.randint(-10, 10)
#     c = random.choice(list(symbols))
#     if b == 0 and c == '/':
#         continue
#     elif c == '+':
#         correct_answer = a + b
#     elif c == '-':
#         correct_answer = a - b
#     elif c == '*':
#         correct_answer = a * b
#     elif c == '/':
#         correct_answer = a / b
#
#     answer = input(f'How much {a} {c} {b}\n:')
#     if answer == 'q':
#         break
#
#     elif correct_answer == int(answer):
#         counter += 1
#         print(f"That's right, your score: {counter} !")
#     elif not answer.isdigit():
#         print('ONLY DIGITS ALOWED, try again')
#     else:
#         print(f'It was {correct_answer}, keep trying')
#
# print("You win, congratulations !!")


# Task 4
#
# The name check.
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The
# program should check if your input is equal to the stored name even if the given name has another case, e.g., if your
# input is “Anton” and the stored name is “anton”, it should return True.
# while True:
#     users_name = 'dmytro'
# input_username = input('Pls enter your username below:\n')
#
# if input_username == 'q':
#     break
# elif not input_username.isalpha():
#     print('USE ONLY LETTERS')
# elif users_name == input_username.lower():
#     print(True)
#     break
# elif users_name != input_username.lower():
#     print('Wrong username')


# Homework_ 4

# Task 1
#
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
# greatings = "Let's play The Guessing game!"
# escape = ['Q', 'q']
# scoore = 0
#
# while scoore < 2:
#     input_number = input(f'Try to guess what number generate the system, from 1 to 10.(use {escape} to quit)\n:')
#     random_number = random.randrange(1, 11)
#     if input_number in escape:
#         quit()
#     if input_number.isdigit():
#         if int(input_number) == random_number:
#             scoore += 1
#             print(f'Well done, it was {random_number}, your scoore is {scoore}')
#         else:
#             print(f'Sorry it was {random_number},you need guess {10 - scoore} times, to win')
#     else:
#         print(f'Only digits allowed, or special symbols like {escape}')
# else:
#     print("Congratulations YOU WIN !!!!!!!!!")

# Task 2
#
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”
#
# def age_analizator():
#     while not (username_input := input('Enter your name pls\n :')).isalpha():
#         print('Only letters allowed, for your name')
#
#     while not (user_age_input := input('Enter your age pls\n:')).isdigit():
#         print('Only digits allowed, for your age')
#     print(user_age_input)
#     return print(f'Hello, {username_input.capitalize()}, on next birthday you"ll be {int(user_age_input) + 1} years')
#
#
# age_analizator()


#
# Task 3
#
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters
# of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)


# def string_shuffle(string):
#     for _ in range(5):
#         s_s = list(string)
#         random.shuffle((s_s))
#         print(s_s)
#
#
# string_shuffle(input('Put some string below\n:'))


# def string_shuffle_2(string):
#     for _ in range(5):
#         a_s = random.sample(string, len(string))
#         print(a_s)
#
#
# string_shuffle_2(input('Put some string below\n:'))

# Home WORK _ 5

# Task 1
#
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

#
# list_1 = []
# while len(list_1) <= 10:
#     list_1.append(random.randint(-10, 10))
# else:
#     print(f"The largest number of {list_1} is {max(list_1)}")


# Task 2

# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

# list_1 = []
# list_2 = []
# while len(list_1) <= 10:
#     list_1.append(random.randint(1, 10))
#     list_2.append(random.randint(1, 10))
# else:
#     pprint((list_1, list_2))
#     print(list((list_3 := set(list_1).intersection(list_2))))

# Task 3
#
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration
# list_1 =[]
# i = 1
# while i < 101:
#     if not i % 7 and i % 5:
#         list_1.append(i)
#     i+= 1
# else:
#     print(list_1)

# print([_ for _ in range(1, 101) if not _ % 7 and _ % 5])


# HOMEWORK -- 6

# Task 1
#
# The greeting program.
# Make a program that has your name and the current day of the week stored as separate variables and then prints a
# message like this: "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.
#
# An additional bonus will be to use different string formatting methods for constructing result string.
# import os
# import time
#
# print(f"Good day {os.getlogin()}! {time.strftime('%A')} is a perfect day to learn some python.")

# Task 2
#
# Manipulate strings.
# Save your first and last name as separate variables, then use string concatenation to add them together with a white
# space in between and print a greeting.

# name = "Dmytro"
# last_name = "Masiukevych"
# print(f'Hello {name} {last_name}')

# Task 3
#
# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division


# posible_actions = ['+', "-", '/', '*', '**', "//"]
# a = input('eneter first number\n')
# b = input('enter second number\n')
#
# while (action := input(f'what action do you want from possible: {posible_actions}\n')) not in posible_actions:
#     print('Use only allowed symbols')
# else:
#     if action == posible_actions[0]:
#         print(f'{a} + {b} = {int(a) + int(b)}')
#
#     elif action == posible_actions[1]:
#         print(f'{a} - {b} = {int(a) - int(b)}')
#
#     elif action == posible_actions[2]:
#         if int(b) == 0:
#             print('you cant devid na 0')
#         else:
#             print(f'{a} / {b} = {int(a) / int(b)}')
#
#     elif action == posible_actions[3]:
#         print(f'{a} * {b} = {int(a) * int(b)}')
#
#     elif action == posible_actions[4]:
#         print(f'{a} ** {b} = {int(a) ** int(b)}')
#
#     else:
#         print(f'{a} // {b} = {int(a) // int(b)}')
#

# Task 1

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

# Зробіть список з елементів, що зустрічаються в обох послідовностях

# list_3 = list(set(list1).intersection(set(list2)))
# print(list_3)

# Task2

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

# Зробіть список унікальних елементів, що входять у ці два списки

# list_3 = list(set(list1).difference(set(list2)).union(set(list2).difference(set(list1))))
# print(list_3)


# Task3
#
# price = [1.09, 23.56, 57.84, 4.56, 6.78]
# TAX_RATE = 0.2
# У вас є ціни товару без ПДВ та податок ПДВ
# Зробіть список цін з ПДВ

# new = [round(i, 1)  * (TAX_RATE + 1) for i in price]
# print(new)

# Task4
# sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'
#
# Зробіть два списка:
#   - перший: тільки голосні літери з цього речення
#   - другий: тільки приголосні
# list_1 = [i for i in sentence if i in 'aeoiu']
# list_2 = [i for i in sentence.strip() if i not in 'aeoiu']
# print(list_1, list_2)

#
# Task6
#
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# # # Уявіть, що у магазині такі великі дисконти, що можуть бути від'ємні ціни
# # #
# # # Зробіть список так, щоб замість від'ємних цін ви просто виставили 'It's a gift'
# # new = [i if i > 0 else "It's a gift" for i in original_prices]
# # print(new)


# Task7
#
# quote = "If I were married to you, I'd put poison in your coffee. If I were married to you, I'd drink it."
# #
# # Виведіть на екран тільки голосні з цієї цитати без повторень, тільки унікальні
# set_1 = {i for i in quote if i in 'aoieu'}
#
# print(set_1)

# Task8
#
# Виведіть на екран словник у якого ключі будуть числа від 1 до 10, а значення це число у кубі
# Додаткова умова ключі повинні бути не числами а строками 1 - це 'один', 2 - 'два' і т.д.


# dict_1 = {str(i): i**3 for i in range(1, 11)}
#
# keys = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
#
# dict_2 = {k: i ** 3 for i, k in enumerate(keys, start=1)}
#
# print(dict_2)

# Task9
#
# Створіть просту матрицю 5 на 5 з випадкових чисел у диапазоні від -9 до 9
# Виведіть красиво на екран
#
# [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
# ]

# matrix = [[random.randint(-9, 9) for i in range(5)] for _ in range(5)]
# pprint(matrix)

# Task10
#
# Візьміть отриману матрицю, та створіть з її елементів список в один рівень
#
# [0, 1, 2, 3, 4,, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
# 0, 1, 2, 3, 4, 0, 1, 2


# list_matrix = [i for j in matrix for i in j]
# print(list_matrix)
# # Task11
# #
# # Порахуйте суму елементів матриці, не враховуючи відмінні числа
# print(sum([i for i in list_matrix if i > 0]))

# Task12
#
# digits = [1, 4, 6, 7, 4, 1, 12, 3, 7, 18]
#
# Зробіть зі списку список, щоб числа не повторювалися, але важливо зберегти порядок чисел

# digits_2 = []
# for i in digits:
#     if i in digits_2:
#         continue
#     digits_2.append(i)
# quit()
# print(digits_2)


# Homework 7

# Task 1
#
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
# the number of occurrences as values.

# sentence = 'aaaab b b, b cccccc'
#
#
# dict_of_sentence = {a: sentence.split().count(a) for a in sentence.split(' ')}
# print(dict_of_sentence)

# Task 2

# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the
# quantity of this exact item.
# total_sum = 0
# for item in stock:
#     item_sum = stock[item] * prices[item]
#     print(f'Sum of {item}\'s is: {item_sum}')
#     total_sum += item_sum
#
# print(f'Total sum: {total_sum}')


# Task 3
#
# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding
# to `i` squared.

# list_of_squared_numbers = [(i, i ** 2) for i in range(1, 11)]
#
# print(list_of_squared_numbers)

# Task 4
#
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

# list_of_wdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sut', 'Sun']
#
# dict_of_wdays = {k: v for (k, v) in enumerate(list_of_wdays, start=1)}
#
# revers_dict_of_wdays = {k: v for (v, k) in enumerate(list_of_wdays, start=1)}
#
# dict_of_wdays_2 = {}
# for day in list_of_wdays:
#     dict_of_wdays_2[list_of_wdays.index(day) + 1] = day
#
# revers_dict_of_wdays_2 = {}
# for day in list_of_wdays:
#     revers_dict_of_wdays_2[day] = list_of_wdays.index(day) + 1
#
# print(dict_of_wdays)
# print(dict_of_wdays_2)
# print(revers_dict_of_wdays)
# print(revers_dict_of_wdays_2)

# Homework 8

# Task 1
#
# Imports practice
#  Make a directory with 2 modules; make a function in one of them; then import this function in the other module and
#  use that in your script of choice.


# homework 9

# Task 100
#
# A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The
# function should then print “My favorite movie is named {name}”.

# def favorite_movie(movie):
#     assert movie.isalpha()
#     print(f'My favorite movie is {movie}')
#
# favorite_movie("dFF")

# Task 2
#
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a
# dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of
# the dictionary to make sure that it works as intended.
#
# countrys_dict = {}
#
#
# def make_country(name, capital):
#     global countrys_dict
#     countrys_dict[name] = capital
#     print(countrys_dict)
#
#
# make_country(capital='Kyiv',name='Ukraine')

# A simple calculator.
#
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep
# things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second
# parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
#
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

# def adder(args):
#     result = 0
#     for a in args:
#         result += a
#     return result
#
#
# def minuser(args):
#     result = 0
#     for a in args:
#         result -= a
#     return result
#
#
# def multipli(args):
#     result = 1
#     for a in args:
#         result *= a
#     return result
#
#
#
# def make_operation(*args):
#     if args[0] == '+':
#         print(adder(args[1:]))
#     elif args[0] == '-':
#         print(minuser(args[1:]))
#     elif args[0] == '*':
#         print(multipli(args[1:]))
#     else:
#         print("wrong")
#
#
# make_operation('*', 5, 5, 10, 25)


STATES_DATA = [
    {
        "name": "California",
        "population": 39512223,
        "growth_change": 6.1
    },
    {
        "name": "Texas",
        "population": 28995881,
        "growth_change": 15.3
    },
    {
        "name": "Florida",
        "population": 21477737,
        "growth_change": 14.2
    },
    {
        "name": "New York",
        "population": 19453561,
        "growth_change": 0.4
    },
    {
        "name": "Pennsylvania",
        "population": 12801989,
        "growth_change": 0.8
    },
    {
        "name": "Illinois",
        "population": 12671821,
        "growth_change": -1.2
    },
    {
        "name": "Ohio",
        "population": 11689100,
        "growth_change": 1.3
    },
    {
        "name": "Georgia",
        "population": 10617423,
        "growth_change": 9.6
    },
    {
        "name": "North Carolina",
        "population": 10488084,
        "growth_change": 10.0
    },
    {
        "name": "Michigan",
        "population": 9986857,
        "growth_change": 1.0
    },
    {
        "name": "New Jersey",
        "population": 8882190,
        "growth_change": 1.0
    },
    {
        "name": "Virginia",
        "population": 8535519,
        "growth_change": 6.7
    },
    {
        "name": "Washington",
        "population": 7614893,
        "growth_change": 13.2
    },
    {
        "name": "Arizona",
        "population": 7278717,
        "growth_change": 13.9
    },
    {
        "name": "Massachusetts",
        "population": 6949503,
        "growth_change": 5.3
    },
    {
        "name": "Tennessee",
        "population": 6833174,
        "growth_change": 7.6
    },
    {
        "name": "Indiana",
        "population": 6732219,
        "growth_change": 3.8
    },
    {
        "name": "Missouri",
        "population": 6137428,
        "growth_change": 2.5
    },
    {
        "name": "Maryland",
        "population": 6045680,
        "growth_change": 4.7
    },
    {
        "name": "Wisconsin",
        "population": 5822434,
        "growth_change": 2.4
    },
    {
        "name": "Colorado",
        "population": 5758736,
        "growth_change": 14.5
    },
    {
        "name": "Minnesota",
        "population": 5639632,
        "growth_change": 6.3
    },
    {
        "name": "South Carolina",
        "population": 5148714,
        "growth_change": 11.3
    },
    {
        "name": "Alabama",
        "population": 4903185,
        "growth_change": 2.6
    },
    {
        "name": "Louisiana",
        "population": 4648794,
        "growth_change": 2.5
    },
    {
        "name": "Kentucky",
        "population": 4467673,
        "growth_change": 3.0
    },
    {
        "name": "Oregon",
        "population": 4217737,
        "growth_change": 10.1
    },
    {
        "name": "Oklahoma",
        "population": 3956971,
        "growth_change": 5.5
    },
    {
        "name": "Connecticut",
        "population": 3565287,
        "growth_change": -0.2
    },
    {
        "name": "Utah",
        "population": 3205958,
        "growth_change": 16.0
    },
    {
        "name": "Puerto Rico",
        "population": 3193694,
        "growth_change": -14.3
    },
    {
        "name": "Iowa",
        "population": 3155070,
        "growth_change": 3.6
    },
    {
        "name": "Nevada",
        "population": 3080156,
        "growth_change": 14.1
    },
    {
        "name": "Arkansas",
        "population": 3017825,
        "growth_change": 3.5
    },
    {
        "name": "Mississippi",
        "population": 2976149,
        "growth_change": 0.3
    },
    {
        "name": "Kansas",
        "population": 2913314,
        "growth_change": 2.1
    },
    {
        "name": "New Mexico",
        "population": 2096829,
        "growth_change": 1.8
    },
    {
        "name": "Nebraska",
        "population": 1934408,
        "growth_change": 5.9
    },
    {
        "name": "Idaho",
        "population": 1787065,
        "growth_change": 14.0
    },
    {
        "name": "West Virginia",
        "population": 1792147,
        "growth_change": -3.3
    },
    {
        "name": "Hawaii",
        "population": 1415872,
        "growth_change": 4.1
    },
    {
        "name": "New Hampshire",
        "population": 1359711,
        "growth_change": 3.3
    },
    {
        "name": "Maine",
        "population": 1344212,
        "growth_change": 1.2
    },
    {
        "name": "Montana",
        "population": 1068778,
        "growth_change": 8.0
    },
    {
        "name": "Rhode Island",
        "population": 1059361,
        "growth_change": 0.6
    },
    {
        "name": "Delaware",
        "population": 973764,
        "growth_change": 8.4
    },
    {
        "name": "South Dakota",
        "population": 884659,
        "growth_change": 8.7
    },
    {
        "name": "North Dakota",
        "population": 762062,
        "growth_change": 13.3
    },
    {
        "name": "Alaska",
        "population": 731545,
        "growth_change": 3.0
    },
    {
        "name": "District of Columbia",
        "population": 705749,
        "growth_change": 17.3
    },
    {
        "name": "Vermont",
        "population": 623989,
        "growth_change": -0.3
    },
    {
        "name": "Wyoming",
        "population": 578759,
        "growth_change": 2.7
    },
    {
        "name": "Guam",
        "population": 165718,
        "growth_change": 4.0
    },
    {
        "name": "U.S. Virgin Islands",
        "population": 104914,
        "growth_change": -1.4
    },
    {
        "name": "American Samoa",
        "population": 55641,
        "growth_change": 0.22
    }
]
#   ДОДАТКОВЕ ДОМАШНЄ ЗАВДАННЯ.
#
#     Task:
#
#     - створіть новий список з цих данних, але відсортований за зростанням населення,
#       у спадаючому порядку (використайте sorted)
#
#     - створіть новий список з цих данних, але відсортований за кількістю
#       населення у зростаючому порядку (використайте sorted)
#
#     - відфілтруйте список, щоб у ньому залишились тільки штати у яких населення
#       більше за середнє значення по країні (використайте filter)
#
#     - створіть новий список в якому до кожного штату має додатись додаткова
#       інформація, "населення зростає", "населення зменшується",
#       "населення не змінне" зі значеннями True або False (використайте map)
#
#     - порахуйте загальну кількість населення у країні
#       (використайте функцію reduce)
#
#     - PS в усіх завданнях використовуйте lambda функції
from pprint import pprint
from functools import reduce


# task_1 = sorted(STATES_DATA, key=lambda x: x['growth_change'], reverse=True)
# # pprint(task_1)
#
# task_2 = sorted(STATES_DATA, key=lambda x: x["population"])
# # pprint((task_2))
#
# task_5 = reduce(lambda accum, value: accum + value["population"], STATES_DATA, 0)
# # print(task_5)
#
# task_3 = list(filter(lambda x: x["population"] > (task_5/len(STATES_DATA)), STATES_DATA))


# pprint(task_3)
#
# task_4 = list(map(lambda x: x["population"] = 'rr', STATES_DATA))

# print(task_4)

#
# import sys
# print(sys.platform)

# HomeWOrk 10

# Task 1

# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
# that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError
# instead of IndexError?

# def oops():
#     # raise KeyError
#     raise IndexError
#
# def oops_catcher():
#     try:
#         oops()
#     except IndexError:
#         print("Gotcha")

# oops_catcher()

# Task 2
#
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
# input function were not numbers, and if value b was zero (cannot divide by zero).


# def my_func():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     try:
#         res = (a * a) / b
#         return print(res)
#     except ZeroDivisionError:
#         print('cannot divide by zero')
#
#
# my_func()

# Task 1
#
# Files
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. Then
# write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system
# command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of the string
# if you want to fully terminate the line in the file.

# with open('my_file.txt', 'w') as file:
#     file.write("Hello file world!!")

# with open('my_file.txt') as file:
#     string_ = file.read()
#
# print(string_)


# HOMEWORK 13


# Task 1
# Write a Python program to detect the number of local variables declared in a function.
#
# def counter():
#     x = 10
#     y = 'Ten'
#     z = [10]


# print(counter.__code__.co_nlocals)
#
# print(dir(counter.__code__))

#
# Task 2
#
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

# def my_func(a, b):
#     def inner():
#         return a + b
#     return inner()
#
#
# print(my_func(5, 10))


# Task 3
#
# Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the list
# are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the
# second one

# def choose_func(nums: list, func1, func2):
#     if all(i > 0 for i in nums):
#         # print('1')
#         return func1(nums)
#
#     else:
#         # print('2')
#         return func2(nums)
#
#
# nums1 = [1, 2, 3, 4, 5]
#
# nums2 = [1, -2, 3, -4, 5]


# def square_nums(nums):
#     return [num ** 2 for num in nums]
#
#
# def remove_negatives(nums):
#     return [num for num in nums if num > 0]

#
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
#
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

# print(choose_func(nums2, square_nums, remove_negatives))
# print(square_nums(nums1))
# print(remove_negatives(nums2))


# args = list(range(5))
# # print(args)
#
#
# def sum_recursion(nums: list):
#
#     if nums[0] == nums[-1]:
#         return nums[0]
#
#     return nums.pop() + sum_recursion(nums)
#
#
# print(sum_recursion(args))

# print(args[0])

# print(args.pop())
# print(args)

# HOMEWORK 14
# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#
# "add called with 4, 5"
# def fucc_args(func):
#     def wrapper(*args, **kwargs):
#         print(f'{func.__name__} calls with {args, kwargs}')
#     return wrapper
#
# @fucc_args
# def adder(a, b):
#     return a + b

# adder(4, 5)

# @fucc_args
# def square_all(*args):
#
#     return [arg ** 2 for arg in args]
#
# square_all(range(4))

from functools import wraps
# Task 2
#
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
#
# def stop_words(words: list):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             slogan = func(*args, *kwargs)
#             for word in words:
#                 slogan = slogan.replace(word, "*")
#
#             return slogan
#         return wrapper
#     return inner
#
#
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"

# print(create_slogan("Steve"))
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise
# , return the result.
#
# def arg_rules(type_: type, max_length: int, contains: list):
#     def inner(funcion):
#         def wrapper(smth):
#             res = funcion(smth)
#             if not isinstance(smth, type_):
#                 print(f"not {type_}")
#                 return False
#
#             elif len(smth) >= 15:
#                 print(f"Longer then {max_length}")
#                 return False
#             for element in contains:
#                     if not element in smth:
#                         print(f'It must contain {contains}')
#                         return False
#             return res
#
#         return wrapper
#     return inner
#
#
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#
#     return f"{name} drinks pepsi in his brand new BMW!"
# #
#
# assert create_slogan('johndoe05@gmail.com') is False
# #
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
#
# create_slogan('S@SH05')


# def cacher(function):
#     dict_of_res = {}
#     def wrapper(*args, **kwargs):
#         key = args + tuple(kwargs.values())
#         if key in dict_of_res:
#             return dict_of_res[key]
#         else:
#             result = function(*args, **kwargs)
#             dict_of_res[key] = result
#             print('new_data')
#             return result
#     return wrapper
#
#
# @cacher
# def add_two(x, y):
#     return x + y
#
# print((add_two(4, 7)))
# print((add_two(4, 7)))
# print((add_two(4, 9)))
# print((add_two(4, y = 10)))
# print((add_two(4, 10)))

