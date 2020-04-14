# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# (i.e., the whole email address). At the end of the program, print out
# the contents of your dictionary
# SUCCESS

file_name = 'mbox-short.txt'
handle = open(file_name)

email_dic = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) < 3:
            continue
        else:
            at = words[1].find('@')  # finds @ position
            domain = words[1][at+1:]  # @ pos + 1 : thru end of string
            email_dic[domain] = email_dic.get(domain, 0) + 1
print(email_dic)
