import hashlib, secrets

salt = secrets.token_hex(16)
hash = hashlib.pbkdf2_hmac("sha256", b"password", salt.encode(), 600000)

print(hash.hex())