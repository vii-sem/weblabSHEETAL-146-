#!/usr/bin/python # This is server.py file
import socket # Import socket module
serversocket =socket.socket()# Create a socket object
host=socket.gethostname()# Get local machine name
port=12345# Reserve a port for your service.
serversocket.bind((host, port))# Bind to the port
serversocket.listen(5)# Now wait for client connection.
while True:
    
    clientsocket,addr=serversocket.accept()# Establish connection with client.
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()