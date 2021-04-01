from umbral import pre, keys, signing
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def Upload_File_GD(filename):
    file= open(filename,'r').read()
    f = drive.CreateFile({'title': filename})
    f.SetContentString(file)
    f.Upload()
    str = filename + ' Successfully Uploaded to Google Drive'
    print(str)

def Download_File_GD(filename, file_ID):  # File Id for the text file i.e .txt file
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    file = drive.CreateFile({'id': file_ID})
    file.GetContentFile(filename)
    str = filename + ' Successfully Downloaded from Google Drive'
    print(str)


file_name = open('Test_file.txt', 'w')
file_name.write('After the Interstate Highway System was authorized in 1956, planners decided that I-40 would link '
                'Tennessee’s big cities, from Knoxville to Nashville to Memphis. But in Memphis, locals looked at the proposed'
                ' route of the highway and were appalled. It would barrel through Overton Park, a beloved local green space '
                'dotted with ponds, paths, and a stand of old-growth forest')
file_name.close()

file_name=open('Test_file.txt','r')
file_content= file_name.read()
original_file_content= file_content
file_name.close()

# Generate Umbral keys for Alice.
alice_private_key = keys.UmbralPrivateKey.gen_key()
alice_public_key = alice_private_key.get_pubkey()

alice_signing_key = keys.UmbralPrivateKey.gen_key()
alice_verifying_key = alice_signing_key.get_pubkey()
alice_signer = signing.Signer(private_key=alice_signing_key)

# Generate Umbral keys for Bob.
bob_private_key = keys.UmbralPrivateKey.gen_key()
bob_public_key = bob_private_key.get_pubkey()

message= file_content.encode() # string in bytes format
#print(message)

# Encrypt data with Alice's public key.

ciphertext, capsule = pre.encrypt(alice_public_key, message)
print(ciphertext,"  ",capsule)

# Decrypt data with Alice's private key.
cleartext = pre.decrypt(ciphertext=ciphertext, capsule=capsule, decrypting_key=alice_private_key)
print(cleartext) # in bytes format

# Alice generates "M of N" re-encryption key fragments (or "KFrags") for Bob.
# In this example, 10 out of 20.
kfrags = pre.generate_kfrags(delegating_privkey=alice_private_key,
                              signer=alice_signer,
                              receiving_pubkey=bob_public_key,
                              threshold=10,
                              N=20)

capsule.set_correctness_keys(delegating=alice_public_key, receiving=bob_public_key, verifying=alice_verifying_key)


cfrags = list()  # Bob's cfrag collection
for kfrag in kfrags[:10]:
     cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule)
     cfrags.append(cfrag)  # Bob collects a cfrag

for cfrag in cfrags:
     capsule.attach_cfrag(cfrag)

print(ciphertext)
bob_cleartext = pre.decrypt(ciphertext=ciphertext, capsule=capsule, decrypting_key=bob_private_key)

re_cipher_text="Hello"
file_name= open('Test_file.txt','w')
file_name.write(str(re_cipher_text))
file_name.close()


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#Upload_File_GD('Test_file.txt')

Download_File_GD('Test_file_1.txt','1xc8UozelnAL76mbzNUX2i5GCg2AZLekK')
print(bob_cleartext)
