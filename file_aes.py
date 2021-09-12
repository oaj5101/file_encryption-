import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def readFile(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
    return file_data
#==================================================================================

def generateKey():
    key = AESGCM.generate_key(bit_length=128)
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
#===============================================================================

def loadKey():
    return open("secret.key", "rb").read()
#===============================================================================

def encrypt(filename):
    generateKey()
    key = loadKey()
    data = readFile(filename)
    aad = b"authenticated but unencrypted data"
    aesgcm = AESGCM(key)
    global nonce
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, aad)
    with open(filename, "wb") as file:
        file.write(ct)
#===============================================================================

def decrypt(filename):
    key = loadKey()
    data = readFile(filename)
    aad = b"authenticated but unencrypted data"
    aesgcm = AESGCM(key)
    message = aesgcm.decrypt(nonce, data, aad)
    with open(filename, "wb") as file:
        file.write(message)

# data = b"a secret message"
# print(key)
# print(ct)
# print(messag/e)
global filename
filename = ""
# encrypt(filename)
print("Encryption is completed.")
decrypt(filename)
print("Decryption is completed.")
