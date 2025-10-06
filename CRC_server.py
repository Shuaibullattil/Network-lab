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

# Decode received data using CRC check
def decodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    return int(remainder)

def server_program():
    host = socket.gethostname()
    port = 5001

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Server is listening...")
    conn, address = server_socket.accept()
    print("Connection from:", str(address))

    while True:
        received_data = conn.recv(1024).decode()
        if not received_data:
            break

        # Exit condition
        if received_data == '2':
            print("Client disconnected.")
            break

        # Data received in form: encodedData,key
        data, key = received_data.split(',')
        remainder = decodeData(data, key)

        print("\nReceived Data:", data)
        print("Key:", key)
        print("Remainder:", remainder)

        if remainder == 0:
            print("✅ No Error Detected")
        else:
            print("❌ Error Detected")

    conn.close()
    server_socket.close()

if __name__ == '__main__':
    server_program()
