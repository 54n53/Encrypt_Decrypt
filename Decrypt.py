from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Utiliza la misma clave que se utilizó para cifrar
# key = "your_key_here"  # Utiliza la misma clave que se generó anteriormente
# (asegúrate de almacenarla de manera segura)
key = b'\x84\xf0{\xc15r\xb6\xc7\xb3hi\xd9\xe6\xd3z%\xa9t\x8e\x96\xf8\xaf\x86\xa8\xec\x99\xb8%\xc1\xb8\xa8\xb0'

# Ingresa la ruta del directorio que contiene los archivos cifrados
directory_path = input("Enter the directory path containing encrypted files: ")
"""
def decrypt_file(encrypted_file_path, key):
    # Lee el IV y el tamaño del archivo cifrado
    with open(encrypted_file_path, "rb") as encrypted_file:
        iv = encrypted_file.read(AES.block_size)
        encrypted_file_size = int.from_bytes(encrypted_file.read(16), 'big')

        # Crea un objeto AES para descifrar con la clave y el IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Descifra y elimina el acolchado
        decrypted_data = unpad(cipher.decrypt(encrypted_file.read()), AES.block_size)

    # Escribe los datos descifrados en un nuevo archivo
    decrypted_file_path = encrypted_file_path[:-4]  # Elimina la extensión .enc
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
"""
def decrypt_file(encrypted_file_path, key):
    # Lee el IV y el tamaño del archivo cifrado
    with open(encrypted_file_path, "rb") as encrypted_file:
        iv = encrypted_file.read(AES.block_size)
        encrypted_file_size = int.from_bytes(encrypted_file.read(16), 'big')

        # Crea un objeto AES para descifrar con la clave y el IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Descifra y elimina el acolchado
        decrypted_data = unpad(cipher.decrypt(encrypted_file.read()), AES.block_size)

    # Escribe los datos descifrados en un nuevo archivo, excluyendo el IV
    decrypted_file_path = encrypted_file_path[:-4]  # Elimina la extensión .enc
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data[AES.block_size:])
        
def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".enc"):
                encrypted_file_path = os.path.join(root, file)
                decrypt_file(encrypted_file_path, key)

decrypt_directory(directory_path, key)

