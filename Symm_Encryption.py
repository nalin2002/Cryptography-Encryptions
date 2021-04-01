#---------------------Symmetric Ency=ryption for strings and files---------------------------

from cryptography.fernet import Fernet
file_name='Test.txt'

def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

def load_key():
    file=open('key.key','rb')
    k=file.read()
    return k

def encrypt_file(filename,key):
    f= Fernet(key)
    with open(filename,'rb') as file:
        mssg=file.read()
    encrypt_mssg= f.encrypt(mssg)
    with open(filename,'wb') as file:
        file.write(encrypt_mssg)

def decrypt_file(filename,key):
    f= Fernet(key)
    with open(filename,'rb') as file:
        encrypt_mssg= file.read()
    decrypt_mssg= f.decrypt(encrypt_mssg)
    with open(filename,'wb') as file:
        file.write(decrypt_mssg)


write_key()
key=load_key()
message='Message to be symmetrically encrypted'.encode()
 # converts strings to bytes to be suitable for encryption
 #encode() encodes that string using utf-8 codec
f=Fernet(key)
encrypt_mssg= f.encrypt(message)
decrypt_mssg= f.decrypt(encrypt_mssg)


key1=load_key()
with open(file_name,'w') as f:
    text="This is an implementation symmetric encryption which is a " \
         "type of cryptographic encryption"
    f.write(text)
encrypt_file(file_name,key1)
decrypt_file(file_name,key1)
