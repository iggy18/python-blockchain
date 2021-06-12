import hashlib
import json
import time

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

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction ={
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = BlockChain()

t1 = blockchain.new_transaction('seth', 'mike', '15 BTC')
t2 = blockchain.new_transaction('mike', 'nikki', '12 BTC')
t3 = blockchain.new_transaction('nikki', 'gabe', '10 BTC')
blockchain.new_block(4242)

t4 = blockchain.new_transaction('gabe', 'kyle', '8 BTC')
t5 = blockchain.new_transaction('kyle', 'lou', '6 BTC')
t6 = blockchain.new_transaction('lou', 'evan', '4 BTC')
t6 = blockchain.new_transaction('evan', '', '2 BTC')
blockchain.new_block(4242)

print('blockchain:', blockchain.chain)
