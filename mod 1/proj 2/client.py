import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
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