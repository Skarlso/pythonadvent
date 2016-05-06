import hashlib
INPUT = b"bgvyzdsv"
h = hashlib.md5(INPUT)
print(h.hexdigest())
