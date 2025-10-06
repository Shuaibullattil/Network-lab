import socket

HOST = '127.0.0.1'
PORT = 8080

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP Server is running on {HOST}:{PORT}")

# Receive data from client
data, client_addr = server_socket.recvfrom(1024)
print(f"Client: {data.decode()}")  # Decoding bytes to string

# Send reply to client (using .encode())
server_socket.sendto("Hello from server".encode(), client_addr)

server_socket.close()
