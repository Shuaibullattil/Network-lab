import socket

# Public parameters
p = 23
g = 5

def server_program():
    host = '127.0.0.1'
    port = 65434

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connected to: {addr}")

    # Server's private key
    b = 15
    B = pow(g, b, p)  # Server's public key

    # Send public parameters p, g, B
    message = str(p) + "," + str(g) + "," + str(B)
    conn.sendall(message.encode())

    # Receive client's public key A
    A_bytes = conn.recv(1024)
    A_str = A_bytes.decode()
    A = int(A_str)
    print("Received client's public key:", A)

    # Compute shared secret
    shared_secret = pow(A, b, p)
    print("Shared secret computed by server:", shared_secret)

    conn.sendall(("Shared secret: " + str(shared_secret)).encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    server_program()
