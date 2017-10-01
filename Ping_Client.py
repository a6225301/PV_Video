import socket               # Import socket module
import os
import time

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# print (host)

host=''
port = 11098
s.connect((host, port))
print s.recv(1024)
s.close     
print ('scuccess')