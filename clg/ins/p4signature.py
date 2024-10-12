from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_15
print("no module found")
#print(PKCS1_15)
# pip install pycryptodome
from Crypto.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()  # Fix here

# Documents
original_docs = b"this is original docs.."
modified_docs = b"this is modified docs.."

# Hashes
original_hash = SHA256.new(original_docs)
modified_hash = SHA256.new(modified_docs)

# Sign the original document
signature = PKCS1_15.new(RSA.import_key(private_key)).sign(original_hash)

# Verify the signature
try:
    PKCS1_15.new(RSA.import_key(public_key)).verify(modified_hash, signature)
    print("valid signature...")
except (ValueError, TypeError):
    print("invalid signature...")
