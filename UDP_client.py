import socket

SERVER_IP = '127.0.0.1'
PORT = 8080

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send message to server (using .encode())
message = "Hello from client"
client_socket.sendto(message.encode(), (SERVER_IP, PORT))

# Receive response from server
data, _ = client_socket.recvfrom(1024)
print(f"Server: {data.decode()}")  # Decoding bytes to string

client_socket.close()
