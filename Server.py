import socket
import threading
import sys

BUFFER_SIZE = 1024                                             # We define buffer size as 1024 bytes because we are sending the file in chunks of 1024 bytes
TCP_IP = "localhost"                                           # ip address of the server
TCP_PORT = int(input("Enter Server's Port Number: "))                    # port number of the server

# This class is used to handle the incoming connections from the clients
# It does the following:'
# 1. Accepts the connection from the client
# 2. Receives the filename from the client
# 3. Sends the file to the client
class Thread(threading.Thread):
    # This function is called when the thread is started
    def __init__(self, ip, port, sock):
        threading.Thread.__init__(self)
        self.ip = ip # ip address of the client
        self.port = port # port number of the client
        self.sock = sock # socket object of the client
        print("Client IP address : " + ip + " Port Number:" + str(port)) # print ip and port of the server

    def run(self): # This function is called when the thread is started
        try: # try block to handle exceptions
            request = self.sock.recv(BUFFER_SIZE) # receive the filename from the client
            print(request) # print the filename
            filename = request.split()[1] # extract the filename from the request. The filename is present in the request after the first space, thats why i am using [1]]                      
            print("Requested file is:", filename[1:]) # print the filename
            file = open(filename[1:])                           # open the file
            data = file.read()                                  # read the file
            file.close()                                        # close the file
            print("Content of the file:", data)                # print the content of the file
            self.sock.send(b'HTTP/1.1 200 OK')                  # send the response to the client
            self.sock.send(data.encode())                       # send the content of the file to the client
            print('Success! File sent to the client')
            self.sock.close()                                   # close the socket
        except IOError: # if the file is not found
            self.sock.send(b'HTTP/1.1 404 Not Found')       # send the response to the client          
            print("Sorry, Requested file not found")        # print the message
            self.sock.close()                                   # close the socket


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create a socket object  
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # set the socket options
threads = [];                                                   # create an empty list to store the threads

try:                                                        # try block to handle exceptions
    tcpsock.bind((TCP_IP, TCP_PORT))                            # bind the socket to the ip address and port number
    print('Server bind is Complete')

except socket.error as msg:                                # if the socket is not created
    print(msg)  												    # print the error message
    sys.exit()                                                # exit the program

tcpsock.listen(10)                                                  # listen for incoming connections
print('Server is ready to accept connections')                    # print the message

while True:                                                    # while loop to accept multiple connections
    connection, address = tcpsock.accept()                          # accept the connection
    print("\nClient is connected with Ip Address:" + address[0] + " Port Number:" + str(address[1])) # print the ip address and port number of the client
    print(connection)
    print("Host name: " + str(connection.getpeername())) # print the host name()
    print('Socket Family: ' + str(connection.family))   # print the socket family(2 for IPv4)
    print('Socket Type: ' + str(connection.type))      # print the socket type(1 for TCP)
    print('Time out: ' + str(connection.timeout))     # print the timeout
    print('Socket Protocol: ' + str(connection.proto)) # print the socket protocol(6 for TCP)
    conn = Thread(address[0], address[1], connection) # create a thread object
    conn.start()                                    # start the thread
    threads.append(conn)                                        # Append new connection
