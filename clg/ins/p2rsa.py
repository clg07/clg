#  pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keyPair = RSA.generate(1024)
pubkey = keyPair.publickey()

# Display public key parameters
n = hex(pubkey.n)
e = hex(pubkey.e)
print("Public Key:")
print(n)
print(e)

# Export public key in PEM format
pubkeyPEM = pubkey.exportKey()
print(pubkeyPEM.decode("ascii"))

# Display private key parameters
en = hex(pubkey.n)
ed = hex(keyPair.d)
print("Private Key:")
print(en)
print(ed)

# Export private key in PEM format
privateKeyPEM = keyPair.exportKey()
print(privateKeyPEM.decode("ascii"))

# Message to be encrypted
amsg = "Smile Academy"
msg = amsg.encode("utf-8")  # Correct encoding of the message

# Encrypt the message
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)

# Convert the encrypted message to hex
result = binascii.hexlify(encrypted)
print("Encrypted: ", result)
