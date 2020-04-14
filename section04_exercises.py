# import random

# Exercise 1: Run the program on your system and see what numbers
# you get.

# print(random.randint(5, 10))  # Random integer from 2 params
# print(random.random())  # Random float x, 0.0 <= x < 1.0
# print(random.uniform(1, 10))  # Random float x, 1.0 <= x < 10.0
#
# t = [1, 2, 3]  # provided list
# print(random.choice(t))  # Random select element from provided list
# print(random.choice('MooRTY'))  # Random select char from string

# Random module also provides functions to generate random values
# from continuous distributions including Gaussian, exponential,
# gamma, and a few more

# Code for Exercise 2 & 3:

# def print_lyrics():
#     print('I\'m a lumberjack, and I\'m okay.')
#     print('I sleep all night and I work all day.')
#
#
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
#
# repeat_lyrics()

# Exercise 2: Move the last line of this program to the top,
# so the function call appears before the definitions. Run the
# program and see what error message you get.

# NameError: name 'repeat_lyrics' is not defined

# Exercise 3: Move the function call back to the bottom and move
# the definition of print_print lyrics after the definition of
# repeat lyrics. What happens when you run this program?

# The program runs as expected. The order of the function
# definitions doesn't seem to matter, but a function call cannot
# be made before a function exists (must be below the created
# function) -- see flow of execution


# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
#
# def print_lyrics():
#     print('I\'m a lumberjack, and I\'m okay.')
#     print('I sleep all night and I work all day.')
#
#
# repeat_lyrics()

# Exercise 6: Rewrite your pay computation program from the previous
# chapter and create a function called compute_pay which also takes
# two parameters (hours and rate)


def compute_pay(hours, rate):
    if hours > 40:
        overtime = (hours - 40) * (1.5 * rate)
        return overtime + (40 * rate)
    else:
        return hours * rate


print(compute_pay(45, 10))

# Exercise 7: Rewrite the grade program from the previous chapter
# using a function called compute_grade that takes a score as its
# parameter and returns a grade as a string.


def compute_grade(score):
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return'D'
        else:
            return 'F'
    else:
        return 'Bad Score'


try:
    user_score = float(input("Enter a score between 0.0 and 1.0: "))
    print(compute_grade(user_score))
except ValueError:
    print("ValueError, Enter a number next time!")
