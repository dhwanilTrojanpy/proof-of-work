import hashlib


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


a = sha256("Ken paid 500")
b = sha256("Ken paid 50")

same = sum(1 for x, y in zip(a, b) if x == y)
print(f"{same} of 64 characters happen to match")
print(f"{64 - same} of 64 characters changed")