def hexToBin(s, numOfBits=64):
    scale = 16  # # equals to hexadecimal 
    binary = bin(int(s, scale))[2:].zfill(numOfBits)
    return binary

print hexToBin('0x7f')
