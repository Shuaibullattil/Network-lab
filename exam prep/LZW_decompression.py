





d = "115#104#117#97#105#98#32#117#108#108#97#116#116#105#108"

dictionary = {i:chr(i) for i in range(256)}
dict_size = 256
compressed = [int(x) for x in d.split("#")]

w = chr(compressed[0])
decompress = [w]

for k in compressed[1:]:
    if k in dictionary:
        entry = dictionary[k]
    elif k == dict_size:
        entry = w + w[0]
    else:
        ValueError(f"bad compression for {k}")
    
    decompress.append(entry)

    dictionary[dict_size] = w + entry[0]
    dict_size +=1

    w = entry[0]

final =  ''.join(decompress)
print(f"your string  {d}\nafter decompression {final}")
    