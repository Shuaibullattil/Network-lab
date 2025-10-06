# LZW CLIENT
import socket

# Function to perform LZW Compression
def lzw_compress(input_string):
    # Initialize dictionary with ASCII characters
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    w = ""
    compressed = ""

    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed += str(dictionary[w]) + "#"
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        compressed += str(dictionary[w]) + "#"

    return compressed[:-1]  # Remove last extra '#'


# Function to start client
def client_program():
    host = '127.0.0.1'  # Localhost
    port = 65433        # Must match server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            data = input("\nEnter plain text to compress: ")
            if not data:
                break

            encrypted = lzw_compress(data)
            print("Compressed string:", encrypted)

            # Send compressed data to server
            client_socket.sendall(encrypted.encode())

    finally:
        client_socket.close()


if __name__ == '__main__':
    client_program()
