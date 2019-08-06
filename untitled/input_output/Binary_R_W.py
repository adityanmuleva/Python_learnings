with open("binary",'bw') as binary_File:
    for i in range (17):
        binary_File.write(bytes([i]))

with open("binary",'br') as BinaryFile:
    for b in BinaryFile:
        print(b)