from cocks.cocks import CocksPKG, Cocks # gmpy2

cocks_pkg = CocksPKG()

# Extract private key, r, from an identity string (User1)
# a is required for encryption and decryption.
r, a = cocks_pkg.extract("User1") # "User1" is the identity string

cocks = Cocks(cocks_pkg.n)  # Must use same public modulus, n, from cocks_pkg
mssg="This is the implementation of Identity based encryption".encode()
print("Original Message:-- "+str(mssg))

encrypt_mssg= cocks.encrypt(mssg, a)
print("Encrypted Message:-- "+str(encrypt_mssg))

decrypt_mssg = cocks.decrypt(encrypt_mssg, r, a)
print("Decrypted Message:-- "+str(decrypt_mssg))