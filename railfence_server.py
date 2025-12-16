import socket

# Function to decrypt Rail Fence cipher
def decrypt_rail_fence(cipher_text, key):
    n = len(cipher_text)

    # Step 1: Create an empty matrix
    rail = []
    for i in range(key):
        row = ['\n'] * n
        rail.append(row)

    # Step 2: Mark the zigzag pattern with '*'
    direction_down = False
    row, col = 0, 0

    for i in range(n):
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Step 3: Fill cipher text in zigzag pattern
    index = 0
    for i in range(key):
        for j in range(n):
            if rail[i][j] == '*' and index < n:
                rail[i][j] = cipher_text[index]
                index += 1

    # Step 4: Read matrix in zigzag to get plain text
    result = []
    direction_down = False
    row, col = 0, 0

    for i in range(n):
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        if rail[row][col] != '\n':
            result.append(rail[row][col])

        if i < n - 1:
            col += 1
            if direction_down:
                row += 1
            else:
                row -= 1

    return "".join(result)


def start_server():
    host = '127.0.0.1'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"\nReceived Encrypted Data: {data}")
        key = int(input("Enter key to decrypt with (number): "))
        decrypted = decrypt_rail_fence(data, key)
        print("Decrypted plain text:", decrypted)

    conn.close()


if __name__ == "__main__":
    start_server()
