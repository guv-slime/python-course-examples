# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly pay for hours worked about 40 hours

# Enter hours: 45
# Enter rate: 10
# Pay: 475.0

# Exercise 2: Rewrite your pay program using try and except so that
# your program handles non-numeric input gracefully by printing a
# message and exiting the program.

# try:
#     hours = float(input('Enter your hours for this week: '))
#     rate = float(input('Enter your hourly rate: '))
#     if hours > 40:
#         overtime = (hours - 40) * (1.5 * rate)
#         pay = overtime + (40 * rate)
#     else:
#         pay = hours * rate
#     print(pay)
# except ValueError:
#     print('Value Error, please enter numeric input next time')

# Exercise 3: Write a program to prompt for a score between 0.0
# and 1.0.  If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade (A - F)

try:
    score = float(input('Enter a score between 0.0 and 1.0: '))
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print('Bad Score')
except ValueError:
    print('Value Error, please enter a valid number')
