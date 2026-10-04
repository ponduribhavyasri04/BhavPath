import streamlit as st
import os, glob, csv
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

# ===== TITLE =====
st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#333;'>What is Your Placement Story..??</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Enter details & Build your DNA</p>", unsafe_allow_html=True)
st.markdown("---")

# ===== INPUTS =====
name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT"], index=None, placeholder="Choose Branch")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")
btech_per = st.text_input("B.Tech Percentage / CGPA", placeholder="Ex: 78% or 8.2 CGPA")
skills = st.multiselect("Choose Your Skills", ["Python","C","C++","Java","DSA","SQL","Communication","Aptitude"], placeholder="Select skills")

CSV_FILE = "bhavpath_leads.csv"

# ===== GENERATE + SAVE =====
if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    if not name or not btech_per:
        st.warning("Please enter Name & Percentage!")
    else:
        # SAVE TO YOUR DATABASE (CSV)
        file_exists = os.path.isfile(CSV_FILE)
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            if not file_exists:
                w.writerow(["Timestamp","Name","Branch","College","Percentage","Skills"])
            w.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, branch, college, btech_per, ", ".join(skills)])

        st.balloons()
        st.success(f"🔥 {name} | Your Placement Story Started! Saved!")
        try:
            per_val = float(''.join(filter(lambda x: x.isdigit() or x=='.', btech_per))[:4])
            if per_val <= 10: per_val *= 9.5
        except: per_val = 70

        st.markdown("### 🎯 Eligible Companies")
        if per_val >= 60:
            st.write("✅ TCS Ninja, Infosys, Wipro, Tech Mahindra")
        if per_val >= 70:
            st.write("✅ Accenture, Cognizant, HCL, IBM")
        if per_val >= 75:
            st.write("🔥 Amazon, Microsoft, Google - Product Based")

# ===== INTERVIEW QUESTIONS BOX =====
st.markdown("---")
st.markdown("### Interview Questions")

company_qa = {
    "TCS Ninja": [
        ("What is OOPs?", "4 pillars: Encapsulation (data hiding), Abstraction (hide complexity), Inheritance (reuse), Polymorphism (many forms)"),
        ("Difference C vs Java?", "C procedural, manual memory, no OOPs. Java OOPs, auto GC, platform independent via JVM"),
        ("What is SDLC?", "Req Analysis -> Design -> Coding -> Testing -> Deployment -> Maintenance"),
        ("Reverse a string?", "Python: s[::-1], C: loop from end"),
        ("What is pointer?", "Variable storing address of another variable. * for value, & for address"),
        ("Array vs Linked List?", "Array fixed contiguous, LL dynamic non-contiguous extra pointer"),
        ("What is DBMS?", "Database Management System to store data - MySQL, Oracle"),
        ("Explain your project?", "Title, Tech stack, Your role, Challenges, Outcome - 2 mins STAR"),
        ("Ready to relocate?", "Yes flexible as per company needs, excited to learn new environment"),
        ("Inheritance types?", "Single, Multiple, Multilevel, Hierarchical, Hybrid"),
        ("Polymorphism example?", "Same function different behavior - overloading compile-time, overriding runtime"),
        ("Agile methodology?", "Iterative, sprints 2-4 weeks, daily standup, customer feedback"),
        ("Palindrome program?", "Check s == s[::-1]"),
        ("What is OS?", "Manages hardware - Batch, Time-sharing, Distributed, Real-time"),
        ("Deadlock?", "2 processes waiting forever - 4 conditions: Mutual exclusion, Hold&wait, No preemption, Circular wait"),
        ("Tell me about yourself?", "Name, College, Branch, %, Skills, Projects, Internship, Strength, Why TCS"),
        ("Why hire you?", "Required technical skills + communication + quick learner + adaptable")
    ],
    "Infosys": [
        ("List vs Tuple vs Set vs Dict?", "List mutable [], Tuple immutable () faster, Set unique {}, Dict key:value {}"),
        ("What are Joins?", "INNER common only, LEFT all left + common right, RIGHT opposite, FULL all"),
        ("Primary vs Foreign Key?", "Primary unique+not null identifies row, Foreign links to primary of another table"),
        ("Normalization?", "Reduce redundancy. 1NF atomic, 2NF no partial dependency, 3NF no transitive"),
        ("Python decorators?", "Function wrapping another to extend behavior without modifying - @decorator"),
        ("Exception handling?", "try, except, finally - handle runtime errors gracefully"),
        ("3L 5L jug puzzle 4L?", "Fill 5L pour to 3L -> 2L left in 5L, empty 3L, pour 2L to 3L, fill 5L pour 1L -> 4L in 5L"),
        ("What is API?", "Application Programming Interface - 2 apps communicate via REST, SOAP"),
        ("SQL 2nd highest salary?", "SELECT MAX(sal) FROM emp WHERE sal < (SELECT MAX(sal) FROM emp)"),
        ("Indexing in DB?", "Speeds up retrieval with data structure, but slows insert/update"),
        ("Swap without 3rd variable?", "a,b = b,a in Python OR a=a+b, b=a-b, a=a-b"),
        ("SDLC vs STLC?", "SDLC dev lifecycle, STLC testing lifecycle"),
        ("5 years goal?", "Responsible role, leading team, expert, contributing to Infosys growth")
    ],
    "Amazon": [
        ("Two Sum problem?", "Use HashMap O(n): dict={}; if target-num in dict return"),
        ("Reverse Linked List?", "prev=None, curr=head, while curr: next=curr.next, curr.next=prev, prev=curr, curr=next"),
        ("LRU Cache Design?", "HashMap + Doubly Linked List O(1) get/put, remove LRU when full"),
        ("Valid Parentheses?", "Use Stack: push opening, if closing check top matches else false"),
        ("What is AWS?", "Amazon Web Services - EC2 compute, S3 storage, RDS DB, Lambda serverless, VPC"),
        ("EC2 vs S3 vs Lambda?", "EC2 virtual server you manage, S3 file storage, Lambda run code without server"),
        ("System Design URL shortener?", "Req, Capacity, API, DB base62, Scaling, Caching"),
        ("CAP Theorem?", "Consistency, Availability, Partition Tolerance - can have only 2 of 3"),
        ("Load balancer?", "Distributes traffic across servers - Round robin, Least connections"),
        ("Ownership LP?", "Never say not my job - show example you took responsibility beyond role"),
        ("Time you failed?", "STAR: Situation Task Action Result - show learning and ownership"),
        ("Microservices vs Monolith?", "Monolith single codebase, Microservices small independent services via API"),
        ("SQL vs NoSQL?", "SQL relational ACID structured, NoSQL non-relational flexible scalable"),
        ("Docker & Kubernetes?", "Docker containerizes app+dependencies, K8s orchestrates containers"),
        ("Binary Search?", "Sorted array, low=0 high=n-1 mid=(low+high)//2 compare adjust O(log n)"),
        ("Why Amazon?", "Customer obsession, innovation, leadership principles align with my values"),
        ("Any questions for us?", "Ask growth path, tech stack, team culture - never say no")
    ],
    "Wipro": [
        ("Recursion example?", "Function calling itself with base condition - factorial"),
        ("Array vs Linked List?", "Array fixed contiguous, LL dynamic non-contiguous extra pointer memory"),
        ("OS Deadlock?", "Mutual exclusion, Hold&wait, No preemption, Circular wait"),
        ("Prime number?", "Check divisibility 2 to sqrt(n)"),
        ("Fibonacci?", "0,1,1,2,3,5 next = sum of previous two"),
        ("What is Cloud?", "On-demand IT resources IaaS PaaS SaaS - AWS Azure"),
        ("TCP vs UDP?", "TCP reliable connection oriented 3-way handshake, UDP fast unreliable video streaming"),
        ("HTTP vs HTTPS?", "HTTP 80 plain, HTTPS 443 encrypted SSL/TLS"),
        ("String vs StringBuilder?", "String immutable, Builder mutable faster for modifications"),
        ("Testing types?", "Unit, Integration, System, UAT - Manual, Automation")
    ],
    "Accenture": [
        ("Cloud Computing?", "On-demand delivery IaaS EC2, PaaS Heroku, SaaS Gmail - Public Private Hybrid"),
        ("Agile Scrum?", "Sprint 2 weeks, Roles PO Scrum Master Team, Ceremonies Planning Daily Review Retro"),
        ("Pseudo code?", "Informal logic description - no syntax only output practice"),
        ("OSI layers?", "Physical, Data Link, Network, Transport, Session, Presentation, Application"),
        ("What is DNS?", "Domain Name System converts domain to IP like phonebook"),
        ("Git commands?", "add, commit, push, pull, branch, merge"),
        ("Big O?", "Time complexity O(1), O(n), O(n^2), O(log n)"),
        ("AI ML DL?", "AI mimics human, ML learns from data, DL neural networks")
    ],
    "Capgemini": [
        ("2nd Highest Salary SQL?", "SELECT MAX(salary) WHERE salary < (SELECT MAX(salary) FROM emp)"),
        ("Inheritance?", "Acquiring properties of parent - Single Multiple Multilevel"),
        ("Stack vs Queue?", "Stack LIFO push/pop undo, Queue FIFO enqueue/dequeue scheduling"),
        ("Group Discussion tips?", "Initiate if confident, listen, give chance, add data, summarize"),
        ("Aptitude Time & Work?", "1 day work = 1/x, together = 1/x+1/y")
    ]
}

selected = st.selectbox("Select Company", ["--Choose Company--"] + list(company_qa.keys()))

if selected!= "--Choose Company--":
    st.markdown(f"#### {selected} - Interview Questions")
    for q, a in company_qa[selected]:
        with st.expander(f"Q: {q}"):
            st.success(f"Ans: {a}")

# ===== PDFs =====
st.markdown("---")
st.markdown("### Study Materials")
all_pdfs = sorted(list(set(glob.glob("*.pdf") + glob.glob("*.PDF"))))
st.write(f"Total Found: {len(all_pdfs)} PDFs")
for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 {fname}", f, file_name=fname, key=f"all_{i}", use_container_width=True)

# ===== SECRET ADMIN - ONLY YOU =====
# Students ki kanipinchadu! Nuvvu?admin=bhavya add chesthe ne vastundi
query_params = st.query_params
is_admin = query_params.get("admin") == "Bhavya Ponduri"

if is_admin:
    st.markdown("---")
    st.markdown("## 🔐 Bhavya's Private Dashboard - Only You Can See")
    pwd = st.text_input("Enter Secret Password", type="password", placeholder="Enter password")
    if pwd == "1234Bhav":
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            st.success(f"Total Leads Collected: {len(df)}")
            st.dataframe(df, use_container_width=True)
            with open(CSV_FILE, "rb") as f:
                st.download_button("📥 Download All Leads CSV", f, file_name="bhavpath_leads.csv", type="primary", use_container_width=True)
        else:
            st.info("No leads yet - Students not entered")
    elif pwd:
        st.error("Wrong password!")
