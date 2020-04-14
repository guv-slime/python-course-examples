# Exercise 1: Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

polar_bear = 'polar bear'
index = len(polar_bear)

while index > 0:
    print(polar_bear[index-1])
    index -= 1


# Exercise 3: Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

def count(yo_string, yo_letter):
    word = yo_string
    counter = 0
    for letter in word:
        if letter == yo_letter:
            counter += 1
    print(counter)


count('polar bear', 'a')


# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character  and then use the float function to convert the extracted
# string into a floating point number.

sample = 'X-DSPAM-Confidence:0.8475'
colon = sample.find(':')
answer = float(sample[colon + 1:])
print(answer)
