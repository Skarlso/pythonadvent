import hashlib

orig = "bgvyzdsv"
count = 0
inp = ""
while True:
    inp = orig + str(count)
    h = hashlib.md5(str.encode(inp))
    if h.hexdigest()[:6] == "000000":
        break
    count += 1

print(count)
