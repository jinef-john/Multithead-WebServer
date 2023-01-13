## How to run the server
1. Make sure you have Python3 installed on your machine.
2. Open a terminal and navigate to the directory where the python file is located.
3. Run the following command: `python3 Server.py`
4. The server will start running.
## Alternative
1. If you already have python3 installed on your machine, you can run the server by double clicking the python file.
2. The server will start running.
3. Enter the port number you want to use and press enter.
 --> Example `Enter Port Number: 12345`

## How to run the client
1. Make sure you have Python3 installed on your machine.
2. Open a terminal and navigate to the directory where the python file is located.
3. Run the following command: `python3 Client.py`
4. The client will start running.
5. Enter the IP address of the server and press enter.
 --> Example `Enter IP Address: 127.0.0.1` Make sure you use this IP address if you are running the server and client on the same machine. Its called a loopback address. Why? Because the server is running on the same machine as the client.
 --> Example `Enter Port Number: 12345`
 --> Example `Enter File Name: sample.txt`

## Description: 
- The Web Server and Web Client communicate using a text-based protocol called HTTP.
- The server being multi-threaded will be able to handle multiple requests concurrently. 
- The main thread (server), listens to a specified port like the standard port for HTTP (8080).
- Upon receiving a HTTP request, the server sets up a TCP connection to the requesting client and serves the request in a separate thread using a new port. After sending the response back to the client, it closes the connection.
  
- The client requests for a file from the server. 
  1.	If this file exists, the server responds with ‘HTTP/1.1 200 OK’ 
  2.	If the file doesn’t exists, the server responds with ‘HTTP/1.1 404 Not Found’.
- The following information are extracted from the connection objects: 
  1.	RTT for the client request. RTT is the time it takes for a packet to travel from the client to the server and back to the client.
  2.	Relevant details like Host Name of the server, socket family, socket type, protocol, timeout and get peer 
      name are extracted on client side and server side.
      