from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
key = RSA.generate(2048)
public_key = key.publickey()
message = "Ismile Academy"
message_bytes = message.encode()
hash_message = SHA256.new(message_bytes)
signature = pkcs1_15.new(key).sign(hash_message)
try:
    pkcs1_15.new(public_key).verify(hash_message, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is invalid.")
