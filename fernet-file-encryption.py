from cryptography.fernet import Fernet



def generate_key():
    key = Fernet.generate_key()                                                 # generates key
    with open("secret.key","wb") as key_file:                                   #key genrated at line 5 will be stored in file secret.key
         key_file.write(key)
         print("Key is genrated")
         return key
def load_key():
    return open("D:\Engineering\Internship 2k21\GUI\test.pdf", "rb").read()
# keygeneration done

#===============================================================================
# encryting the file
def encrypt(filename):
    key = load_key()                                                            #loading the keys
    f = Fernet(key)                                                             #pass the keys to Fernet
    with open(filename, "rb") as file:                                          #opening the file
        file_data = file.read()                                                 #loading the file
    encrypted_data = f.encrypt(file_data)                                       #encrypted the message
    with open(filename, "wb") as file:                                          #opening the file
        file.write(encrypted_data)                                              #saved the encrypted data in same file at the same loc

#===============================================================================
# decrypting the file
def decrypt(filename):
    key = load_key()                                                            #loading the keys
    f = Fernet(key)                                                             #pass the keys to Fernet
    with open(filename, "rb") as file:                                          #opening the file
        file_data = file.read()
    decrypted_data= f.decrypt(file_data)                                        #decrypted the message
    with open(filename, "wb") as file:
        file.write(decrypted_data)                                              #saved the decrpted data in the same file at same path

#===============================================================================
#key = generate_key()
file = ""                                                          #before testing pls change the filepath for different location
#encrypt(file)
print("Your file has been encrypted.")
print("Your key for encryption is: ")
# print(key)
decrypt(file)
print("Your file has been decrypted.")
