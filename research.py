import json
from cryptography.fernet import Fernet
from datetime import datetime
import os

if not os.path.exists("research.key"):
    key = Fernet.generate_key()
    with open("research.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("research.key", "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

def load_research_data():
    try:
        with open("research_data.json", "r") as file:
            encrypted_data = file.read().encode()
            decrypted_data = cipher.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
    except FileNotFoundError:
        return {"subjects": [], "clinical_trials": []}

def save_research_data(data):
    encrypted_data = cipher.encrypt(json.dumps(data).encode())
    with open("research_data.json", "wb") as file:
        file.write(encrypted_data)

def add_subject(subject_id, anonymized_data):
    data = load_research_data()
    data["subjects"].append({
        "subject_id": subject_id,
        "data": anonymized_data,
        "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_research_data(data)
    return "Research subject data added with privacy preserved."

def retrieve_subject_data(subject_id, authorized):
    data = load_research_data()
    if not authorized:
        return "Access Denied: Unauthorized access attempt."
    for subject in data["subjects"]:
        if subject["subject_id"] == subject_id:
            return subject["data"]
    return "Subject data not found."

def manage_clinical_trial(trial_id, trial_data=None):
    data = load_research_data()
    for trial in data["clinical_trials"]:
        if trial["trial_id"] == trial_id:
            if trial_data:
                trial.update(trial_data)
                trial["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_research_data(data)
                return "Clinical trial information updated."
            else:
                return trial
    if trial_data:
        trial_data["trial_id"] = trial_id
        trial_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["clinical_trials"].append(trial_data)
        save_research_data(data)
        return "New clinical trial added."
    return "Clinical trial not found."

def clear_all_research_data():
    save_research_data({"subjects": [], "clinical_trials": []})
    return "All research data cleared."
