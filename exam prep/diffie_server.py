import socket


p=25
g=13
b=5

HOST  = "127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(1)
print("server is listening......")

B = pow(g,b,p)
data = f"{p}+{g}+{B}"

conn,addr = server_socket.accept()

conn.send(data.encode())
rec = conn.recv(1024).decode()
print(f"message from client A: {rec}")
A = int(rec)
shared_secret = pow(A,b,p)
print(f"Shared Secret: {shared_secret}")
conn.close()
server_socket.close()
