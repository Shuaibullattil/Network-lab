
def LZW_compression(message):

    dictionary = {chr(i) : i for i in range(256)}
    dict_size = 256

    w =""
    compressed = ""
    for c in message:
        wc = w+c
        if wc in dictionary:
            w = wc
        else:
            compressed += str(dictionary[w]) + "#"
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        compressed += str(dictionary[w]) + "#"
    return compressed[:-1]



message = input("enter the message")
hashed = LZW_compression(message)
print(f"your message {message}\ncompressed string :{hashed}")
