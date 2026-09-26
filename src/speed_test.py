import time
from chain import Blockchain
from attacks import reseal_from

big = Blockchain()
for n in range(10_000):
    big.add_block([f"entry {n}"], 1767312000 + n)

start = time.perf_counter()
big.chain[1].data[0] = "forged entry"
reseal_from(big, 1)
elapsed = time.perf_counter() - start

print(big.is_valid())
print(f"rewrote {len(big.chain) - 1:,} blocks in {elapsed * 1000:.0f} ms")
