import streamlit as st
import os, csv
from datetime import datetime

st.set_page_config(page_title="BhavPath", layout="centered")

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.btech = 70

if not os.path.exists("saved_answers.csv"):
    with open("saved_answers.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Name","Company","Question","MyAnswer","Time"])

def auto_save(name, company, question, answer):
    if answer.strip():
        with open("saved_answers.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, company, question, answer, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

if not st.session_state.login:
    st.title("🚀 BhavPath")
    st.subheader("What's Your Placement Story..??")
    full_name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
    branch = st.selectbox("Branch", ["Data Science", "CSE", "ECE", "IT", "Other"])
    college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
    btech = st.number_input("BTech Percentage %", 0, 100, 70)
    if st.button("Submit & Get Access", use_container_width=True, type="primary"):
        if full_name and college:
            st.session_state.login = True
            st.session_state.name = full_name
            st.session_state.btech = btech
            st.rerun()
        else:
            st.error("Fill all details")
else:
    # --- ONLY FOR ADMIN - HIDDEN ---
    qp = st.query_params.get("admin", "")
    if qp == "bhavya":
        st.sidebar.title("🔐 Admin Panel - Only You")
        admin_name = st.sidebar.text_input("Admin Name")
        admin_pass = st.sidebar.text_input("Password", type="password")
        if admin_name == "Bhavya Ponduri" and admin_pass == "1234Bhav":
            st.sidebar.success("Welcome Boss!")
            if os.path.exists("saved_answers.csv"):
                import pandas as pd
                df = pd.read_csv("saved_answers.csv")
                st.subheader(f"👁️ Saved Answers - {len(df)} - Only You See")
                st.dataframe(df, use_container_width=True)
                with open("saved_answers.csv", "rb") as f:
                    st.download_button("📥 Download All", f, "Bhavya_Saved_Answers.csv", type="primary", use_container_width=True)

    st.title(f"Welcome {st.session_state.name} 🎉")
    st.write(f"BTech: **{st.session_state.btech}%**")
    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()

    tab1, tab2, tab3 = st.tabs(["📚 Skilled Material", "💼 Interview Q&A", "📝 Weekly Tests"])
    with tab1:
        st.subheader("📚 Your 7 PDFs")
        pdfs = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
        for pdf in pdfs:
            with st.container(border=True):
                st.write(f"📄 {pdf}")
                with open(pdf, "rb") as f:
                    st.download_button("View / Download", f, file_name=pdf, key=pdf, use_container_width=True)

    with tab2:
        st.subheader("💼 Interview Q&A With Answers")
        all_qs_ans = {
            "TCS NQT": [("Tell me about yourself?","I'm Bhavya from Data Science..."),("What is OOPs? 4 Pillars?","OOPs = Object Oriented Programming...")],
            "Infosys": [("DBMS & Normalization?","DBMS manages data...")],
            "Wipro": [("Stack vs Queue?","Stack LIFO Queue FIFO")],
            "Accenture": [("Cloud Computing?","On-demand IT AWS")],
            "Capgemini": [("Java vs Python?","Java compiled...")]
        }
        sel = st.selectbox("Company Select", list(all_qs_ans.keys()))
        need_map = {"TCS NQT":60, "Infosys":65, "Wipro":60, "Accenture":65, "Capgemini":60}
        need = need_map[sel]
        if st.session_state.btech >= need:
            st.success(f"✅ Eligible for {sel}")
        else:
            st.error(f"❌ Not Eligible")
        for i, (q, a) in enumerate(all_qs_ans[sel], 1):
            with st.container(border=True):
                st.markdown(f"**Q{i}. {q}**")
                with st.expander("👁️ To See Answer"):
                    st.info(a)
                def save_cb(q_text=q):
                    auto_save(st.session_state.name, sel, q_text, st.session_state.get(f"prac_{sel}_{q_text}", ""))
                st.text_area("Practice Your Answer (Auto Saves)", key=f"prac_{sel}_{q}", placeholder="Type here... auto saves", on_change=save_cb)
                if st.session_state.get(f"prac_{sel}_{q}", "").strip():
                    st.caption("✅ Auto Saved!")

    with tab3:
        st.subheader("📝 Weekly Tests")
        st.write("Your tests here - same as before")
