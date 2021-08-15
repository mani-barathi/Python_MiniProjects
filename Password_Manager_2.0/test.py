from cryptography.fernet import Fernet # pip install cryptography
from os import environ

# to generate a key which can be used for encyrption and decryption
key = Fernet.generate_key()

# creating a Fernet Obj with the generated key
# Fernet obj will do the encryption and decryption
fernet = Fernet(key)

password = 'this is a password'.encode()
encrypted_password = fernet.encrypt(password)

print(password)
print(encrypted_password)

decrypted_password = fernet.decrypt(encrypted_password)

print(decrypted_password.decode())
