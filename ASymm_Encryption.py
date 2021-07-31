#-----------------Public Key Encryption--------------

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

file_name='Test.txt'
with open(file_name,'w') as f:
    f.write("Public and Private key encryption")
with open(file_name,'rb') as f:
    mssg=f.read()

print(mssg)
# generating private key of length of 1024 bits
private_key=RSA.generate(1024)
# generating the public key from private key
public_key=private_key.publickey()

# private_key and public_key are RSA Key objects .Now converting them to strings
private_key_str= private_key.export_key().decode()
public_key_str= public_key.export_key().decode()

#writing the public and private keys to .pem files
with open('private_key.pem','w') as pr:
    pr.write(private_key_str)
with open('public_key.pem','w') as pr:
    pr.write(public_key_str)

# importing keys from pem files and converting to RSA key objects
pr_key=RSA.import_key(open('private_key.pem','r').read())
pu_key=RSA.import_key(open('public_key.pem','r').read())

# encryption part
cipher= PKCS1_OAEP.new(key=public_key)
cipher_text= cipher.encrypt(mssg)
print((cipher_text))

#decryption part
decrypt_cipher=PKCS1_OAEP.new(key=private_key)
decrypt_mssg=decrypt_cipher.decrypt(cipher_text)
print(decrypt_mssg)

