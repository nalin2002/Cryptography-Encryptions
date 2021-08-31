from umbral import pre, keys, signing
from umbral import SecretKey, Signer
from umbral import encrypt, decrypt_original
from umbral import generate_kfrags
from umbral import reencrypt
from umbral import decrypt_reencrypted
import hashlib
from time import time
import math
import matplotlib.pyplot as plt

# Ref: https://github.com/nucypher/pyUmbral

def PRE(filename,size):

    init=time()
    # Generate Umbral keys for Alice.
    # Generate Umbral keys for Alice.
    alices_secret_key = SecretKey.random()
    alices_public_key = alices_secret_key.public_key()

    alices_signing_key = SecretKey.random()
    alices_signer = Signer(alices_signing_key)
    alices_verifying_key = alices_signing_key.public_key()

    # Generate Umbral keys for Bob.
    bobs_secret_key = SecretKey.random()
    bobs_public_key = bobs_secret_key.public_key()
    print("Time taken to generate all keys for both alice and bob is : ",time()-init)
    print(" ")

    # Encrypt data with Alice's public key.
    message = open(filename,'r').read().encode()

    init = time()
    original_sha_value = hashlib.sha256(message)
    print("Time taken to generate hash value for message of size " + size + " : ", time() - init)
    print(" ")

    init=time()
    capsule, ciphertext = encrypt(alices_public_key, message)
    encrypt_time = time() - init
    print("Time taken to generate ciphertext for ALice from original message of size " + size + " : ", encrypt_time)
    #print(ciphertext, "  ", capsule)

    # Decrypt data with Alice's private key.
    init=time()
    cleartext = decrypt_original(alices_secret_key, capsule, ciphertext)
    decrypt_time = time() - init
    print("Time taken to decrypt ciphertext received by ALice : ", decrypt_time)
    print(" ")

    alice_sha_value= hashlib.sha256(cleartext)

    if original_sha_value.hexdigest()==alice_sha_value.hexdigest():
        print("Alice received the correct message....!")
    else:
        print("Alice received the wrong message....!!")
    print(" ")

    init=time()
    # Alice generates "M of N" re-encryption key fragments (or "KFrags") for Bob.In this example, 10 out of 20.
    kfrags = generate_kfrags(delegating_sk=alices_secret_key,receiving_pk=bobs_public_key,signer=alices_signer,
                             threshold=10,num_kfrags=20)
    print("Time taken to generate re-encryption key fragments is : ",time()-init)

    init=time()
    # Several Ursulas perform re-encryption, and Bob collects the resulting `cfrags`.
    cfrags = list()  # Bob's cfrag collection
    for kfrag in kfrags[:10]:
        cfrag = pre.reencrypt(capsule=capsule, kfrag=kfrag)
        cfrags.append(cfrag)  # Bob collects a cfrag
    print("Time taken by proxy to re-encrypt the alice ciphertext for bob is : ",time()-init)

    init=time()
    bob_cleartext = pre.decrypt_reencrypted(receiving_sk=bobs_secret_key,delegating_pk=alices_public_key,capsule=capsule,
                                            verified_cfrags=cfrags,ciphertext=ciphertext)
    print("Time taken to decrypt the re-encrypted ciphertext by bob is : ",time()-init)
    print(" ")

    bob_sha_value= hashlib.sha256(bob_cleartext)

    if original_sha_value.hexdigest()==bob_sha_value.hexdigest():
        print("Bob received the correct message....!")
    else:
        print("Bob received the wrong message....!!")
    print(" ")
    print("---------------------------------------------------------------------------------------------------------------")
    return encrypt_time,decrypt_time


t1,t2= PRE('2KB_file.txt','2KB')
t3,t4= PRE('16KB_file.txt','16KB')
t5,t6= PRE('256KB_file.txt','256KB')
t7,t8= PRE('4MB_file.txt','4MB')
t9,t10=PRE('64MB_file.txt','64MB')
