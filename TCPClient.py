
from socket import *
serverName = 'localhost'
serverPort=8080
clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket((serverName,serverPort))
sentence=raw_input('Enter lowercase')
clientSocket.send(sentence)
modifiedSentence=clientSocket.recv(1024)
print modifiedSentence
clientSocket.close()

