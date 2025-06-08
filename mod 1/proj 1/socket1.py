import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # this might give us an error if the link is not correct
# we can set up a try catch aswell if needed.

# this is the actual get request that we will be sending.
# the encode will convert unicode into utf-8 format.
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# continuously read data from server and display it.
while True:
    data = mysock.recv(512)
    # break the loop if no data is available anymore
    if len(data) < 1:
        break
    # display the data after converting utf-8 to unicode
    print(data.decode(), end='')

# close the connection
mysock.close()