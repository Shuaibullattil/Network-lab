import socket
import threading

def recieve_msg(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            print(msg)
        except:
            break

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

threading.Thread(target=recieve_msg,args=(client_socket,)).start()

while True:
    msg = input()
    if msg.lower() == 'exit':
        break
    client_socket.send(msg.encode())
client_socket.close()