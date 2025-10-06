# server.py
import socket
import sys

# Function to calculate parity for a given position
def calc_parity(data, pos):
    parity = 0
    for i in range(1, len(data)):
        if i & pos == pos:
            parity ^= data[i]
    return parity

# Function to detect error position
def detect_error(code):
    error_pos = 0
    pos = 1
    while pos < len(code):
        if calc_parity(code, pos) != code[pos]:
            error_pos += pos
        pos *= 2
    return error_pos

# Server program
def main():
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        return

    port = int(sys.argv[1])
    host = '127.0.0.1'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    print("Received Hamming Code:", data)

    code = [0] + [int(b) for b in data]  # 1-based indexing

    error_pos = detect_error(code)

    if error_pos == 0:
        response = "No errors detected"
    else:
        response = f"Error detected at position {error_pos}"

    conn.sendall(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
