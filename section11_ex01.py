# exercise 01
import socket

# Create Socket ( Step 1 )
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# URL Input / URL Split
urlin = input('Enter a URL: ')
newurl = urlin.split('/')

try:
    # Extract Host Name & Concat GET CMD
    hostname = newurl[2]
    hostget = 'GET ' + urlin + ' HTTP/1.0\r\n\r\n'

    # Connect Socket ( Step 2 )
    mysock.connect((hostname, 80))
    cmd = hostget.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()
except (socket.gaierror, IndexError):
    print('please enter a valid url')

