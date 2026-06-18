import hashlib

h = hashlib.sha256(b"ciao").hexdigest()

# File grandi: a blocchi da 64KB
def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()
print(h) #stampo l'hash generato in SHA-256 di 64 char HEX 