# Exercise 4: Expanding on exercise 3, add code to figure out who
# has the most emails in the file. After all the data has been read
# and the dictionary has been created, look through the dictionary using
# a maximum loop (see chapter 5: Maximum and Minimum loops) to find out
# who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# PASSED

# Enter a file name: mbox.txt
# zqian@umich.edu 195
# PASSED

# file_name = 'mbox-short.txt'
file_name = 'mbox.txt'
handle = open(file_name)

email_dic = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) < 3:
            continue
        else:
            email_dic[words[1]] = email_dic.get(words[1], 0) + 1

most_mail = None
for email in email_dic:
    if most_mail is None or email_dic[most_mail] < email_dic[email]:
        # print('DA MOST AT DA MOMENT =', email, email_dic[email])
        most_mail = email
print(most_mail, email_dic[most_mail])
