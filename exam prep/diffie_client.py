import socket

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

msg = client_socket.recv(1024).decode()
data = msg.split("+")
p = int(data[0])
g = int(data[1])
B = int(data[2])

print(f"p:{p} g:{g} B:{B}")

a= 6
A = pow(g,a,p)
print(f"A:{A}")
client_socket.send(str(A).encode())
shared_secret = pow(B,a,p)
print(f"shared secret: {shared_secret}")

client_socket.close()
