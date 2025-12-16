import socket
import random

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

def encode_data(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def introduce_error(data):
    data_list = list(data)
    pos = random.randint(0, len(data_list) - 1)
    data_list[pos] = '1' if data_list[pos] == '0' else '0'
    print(f"Error introduced at position {pos}")
    return ''.join(data_list)

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    key = input("Enter CRC key (binary polynomial divisor, e.g., 1001): ")
    s.send(key.encode())

    choice = input("Enter 1 for binary input, 2 for string input: ")

    if choice == "1":
        data = input("Enter binary data: ")
    else:
        string_data = input("Enter a string: ")
        data = ''.join(format(ord(x), '08b') for x in string_data)

    print("Binary form of data:", data)

    codeword = encode_data(data, key)
    print("Data with CRC before sending:", codeword)

    err_choice = input("Do you want to introduce an error? (y/n): ").lower()
    if err_choice == 'y':
        codeword = introduce_error(codeword)

    s.send(codeword.encode())

    response = s.recv(1024).decode()
    print("Server Response:", response)
