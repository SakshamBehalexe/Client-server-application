import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
#using portnumber > 1024 as portnumbers< 1024 are reserved for system services
#hence to avoid conflicts i have used portnumber > 1024
port = 1025

# bind the socket object to a specific address and port
server_socket.bind(('', port))

# set the server to listen for incoming connections
server_socket.listen(1)

# wait for a client to connect
print('Waiting for client connection...')
client_socket, client_address = server_socket.accept()
print('Client connected:', client_address)

# receive message "Hello" from client
message = client_socket.recv(1024).decode()
print('Received message:', message)

# send message "Hello, What's your name?" to client
response = 'Hello, What\'s your name?'
client_socket.send(response.encode())

# receive client name from terminal
name = client_socket.recv(1024).decode()
print('Received message:', name)

# send message "Hello name, Welcome to SIT202" to client
response = f'Hello {name}, Welcome to SIT202'
client_socket.send(response.encode())

# close the connection
client_socket.close()
server_socket.close()
