import json
import hashlib
from datetime import datetime
import os

class MockBlockchain:
    def __init__(self, blockchain_file="blockchain.json"):
        self.blockchain_file = blockchain_file
        self.chain = self.load_chain()
        if not self.chain:
            self.create_genesis_block()

    def create_genesis_block(self):
        """Creates the first block in the blockchain."""
        genesis_block = {
            "index": 0,
            "timestamp": str(datetime.now()),
            "data": "Genesis Block",
            "prev_hash": "0",
            "hash": self.hash_block(0, "Genesis Block", "0")
        }
        self.chain.append(genesis_block)
        self.save_chain()

    def add_block(self, data):
        """Adds a new block to the blockchain."""
        prev_block = self.chain[-1]
        index = prev_block["index"] + 1
        prev_hash = prev_block["hash"]
        timestamp = str(datetime.now())
        block_hash = self.hash_block(index, data, prev_hash)

        new_block = {
            "index": index,
            "timestamp": timestamp,
            "data": data,
            "prev_hash": prev_hash,
            "hash": block_hash
        }
        self.chain.append(new_block)
        self.save_chain()
        return new_block

    @staticmethod
    def hash_block(index, data, prev_hash):
        """Creates a SHA-256 hash of a block."""
        block_content = f"{index}{data}{prev_hash}".encode()
        return hashlib.sha256(block_content).hexdigest()

    def clear_blockchain(self):
        """Clears all blocks except the genesis block."""
        self.chain = self.chain[:1]
        self.save_chain()

    def load_chain(self):
        """Loads the blockchain from a file."""
        if os.path.exists(self.blockchain_file):
            with open(self.blockchain_file, "r") as file:
                return json.load(file)
        return []

    def save_chain(self):
        """Saves the blockchain to a file."""
        with open(self.blockchain_file, "w") as file:
            json.dump(self.chain, file, indent=4)