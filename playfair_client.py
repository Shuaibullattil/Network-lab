import socket

def start_client():
    host = 'localhost'
    port = 60014

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server\n")

    key = input("Enter a key: ")
    client_socket.send(key.encode('utf-8'))

    message = input("Enter a message: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print("\nEncrypted message from server:", response)

    client_socket.close()


if __name__ == "__main__":
    start_client()
