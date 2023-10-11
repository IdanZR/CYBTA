def encrypt(plaintext, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in plaintext:
        if char in alphabet:
            char_index = alphabet.index(char)
            shifted_index = (char_index - k) % 26
            encrypted_char = alphabet[shifted_index]
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

