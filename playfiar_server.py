import socket

# Function to find the position of a letter in the 5x5 matrix
def search(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j
    return None, None


# Function to prepare the message (convert to pairs)
def preprocess_playfair(message):
    message = message.lower()
    message = message.replace(" ", "")
    message = message.replace("j", "i")

    pairs = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i + 1]
            if a == b:
                pairs.append(a + 'x')
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + 'x')
            i += 1
    return ''.join(pairs), pairs


# Function to create the 5x5 Playfair matrix
def create_matrix(key):
    alphabets = "abcdefghiklmnopqrstuvwxyz"  # j is merged with i
    key = key.lower()
    key_letters = []

    # Add unique letters from the key
    for ch in key:
        if ch == 'j':
            ch = 'i'
        if ch not in key_letters and ch in alphabets:
            key_letters.append(ch)

    # Add remaining alphabets not in the key
    for ch in alphabets:
        if ch not in key_letters:
            key_letters.append(ch)

    # Create 5x5 matrix
    matrix = []
    index = 0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(key_letters[index])
            index += 1
        matrix.append(row)

    return matrix


# Function to perform encryption
def encrypt(key, message):
    plain_text, digraphs = preprocess_playfair(message)
    matrix = create_matrix(key)

    print("\nPlain text:", plain_text)
    print("Digraphs:", digraphs)
    print("Matrix:")
    for row in matrix:
        print(row)

    ciphertext = ""

    for pair in digraphs:
        a = pair[0]
        b = pair[1]
        r1, c1 = search(matrix, a)
        r2, c2 = search(matrix, b)

        if r1 == r2:  # Same row
            ciphertext += matrix[r1][(c1 + 1) % 5]
            ciphertext += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  # Same column
            ciphertext += matrix[(r1 + 1) % 5][c1]
            ciphertext += matrix[(r2 + 1) % 5][c2]
        else:  # Rectangle case
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]

    print("Cipher text:", ciphertext)
    return ciphertext


# Start TCP Server
def start_server():
    host = 'localhost'
    port = 60014

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"\nConnection from {addr}")

        key = client_socket.recv(1024).decode('utf-8')
        message = client_socket.recv(1024).decode('utf-8')

        print(f"Received key: {key}")
        print(f"Received message: {message}")

        ciphertext = encrypt(key, message)

        client_socket.send(ciphertext.encode('utf-8'))
        client_socket.close()
        print("Client disconnected.\n")


if __name__ == "__main__":
    start_server()
