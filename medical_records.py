import json
from datetime import datetime

def load_records():
    try:
        with open("medical_records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        base_structure = {"patients": []}
        save_records(base_structure)  
        return base_structure

def save_records(records):
    with open("medical_records.json", "w") as file:
        json.dump(records, file, indent=4)

def add_patient(patient_id, name, age):
    records = load_records()
    if any(patient["id"] == patient_id for patient in records["patients"]):
        return "Patient already exists."
    new_patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "medical_history": [],
        "prescriptions": []
    }
    records["patients"].append(new_patient)
    save_records(records)
    return "New patient added successfully."

def add_medical_record(patient_id, diagnosis, notes):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            for record in patient["medical_history"]:
                if record["diagnosis"] == diagnosis:
                    return "Medical record with this diagnosis already exists."
            new_record = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "diagnosis": diagnosis,
                "notes": notes
            }
            patient["medical_history"].append(new_record)
            save_records(records)
            return "Medical record added successfully."
    return "Patient not found."

def view_medical_record(patient_id):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            return patient["medical_history"]
    return "Patient not found."

def add_prescription(patient_id, prescription_id, medication, dosage):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            for presc in patient["prescriptions"]:
                if presc["prescription_id"] == prescription_id:
                    return "Prescription with this ID already exists."
            new_prescription = {
                "prescription_id": prescription_id,
                "medication": medication,
                "dosage": dosage,
                "status": "unverified"
            }
            patient["prescriptions"].append(new_prescription)
            save_records(records)
            return "Prescription added successfully."
    return "Patient not found."

def verify_prescription(patient_id, prescription_id, role):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            for presc in patient["prescriptions"]:
                if presc["prescription_id"] == prescription_id:
                    presc["status"] = "verified"
                    if "verification_log" not in presc:
                        presc["verification_log"] = []
                    verification_entry = {
                        "verified_by": role,
                        "verified_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    presc["verification_log"].append(verification_entry)
                    save_records(records)
                    return "Prescription verified."
    return "Prescription or patient not found."

def view_prescriptions(patient_id):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            return patient["prescriptions"]
    return "Patient not found."

def update_medical_record(patient_id, diagnosis, new_notes, role):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            for record in patient["medical_history"]:
                if record["diagnosis"] == diagnosis:
                    record["notes"] += " " + new_notes
                    record["last_updated_by"] = role
                    record["last_updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_records(records)
                    return "Record updated successfully."
    return "Record or patient not found."

def verify_medical_entry(patient_id, diagnosis, role):
    records = load_records()
    for patient in records["patients"]:
        if patient["id"] == patient_id:
            for record in patient["medical_history"]:
                if record["diagnosis"] == diagnosis:
                    if "verification_log" not in record:
                        record["verification_log"] = []
                    verification_entry = {
                        "verified_by": role,
                        "verified_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    record["verification_log"].append(verification_entry)
                    save_records(records)
                    return "Medical entry verified successfully."
    return "Medical entry or patient not found."

def clear_all_records():
    save_records({"patients": []})
    return "All records cleared. Database reset to base structure."