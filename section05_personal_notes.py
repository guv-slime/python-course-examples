
# While loops are indefinite loops
# they're called indefinite loops because they keep going until
# a logical condition becomes FALSE
is_fat = True
mileage = 0
while is_fat:
    print('run a mile')
    mileage += 1
    if mileage > 100:
        is_fat = False
    elif mileage >= 90:
        print("final stretch -- continue", mileage)
        continue
    else:
        print('keep running!')

print('\nYou slim mudda fukka ;)')

# For Loops are definite loops
# loops through some set of things (runs a finite number of times)

largest_so_far = -1
for num in [3, 41, 12, 74, 5]:
    if largest_so_far < num:
        largest_so_far = num

print(largest_so_far)

# None Type
# Smallest so far loop example:

smallest = None
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

# only use "is" or "is not" on booleans and None
