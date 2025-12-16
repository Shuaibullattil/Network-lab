import socket

# Function to encrypt text using Rail Fence Cipher
def encrypt_rail_fence(text, key):
    n = len(text)

    # Step 1: Create empty matrix
    rail = []
    for i in range(key):
        row = ['\n'] * n
        rail.append(row)

    # Step 2: Fill letters in zigzag pattern
    direction_down = False
    row, col = 0, 0

    for ch in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = ch
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Step 3: Read row-wise to form cipher text
    result = []
    for i in range(key):
        for j in range(n):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)


def start_client():
    host = '127.0.0.1'
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server!\n")

    while True:
        key = int(input("Enter key (number): "))
        text = input("Enter plain text: ")
        encrypted = encrypt_rail_fence(text, key)
        print("Encrypted text:", encrypted)
        client_socket.send(encrypted.encode())


if __name__ == "__main__":
    start_client()
