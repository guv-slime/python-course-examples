# Exercise 1: Revise a previous program as follows:
# Read and parse the "From" lines and pull out the
# addresses from the line.
# COMPLETED

# Count the number of messages from each person
# using a dictionary.
# COMPLETED

# After all the data has been read, create a list
# of (count, email) tuples from the dictionary.
# COMPLETED

# Then sort the list in reverse order and print out the
# person who has the most commits.
# COMPLETED

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
# print(email_dic)

# print(sorted([(v, k) for k, v in email_dic.items()], reverse=True))
# ^ Most elegant way to sort this without creating new variable = below
# but doesn't print as nicely, but could be stored in a variable all
# the same

val_first = []  # could also be set to equal list()
for k, v in email_dic.items():
    val_first.append((v, k))
# print(val_first)

reversal = sorted(val_first, reverse=True)

for v, k in reversal[:1]:
    print(k, v)
