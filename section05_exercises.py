
# Exercise 1: Write a program which repeatedly reads numbers
# until the user enters "done". Once "done" is entered, print out the
# total, count, and average of the numbers. If the user enters
# anything other than a number, detect their mistake using try
# and except and print an error message and skip to the next number

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid Input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333333  # Total, Count, Average

# total = 0
# count = 0
# while True:
#     user_inp = input("Enter a number: ")
#     try:
#         if user_inp == 'done':
#             print(total, count, (total / count))
#             break
#         else:
#             total += int(user_inp)
#             count += 1
#     except ValueError:
#         print("Invalid Input, type 'done' to exit")

# Exercise 2: Write another program that prompts for a list of
# numbers as above and at the end prints out both the maximum and
# minimum of the numbers instead of the average

maximum = None
minimum = None
while True:
    user_inp = input("Enter a number: ")
    try:
        if user_inp == 'done':
            print(maximum, minimum)
            break
        elif maximum is None or minimum is None:
            maximum = int(user_inp)
            minimum = int(user_inp)
        else:
            if int(user_inp) > maximum:
                maximum = int(user_inp)
            elif int(user_inp) < minimum:
                minimum = int(user_inp)
    except ValueError:
        print("Invalid Input, type 'done' to exit")

# I could clean this code up a lot more if I used functions
# Since functions weren't recommended in the instructions, I didn't
# do it. I din't do it ~ blurp - I din't do it ~ blurp - ... n
