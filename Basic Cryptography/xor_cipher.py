def encrypt(plaintext, key):
    ciphertext = ''
    
    for i in range(len(plaintext)):
        # XOR the ASCII values of the characters
        result = ord(plaintext[i]) ^ ord(key[i])
        ciphertext += chr(result)
    
    return ciphertext
