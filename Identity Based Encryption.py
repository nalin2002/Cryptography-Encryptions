from cocks.cocks import CocksPKG, Cocks # gmpy2
import hashlib
from time import time
import math
import matplotlib.pyplot as plt

def IBE(filename,size,ID,obj):
    # Extract private key, r, from an identity string (ID) and a is required for encryption and decryption.
    r, a = obj.extract(ID)

    # Must use same public modulus, n, from cocks_pkg
    cocks = Cocks(obj.n)
    mssg = open(filename,'r').read().encode()
    init= time()
    original_sha_value= hashlib.sha256(mssg)
    print("Time taken to generate hash value for mssg of size "+size+" : ",time()-init)
    #print("Original Message:-- " + str(mssg))

    init=time()
    encrypt_mssg = cocks.encrypt(mssg, a)
    encrypt_time = time()-init
    print("Time taken to generate ciphertext for mssg of size "+size+" : ",encrypt_time)
    #print("Encrypted Message:-- " + str(encrypt_mssg))

    init=time()
    decrypt_mssg = cocks.decrypt(encrypt_mssg, r, a)
    decrypt_time= time()-init
    print("Time taken to decrypt ciphertext of mssg of size " + size + " : ", decrypt_time)
    # print("Decrypted Message:-- " + str(decrypt_mssg))

    received_sha_value= hashlib.sha256(decrypt_mssg)
    print(" ")
    if original_sha_value.hexdigest()==received_sha_value.hexdigest():
        print("The original message is same as received message")
    else:
        print("Incorrect received message")
    print("------------------------------------------------------------------------------------------------------\n")
    return encrypt_mssg,decrypt_mssg


#
cocks_pkg = CocksPKG()
t1,t2= IBE('2KB_file.txt','2KB','aprabhath@ec.iitr.ac.in',cocks_pkg)
t3,t4=IBE('16KB_file.txt','16KB','aprabhath@ec.iitr.ac.in',cocks_pkg)
t5,t6=IBE('256KB_file.txt','256KB','aprabhath@ec.iitr.ac.in',cocks_pkg)
t7,t8=IBE('4MB_file.txt','4MB','aprabhath@ec.iitr.ac.in',cocks_pkg)
t9,t10=IBE('64MB_file.txt','64MB','aprabhath@ec.iitr.ac.in',cocks_pkg)


# x axis values
x = [2, 16, 256,4000,64000]
# corresponding y axis values
y = [2.229, 18.03, 274.82,4458,71330]

# plotting the points
#plt.plot(x, y)

plt.plot(x,y, color='green', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# naming the x axis
plt.xlabel('File size (KB)')
# naming the y axis
plt.ylabel('Time in seconds')
# giving a title to my graph
plt.title('IBE Encryption Plot')

# function to show the plot
plt.show()

