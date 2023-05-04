import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 1025

# connect to the server
client_socket.connect(('', port))

# send message "Hello" to server
message = 'Hello'
client_socket.send(message.encode())

# receive message "Hello, What's your name?" from server
response = client_socket.recv(1024).decode()
print('Received message:', response)

# receive name from terminal and send it to server
name = input('Enter your name: ')
client_socket.send(name.encode())

# receive message "Hello name, Welcome to SIT202" from server
response = client_socket.recv(1024).decode()
print('Received message:', response)

# close the connection
client_socket.close()
