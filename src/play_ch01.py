from chain import Blockchain
from attacks import reseal_from,reseal_effort

JAN = 1767657600  # 5 Jan 2026
FEB = 1770076800  # 2 Feb 2026
MAR = 1772496000  # 2 Mar 2026

circle = Blockchain()
circle.add_block(["Aisha paid 500", "Ken paid 500", "Marco paid 500",
                  "Priya paid 500", "Aisha took the pot: 2000"], JAN)
circle.add_block(["Aisha paid 500", "Ken paid 500", "Marco paid 500",
                  "Priya paid 500", "Ken took the pot: 2000"], FEB)
circle.add_block(["Aisha paid 500", "Ken paid 500", "Marco paid 500",
                  "Priya paid 500", "Marco took the pot: 2000"], MAR)

print("--- the honest notebook ---")
for block in circle.chain:
    print(block)
print(circle.is_valid())
honest_tip = circle.last_block().hash

print("\n--- step 1: someone edits February ---")
circle.chain[2].data[1] = "Ken paid 50"
print(circle.is_valid())

print("\n--- step 2: they re-seal February ---")
circle.chain[2].hash = circle.chain[2].compute_hash()
print(circle.is_valid())

print("\n--- step 3: they re-seal everything after it ---")
reseal_from(circle, 3)
print(circle.is_valid())
for block in circle.chain:
    print(block)

print("\nhonest March hash:", honest_tip[:16], "...")
print("forged March hash:", circle.last_block().hash[:16], "...")

for i in range(len(circle.chain)):
    print(f"effort to reseal from {i} block is {reseal_effort(circle,i)}")