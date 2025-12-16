import socket

def encrypt_railfence(plaintext,key):
    n = len(plaintext)

    matrix = []
    for i in range(key):
        row = ['\n']*len(plaintext)
        matrix.append(row)
    
    directionDown = False
    row = 0
    col = 0
    
    for ch in plaintext:
        if row == 0 or row == key-1:
            directionDown = not directionDown
        matrix[row][col] = ch
        col += 1
        if directionDown:
            row += 1
        else:
            row -= 1
    temp = []
    for i in range(key):
        for j in range(n):
            if matrix[i][j] != '\n':
                temp.append(matrix[i][j])
    ciphertext = ''.join(temp)
    return matrix,ciphertext
    




plaintext = "shuaib ullattil 20222099"
key = 6

matrix,ciphertext = encrypt_railfence(plaintext,key)
for row in matrix:
    print(row)
print(f'cipher text : {ciphertext}')
