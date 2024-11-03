import json
import streamlit as st
from datetime import datetime
from medical_records import (
    add_patient, add_medical_record, view_medical_record, 
    add_prescription, verify_prescription, view_prescriptions, 
    update_medical_record, verify_medical_entry, clear_all_records, load_records
)
from data_storage import add_data, retrieve_data, clear_all_data
from digital_transaction import link_patient_data, update_insurance, generate_bill, view_billing_transactions, clear_all_transactions
from supply_chain import track_drug, authenticate_drug, view_drug_info, clear_all_supply_chain
from research import add_subject, retrieve_subject_data, manage_clinical_trial, clear_all_research_data

st.title("Healthcare Information Management System")

st.sidebar.title("Navigation")
options = st.sidebar.selectbox("Choose an action", [
    "Add Patient", "View Patient Records", "Add Medical Record", 
    "Update Medical Record", "Add Prescription", "Verify Prescription", 
    "Verify Medical Entry", "View Prescriptions", "Clear All Records",
    "Add Data to Central Storage", "Retrieve Data from Central Storage", "Clear Central Data Storage",
    "Link Patient Data for Interoperability", "Update Insurance Automatically", 
    "Generate Direct Bill", "View Billing Transactions", "Clear All Transactions",
    "Track Drug", "Authenticate Drug", "View Drug Info", "Clear Supply Chain Data",
    "Add Research Subject", "Retrieve Subject Data", "Manage Clinical Trial", "Clear Research Data"
])

# Medical Records Actions
if options == "Add Patient":
    st.subheader("Add a New Patient")
    patient_id = st.text_input("Patient ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    if st.button("Add Patient"):
        result = add_patient(patient_id, name, age)
        st.write(result)

elif options == "View Patient Records":
    st.subheader("View Medical Records for a Patient")
    patient_id = st.text_input("Patient ID")
    if st.button("View Records"):
        records = view_medical_record(patient_id)
        st.write(records)

elif options == "Add Medical Record":
    st.subheader("Add Medical Record for a Patient")
    patient_id = st.text_input("Patient ID")
    diagnosis = st.text_input("Diagnosis")
    notes = st.text_area("Notes")
    if st.button("Add Medical Record"):
        result = add_medical_record(patient_id, diagnosis, notes)
        st.write(result)

elif options == "Update Medical Record":
    st.subheader("Update Medical Record for a Patient")
    patient_id = st.text_input("Patient ID")
    diagnosis = st.text_input("Diagnosis")
    new_notes = st.text_area("New Notes")
    role = st.selectbox("Updated By", ["doctor", "nurse", "hospital worker"])
    if st.button("Update Medical Record"):
        result = update_medical_record(patient_id, diagnosis, new_notes, role)
        st.write(result)

elif options == "Add Prescription":
    st.subheader("Add Prescription for a Patient")
    patient_id = st.text_input("Patient ID")
    prescription_id = st.text_input("Prescription ID")
    medication = st.text_input("Medication")
    dosage = st.text_input("Dosage")
    if st.button("Add Prescription"):
        result = add_prescription(patient_id, prescription_id, medication, dosage)
        st.write(result)

elif options == "Verify Prescription":
    st.subheader("Verify Prescription for a Patient")
    patient_id = st.text_input("Patient ID")
    prescription_id = st.text_input("Prescription ID")
    role = st.selectbox("Verified By", ["pharmacist", "doctor"])
    if st.button("Verify Prescription"):
        result = verify_prescription(patient_id, prescription_id, role)
        st.write(result)

elif options == "Verify Medical Entry":
    st.subheader("Verify Medical Entry")
    patient_id = st.text_input("Patient ID")
    diagnosis = st.text_input("Diagnosis")
    role = st.selectbox("Verified By", ["doctor", "hospital_worker"])
    if st.button("Verify Medical Entry"):
        result = verify_medical_entry(patient_id, diagnosis, role)
        st.write(result)

elif options == "View Prescriptions":
    st.subheader("View Prescriptions for a Patient")
    patient_id = st.text_input("Patient ID")
    if st.button("View Prescriptions"):
        prescriptions = view_prescriptions(patient_id)
        st.write(prescriptions)

elif options == "Clear All Records":
    st.subheader("Clear All Records")
    if st.button("Clear Records"):
        result = clear_all_records()
        st.write(result)


# Data Storage Actions
elif options == "Add Data to Central Storage":
    st.subheader("Add Data to Central Storage")
    data_type = st.selectbox("Data Type", ["medical_records", "prescriptions", "research_data"])
    data_content = st.text_area("Data Content (in JSON format)")
    if st.button("Add Data"):
        try:
            data_content = json.loads(data_content)  
            result = add_data(data_type, data_content)
            st.write(result)
        except json.JSONDecodeError:
            st.write("Invalid JSON format.")

elif options == "Retrieve Data from Central Storage":
    st.subheader("Retrieve Data from Central Storage")
    data_type = st.selectbox("Data Type", ["medical_records", "prescriptions", "research_data"])
    if st.button("Retrieve Data"):
        data = retrieve_data(data_type)
        st.json(data)

elif options == "Clear Central Data Storage":
    st.subheader("Clear All Data in Central Storage")
    if st.button("Clear Data"):
        result = clear_all_data()
        st.write(result)


# Digital Transaction Actions
if options == "Link Patient Data for Interoperability":
    st.subheader("Link Patient Data")
    patient_id = st.text_input("Patient ID")
    insurance_data = st.text_area("Insurance Data (in JSON format)")
    billing_data = st.text_area("Billing Data (in JSON format)")
    if st.button("Link Data"):
        try:
            insurance_data = json.loads(insurance_data)
            billing_data = json.loads(billing_data)
            result = link_patient_data(patient_id, insurance_data, billing_data)
            st.write(result)
        except json.JSONDecodeError:
            st.write("Invalid JSON format.")

elif options == "Update Insurance Automatically":
    st.subheader("Update Insurance Automatically")
    patient_id = st.text_input("Patient ID")
    update_details = st.text_area("Update Details (in JSON format)")
    if st.button("Update Insurance"):
        try:
            update_details = json.loads(update_details)
            result = update_insurance(patient_id, update_details)
            st.write(result)
        except json.JSONDecodeError:
            st.write("Invalid JSON format.")

elif options == "Generate Direct Bill":
    st.subheader("Generate Direct Bill")
    patient_id = st.text_input("Patient ID")
    service_details = st.text_area("Service Details (in JSON format)")
    if st.button("Generate Bill"):
        try:
            service_details = json.loads(service_details)
            result = generate_bill(patient_id, service_details)
            st.write(result)
        except json.JSONDecodeError:
            st.write("Invalid JSON format.")

elif options == "View Billing Transactions":
    st.subheader("View Billing Transactions")
    patient_id = st.text_input("Patient ID")
    if st.button("View Transactions"):
        transactions = view_billing_transactions(patient_id)
        st.json(transactions)

elif options == "Clear All Transactions":
    st.subheader("Clear All Digital Transactions")
    if st.button("Clear Transactions"):
        result = clear_all_transactions()
        st.write(result)


# Supply Chain Management Actions
if options == "Track Drug":
    st.subheader("Track Drug Shipment")
    drug_id = st.text_input("Drug ID")
    location = st.text_input("Current Location")
    status = st.text_input("Status (e.g., In Transit, Delivered)")
    eta = st.text_input("Estimated Delivery (e.g., 2024-11-05)")
    if st.button("Track Drug"):
        result = track_drug(drug_id, location, status, eta)
        st.write(result)

elif options == "Authenticate Drug":
    st.subheader("Authenticate Drug")
    drug_id = st.text_input("Drug ID")
    supplier_verified = st.checkbox("Verified by Supplier")
    if st.button("Authenticate Drug"):
        result = authenticate_drug(drug_id, supplier_verified)
        st.write(result)

elif options == "View Drug Info":
    st.subheader("View Drug Information")
    drug_id = st.text_input("Drug ID")
    if st.button("View Info"):
        drug_info = view_drug_info(drug_id)
        st.json(drug_info)

elif options == "Clear Supply Chain Data":
    st.subheader("Clear All Supply Chain Data")
    if st.button("Clear Data"):
        result = clear_all_supply_chain()
        st.write(result)


# Research Actions
if options == "Add Research Subject":
    st.subheader("Add Research Subject Data")
    subject_id = st.text_input("Subject ID")
    anonymized_data = st.text_area("Anonymized Data (in JSON format)")
    if st.button("Add Subject"):
        try:
            anonymized_data = json.loads(anonymized_data) 
            result = add_subject(subject_id, anonymized_data)
            st.write(result)
        except json.JSONDecodeError:
            st.write("Invalid JSON format.")

elif options == "Retrieve Subject Data":
    st.subheader("Retrieve Research Subject Data")
    subject_id = st.text_input("Subject ID")
    authorized = st.checkbox("I am authorized")
    if st.button("Retrieve Data"):
        result = retrieve_subject_data(subject_id, authorized)
        st.write(result)

elif options == "Manage Clinical Trial":
    st.subheader("Manage Clinical Trial Data")
    trial_id = st.text_input("Trial ID")
    trial_data = st.text_area("Trial Data (in JSON format, optional)")
    if st.button("Manage Trial"):
        try:
            if trial_data:
                trial_data = json.loads(trial_data) 
            result = manage_clinical_trial(trial_id, trial_data)
            st.write(result)
        except json.JSONDecodeError:
            st.write("Invalid JSON format.")

elif options == "Clear Research Data":
    st.subheader("Clear All Research Data")
    if st.button("Clear Data"):
        result = clear_all_research_data()
        st.write(result)


# show current JSON data
if st.sidebar.checkbox("Show Raw JSON Data"):
    records = load_records()
    st.json(records)