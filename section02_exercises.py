# These exercises were taken from the Python for Everyone PDF

# Exercise 2: Write a program that uses input to prompt a user
# for their name and then welcomes them.

# name = input("Enter your name: ")
# print("Hello " + name)

# Exercise 3: Write a program to prompt the user for hours and rate
# per hour to compute gross pay.

# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Pay Rate: "))
# pay = rate * hours
# print(pay)

# Exercise 4: Assume we execute the following assignment statements
# width = 17
# height = 12.0

# For each of the following expressions, write the value of the
# expression and the type (of the value of the expression)

# width // 2  ==> returns 8
# width / 2.0 ==> return 8.5
# height / 3  ==> returns 4.0
# 1 + 2 * 5   ==> returns 11

# use the python interpreter to check your answers ^

# Exercise 4: Write a program which prompts the user for a Celsius
# temperature, convert the temperature to Fahrenheit, and print out
# the converted temperature.

cel = float(input("Please enter a Celsius temperature: "))
fah = cel * 9 / 5 + 32
print(fah)

