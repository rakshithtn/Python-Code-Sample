#!/usr/bin/python

from socket import *
#import smtplib

message='\r\nFrom: <raksha.tn@gmail.com>\r\nTo: <rtn221@nyu.edu>\r\nSubject: HELLOHIBYE\r\n'

mailServer='localhost'
serverPort=25

connectionSocket=socket(AF_INET,SOCK_STREAM)
connectionSocket.connect((mailServer,serverPort))

getMessage=connectionSocket.recv(1024)
print getMessage


if getMessage[:3] != '220':
	print  '220 reply not received from server'

helocmd='HELO Raks\r\n'
connectionSocket.send(helocmd)

getMessage1=connectionSocket.recv(1024)
print getMessage1

if getMessage1[:3] != '250':
	print '250 response not received from server'

fromCmd='MAIL FROM: <raksha.tn@gmail.com>\r\n'
connectionSocket.send(fromCmd)

getMessage=connectionSocket.recv(1024)
print getMessage

toCmd='RCPT TO: <rtn221@nyu.edu>\r\n'
connectionSocket.send(toCmd)

getMessage=connectionSocket.recv(1024)
print getMessage

connectionSocket.send('DATA\r\n')

connectionSocket.send(message)

connectionSocket.send('.\r\n')

getMessage=connectionSocket.recv(1024)
print getMessage

connectionSocket.send(str.encode('QUIT\r\n'))

getMessage=connectionSocket.recv(1024)

print getMessage
connectionSocket.close()
