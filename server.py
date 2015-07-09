#!usr/bin/python3 

import socket;
import time;

host='0.0.0.0'#global host IP address

port=9000 #creating server port to establish a connection

#creating a socket using socket library
connectionsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #af_inet- tcp/ip connection
#socket_stream= buffer size of the socket connection 

#setting up socketoptions  SO_REUSEADDR reusablity of socket
#connectionsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#binding the socket,host is a global socket and it is directed to port number 8080
connectionsocket.bind((host,9000))

#server is listening for requests and waiting for connection
connectionsocket.listen(1)

#print("server is waiting for request")
(csock,caddr ) =connectionsocket.accept() #accept the request from client and get teh client address and request
print("request received and connection established")	

while 1:
	
		try:
			(csock,caddr ) =connectionsocket.accept() #accept the request from client and get teh client address and request
			#print "hi"
			data=csock.recv(1024) #recv helps to received the request header
		except Exception:
			csock.close()
			continue
		
		#csock.send(data)
		address=data.split(" ")[1] #spliting request to get pathname of the file
		address.replace("/","",1)
		pathfilename="WWW/"+address
		try:
			file=open(pathfilename,"r")
			text=file.read()#reading the data from the text file
			#csock.send(text)#sending the content to the destination
			buffer_data=text
			content_size=len(text)
			file.close()
			localtime = time.asctime( time.localtime(time.time()) )
			
			#response message
			csock.send("HTTP/1.0 200 OK \n\r")
			csock.send("Date:%s \n\r"%(localtime))
			csock.send("Connection:close \n\r") 
			csock.send("Server: Apache/1.3.27 \n\r")
			csock.send("Content-Type: text/html \n\r")
			csock.send("Content:length:%d \n\r\n\r"%(content_size))
			csock.send("%s \n"%(buffer_data))
			csock.close()
		except IOError:
			print("server not found")
			csock.send("\n 404 ERROR:File not Found")
			csock.close()
		except Exception:
			csock.close()
			connectionsocket.close()
			exit()	