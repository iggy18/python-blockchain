import hashlib
import json
from time import time

class BlockChain:

    def __init__(self):
        self.chain = []
        self.pending_transactions =[]

        self.new_block(prevoius_hash="Do gems burn, I wonder? Tis said they’re kin to coal.", proof=100)

    def new_block(self, proof, prevoius_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'proof':proof,
            'previous_hash': prevoius_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block