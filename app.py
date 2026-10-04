import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="wide")
st.title("🚀 BhavPath")
st.write("Your Placement Journey Starts Here!")

# Session to keep login
if "logged" not in st.session_state:
    st.session_state.logged = False

# --- 1. LOGIN FORM (Nee Old Screen) ---
if not st.session_state.logged:
    st.subheader("Student Details")
    full_name = st.text_input("Full Name", value="bhavya ponduri")
    branch = st.selectbox("Branch", ["Data Science", "CSE", "ECE", "IT", "Other"])
    college = st.text_input("College Name", value="Rise")
    phone = st.text_input("Phone Number", value="987654321")
    btech_per = st.number_input("BTech Percentage %", 0, 100, 70, help="Idi kotta add chesa Bhavya!")

    if st.button("Submit & Get Access", use_container_width=True, type="primary"):
        if full_name and college and phone:
            st.session_state.logged = True
            st.session_state.name = full_name
            st.session_state.btech = btech_per
            st.rerun()
        else:
            st.error("Fill all details")

# --- 2. AFTER LOGIN - MAIN APP ---
else:
    st.success(f"Welcome {st.session_state.name}! BTech: {st.session_state.btech}%")
    if st.button("Logout"):
        st.session_state.logged = False
        st.rerun()

    tab1, tab2 = st.tabs(["📚 Skilled Material", "💼 Interview Questions"])

    with tab1:
        st.header("📚 Your Skilled Materials - 7 PDFs")
        pdfs = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
        if pdfs:
            for pdf in pdfs:
                with st.container(border=True):
                    col1, col2 = st.columns([3,1])
                    col1.write(f"📄 **{pdf}**")
                    with open(pdf, "rb") as f:
                        col2.download_button("View / Download", f, file_name=pdf, key=pdf, use_container_width=True)
        else:
            st.warning("PDFs not found in GitHub root")

    with tab2:
        st.header("💼 Company-wise Interview Questions")

        companies = {
            "TCS NQT": {"btech": 60, "cgpa": 6.0, "qs": ["Tell me about yourself?", "What is OOPs? 4 pillars?", "C vs Java?", "What is SDLC?", "Reverse string program"]},
            "Infosys": {"btech": 65, "cgpa": 6.5, "qs": ["What is DBMS? Normalization?", "List vs Tuple?", "Exception handling?", "Puzzle: 3 bulbs"]},
            "Wipro": {"btech": 60, "cgpa": 6.0, "qs": ["Stack vs Queue?", "SQL Joins?", "Agile & Scrum?", "Why hire you?"]},
            "Accenture": {"btech": 65, "cgpa": 6.5, "qs": ["What is Cloud Computing?", "SE Models?", "Pseudo-code?", "Email writing"]},
            "Capgemini": {"btech": 60, "cgpa": 6.0, "qs": ["Java vs Python?", "Inheritance example?", "SQL Injection?"]}
        }

        # Auto check with entered BTech %
        my_btech = st.session_state.btech
        st.info(f"Your BTech % = {my_btech}% - Check eligible companies below")

        eligible = [c for c, d in companies.items() if my_btech >= d["btech"]]
        st.success(f"✅ You are eligible for: {', '.join(eligible) if eligible else 'None - Improve %'}")

        st.divider()
        selected = st.selectbox("Select Company for Questions", list(companies.keys()))
        data = companies[selected]
        st.write(f"**Eligibility for {selected}:** BTech {data['btech']}%+, CGPA {data['cgpa']}")
        st.write(f"**Your Status:** {'✅ Eligible' if my_btech >= data['btech'] else '❌ Not Eligible'}")
        st.subheader("Practice Questions:")
        for i, q in enumerate(data["qs"], 1):
            st.write(f"{i}. {q}")
