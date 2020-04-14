# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.13.90])
#   BY FRANKENSTEIN.MAIL.UMICH.EDU (CRYUS V2.3.8) WITH LMTPA;
#   SAT, 05 JAN 2008 09:14:16 -0500

# f_name = input("Enter a file name: ")
# f_hand = None
# try:
#     f_hand = open(f_name)
# except FileNotFoundError:
#     print("Please enter a valid file name.")
#     quit()
#
# for line in f_hand:  # not sure how to fix this
#     line_strip = line.rstrip()
#     print(line_strip.upper())

# Note that spaces are still printed throughout the file...


# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:

# X-DSPAM-CONFIDENCE: 0.8475

# When you encounter a line that starts with "X-DSPAM-CONFIDENCE..." pull
# apart the line to extract the floating-point number on the line. Count
# these lines and then compute the total of the spam confidence values
# from these lines. When you reach the end of the file, print out the
# average spam confidence.

f_name = input("Enter a file name: ")
f_hand = None
try:
    f_hand = open(f_name)
except FileNotFoundError:
    if f_name == "na na boo boo":
        print('NA NA BOO BOO TO YOU TOO, BITCH')
    else:
        print("Please enter a valid file name.")
    quit()

summed = 0
count = 0
for line in f_hand:
    colon_location = 0
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        # print(line.rstrip())
        colon_location = line.find(':')
        summed += float(line[colon_location + 1:])

print('Average spam confidence:', summed / count)
