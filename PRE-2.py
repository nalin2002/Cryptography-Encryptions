from umbral import pre,keys,signing


# Generate Umbral keys for Alice.
alice_private_key = keys.UmbralPrivateKey.gen_key()
alice_public_key = alice_private_key.get_pubkey()

alice_signing_key = keys.UmbralPrivateKey.gen_key()
alice_verifying_key = alice_signing_key.get_pubkey()
alice_signer = signing.Signer(private_key=alice_signing_key)

# Generate Umbral keys for Bob.
bob_private_key = keys.UmbralPrivateKey.gen_key()
bob_public_key = bob_private_key.get_pubkey()

# Encrypt data with Alice's public key.
message = b'Proxy Re-Encryption is cool!'
print(message)

ciphertext, capsule = pre.encrypt(alice_public_key, message)
print(ciphertext,"  ",capsule)

# Decrypt data with Alice's private key.
cleartext = pre.decrypt(ciphertext=ciphertext,capsule=capsule,decrypting_key=alice_private_key)
print(cleartext)   

# Alice generates "M of N" re-encryption key fragments (or "KFrags") for Bob.
# In this example, 10 out of 20.
kfrags = pre.generate_kfrags(delegating_privkey=alice_private_key,
                             signer=alice_signer,
                             receiving_pubkey=bob_public_key,
                             threshold=10,
                             N=20)
                             
capsule.set_correctness_keys(delegating=alice_public_key,receiving=bob_public_key,verifying=alice_verifying_key)

cfrags = list()           # Bob's cfrag collection
for kfrag in kfrags[:10]:
  cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule)
  cfrags.append(cfrag)    # Bob collects a cfrag

for cfrag in cfrags:
  capsule.attach_cfrag(cfrag)

bob_cleartext = pre.decrypt(ciphertext=ciphertext, capsule=capsule,decrypting_key=bob_private_key)
print(bob_cleartext)

