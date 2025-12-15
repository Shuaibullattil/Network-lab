import socket

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

message = "how are you"
key = "beware"

start = client_socket.recv(1024).decode()
print(start)
client_socket.send(message.encode())
client_socket.send(key.encode())

ciphertext =  client_socket.recv(1024).decode()
print(f"cipcher text : {ciphertext}")

client_socket.close()