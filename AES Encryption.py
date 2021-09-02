from Crypto.Cipher import AES
from secrets import token_bytes
from time import time
import hashlib
# PLotting time plot
import matplotlib.pyplot as plt
import numpy as np
key = token_bytes(16)

def encrypt(filename):
    msg= open(filename,'r').read()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

# AES on 2KB file
filename='2KB_file.txt'
mssg= open(filename,'r').read()

init=time()
original_sha_value= hashlib.sha256(mssg.encode())
print("Time taken to generate a SHA hash value for message of 2KB file is : \n",time()-init)

init=time()
nonce,ciphertext,tag= encrypt(filename)
t9=time()-init
print("Time taken to generate a ciphertext for message of 2KB file is : ",t9)

init=time()
plaintext= decrypt(nonce,ciphertext,tag)
t10=time()-init
print("Time taken to decrypt the ciphertext of message of size 2KB is : \n",t10)

received_sha_value= hashlib.sha256(plaintext.encode())

if original_sha_value.hexdigest()==received_sha_value.hexdigest():
  print("Correct message is received....:)")
else:
  print("Incorrect message received....!!!")
  

# AES on 16KB file
filename='16KB_file.txt'
mssg= open(filename,'r').read()

init=time()
original_sha_value= hashlib.sha256(mssg.encode())
print("Time taken to generate a SHA hash value for message of 16KB file is : \n",time()-init)

init=time()
nonce,ciphertext,tag= encrypt(filename)
t1=time()-init
print("Time taken to generate a ciphertext for message of 16KB file is : ",t1)

init=time()
plaintext= decrypt(nonce,ciphertext,tag)
t2=time()-init
print("Time taken to decrypt the ciphertext of message of size 16KB is : \n",t2)

received_sha_value= hashlib.sha256(plaintext.encode())

if original_sha_value.hexdigest()==received_sha_value.hexdigest():
  print("Correct message is received....:)")
else:
  print("Incorrect message received....!!!")

# AES on 256KB file
filename='256KB_file.txt'
mssg= open(filename,'r').read()

init=time()
original_sha_value= hashlib.sha256(mssg.encode())
print("Time taken to generate a SHA hash value for message of 256KB file is : \n",time()-init)

init=time()
nonce,ciphertext,tag= encrypt(filename)
t3=time()-init
print("Time taken to generate a ciphertext for message of 256KB file is : ",t3)

init=time()
plaintext= decrypt(nonce,ciphertext,tag)
t4=time()-init
print("Time taken to decrypt the ciphertext of message of size 256KB is : \n",t4)

received_sha_value= hashlib.sha256(plaintext.encode())

if original_sha_value.hexdigest()==received_sha_value.hexdigest():
  print("Correct message is received....:)")
else:
  print("Incorrect message received....!!!")
  
# AES on 4MB file
filename='4MB_file.txt'
mssg= open(filename,'r').read()

init=time()
original_sha_value= hashlib.sha256(mssg.encode())
print("Time taken to generate a SHA hash value for message of 4MB file is : \n",time()-init)

init=time()
nonce,ciphertext,tag= encrypt(filename)
t5=time()-init
print("Time taken to generate a ciphertext for message of 4MB file is : ",t5)

init=time()
plaintext= decrypt(nonce,ciphertext,tag)
t6=time()-init
print("Time taken to decrypt the ciphertext of message of size 4MB is : \n",t6)

received_sha_value= hashlib.sha256(plaintext.encode())

if original_sha_value.hexdigest()==received_sha_value.hexdigest():
  print("Correct message is received....:)")
else:
  print("Incorrect message received....!!!")
  
# x axis values
x = [2,16,256,4000,64000]
# corresponding y axis values
y = [t9,t1,t3,t5,t7]

plt.plot(x,y, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.xscale('log')
# naming the x axis
plt.xlabel('File size (KB)')
# naming the y axis
plt.ylabel('Time in seconds')
# giving a title to my graph
plt.title('AES Encryption Plot')
#plt.xticks([1,2**4,2**8,2**12,2**16])
# function to show the plot
plt.show()

# x axis values
x = [2, 16, 256,4000,64000]
# corresponding y axis values
y = [t10,t2,t4,t6,t8]

plt.plot(x,y, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.xscale('log')
# naming the x axis
plt.xlabel('File size (KB)')
# naming the y axis
plt.ylabel('Time in seconds')
# giving a title to my graph
plt.title('AES Decryption Plot')

# function to show the plot
plt.show()
  


