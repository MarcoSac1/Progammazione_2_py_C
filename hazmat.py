from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)
nonce = os.urandom(12)

ct = aesgcm.encrypt(nonce, b"segreto", b"meta")
pt = aesgcm.decrypt(nonce, ct, b"meta")

print(pt)