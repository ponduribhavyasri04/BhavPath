import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

# TITLE - Nuvvu adigina design
st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#333;'>What is Your Placement Story..??</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Enter your details & Discover your journey</p>", unsafe_allow_html=True)

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT"], index=None, placeholder="Ex: Data Science")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")
btech_per = st.text_input("B.Tech Percentage / CGPA", placeholder="Ex: 78% or 8.2 CGPA")
skills = st.multiselect("Choose Your Skills", ["Python","C","C++","Java","Communication"], placeholder="Select skills")

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    st.success(f"🔥 {name} | Your Placement Story Started!")
    try:
        per_val = float(''.join(filter(lambda x: x.isdigit() or x=='.', btech_per))[:4])
        if per_val <=10: per_val*=9.5
    except: per_val=70
    if per_val>=60: st.write("✅ TCS Ninja, Infosys, Wipro")
    if per_val>=70: st.write("✅ Accenture, Cognizant, HCL")
    if per_val>=75: st.write("🔥 Amazon, Microsoft, Google")

st.markdown("---")
st.markdown("### Interview Questions")

company_qa = {
    "TCS Ninja": [("What is OOPs?", "4 pillars: Encapsulation, Abstraction, Inheritance, Polymorphism"),("Difference C vs Java?", "C procedural manual memory, Java OOPs auto GC"),("Reverse a string?", "Python s[::-1]"),("Tell me about yourself?", "Name College Branch Skills Project Why TCS")],
    "Infosys": [("List vs Tuple?", "List mutable [], Tuple immutable ()"),("What are Joins?", "INNER LEFT RIGHT FULL"),("Primary vs Foreign Key?", "Primary unique, Foreign references other table"),("3L 5L jug 4L?", "Fill 5L pour 3L leave 2L, empty 3L pour 2L, fill 5L pour 1L -> 4L")],
    "Amazon": [("Two Sum?", "HashMap O(n)"),("Reverse Linked List?", "prev None curr head logic"),("What is AWS?", "EC2 S3 RDS Lambda"),("LRU Cache?", "HashMap + Doubly LL O(1)"),("Leadership Principle?", "Ownership example with STAR")],
    "Wipro": [("Recursion?", "Function calling itself"),("OS Deadlock?", "4 conditions"),("TCP vs UDP?", "TCP reliable, UDP fast")],
    "Accenture": [("Agile Scrum?", "Sprint 2 weeks, Planning Daily Review Retro"),("Cloud?", "IaaS PaaS SaaS"),("OSI layers?", "7 layers P D N T S P A")],
    "Capgemini": [("2nd Highest Salary SQL?", "SELECT MAX WHERE sal < MAX"),("Stack vs Queue?", "Stack LIFO, Queue FIFO")]
}

selected = st.selectbox("Select Company", ["--Choose Company--"] + list(company_qa.keys()))
if selected!= "--Choose Company--":
    st.markdown(f"#### {selected} - Interview Questions")
    for q, a in company_qa[selected]:
        with st.expander(f"Q: {q}"):
            st.write(f"Ans: {a}")

st.markdown("---")
st.markdown("### Study Materials")
all_pdfs = sorted(list(set(glob.glob("*.pdf") + glob.glob("*.PDF"))))
st.write(f"Total Found: {len(all_pdfs)} PDFs")
for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 {fname}", f, file_name=fname, key=f"story_{i}", use_container_width=True)
