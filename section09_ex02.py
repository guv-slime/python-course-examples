# Exercise 2: This program counts the distribution of the hour of the
# day for each of the messages. You can pull the hour from
# the “From” line by finding the time string and then splitting
# that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out
# the counts, one per line, sorted by hour as shown below.

file_name = 'mbox-short.txt'
handle = open(file_name)

email_dic = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) < 3:
            continue
        else:
            email_dic[words[5][:2]] = email_dic.get(words[5][:2], 0) + 1

for k, v in sorted(email_dic.items()):
    print(k, v)
