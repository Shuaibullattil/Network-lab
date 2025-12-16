import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = "127.0.0.1"
PORT = 8080
server_socket.bind((HOST,PORT))

data,client_addr = server_socket.recvfrom(1024)

print(f"data is recieved {data.decode()}")

server_socket.sendto("hi this is from UDP server".encode(),client_addr)
server_socket.close()



