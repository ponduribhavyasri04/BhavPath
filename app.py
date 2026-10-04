import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

# NUVVU ADIGINA TITLE
st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#333;'>What is Your Placement Story..??</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Enter your details & build your placement journey</p>", unsafe_allow_html=True)
st.markdown("---")

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT"], index=None, placeholder="Ex: Data Science")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")
btech_per = st.text_input("B.Tech Percentage / CGPA", placeholder="Ex: 78% or 8.2 CGPA")
skills = st.multiselect("Choose Your Skills", ["Python","C","C++","Java","Communication"], placeholder="Select skills")

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    st.success(f"🔥 {name} | {branch} | {btech_per} - DNA Generated!")
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
    "TCS Ninja": [
        ("What is OOPs?", "4 pillars: Encapsulation, Abstraction, Inheritance, Polymorphism"),
        ("Difference C vs Java?", "C procedural, manual memory. Java OOPs, auto GC, platform independent"),
        ("What is SDLC?", "Requirement, Design, Coding, Testing, Deployment, Maintenance"),
        ("Reverse a string?", "Python s[::-1], C loop from end"),
        ("What is pointer?", "Variable storing address. * value, & address"),
        ("Array vs Linked List?", "Array fixed contiguous, LL dynamic non-contiguous"),
        ("What is DBMS?", "Database Management System - MySQL, Oracle"),
        ("Explain your project?", "Title, Tech stack, Role, Challenges, Outcome - 2 mins"),
        ("Ready to relocate?", "Yes, flexible as per company needs"),
        ("What is inheritance?", "Acquiring parent properties. Single, Multiple, Multilevel etc"),
        ("Polymorphism example?", "Same function different behavior - overloading, overriding"),
        ("Agile methodology?", "Iterative, sprints 2-4 weeks, daily standup"),
        ("Palindrome program?", "Check s == s[::-1]"),
        ("What is OS?", "Manages hardware - Batch, Time-sharing, Distributed"),
        ("Deadlock?", "2 processes waiting forever - 4 conditions"),
        ("Tell me about yourself?", "Name, College, Branch, Skills, Project, Why TCS"),
        ("Why hire you?", "Required skills + quick learner + adaptable")
    ],
    "Infosys": [
        ("List vs Tuple?", "List mutable [], Tuple immutable () faster"),
        ("What are Joins?", "INNER common, LEFT all left, RIGHT all right, FULL all"),
        ("Primary vs Foreign Key?", "Primary unique identifier, Foreign links to other table primary"),
        ("What is normalization?", "Reduce redundancy - 1NF atomic, 2NF, 3NF"),
        ("Python decorators?", "Wrapping function to extend behavior - @decorator"),
        ("Exception handling?", "try, except, finally to handle errors gracefully"),
        ("3L 5L jug puzzle 4L?", "Fill 5L pour to 3L leave 2L, empty 3L, pour 2L to 3L, fill 5L pour 1L -> 4L left"),
        ("What is API?", "Interface for 2 apps to communicate - REST, SOAP"),
        ("SQL 2nd highest salary?", "SELECT MAX(sal) WHERE sal < (SELECT MAX(sal) FROM emp)"),
        ("What is indexing?", "Speeds retrieval, slows insert"),
        ("Swap without 3rd var?", "a,b=b,a in Python"),
        ("SDLC vs STLC?", "SDLC development, STLC testing lifecycle"),
        ("5 years goal?", "Responsible role, expert, contributing to Infosys growth")
    ],
    "Amazon": [
        ("Two Sum problem?", "Use HashMap O(n) - check target-num in dict"),
        ("Reverse Linked List?", "prev=None, curr=head, next=curr.next, curr.next=prev, prev=curr, curr=next"),
        ("LRU Cache?", "HashMap + Doubly LL O(1) get/put"),
        ("Valid Parentheses?", "Stack - push opening, check closing matches"),
        ("What is AWS?", "EC2 compute, S3 storage, RDS DB, Lambda serverless"),
        ("EC2 vs S3 vs Lambda?", "EC2 virtual server, S3 file storage, Lambda run code without server"),
        ("System Design - URL shortener?", "Base62 encoding, DB, caching, scaling"),
        ("CAP Theorem?", "Consistency, Availability, Partition - only 2 possible"),
        ("Load balancer?", "Distributes traffic - Round robin, Least connections"),
        ("Ownership principle?", "Never say not my job - show example you took extra responsibility"),
        ("Time you failed?", "STAR - Situation Task Action Result - show learning"),
        ("Microservices vs Monolith?", "Monolith single, Microservices independent services via API"),
        ("SQL vs NoSQL?", "SQL relational ACID, NoSQL flexible scalable MongoDB"),
        ("Docker Kubernetes?", "Docker containerizes, K8s orchestrates containers"),
        ("Binary Search?", "Sorted array, mid compare, adjust low/high O(log n)"),
        ("Multithreading?", "Multiple threads sharing memory - need synchronization"),
        ("Why Amazon?", "Customer obsession, innovation aligns with my values"),
        ("Any question?", "Ask growth path, tech stack, team culture")
    ],
    "Wipro": [
        ("Recursion example?", "Function calling itself with base condition - factorial"),
        ("Array vs Linked List?", "Array fixed, LL dynamic extra pointer memory"),
        ("What is OS Deadlock?", "Mutual exclusion, Hold wait, No preemption, Circular wait"),
        ("Prime number program?", "Check divisibility 2 to sqrt(n)"),
        ("Fibonacci?", "0,1,1,2,3,5 sum of previous two"),
        ("What is Cloud?", "IaaS, PaaS, SaaS - AWS, Azure"),
        ("TCP vs UDP?", "TCP reliable handshake, UDP fast unreliable"),
        ("HTTP vs HTTPS?", "HTTP 80 plain, HTTPS 443 encrypted SSL"),
        ("Java String vs StringBuilder?", "String immutable, Builder mutable faster"),
        ("Final finally finalize?", "final constant, finally always executes, finalize GC"),
        ("Testing types?", "Unit, Integration, System, UAT - Manual, Automation")
    ],
    "Accenture": [
        ("Cloud Computing?", "On-demand IT resources - IaaS PaaS SaaS"),
        ("Agile Scrum?", "Sprint 2 weeks, PO, Scrum Master, Planning Daily Review Retro"),
        ("Pseudo code output?", "Practice loops, conditions, operators"),
        ("CN OSI layers?", "Physical, Data Link, Network, Transport, Session, Presentation, Application"),
        ("What is DNS?", "Converts domain to IP - phonebook"),
        ("Git commands?", "add, commit, push, pull, branch, merge"),
        ("Big O?", "Time complexity O(1), O(n), O(n2), O(log n)"),
        ("AI ML DL?", "AI mimics human, ML learns data, DL neural networks")
    ],
    "Capgemini": [
        ("2nd Highest Salary SQL?", "SELECT MAX(salary) WHERE salary < (SELECT MAX(salary))"),
        ("Inheritance types?", "Single, Multiple, Multilevel, Hierarchical, Hybrid"),
        ("Aptitude Time Work?", "1 day work = 1/x, together = 1/x+1/y"),
        ("Stack vs Queue?", "Stack LIFO push/pop, Queue FIFO enqueue/dequeue"),
        ("Group Discussion tips?", "Initiate, listen, give chance, add data, summarize")
    ]
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
