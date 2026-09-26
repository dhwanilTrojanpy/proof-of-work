import hashlib
import json

class Block: 
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        contents = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
        }
        encoded = json.dumps(contents, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def __repr__(self):
        return (f"Block #{self.index}  "
                f"hash={self.hash[:10]}...  "
                f"prev={self.prev_hash[:10]}...")