# Exercise 2: Change your socket program so that it counts the number of characters it has
# received and stops displaying any text after it has shown 3000 characters. The program
# should retrieve the entire document and count the total number of characters and display
# the count of the number of characters at the end of the document.

# I hate this section gonna move on and revisit another time

# http://data.pr4e.org/romeo-full.txt

# Pulled out Tasks:
# 01) Count total number of characters it has received
# 02) stop displaying text after 3000 chars
# 03) display the count at end of document# exercise 02

import socket

# Create Socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# URL Input / URL Split
urlin = input('Enter a URL: ')
newurl = urlin.split('/')

try:
    # Extract Host Name & Concat GET CMD
    hostname = newurl[2]
    hostget = 'GET ' + urlin + ' HTTP/1.0\r\n\r\n'

    # Connect Socket
    mysock.connect((hostname, 80))
    cmd = hostget.encode()
    mysock.send(cmd)

    # Counters
    countChars = 0

    while True:
        data = mysock.recv(512)
        countChars += len(data)
        if len(data) < 1 or countChars >= 3000:
            break
        print(data.decode(), end='')
    print(countChars)

    mysock.close()
except (socket.gaierror, IndexError):
    print('please enter a valid url')
