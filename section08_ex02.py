# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with "From", then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order doesn't matter)

# Sample Line:
# From stephen.marquard@ac.za Sat Jan 5 09:14:16 2008

# Sample Execution:
# pytho dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

file_name = 'mbox-short.txt'
handle = open(file_name)

day_dic = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) < 3:
            continue
        else:
            # print(words[2])
            day_dic[words[2]] = day_dic.get(words[2], 0) + 1

print(file_name, day_dic)
