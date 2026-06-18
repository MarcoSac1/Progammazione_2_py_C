import hmac, hashlib

tag = hmac.new(b"chiave", b"msg", hashlib.sha256).hexdigest()

print(tag)
# MAI == (timing attack!)
if hmac.compare_digest(tag, "e9f42de36c241cb4bcef923d9b6b80c558b8bcae42fc251b3fbbb7ddf30191e0"):
    print("OK")
    