from caesar import encrypt, decrypt

plaintext = "hello world"
shift = 3

# Encrypt plaintext
ciphertext = encrypt(plaintext, shift)
print(f"Encrypted message: {ciphertext}")

# Decrypt ciphertext
decrypted_text = decrypt(ciphertext, shift)
print(f"Decrypted message: {decrypted_text}")