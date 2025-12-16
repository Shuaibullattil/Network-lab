import socket


HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client_socket.sendto("hi i am new client".encode(),(HOST,PORT))
data, _ = client_socket.recvfrom(1024)

print(f"{data.decode()}")


client_socket.close