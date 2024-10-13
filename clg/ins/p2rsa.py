from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keyPair = RSA.generate(1024)
pubkey = keyPair.publickey()

# Display keys and export them in PEM format
print("Public Key (n, e):", hex(pubkey.n), hex(pubkey.e))
print(pubkey.exportKey().decode("ascii"))

print("Private Key (n, d):", hex(pubkey.n), hex(keyPair.d))
print(keyPair.exportKey().decode("ascii"))

# Encrypt the message
msg = "Smile Academy".encode("utf-8")
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)

# Output the encrypted message in hex
print("Encrypted:", binascii.hexlify(encrypted))
