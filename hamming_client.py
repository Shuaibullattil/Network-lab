# client.py
import socket
import sys
import random

# Function to calculate parity for a given position
def calc_parity(data, pos):
    parity = 0
    for i in range(1, len(data)):
        if i & pos == pos:
            parity ^= data[i]
    return parity

# Function to generate Hamming code
def generate_hamming(message):
    m = len(message)
    r = 1

    # Step 1: Calculate number of parity bits
    while 2**r < m + r + 1:
        r += 1

    code_length = m + r
    code = [0] * (code_length + 1)  # 1-based indexing

    j = 0  # message bit index
    for i in range(1, code_length + 1):
        if i & (i - 1) != 0:  # if not a power of 2 → data bit
            code[i] = int(message[j])
            j += 1

    # Step 2: Calculate parity bits
    for i in range(r):
        pos = 2**i
        code[pos] = calc_parity(code, pos)

    return code

# Function to introduce a random error
def introduce_error(code):
    bit = random.randint(1, len(code) - 1)
    code[bit] = 1 - code[bit]  # flip the bit
    print(f"Error introduced at position {bit}")

# Client program
def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <port>")
        return

    port = int(sys.argv[1])
    host = '127.0.0.1'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    message = input("Enter binary message: ")
    code = generate_hamming(message)
    print("Generated Hamming Code:", ''.join(map(str, code[1:])))

    if input("Introduce error? (y/n): ").lower() == 'y':
        introduce_error(code)
        print("Modified Hamming Code:", ''.join(map(str, code[1:])))

    sock.sendall(''.join(map(str, code[1:])).encode())

    response = sock.recv(1024).decode()
    print("Server response:", response)

    sock.close()

if __name__ == "__main__":
    main()
