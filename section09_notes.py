'''
Key Methods / Ideas for this section:
- using a dictionary with the '.items()'
    .items() returns a list of tuple pairs
- creating a temporary list to hold tuple pairs (using .items())
- sorting the list with '.sorted()'
    - .sorted(iterable, key=None, reverse=False)
    - iterable = what is being searched through
    - key(OPTIONAL) = function that serves as a key for the sort
      comparison. Defaults to None. (can pass it a function)
    - reverse(OPTIONAL) = If True, the sorted list is reversed (or
      sorted in descending order). Defaults to false if not provided
- sorting list by value first instead of key first
'''
# sorted function
# d = {'a': 10, 'c': 1, 'b': 22}
# print(d.items(), '\n')
# print(sorted(d.items()))  # sorts d by key in alpha order

# sorted function loop
# d = {'a': 10, 'b': 1, 'c': 22}
# for k, v in sorted(d.items()):
#     print(k, v)

# sort by values instead of key

c = {'a': 10, 'b': 1, 'c': 22}
tmp = []
for k, v in c.items():  # traceback occurs if you don't use .items() on a dictionary
    tmp.append((v, k))
print('Key Switch:', tmp)
tmp = sorted(tmp)  # for smallest to largest
print('Small Val- default sorted:', tmp)
tmp = sorted(tmp, reverse=True)  # for largest to smallest
print('Descending Val Sorted:', tmp)
