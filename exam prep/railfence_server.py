import socket

def decrypt_railfence(ciphertext,key):
    n = len(ciphertext)
    matrix = []
    for i in range(key):
        row = ['\n'] * n
        matrix.append(row)

    row = 0
    col = 0
    direction_down = False
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        
        matrix[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(n):
            if matrix[i][j] == '*' and index<n:
                matrix[i][j] = ciphertext[index]
                index +=1
    
    row = 0
    col = 0
    direction_down = False
    temp = []
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        temp.append(matrix[row][col])
        
        if i < n - 1:
            col += 1
            if direction_down:
                row += 1
            else:
                row -= 1

    return matrix,''.join(temp)

ciphertext = "sa2hlt20ult29aui09i l2b"
key = 6

matrix,plaintext = decrypt_railfence(ciphertext,key)
for row in matrix:
    print(row)

print(f"plain text {plaintext}")