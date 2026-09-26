from block import Block

GENESIS_TIME = 1767312000  # 1 Jan 2026, 7pm Toronto

class Blockchain:
    def __init__(self):
        genesis = Block(0, GENESIS_TIME, ["Dhwanil's chain first Genesis Block"], "0" * 64)
        self.chain = [genesis]

    def last_block(self):
        return self.chain[-1]

    def add_block(self, data, timestamp):
        prev = self.last_block()
        block = Block(prev.index + 1, timestamp, data, prev.hash)
        self.chain.append(block)
        return block

    def is_valid(self):
        for i, block in enumerate(self.chain):
            if block.hash != block.compute_hash():
                return False, f"block {i}: contents changed after it was sealed"
            if i > 0 and block.prev_hash != self.chain[i - 1].hash:
                return False, f"block {i}: no longer points to block {i - 1}"
        return True, "every block checks out"

