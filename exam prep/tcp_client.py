import socket

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

client_socket.send("hi how are you".encode())

data = client_socket.recv(1024).decode()
print(data)

client_socket.close()
