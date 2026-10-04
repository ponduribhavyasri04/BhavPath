import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="centered")

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.btech = 70

if not st.session_state.login:
    st.title("🚀 BhavPath")
    st.write("Your Placement Journey Starts Here!")
    full_name = st.text_input("Full Name")
    branch = st.selectbox("Branch", ["Data Science", "CSE", "ECE", "IT", "Other"])
    college = st.text_input("College Name")
    phone = st.text_input("Phone Number")
    btech = st.number_input("BTech Percentage %", 0, 100, 70)
    if st.button("Submit & Get Access", use_container_width=True, type="primary"):
        if full_name and college and phone:
            st.session_state.login = True
            st.session_state.name = full_name
            st.session_state.btech = btech
            st.rerun()
        else:
            st.error("Fill all details")
else:
    st.title(f"Welcome {st.session_state.name} 🎉")
    if st.button("Logout"):
        st.session_state.login=False
        st.rerun()

    tab1, tab2, tab3 = st.tabs(["📚 Skilled Material", "💼 Interview Q&A", "📝 Weekly Tests"])

    with tab1:
        st.subheader("📚 Your 7 PDFs")
        pdfs = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
        for pdf in pdfs:
            with st.container(border=True):
                st.write(f"📄 {pdf}")
                with open(pdf,"rb") as f:
                    st.download_button("View / Download", f, file_name=pdf, key=pdf, use_container_width=True)

    with tab2:
        st.subheader(f"💼 Interview Questions - Your BTech {st.session_state.btech}%")

        all_qs = {
            "TCS NQT": ["Tell me about yourself?","What is OOPs? 4 pillars?","Difference C vs Java?","What is SDLC?","Reverse a string in Python?","What is DBMS?","Primary key vs Foreign key?","What is Normalization?","Stack vs Queue?","What is Recursion?","Explain Inheritance?","What is Polymorphism?","SQL Joins types?","What is Exception handling?","Why TCS?"],
            "Infosys": ["DBMS & Normalization?","List vs Tuple vs Set?","What is Python decorator?","Exception handling in Python?","What is OOPs?","Puzzle: 3 bulbs 3 switches?","What is SDLC?","Agile methodology?","What is Cloud Computing?","Write prime number program?","What is Constructor?","Abstract class vs Interface?","What is indexing in SQL?","Tell me about your project?"],
            "Wipro": ["Stack vs Queue?","SQL Joins?","Agile & Scrum?","Why should we hire you?","What is OS?","Process vs Thread?","What is Data Structure?","Linked List vs Array?","What is API?","What is Git?","OOPs concepts?","Where do you see yourself in 5 years?","Explain your final year project?"],
            "Accenture": ["What is Cloud Computing?","SDLC Models?","Pseudo-code round?","Email writing test?","What is Networking?","What is AI vs ML?","What is SDLC?","Communication test?","What is DevOps?","SQL queries?","Aptitude: Time & Work?","Why Accenture?"],
            "Capgemini": ["Java vs Python?","Inheritance example?","SQL Injection?","What is Encapsulation?","What is Abstraction?","Write Fibonacci series?","What is Testing?","Manual vs Automation?","What is HTML/CSS?","Aptitude: Profit Loss?","Why Capgemini?"]
        }

        sel = st.selectbox("Company Select", list(all_qs.keys()))
        btech_need = {"TCS NQT":60, "Infosys":65, "Wipro":60, "Accenture":65, "Capgemini":60}
        need = btech_need[sel]
        if st.session_state.btech >= need:
            st.success(f"✅ Eligible for {sel} (Need {need}%, You have {st.session_state.btech}%)")
        else:
            st.error(f"❌ Not Eligible for {sel} (Need {need}%)")

        for i,q in enumerate(all_qs[sel],1):
            with st.container(border=True):
                st.write(f"**Q{i}. {q}**")
                st.text_area("Your Answer", key=f"{sel}_{i}", placeholder="Type your answer here...")

    with tab3:
        st.subheader("📝 Weekly Tests - Every Sunday New Test")
        week = st.selectbox("Select Week", ["Week 1 - Aptitude", "Week 2 - Python + SQL", "Week 3 - OOPs + DBMS", "Week 4 - Mock Interview"])

        tests = {
            "Week 1 - Aptitude": [{"q":"If A can do work in 10 days, B in 15 days, together?","o":["6 days","5 days","8 days"],"a":0},{"q":"Profit 20% on 500?","o":["100","120","80"],"a":0}],
            "Week 2 - Python + SQL": [{"q":"List is mutable?","o":["Yes","No"],"a":0},{"q":"Primary key allows null?","o":["Yes","No"],"a":1}],
            "Week 3 - OOPs + DBMS": [{"q":"How many pillars in OOPs?","o":["4","3","5"],"a":0}],
            "Week 4 - Mock Interview": [{"q":"Tell me about yourself - Good answer includes?","o":["Project + Skills","Only name","Only college"],"a":0}]
        }

        score=0
        for i, t in enumerate(tests[week]):
            st.write(f"**Q{i+1}. {t['q']}**")
            ans = st.radio("Select", t['o'], key=f"test_{week}_{i}", index=None)
            if ans == t['o'][t['a']]:
                score+=1

        if st.button("Submit Test", type="primary", use_container_width=True):
            st.balloons()
            st.success(f"Your Score: {score}/{len(tests[week])}")
            if score == len(tests[week]):
                st.success("🔥 Excellent Bhavya! Full marks!")
