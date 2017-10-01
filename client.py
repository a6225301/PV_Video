
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


