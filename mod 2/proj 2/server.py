from socket import *
def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # as the socket is bound to a port, we need to make sure that the port is not already in use.
    serverSocket.bind(('', 9000))
    serverSocket.listen(5)  # Allow up to 5 connections # QUEUED
    print("Server is ready to receive")
    try:
        while True:
            # accept a connection from a client
            clientsocket, address = serverSocket.accept()
            print(f"Connection established with {address}")

            # receive the message from the client
            # we can set a timeout for the connection if needed.
            message = clientsocket.recv(5000).decode()
            pieces = message.split('\n')
            if len(pieces) > 0:
                # print the first line of the message
                print(f"Received message: \n{pieces[0]}")

            # send a response back to the client
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += f"<html><body><h1>Hello world</h1></body></html>"
            clientsocket.sendall(data.encode())

            clientsocket.close()  # Close the connection gracefully
    except KeyboardInterrupt:
        print("Server is shutting down")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        serverSocket.close()


    serverSocket.close()

createServer()