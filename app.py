import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT"], index=None, placeholder="Ex: Data Science")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")
btech_per = st.text_input("B.Tech Percentage / CGPA", placeholder="Ex: 78% or 8.2 CGPA")
skills = st.multiselect("Choose Your Skills", ["Python","C","C++","Java","Communication","Aptitude","DSA","SQL","Other"], placeholder="Select skills")

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    st.success(f"🔥 {name} | {branch} | {btech_per}")
    try:
        per_val = float(''.join(filter(lambda x: x.isdigit() or x=='.', btech_per))[:4])
        if per_val <=10: per_val*=9.5
    except: per_val=70
    st.markdown("### 🎯 Eligible Companies")
    if per_val>=60: st.write("✅ TCS Ninja, Infosys, Wipro")
    if per_val>=70: st.write("✅ Accenture, Cognizant, HCL")
    if per_val>=75: st.write("🔥 Amazon, Microsoft, Google")

# INTERVIEW QUESTIONS - EPPUDU KANIPISTAYI - Generate tho sambandam ledu
st.markdown("---")
st.markdown("### 💼 Company Wise Interview Questions - Practice")

with st.expander("🔹 TCS Ninja - Interview Questions"):
    st.write("1. What is OOPs? 4 pillars\n2. Difference C vs Java?\n3. SDLC?\n4. Reverse a string program\n5. Final year project?")
with st.expander("🔹 Infosys - Interview Questions"):
    st.write("1. Python list vs tuple\n2. DBMS joins?\n3. Primary vs Foreign key?\n4. 3L 5L jug puzzle")
with st.expander("🔹 Wipro - Interview Questions"):
    st.write("1. Recursion example\n2. Array vs Linked list\n3. OS Deadlock\n4. Prime number in C")
with st.expander("🔹 Accenture"):
    st.write("1. Cloud computing?\n2. Agile methodology\n3. Pseudo code\n4. Networking basics")
with st.expander("🔹 Amazon SDE"):
    st.write("1. DSA: Two sum, LRU Cache\n2. AWS EC2 vs S3\n3. Leadership principles\n4. System Design")
with st.expander("🔹 Capgemini / Cognizant"):
    st.write("1. Aptitude: Time & Work\n2. Pseudo code output\n3. Inheritance?\n4. SQL - 2nd highest salary")

st.markdown("---")
st.markdown("### 📚 BhavPath Materials")
all_pdfs = sorted(list(set(glob.glob("*.pdf") + glob.glob("*.PDF"))))
st.write(f"Total Found: {len(all_pdfs)} PDFs")
for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 {fname}", f, file_name=fname, key=f"fix_{i}", use_container_width=True)
