# gff206 python program for Web Server Assignment 2-19-22.

# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(4)
    #print('The server is ready to receive')
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr =  serverSocket.accept()# Fill in start      #Fill in end
        try:

            try:
                message = connectionSocket.recv(4096) # Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read() # Fill in start     #Fill in end

                # Send one HTTP header line into socket.
                # Fill in start
                connectionSocket.send('HTTP/1.1 200 OK \r\n'.encode())
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
        # Send response message for file not found (404)
        # Fill in start
                connectionSocket.send("HTTP/1.1 200 OK \r\n 404 Not Found Try Again, lol!".encode())
        # Fill in end

        # Close client socket
        # Fill in start
            connectionSocket.close()
        # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            Pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
