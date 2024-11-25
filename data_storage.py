import json
from cryptography.fernet import Fernet
from datetime import datetime
import os
from mock_blockchain import MockBlockchain

# Initialize the blockchain
blockchain = MockBlockchain()
print("Blockchain initialized:", blockchain.chain)

if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

def load_data():
    try:
        with open("data_storage.json", "r") as file:
            encrypted_data = file.read().encode()
            decrypted_data = cipher.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
    except FileNotFoundError:
        return {}

def add_data(data_type, **kwargs):
    """
    Adds data to the blockchain with automatic formatting.
    :param data_type: The type of data (e.g., 'patient', 'medical_record').
    :param kwargs: Key-value pairs of data fields.
    :return: A success message.
    """
    # Format data based on type
    if data_type == "patient":
        data = {
            "type": "patient",
            "patient_id": kwargs.get("patient_id"),
            "name": kwargs.get("name"),
            "age": kwargs.get("age"),
            "timestamp": str(datetime.now())
        }
    elif data_type == "medical_record":
        data = {
            "type": "medical_record",
            "patient_id": kwargs.get("patient_id"),
            "diagnosis": kwargs.get("diagnosis"),
            "notes": kwargs.get("notes"),
            "timestamp": str(datetime.now())
        }
    elif data_type == "transaction":
        data = {
            "type": "transaction",
            "transaction_id": kwargs.get("transaction_id"),
            "patient_id": kwargs.get("patient_id"),
            "amount": kwargs.get("amount"),
            "timestamp": str(datetime.now())
        }
    elif data_type == "supply_chain":
        data = {
            "type": "supply_chain",
            "drug_id": kwargs.get("drug_id"),
            "location": kwargs.get("location"),
            "status": kwargs.get("status"),
            "timestamp": str(datetime.now())
        }
    else:
        return f"Unknown data type: {data_type}. Cannot add data."

    # Add block to the blockchain
    blockchain.add_block(data)
    return f"{data_type.capitalize()} added successfully."

def retrieve_data(data_type):
    """
    Retrieves data from the blockchain by type.
    :param data_type: The type of data to retrieve.
    :return: A list of matching data or a message if no data is found.
    """
    results = [
        block["data"]
        for block in blockchain.chain
        if isinstance(block["data"], dict) and block["data"].get("type") == data_type
    ]
    return results if results else f"No {data_type} data found."

def clear_all_data():
    """
    Clears the blockchain except for the genesis block.
    :return: A success message.
    """
    blockchain.clear_blockchain()
    return "Blockchain data cleared."