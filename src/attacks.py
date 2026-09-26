def reseal_from(blockchain, start):
    for i in range(start, len(blockchain.chain)):
        block = blockchain.chain[i]
        block.prev_hash = blockchain.chain[i - 1].hash
        block.hash = block.compute_hash()


def reseal_effort(blockchain,start):
    effort = len(blockchain.chain) - start
    return effort            