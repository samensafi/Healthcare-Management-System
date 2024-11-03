import json
from datetime import datetime

def load_supply_chain():
    try:
        with open("supply_chain.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"drugs": []}

def save_supply_chain(data):
    with open("supply_chain.json", "w") as file:
        json.dump(data, file, indent=4)

def track_drug(drug_id, location, status, eta):
    data = load_supply_chain()
    for drug in data["drugs"]:
        if drug["drug_id"] == drug_id:
            drug["tracking"] = {
                "location": location,
                "status": status,
                "eta": eta,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            save_supply_chain(data)
            return "Drug tracking information updated successfully."
    
    new_drug = {
        "drug_id": drug_id,
        "tracking": {
            "location": location,
            "status": status,
            "eta": eta,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "authenticity": False  
    }
    data["drugs"].append(new_drug)
    save_supply_chain(data)
    return "Drug added to tracking system."

def authenticate_drug(drug_id, supplier_verified):
    data = load_supply_chain()
    for drug in data["drugs"]:
        if drug["drug_id"] == drug_id:
            drug["authenticity"] = supplier_verified
            drug["last_verified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_supply_chain(data)
            return "Drug authentication status updated."
    return "Drug not found in the system."

def view_drug_info(drug_id):
    data = load_supply_chain()
    for drug in data["drugs"]:
        if drug["drug_id"] == drug_id:
            return drug
    return "Drug not found in the system."

def clear_all_supply_chain():
    save_supply_chain({"drugs": []})
    return "All supply chain data cleared."