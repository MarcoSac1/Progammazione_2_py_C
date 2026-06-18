import secrets, string

token  = secrets.token_hex(32)
print(f'{token} -primo token')
token2 = secrets.token_urlsafe(32)
print(f'{token2} -secondo token')

pw     = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

print(f'{pw} -hash ottenuto')