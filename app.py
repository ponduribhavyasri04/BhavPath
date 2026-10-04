import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")
st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT"], index=None, placeholder="Ex: Data Science")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")
btech_per = st.text_input("B.Tech Percentage / CGPA", placeholder="Ex: 78% or 8.2 CGPA")
skills = st.multiselect("Choose Your Skills", ["Python","C","C++","Java","Communication","Aptitude","DSA","SQL","Other"], placeholder="Select skills - Ex: Python, C")

eligible = []

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    try:
        per_val = float(''.join(filter(lambda x: x.isdigit() or x=='.', btech_per))[:4])
        if per_val <=10: per_val*=9.5
    except: per_val=70
    
    st.success(f"🔥 {name} | {branch} | {btech_per} - DNA Generated!")
    st.markdown("### 🎯 Eligible Companies")
    if per_val>=60:
        st.write("✅ TCS Ninja, Infosys, Wipro, Tech Mahindra")
        eligible = ["TCS Ninja","Infosys","Wipro","Accenture","Amazon","Capgemini"]
    if per_val>=70:
        st.write("✅ + Accenture, Cognizant, HCL, IBM")
    if per_val>=75:
        st.write("🔥 + Amazon, Microsoft, Google")
    
    st.session_state['eligible'] = eligible
    st.session_state['generated'] = True

# --- SEPARATE INTERVIEW QUESTION BOX ---
st.markdown("---")
st.markdown("### 📦 Interview Questions Box")
st.info("Click below to practice with Answers!")

company_qa = {
    "TCS Ninja": [
        ("What is OOPs?", "OOPs has 4 pillars: Encapsulation, Inheritance, Polymorphism, Abstraction. It organizes code around objects."),
        ("Reverse a string in Python?", "s[::-1] or using loop. Ex: `''.join(reversed(s))`"),
        ("What is SDLC?", "Software Development Life Cycle - Requirement, Design, Coding, Testing, Deployment, Maintenance."),
        ("Ready to relocate?", "Yes, I'm open to relocate as per company requirements and excited to work in new environment.")
    ],
    "Infosys": [
        ("List vs Tuple in Python?", "List is mutable [], Tuple immutable (). List slower, Tuple faster and can be dict key."),
        ("What are Joins in DBMS?", "INNER, LEFT, RIGHT, FULL. Used to combine rows from 2+ tables."),
        ("Primary vs Foreign Key?", "Primary uniquely identifies row, Foreign links to primary of another table.")
    ],
    "Wipro": [
        ("What is recursion?", "Function calling itself. Needs base condition. Ex: factorial."),
        ("Array vs Linked List?", "Array contiguous memory, fixed size. LL non-contiguous, dynamic, extra pointer memory."),
        ("What is Deadlock?", "When 2 processes wait for each other indefinitely. 4 conditions: Mutual exclusion, Hold & wait, No preemption, Circular wait.")
    ],
    "Accenture": [
        ("What is Cloud Computing?", "On-demand delivery of IT resources over internet - AWS, Azure. Types: IaaS, PaaS, SaaS."),
        ("Agile vs Waterfall?", "Agile iterative, flexible, sprints. Waterfall sequential, fixed stages."),
        ("Pseudo code - find output?", "Practice: loops, conditions, operator precedence.")
    ],
    "Amazon": [
        ("Two Sum Problem?", "Use HashMap: for i, num in enumerate(nums): if target-num in map -> return. O(n)"),
        ("What is AWS EC2 vs S3?", "EC2 is virtual server (compute), S3 is storage for objects/files."),
        ("Tell me a time you failed - LP?", "Use STAR: Situation, Task, Action, Result. Show learning and ownership."),
        ("What is LRU Cache?", "Least Recently Used - O(1) get/put using HashMap + Doubly Linked List.")
    ],
    "Capgemini": [
        ("2nd Highest Salary SQL?", "SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp)"),
        ("What is Inheritance?", "One class acquiring properties of another. Types: Single, Multiple, Multilevel.")
    ]
}

# Box lekkalo - Dropdown
selected_company = st.selectbox("👉 Select Company to Practice", ["--Choose Company--"] + list(company_qa.keys()))

if selected_company != "--Choose Company--":
    st.markdown(f"#### 🔥 {selected_company} - Questions with Answers")
    for q, a in company_qa[selected_company]:
        with st.expander(f"Q: {q}"):
            st.write(f"**Ans:** {a}")

st.markdown("---")
st.markdown("### 📚 BhavPath Materials")
all_pdfs = sorted(list(set(glob.glob("*.pdf") + glob.glob("*.PDF"))))
st.write(f"Total Found: {len(all_pdfs)} PDFs")
for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 {fname}", f, file_name=fname, key=f"box_{i}", use_container_width=True)
