import json
from datetime import datetime

def load_transactions():
    try:
        with open("digital_transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"insurance_records": [], "billing_transactions": []}

def save_transactions(data):
    with open("digital_transactions.json", "w") as file:
        json.dump(data, file, indent=4)

def link_patient_data(patient_id, insurance_data, billing_data):
    data = load_transactions()
    data_entry = {
        "patient_id": patient_id,
        "insurance_data": insurance_data,
        "billing_data": billing_data,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["insurance_records"].append(data_entry)
    save_transactions(data)
    return "Patient data linked successfully for interoperability."

def update_insurance(patient_id, update_details):
    data = load_transactions()
    for record in data["insurance_records"]:
        if record["patient_id"] == patient_id:
            record["insurance_data"].update(update_details)
            record["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_transactions(data)
            return "Insurance data updated automatically."
    return "Patient insurance record not found."

def generate_bill(patient_id, service_details):
    data = load_transactions()
    bill_entry = {
        "patient_id": patient_id,
        "service_details": service_details,
        "total_amount": service_details["amount"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["billing_transactions"].append(bill_entry)
    save_transactions(data)
    return "Bill generated directly between patient and provider."

def view_billing_transactions(patient_id):
    data = load_transactions()
    transactions = [entry for entry in data["billing_transactions"] if entry["patient_id"] == patient_id]
    return transactions if transactions else "No transactions found for this patient."

def clear_all_transactions():
    save_transactions({"insurance_records": [], "billing_transactions": []})
    return "All digital transaction data cleared."