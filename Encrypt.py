import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Set the key for encryption and decryption
# Generates a 32 bytes length AES key
key = get_random_bytes(32)
print(key)

# Choose a directory to encrypt
directory_path = input("Choose a directory to encrypt: ")

# Encrypt the files in the directory
def encrypt_file(file_path, key):
    # Get the file size
    file_size = os.path.getsize(file_path)

    # Generate a random IV
    iv = get_random_bytes(AES.block_size)

    # Encrypt the file
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(iv)
        # Pad the file size to a multiple of 16 bytes
        padded_file_size = pad(file_size.to_bytes(16, 'big'), AES.block_size)
        encrypted_file.write(cipher.encrypt(padded_file_size))
        with open(file_path, "rb") as original_file:
            # Pad the original file content
            padded_data = pad(original_file.read(), AES.block_size)
            encrypted_file.write(cipher.encrypt(padded_data))

    # Delete the original file
    os.remove(file_path)

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

encrypt_directory(directory_path, key)

