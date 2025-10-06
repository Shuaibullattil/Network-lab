import socket

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    num = input("enter your number")
    client_socket.send(num.encode())
    data = client_socket.recv(1024).decode()
    print(data)

    if num == "exit":
        break
client_socket.close()