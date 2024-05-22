from socket import *
# Create a UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Type a message to send or "exit" to quit:')

while message != "exit":
     # Send a message through the client socket
     # The destination is specified by a tuple of IP and port
     serverName = '127.0.0.1'
     serverPort = 12000
     clientSocket.sendto(message.encode(),(serverName, serverPort))
     # Receive a message from the client socket
     # The sender information is attached with the message
     replyMessage, serverAddress = clientSocket.recvfrom(2048)
     print(replyMessage.decode())
     message = input('Type a message to send or "exit" to quit:')

clientSocket.close()



