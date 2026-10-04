import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="wide")
st.title("🚀 BhavPath - Your Career Path")

tab1, tab2, tab3 = st.tabs(["🏠 Home", "📚 Skilled Material", "💼 Interview Questions"])

with tab1:
    st.header("Welcome to BhavPath!")
    st.success("✅ 7 Skilled Materials | ✅ Company Questions | ✅ BTech % Checker")

with tab2:
    st.header("📚 Skilled Materials")
    pdf_folder = "materials"
    root_pdfs = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
    folder_pdfs = []
    if os.path.exists(pdf_folder):
        folder_pdfs = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]
    all_pdfs = root_pdfs + folder_pdfs
    if all_pdfs:
        st.success(f"✅ {len(all_pdfs)} PDFs Found!")
        for pdf in all_pdfs:
            path = pdf if pdf in root_pdfs else os.path.join(pdf_folder, pdf)
            if os.path.exists(path):
                with open(path, "rb") as f:
                    st.download_button(f"📄 {pdf}", f, file_name=pdf, key=pdf)

with tab3:
    st.header("💼 Company-wise Interview Questions")

    companies = {
        "TCS NQT": {"10th": 60, "12th": 60, "btech": 60, "cgpa": 6.0, "backlog": "No active", "questions": ["Tell me about yourself?", "What is OOPs?", "Difference C vs Java?", "SDLC models?", "Reverse string program"]},
        "Infosys": {"10th": 60, "12th": 60, "btech": 65, "cgpa": 6.5, "backlog": "No active", "questions": ["What is DBMS & Normalization?", "List vs Tuple?", "Exception handling?", "Puzzle: 3 bulbs"]},
        "Wipro": {"10th": 60, "12th": 60, "btech": 60, "cgpa": 6.0, "backlog": "No active", "questions": ["Stack vs Queue?", "SQL Joins?", "Agile & Scrum?", "Why hire you?"]},
        "Accenture": {"10th": 65, "12th": 65, "btech": 65, "cgpa": 6.5, "backlog": "No active", "questions": ["Cloud Computing?", "SE models?", "Pseudo-code?", "Email writing"]},
        "Capgemini": {"10th": 60, "12th": 60, "btech": 60, "cgpa": 6.0, "backlog": "No active", "questions": ["Java vs Python?", "Inheritance example", "SQL Injection?"]},
    }

    sub1, sub2 = st.tabs(["📋 Company Questions", "🎯 Check My Eligibility (BTech %)"])

    with sub1:
        selected = st.selectbox("Select Company", list(companies.keys()))
        data = companies[selected]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("✅ Eligibility Criteria")
            st.write(f"**10th:** {data['10th']}%")
            st.write(f"**12th:** {data['12th']}%")
            st.write(f"**BTech %:** {data['btech']}%")
            st.write(f"**CGPA:** {data['cgpa']}")
            st.write(f"**Backlogs:** {data['backlog']}")
        with col2:
            st.subheader("🎯 Practice Questions")
            for i, q in enumerate(data["questions"], 1):
                st.write(f"**{i}.** {q}")

    with sub2:
        st.subheader("🎯 Enter Your Percentages")
        c1, c2, c3 = st.columns(3)
        with c1: tenth = st.number_input("10th %", 0, 100, 75)
        with c2: twelfth = st.number_input("12th %", 0, 100, 75)
        with c3: btech = st.number_input("BTech %", 0, 100, 70)
        cgpa = st.number_input("CGPA (out of 10)", 0.0, 10.0, 7.0)
        backlog = st.selectbox("Backlogs?", ["No active", "1 active", "2+ active"])

        if st.button("Check Eligible Companies"):
            eligible = []
            for comp, req in companies.items():
                if tenth >= req["10th"] and twelfth >= req["12th"] and btech >= req["btech"] and cgpa >= req["cgpa"]:
                    if backlog == "No active" or req["backlog"]!= "No active":
                        eligible.append(comp)
            if eligible:
                st.success(f"🎉 You are eligible for {len(eligible)} companies!")
                for c in eligible: st.write(f"✅ {c}")
            else:
                st.error("😔 No companies matched, improve BTech %!")
