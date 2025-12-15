import socket


def search(matrix,element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i,j
    return None,None

def create_matrix(key):
    key = key.lower()
    alphabets = "abcdefghiklmnopqrstuvwxyz"
    key_elements = []
    for ch in key:
        if ch == "j":
            ch = "i"
        if ch not in key_elements and ch in alphabets:
            key_elements.append(ch)
    for ch in alphabets:
        if ch not in key_elements:
            key_elements.append(ch)
    temp = []
    k=0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(key_elements[k])
            k +=1
        temp.append(row)
    return temp

def playfair_preprocess(message):
    message = message.lower()
    message = message.replace(" ","")
    message = message.replace("j","i")

    i = 0
    diagrams = []
    while i<len(message):
        a = message[i]
        if (i+1)<len(message):
            b = message[i+1]
            if a == b:
                diagrams.append(a + "x")
                i +=1
            else:
                diagrams.append(a + b)
                i += 2
        else:
            diagrams.append(a + "x")
            i += 1
    plaintext = ''.join(diagrams)
    return plaintext,diagrams

    


def encrypt(message,key):
    plaintext,diagrams = playfair_preprocess(message)
    keymatrix = create_matrix(key)

    print(f"plain text : {plaintext}")
    print(f"Diagrams : {diagrams}")
    print(f"KeyMatrix : {keymatrix}")

    text = []
    for pair in diagrams:
        a = pair[0]
        b = pair[1]
        r1,c1 = search(keymatrix,a)
        r2,c2 = search(keymatrix,b)

        if r1 == r2:
            a = keymatrix[r1][(c1 + 1)%5]
            b = keymatrix[r2][(c2 + 1)%5]
        elif c1 == c2:
            a = keymatrix[(r1+1)%5][c1]
            b = keymatrix[(r2+1)%5][c2]
        else:
            a = keymatrix[r1][c2]
            b = keymatrix[r2][c1]
        text.append(a+b)
    return ''.join(text)

HOST = "127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(1)
print("server is listening......")

conn,addr = server_socket.accept()
conn.send("you are online".encode())
message = conn.recv(1024).decode()
key = conn.recv(1024).decode()
ciphertext = encrypt(message,key)
print(f"CIPHER TEXT : {ciphertext}")
conn.send(ciphertext.encode())

conn.close()
server_socket.close()