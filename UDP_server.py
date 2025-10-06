import socket

# Define IP and Port
HOST = '127.0.0.1'
PORT = 8080

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP Server is running on {HOST}:{PORT}")

# Receive data from client
data, client_addr = server_socket.recvfrom(1024)
print(f"Client: {data.decode()}")

# Send reply to client
server_socket.sendto(b"Hello from server", client_addr)

server_socket.close()
