#Rakshith Tumkur Nagabhushana
#N17419862
#Web Server
#10/5/2014


#!/usr/bin/python

from socket import *
import time

serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',7656))

serverSocket.listen(1)


while 1:
	print 'ready to serve...'
	connectionSocket, addr=serverSocket.accept()

	try:

		getMessage=connectionSocket.recv(1024)

		filename=getMessage.split() [1]

		f=open(filename[1:])
		fileData=f.read()
		f.close()
		dataSize=len(fileData)

		timeOfServe=time.asctime(time.localtime(time.time()))

		
		connectionSocket.send('\nHTTP/1.1 200 OK\n')
		connectionSocket.send('Date:%s \n'%(timeOfServe))
		connectionSocket.send("Connection:Close\n")
		connectionSocket.send("Server: Apache 1.3.27\n")
		connectionSocket.send("Content-Type: text/html\n")
		connectionSocket.send('Content-Length: %d\n\r'%(dataSize))


		for i in range(0,len(fileData)):
			connectionSocket.send(fileData[i])

		connectionSocket.close()

	except IOError:
		connectionSocket.send('\n404 ERROR: File Not Found\n')
		connectionSocket.close()

serverSocket.close()
