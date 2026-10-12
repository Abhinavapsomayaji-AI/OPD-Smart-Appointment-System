import streamlit as st
import pandas as pd
import random

# Page Setup
st.set_page_config(page_title="OPD Smart Care", layout="wide")

# Initialize In-Memory Session Storage
if "appointments" not in st.session_state:
    st.session_state.appointments = []

# AI Briefing Function (Offline Demo Mode)
def generate_ai_doctor_brief(patient_data: dict) -> str:
    name = patient_data.get('name', 'Patient')
    complaint = patient_data.get('complaint', 'Not specified')
    conditions = patient_data.get('conditions', 'None')
    surgeries = patient_data.get('surgeries', 'None')
    
    summary = f"""
• **Patient Profile:** {name} presented for evaluation.
• **Primary Issue:** Chief complaint of {complaint.strip().lower()}.
• **Relevant Medical History:** History of {conditions} | Past surgeries/illnesses: {surgeries}.
• **Clinical Action:** Priority triage for assigned doctor evaluation.
    """
    return summary

# Navigation
sidebar_choice = st.sidebar.radio("Select Portal", ["Patient Portal", "Doctor Portal"])

# ------------------- PATIENT PORTAL -------------------
if sidebar_choice == "Patient Portal":
    st.title("🏥 Book Your OPD Appointment")
    st.write("Enter patient details below, or click the button to generate a random medical history.")

    # --- RANDOM DEMO GENERATOR LOGIC ---
    SAMPLE_COMPLAINTS = [
        "Severe headache and dizziness for 2 days", 
        "Mild fever, body ache, and persistent cough", 
        "Routine diabetic checkup and fatigue", 
        "Sharp lower back pain after lifting weight",
        "Acidity and stomach discomfort after meals",
        "Knee Pain since a month"
    ]
    SAMPLE_CONDITIONS = ["Diabetes", "Hypertension", "Asthma", "High Cholesterol", "Arthritis", "Osteoporosis",  "Epilepsy", "Migraines", "Thyroid Disorders", "None"]
    SAMPLE_SURGERIES = ["Appendectomy (2019)", "ACL Surgery (2021)", "Gallbladder Removal (2018)", "None"]

    if st.button("🎲 Generate Random Medical History"):
        st.session_state["demo_complaint"] = random.choice(SAMPLE_COMPLAINTS)
        st.session_state["demo_conditions"] = random.sample(SAMPLE_CONDITIONS, k=random.randint(0, 2))
        st.session_state["demo_surgeries"] = random.choice(SAMPLE_SURGERIES)

    # Pull auto-filled clinical values, leave name blank for user input
    def_complaint = st.session_state.get("demo_complaint", "")
    def_conditions = st.session_state.get("demo_conditions", [])
    def_surgeries = st.session_state.get("demo_surgeries", "None")

    # --- INTAKE FORM ---
    with st.form("patient_intake_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="Enter patient name...")
            age = st.number_input("Age", min_value=1, max_value=110, value=25)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        with col2:
            doctor = st.selectbox(
                "Select Doctor", 
                [
                    "Dr. Sharma (Cardiology)", 
                    "Dr. Rao (General Physician)", 
                    "Dr. Kumar (Orthopedician)", 
                    "Dr. Ravi (Endocrinologist)", 
                    "Dr. Seeta (Pediatrician)", 
                    "Dr. Susheela (Dermatologist)"
                ]
            )
            slot = st.selectbox("Select Available Slot", ["11:00 AM - 11:15 AM", "11:15 AM - 11:30 AM", "11:30 AM - 11:45 AM"])

        st.subheader("Medical Background")
        complaint = st.text_area("Chief Complaint (Why are you visiting today?)", value=def_complaint, placeholder="e.g. Severe headache for 2 days...")
        conditions = st.multiselect("Pre-existing Conditions", ["Diabetes", "Hypertension", "Asthma"], default=def_conditions)
        surgeries = st.text_input("Past Surgeries / Major Illnesses", value=def_surgeries)
        
        submitted = st.form_submit_button("Confirm Appointment")

    if submitted:
        if not name.strip():
            st.error("Please enter a patient name before confirming.")
        else:
            patient_data = {
                "name": name,
                "age": age,
                "gender": gender,
                "doctor": doctor,
                "slot": slot,
                "complaint": complaint,
                "conditions": ", ".join(conditions) if conditions else "None",
                "surgeries": surgeries
            }
            
            patient_data["summary"] = generate_ai_doctor_brief(patient_data)
                
            st.session_state.appointments.append(patient_data)
            st.success(f"Appointment booked for {slot}! Pre-intake summary generated.")

# ------------------- DOCTOR PORTAL -------------------
elif sidebar_choice == "Doctor Portal":
    st.title("👨‍⚕️ Doctor OPD Dashboard")

    st.subheader("Today's Schedule Overview")
    
    all_slots = ["11:00 AM - 11:15 AM", "11:15 AM - 11:30 AM", "11:30 AM - 11:45 AM"]
    booked_slots = [appt["slot"] for appt in st.session_state.appointments]
    
    schedule_data = []
    for s in all_slots:
        status = "Booked" if s in booked_slots else "Available"
        schedule_data.append({"Time": s, "Status": status})
        
    st.table(pd.DataFrame(schedule_data))

    st.subheader("📋 Incoming Patient AI Summaries")
    
    if not st.session_state.appointments:
        st.info("No patient intake submissions yet today.")
    else:
        for appt in st.session_state.appointments:
            with st.expander(f"⏰ {appt['slot']} - {appt['name']} ({appt['age']} yrs, {appt['gender']}) ➔ {appt['doctor']}"):
                st.markdown(f"**Chief Complaint:** {appt['complaint']}")
                st.markdown(f"**Conditions:** {appt['conditions']} | **Surgeries:** {appt['surgeries']}")
                st.info(f"**AI Clinical Briefing:**\n\n{appt['summary']}")