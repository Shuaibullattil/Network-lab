import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append(str(int(a[i]) ^ int(b[i])))
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0:pick]

    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def decode_data(data, key):
    remainder = mod2div(data, key)
    return remainder

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Server is listening...")

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)

        key = conn.recv(1024).decode()
        print("Using Key (Polynomial Divisor):", key)

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            print("Received codeword:", data)
            remainder = decode_data(data, key)
            print("Remainder after division:", remainder)

            if int(remainder) == 0:
                conn.send("No Error detected (CRC Passed)".encode())
            else:
                conn.send("Error detected (CRC Failed)".encode())
