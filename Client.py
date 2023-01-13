
import socket
import time

TCP_IP = input("Enter Server Address : ")      # Enter Host IP Address(this is the IP address of the server)
TCP_PORT = int(input("Enter Server Port Number : "))   # Enter Port Number
BUFFER_SIZE = 1024  # Normally 512, but we want fast response so we need 1024 bytes

tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Create a TCP/IP socket
tcpsoc.connect((TCP_IP, TCP_PORT))                        # Connect to the server
                                             
print("Connected to the Server")                          # Print the message when connected to the server

file = input("Enter The File You Want : ")             # Enter the filename to be sent to the server
print("\nHostname : ", socket.gethostname())          # Print the hostname of the client
print("Port Number : ", TCP_PORT)                    # Print the port number of the client
print("The Server IP Address : ", TCP_IP)        # Print the IP address of the server
print("Your File is : ", file)                  # Print the filename
print("Peer name : "+str(tcpsoc.getpeername())) # Print the peer name of the client

tcpsoc.send(b'Sending..... /'+file.encode())                 # Send the filename to the server
Start = time.time()                                            # Store the time at which the request was made
while True:                                                    # While loop handles the incoming file from the Server
    data = tcpsoc.recv(BUFFER_SIZE)                            # Receive the file from the server
    #if not data: break                                         # If the file is not received, break the loop                         # Read the contents of the file
    if not data:                                            # If no content is present in the file
        break                                                  # Break the loop
    print(data)
End = time.time()                                              # Store the time at which the file was received
rtt = End - Start                                              # Calculate the Round Trip Time (RTT)

print("\nRound Trip Time (RTT) : "+str(rtt) + " Seconds ")  # Print the RTT
print('Socket Family : '+str(tcpsoc.family)) # Print the socket family
print('Socket Protocol : '+str(tcpsoc.proto))   # Print the socket protocol
print('Socket Type : '+str(tcpsoc.type))    # Print the socket type
print('Time out : '+str(tcpsoc.timeout))    # Print the socket timeout
tcpsoc.close()                                                  # Close the Client Socket
print('\nThe Connection is closed')
