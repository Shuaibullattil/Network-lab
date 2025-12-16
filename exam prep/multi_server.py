import socket
import threading

clients = []

def broadcast(msg,sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(msg.encode())
            except:
                client.close()
                clients.remove(client)
            

def handle_client(client_socket,addr):
    print(f"[CONECTED];{addr}")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            broadcast(msg,client_socket)
        except:
            break
    client_socket.close()
    clients.remove(client_socket)
    print(f"[DISCONNECTED {addr}")


HOST ="127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()
print(f"server is listening..... on {PORT}:{HOST}")

while True:
    client_socket,addr = server_socket.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client,args=(client_socket,addr)).start()
    print(f"ACTIVE CONNECTIONS {threading.active_count()-1}")