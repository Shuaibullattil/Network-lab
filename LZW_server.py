# LZW SERVER
import socket

# Function to perform LZW Decompression
def lzw_decompress(compressed):
    # Split the received compressed data into integer codes
    compressed = [int(x) for x in compressed.split("#")]

    # Initialize dictionary with ASCII characters
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256

    w = chr(compressed[0])
    decompressed = [w]

    # Loop through the rest of the compressed data
    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError(f'Bad compressed k: {k}')

        decompressed.append(entry)

        # Add new sequence to dictionary
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry

    return ''.join(decompressed)


# Function to start server
def server_program():
    host = '127.0.0.1'  # Localhost
    port = 65433        # Port number

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    try:
        while True:
            # Receive data from client
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"\nReceived Compressed Data: {data}")
            answer = lzw_decompress(data)
            print("Decompressed plain text:", answer)

    finally:
        conn.close()


if __name__ == '__main__':
    server_program()
