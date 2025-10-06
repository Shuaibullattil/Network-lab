import socket

def client_program():
    host = '127.0.0.1'
    port = 65434

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive public parameters from server
    params_bytes = client_socket.recv(1024)
    params_str = params_bytes.decode()

    params_list = params_str.split(",")
    p = int(params_list[0])
    g = int(params_list[1])
    B = int(params_list[2])

    print("Received p =", p)
    print("Received g =", g)
    print("Received B =", B)

    # Client's private key
    a = 6
    A = pow(g, a, p)  # Client's public key

    # Send A to server
    client_socket.sendall(str(A).encode())

    # Compute shared secret
    shared_secret = pow(B, a, p)
    print("Shared secret computed by client:", shared_secret)

    # Receive server confirmation
    print(client_socket.recv(1024).decode())

    client_socket.close()

if __name__ == "__main__":
    client_program()
