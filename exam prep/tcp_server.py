import socket

HOST = "127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))

server_socket.listen(1)
print("server is listenig........")

conn,addr = server_socket.accept()

print(f"connected by:{addr}")
data = conn.recv(1024).decode()
print(f"data:{data}")

conn.send("your data is recived".encode())

conn.close()
server_socket.close()
