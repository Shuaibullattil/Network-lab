import socket

# XOR operation between two binary strings
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# Performs Mod-2 Division
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

# Encode data with CRC remainder
def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    print("Encoded Data (Data + Remainder):", codeword)
    return codeword

def client_program():
    host = socket.gethostname()
    port = 5001

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        data = input("\nEnter message: ")
        key = input("Enter the key: ")

        # Convert message to binary
        data = ''.join(format(ord(i), '08b') for i in data)

        print("\n--- Sending Data Without Error ---")
        encodedData = encodeData(data, key)
        client_socket.send(f"{encodedData},{key}".encode())

        print("\n--- Sending Data With Error ---")
        # Introduce error by flipping key bits
        error_key = key.replace('0', '1')
        encodedData = encodeData(data, error_key)
        client_socket.send(f"{encodedData},{key}".encode())

        op = input("\nPress 1 to continue or 2 to exit: ")
        client_socket.send(op.encode())
        if op == '2':
            print("Closing connection...")
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()
