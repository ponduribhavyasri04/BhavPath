import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="centered")

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.btech = 70

# ---------- LOGIN PAGE (Nee Photo lo unna Same Page) ----------
if not st.session_state.login:
    st.title("🚀 BhavPath")
    st.write("Your Placement Journey Starts Here!")
    
    full_name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
    branch = st.selectbox("Branch", ["Data Science", "CSE", "ECE", "IT", "Other"])
    college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
    phone = st.text_input("Phone Number", placeholder="Ex: 9876543210")
    # KOTHA ADDED - BTECH %
    btech = st.number_input("BTech Percentage %", min_value=0, max_value=100, value=70)

    if st.button("Submit & Get Access", use_container_width=True):
        if full_name and college and phone:
            st.session_state.login = True
            st.session_state.name = full_name
            st.session_state.btech = btech
            st.rerun()
        else:
            st.error("Fill all details")

# ---------- AFTER SUBMIT ----------
else:
    st.title(f"Welcome {st.session_state.name} 🎉")
    st.write(f"Your BTech: **{st.session_state.btech}%**")
    
    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()

    tab1, tab2 = st.tabs(["📚 Skilled Material", "💼 Interview Questions"])

    with tab1:
        st.subheader("📚 Your 7 PDFs")
        pdfs = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
        if pdfs:
            for pdf in pdfs:
                with st.container(border=True):
                    st.write(f"📄 {pdf}")
                    with open(pdf, "rb") as f:
                        st.download_button("View / Download", f, file_name=pdf, key=f"pdf_{pdf}", use_container_width=True)
        else:
            st.error("PDFs kanipinchaledu - GitHub lo root lo pettu")

    with tab2:
        st.subheader("💼 Company Eligibility + Questions")
        
        b = st.session_state.btech
        st.info(f"Nee BTech {b}% tho eligible companies:")

        companies = {
            "TCS NQT": 60,
            "Wipro": 60,
            "Capgemini": 60,
            "Infosys": 65,
            "Accenture": 65,
        }
        
        for comp, need in companies.items():
            if b >= need:
                st.success(f"✅ {comp} - Eligible (Need {need}%)")
            else:
                st.error(f"❌ {comp} - Not Eligible (Need {need}%, You have {b}%)")

        st.divider()
        st.subheader("Interview Questions")
        comp_sel = st.selectbox("Company Select chey", ["TCS NQT", "Infosys", "Wipro", "Accenture", "Capgemini"])
        
        qs = {
            "TCS NQT": ["Tell me about yourself?", "What is OOPs?", "C vs Java?", "SDLC?", "Reverse a string?"],
            "Infosys": ["DBMS? Normalization?", "List vs Tuple?", "Exception handling?", "3 bulbs puzzle"],
            "Wipro": ["Stack vs Queue?", "SQL Joins?", "Agile? Scrum?", "Why hire you?"],
            "Accenture": ["Cloud Computing?", "SE Models?", "Pseudo code?", "Email writing"],
            "Capgemini": ["Java vs Python?", "Inheritance?", "SQL Injection?"]
        }
        for i, q in enumerate(qs[comp_sel], 1):
            st.write(f"{i}. {q}")
         
