# checking to see if key exists
# counts = dict()
# names = ['Zelda', 'Louie', 'Emory', 'Julie', 'Zelda']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] += 1
# print(counts)

# get method
# counts = dict()
# names = ['Julie', 'Emory', 'Zelda', 'Louie', 'Zelda']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# the in operator tells you if a key appears in the dictionary

# [searchKey] in [dictionary]

# 'one' in eng2sp
# returns true
# 'uno' in eng2sp
# returns false

# to see whether something appears as a value in a dictionary, you can
# use the method .values() as a type that can be converted to a list, and
# then use the in operator

# vals = list(eng2sp.values())
# 'uno' in vals
# returns true


# counts = dict()
# print('Enter a line of text')
# line = input('')
#
# words = line.split()
#
# print('Words:', words)
#
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1  # get is having an issue...
# print('Counts', counts)

# exercise 1: my solution

# webster = dict()
# fhand = open('words.txt')
# words = fhand.read().split()
#
# for word in words:
#     webster[word] = webster.get(word, 0) + 1
# print(webster)
#
# search = 'the'
# print(webster[search])

# Exercise 1: Proper solution (without using read())

name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # ^ same as:
        # if word in words:
        #     counts[word] = counts[word] + 1or word in line:
        print(word)
        # else:
        #    counts[word] = 1

bigcount = None  # or largest could be equal to -1 instead of none
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
# ^ same as ---------------------------------^
# for k, v in dictionary.items()
#     if v > largest:
#         largest = v
#         theword = k  # capture/remember the key that was largest

print(bigword, bigcount)
