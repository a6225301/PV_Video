
import socket               # Import socket module
import os
import time


def ping_server(hostname):
	response = os.system("ping " + hostname)
	if response == 0:
	  	print hostname, 'is up!'
	else:
		print hostname, 'is down!'
	return response

hostname_list= ["" ,'']

def check_server(hostname_list):
	for hostname in hostname_list:
		(ip,port)=hostname.split(':')
		print (ip,port)
		if ping_server(ip)==1:
			print ('restart server...')
	  		os.system('start mstsc /v:'+hostname+'')



while True:
	check_server(hostname_list)
	time.sleep(60)
	pass





# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
# # print (host)

# host='218.3.235.102'
# port=11098
# s.connect((host, port))
# print s.recv(1024)
# s.close     