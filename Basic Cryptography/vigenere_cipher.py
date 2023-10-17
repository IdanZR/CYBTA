def vigenere(text, key, mode='encrypt'):
    result = []

    for i in range(len(text)):
        text_index = LETTERS.index(text[i]) # returns the index in the alphabet
        key_index = LETTERS.index(key[i % len(key)]) #

        if mode == 'encrypt':
            result_index = (text_index + key_index) % 26
        elif mode == 'decrypt':
            result_index = (text_index - key_index) % 26

        result.append(LETTERS[result_index])

    return ''.join(result)
