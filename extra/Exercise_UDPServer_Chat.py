from socket import *
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to port 12000
serverPort = 12000
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    # Receive a message from the socket
    # The sender address is attached with the message
    message, clientAddress = serverSocket.recvfrom(2048)
    clientIP, clientPort = clientAddress
    print(f'message from {clientIP}:{clientPort} = {message.decode()}')
    replyMessage = input('Type a message to reply:')
    # Send a message through the socket
    # The destination address is provided
    serverSocket.sendto(replyMessage.encode(), clientAddress)



