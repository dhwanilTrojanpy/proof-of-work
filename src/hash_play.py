
import hashlib

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


print(sha256("Ken paid 500"))
print(sha256("Ken paid 500"))
print(sha256("Ken paid 50"))