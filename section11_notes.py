# Networked Programs: Section 12.1
# Socket is much like a file, except that a single socket
# provides a two-way connection between two programs.
# You can:
#     -read from and write to the same socket
#     - if you write something to a socket, it is sent to the app at the other end of the socket
#     - if you read from the socket, you are given the data which the other app has sent
#     - if you try to read a socket when the program has not sent any data, you just sit and wait
#     - if the programs on both sides try to read a socket, but neither has sent any data, both wait a long time
#           - this is why it's important to have some sort of protocol

# Protocol - a precise set of rules that determine the following:
#    - who goes first
#    - what they are to do
#    - and then what the responses are to that message
#    - and who sends next
#    - and so on

# To request a document from a web server, we make a connection to the www.pr4e.org server on port 80,
# and then send a line of the form
#     GET http://data.pr4e.org/romeo.txt HTTP/1.0
# where the second parameter is the web page we are requesting, and then we also send a blank line.
# The web server will respond with some header info about the document a blank line followed by
# the document content.

# 12.2 The worlds Simplest web browser
# Below is a program that makes a connection to a web server and follows
# the rules of http protocol to request a document and display what the
# server sends back.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # not sure what this do
mysock.connect(('data.pr4e.org', 80))  # makes connection to port 80 on py4e server
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
# protocol requires us to send the GET command followed by a blank line
# \r\n signifies an EOL (end of line), so \r\n\r\n signifies nothing between
# the two EOL sequences. That is the equivalent of a blank line...

# once the command and blank line have been received this loop will run:
while True:
    data = mysock.recv(512)  # receives data in 512-char chunks from socket
    if len(data) < 1:  # will stop printing data if there is no more data to read
        break
    print(data.decode(), end='')  # prints data while there is still data

mysock.close()

# And that is the world's simplest web browser!
# this example showed us how to make a low-level network connection with sockets.
# sockets can be used to communicate with web server or with a mail server or
# many other kinds of servers.
# 

# your program:            www.py4e.com
# SOCKET:
#     socket                 Web Pages
#     connect  ==Port 80 ==     .
#     send                      .
#     receive                   .
