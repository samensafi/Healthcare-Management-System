import json
from cryptography.fernet import Fernet
import os

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

def save_data(data):
    encrypted_data = cipher.encrypt(json.dumps(data).encode())
    with open("data_storage.json", "wb") as file:
        file.write(encrypted_data)

def add_data(data_type, data_content):
    data = load_data()
    if data_type not in data:
        data[data_type] = []
    data[data_type].append(data_content)
    save_data(data)
    return f"{data_type.capitalize()} added successfully."

def retrieve_data(data_type):
    data = load_data()
    return data.get(data_type, "No data found.")

def clear_all_data():
    save_data({})
    return "Data storage cleared."