import socket

HOST = "127.0.0.1"
PORT = 8080
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))
server_socket.listen(1)
print("server is listening .......")

conn,addr = server_socket.accept()
print("connected by",addr)

data = conn.recv(1024).decode()
print("recieved data from client is ",data)

conn.send("hello from server".encode())

conn.close()
server_socket.close()


