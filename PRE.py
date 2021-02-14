# For this to run we need to install nucypher'-pre-python library
from npre import bbs98
pre=bbs98.PRE()

# private and public key for alice
sk_a=pre.gen_priv(dtype=bytes)
pk_a=pre.priv2pub(sk_a)
print(sk_a)
print(pk_a)

#private and public key for bob
sk_b=pre.gen_priv(dtype=bytes)
pk_b=pre.priv2pub(sk_b)
print(sk_b)
print(pk_b)

# the message to be encrypted
mssg=b'Hello world'

# message encrypted with alice public key
e_mssg_pk_a= pre.encrypt(pk_a,mssg)
print(e_mssg_pk_a)

# decrypting the encrypted mssg with alice private key
d_mssg_sk_a= pre.decrypt(sk_a,e_mssg_pk_a)
print(d_mssg_sk_a)

# generation of re-encryption key
re_key= pre.rekey(sk_a,sk_b)

# re-encrypting the encrypted mssg that alice received with re-encryption key so that bob can de-crypt the mssg that was originally sent to alice with his private key
re_mssg_re_key= pre.reencrypt(re_key,e_mssg_pk_a)

# de-crypting the re-encrypted mssg 
received_mssg= pre.decrypt(sk_b,re_mssg_re_key)
print(received_mssg)

# Here to delegate access to bob alice needs to know the private key of bob which is not ideal.
# to avoid that we can use different proxy-re-encryption algorithm i.e AFGH algo

# But there’s a way to do it with the current algorithm. When Alice delegates access to Bob, she can generate an ephemeral key `sk_e` and produce a re-encryption key `rk_ae`.
# Then she encrypts `sk_e` with Bob’s public key `pk_b` yielding `e_b`.
# The proxy will be given both `rk_e` and `e_b`. When Bob connects, the proxy will hand him `e_b`.
# Then Bob can extract `pk_e` out of it and use that to decrypt encrypted messages coming from the proxy.
