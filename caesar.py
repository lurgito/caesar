def encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            char_code = ord(char)
            shifted_code = (char_code - 65 + shift) % 26 + 65
            ciphertext += chr(shifted_code)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            char_code = ord(char)
            shifted_code = (char_code - 65 - shift) % 26 + 65
            plaintext += chr(shifted_code)
        else:
            plaintext += char
    return plaintext
