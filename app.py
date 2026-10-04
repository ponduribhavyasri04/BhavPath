import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")
st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)

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
st.markdown("### 📦 MEGA Interview Questions Bank - 100+ Q&A")

company_qa = {
    "TCS Ninja (20 Q&A)": [
        ("What is OOPs? 4 Pillars?", "Encapsulation (data hiding), Abstraction (hide complexity), Inheritance (reuse), Polymorphism (many forms)"),
        ("Difference C vs Java?", "C procedural, manual memory, no OOPs. Java OOPs, auto GC, platform independent via JVM"),
        ("What is SDLC? Phases?", "Req Analysis -> Design -> Coding -> Testing -> Deployment -> Maintenance"),
        ("Reverse string program?", "Python: s[::-1], C: loop from end, Java: StringBuilder reverse()"),
        ("What is pointer?", "Variable storing address of another variable. * for value, & for address"),
        ("Array vs Linked List?", "Array fixed, contiguous. LL dynamic, non-contiguous, extra memory for pointer"),
        ("What is DBMS?", "Database Management System to store, retrieve, manage data. Ex: MySQL, Oracle"),
        ("Final year project explanation?", "Tell Title, Tech stack, Your role, Challenges, Outcome in 2 mins STAR format"),
        ("Are you willing to relocate/night shift?", "Yes, I am flexible and adaptable as per company needs and ready to learn"),
        ("What is inheritance? Types?", "Acquiring properties of parent. Types: Single, Multiple, Multilevel, Hierarchical, Hybrid"),
        ("What is polymorphism? Example?", "Same function different behavior. Compile-time (overloading), Runtime (overriding)"),
        ("Explain Agile?", "Iterative development, sprints 2-4 weeks, daily standups, customer feedback"),
        ("What is testing? Types?", "Manual, Automation. Unit, Integration, System, UAT. Black box, White box"),
        ("Palindrome program?", "Check if string == reverse. Python: s==s[::-1]"),
        ("Prime number logic?", "Check divisibility from 2 to sqrt(n). If no divisor -> prime"),
        ("Fibonacci series?", "0,1,1,2,3,5... next = sum of previous two. Use loop or recursion"),
        ("What is OS? Types?", "Manages hardware. Types: Batch, Time-sharing, Distributed, Real-time"),
        ("What is deadlock? How to avoid?", "2 processes waiting forever. Avoid by breaking any of 4 necessary conditions"),
        ("Tell me about yourself?", "Name, College, Branch, %, Skills, Projects, Internship, Strength, Why TCS"),
        ("Why should we hire you?", "I have required technical skills + communication + quick learner + adaptable")
    ],
    "Infosys (15 Q&A)": [
        ("List vs Tuple vs Set vs Dict?", "List mutable [], Tuple immutable (), Set unique {}, Dict key:value {}"),
        ("Explain Joins with example?", "INNER: common, LEFT: all left + common right, RIGHT opposite, FULL all"),
        ("Primary vs Foreign vs Unique key?", "Primary unique+not null, Foreign references primary of other table, Unique can be null but unique"),
        ("What is normalization?", "Reduce redundancy. 1NF atomic, 2NF no partial dependency, 3NF no transitive"),
        ("Python decorators?", "Function wrapping another function to extend behavior without modifying - @decorator"),
        ("What is exception handling?", "try, except, finally. To handle runtime errors gracefully"),
        ("Puzzle - 3L and 5L jug 4L?", "Fill 5L, pour to 3L -> 2L left in 5L, empty 3L, pour 2L to 3L, fill 5L, pour 1L to 3L -> 4L in 5L"),
        ("What is API?", "Application Programming Interface - way for 2 apps to communicate. REST, SOAP"),
        ("OOPs real life example?", "Car - Class, my Car - Object, Engine - Encapsulation, Different cars - Inheritance"),
        ("SQL 2nd highest salary?", "SELECT MAX(sal) FROM emp WHERE sal < (SELECT MAX(sal) FROM emp)"),
        ("What is indexing in DB?", "Speeds up retrieval. Creates data structure for fast search, but slows insert"),
        ("Swap 2 numbers without 3rd variable?", "a=a+b, b=a-b, a=a-b OR a,b=b,a in Python"),
        ("What is SDLC vs STLC?", "SDLC dev lifecycle, STLC testing lifecycle - planning, designing, execution, closure"),
        ("Explain your project challenges?", "Use STAR - what problem, how solved, what learned"),
        ("Where do you see yourself in 5 years?", "In a responsible role, leading team, expert in tech, contributing to Infosys growth")
    ],
    "Amazon SDE (25 Q&A) - TOP": [
        ("Two Sum - LeetCode 1", "HashMap O(n): dict={}; for i,num in enumerate: if target-num in dict: return"),
        ("Reverse Linked List", "Iterative: prev=None, curr=head, while curr: next=curr.next, curr.next=prev, prev=curr, curr=next"),
        ("LRU Cache Design", "HashMap + Doubly LL. O(1) get/put. Remove LRU when capacity full"),
        ("Valid Parentheses", "Use Stack: push opening, if closing check top matches, else false"),
        ("Merge Two Sorted Lists", "Dummy node, compare and attach smaller, move pointer"),
        ("What is AWS? Services?", "Amazon Web Services. EC2 compute, S3 storage, RDS database, Lambda serverless, VPC network"),
        ("EC2 vs S3 vs Lambda?", "EC2 server you manage, S3 file storage, Lambda run code without server"),
        ("What is System Design? URL shortener?", "Requirements, Capacity, API, DB design (base62), Scaling, Caching"),
        ("Explain CAP Theorem?", "Consistency, Availability, Partition Tolerance - can have only 2 of 3 in distributed system"),
        ("What is load balancer?", "Distributes traffic across servers. Types: ALB, NLB, Round robin, Least connections"),
        ("Leadership Principle - Ownership?", "Never say that's not my job. Take initiative, show example when you took responsibility beyond role"),
        ("Tell me time you failed?", "STAR: Project deadline missed due to underestimation, took ownership, fixed by extra hours, learned estimation"),
        ("What is microservices vs monolith?", "Monolith single codebase, Microservices small independent services communicating via API"),
        ("SQL vs NoSQL?", "SQL relational, structured, ACID. NoSQL non-relational, flexible, scalable - MongoDB, DynamoDB"),
        ("What is Docker? Kubernetes?", "Docker containerizes app + dependencies. K8s orchestrates containers - scaling, deployment"),
        ("Binary Search logic?", "Sorted array, low=0 high=n-1, mid=(low+high)//2, compare, adjust low/high. O(log n)"),
        ("What is BST?", "Binary Search Tree - left < root < right. Search O(log n) average, O(n) worst"),
        ("Explain OOPs with Amazon example?", "Order class, Payment inheritance, Encapsulation for price, Polymorphism for payment methods"),
        ("What is multithreading?", "Multiple threads in same process sharing memory. Need synchronization to avoid race condition"),
        ("Star pattern programs?", "Practice nested loops: *, triangle, pyramid, diamond patterns"),
        ("What is deadlock in DB?", "Two transactions waiting for lock. Solution: timeout, deadlock detection graph"),
        ("How to optimize slow query?", "Check EXPLAIN, add index, avoid SELECT *, optimize joins, caching"),
        ("Tell me time you disagreed with teammate?", "Show respect, data-driven discussion, focused on customer, agreed and committed"),
        ("Why Amazon?", "Customer obsession, innovation, leadership principles align with my ownership and learn & be curious"),
        ("Where do you see yourself?", "SDE 2, owning critical service, mentoring juniors, impacting millions of customers")
    ],
    "Wipro + Accenture + Others (40 Q&A)": [
        ("Cloud Computing types?", "IaaS (EC2), PaaS (Heroku), SaaS (Gmail). Public, Private, Hybrid"),
        ("What is Agile? Scrum?", "Iterative, Sprint 2 weeks, Roles: PO, Scrum Master, Team. Ceremonies: Planning, Daily, Review, Retro"),
        ("What is pseudo code?", "Informal description of program logic - no syntax, only logic for output questions"),
        ("Time & Work aptitude?", "If A does in x days, 1 day work =1/x. Together = 1/x+1/y. Practice formulas"),
        ("What is CN? OSI layers?", "7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application"),
        ("TCP vs UDP?", "TCP reliable, connection oriented, 3-way handshake. UDP fast, unreliable, no connection - video streaming"),
        ("What is HTTP vs HTTPS?", "HTTP port 80 plain text, HTTPS port 443 encrypted via SSL/TLS"),
        ("What is DNS?", "Domain Name System - converts domain name to IP - like phonebook"),
        ("C program - factorial recursion?", "int fact(int n){ if(n<=1) return 1; return n*fact(n-1);}"),
        ("Java String vs StringBuilder?", "String immutable, StringBuilder mutable faster for modifications"),
        ("What is final, finally, finalize?", "final constant/class can't inherit, finally block always executes, finalize GC method"),
        ("What is SQL injection?", "Security attack by injecting SQL via input. Prevent by prepared statements"),
        ("Aptitude - Profit Loss?", "CP cost, SP selling, Profit=SP-CP, % = Profit/CP*100"),
        ("Logical - Blood relation?", "Practice family tree, coded relations"),
        ("Communication - Essay tips?", "Intro, Body 3 points with examples, Conclusion. Use simple sentences, no grammar mistake"),
        ("Group Discussion tips?", "Initiate if confident, listen, give chance, add data points, summarize, don't dominate"),
        ("HR - Strength Weakness?", "Strength: quick learner, adaptable. Weakness: perfectionist but learning to prioritize (show improvement)"),
        ("Why our company?", "Mention company values, projects, learning opportunities, your skills align - be specific not generic"),
        ("What is data structure?", "Way to organize data - Array, LL, Stack, Queue, Tree, Graph, HashMap"),
        ("Stack vs Queue?", "Stack LIFO - push/pop. Queue FIFO - enqueue/dequeue. Stack: undo, Queue: scheduling"),
        # 20 more quick
        ("What is Big O?", "Time complexity - O(1), O(n), O(n^2), O(log n)"),
        ("What is AI vs ML vs DL?", "AI mimics human, ML learns from data, DL uses neural networks"),
        ("Python - lambda?", "Anonymous function: lambda x: x*2"),
        ("What is Git?", "Version control - git add, commit, push, pull, branch, merge"),
        ("What is SDLC models?", "Waterfall, Agile, Spiral, V-model, Iterative"),
        ("Test case vs Test scenario?", "Scenario what to test, Case how to test with steps, data, expected"),
        ("What is bug life cycle?", "New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed"),
        ("Difference Verification Validation?", "Verification are we building right product? Validation are we building product right?"),
        ("What is resume? Tips?", "1 page, Skills top, Projects with outcome, No spelling mistakes, ATS friendly"),
        ("Email writing format?", "Subject clear, Greeting, Purpose in 2 lines, Action needed, Thank you, Signature"),
        ("Explain Internet of Things?", "Devices connected via internet - sensors, data, automation. Ex: Smart home"),
        ("What is blockchain?", "Decentralized ledger, blocks chained via hash, immutable, used in crypto"),
        ("Aptitude - Speed Distance?", "Speed=Distance/Time, Convert kmph to m/s *5/18"),
        ("Number series - next?", "Practice patterns: difference, ratio, squares, primes, alternate"),
        ("Syllogism logic?", "All A are B, Some B are C conclusions - use Venn diagram"),
        ("What is 5G?", "5th gen mobile network - high speed, low latency, mmWave"),
        ("Latest tech - ChatGPT?", "LLM, Transformer architecture, trained on huge data, generative AI"),
        ("Group Task - Leadership?", "Show initiative, distribute work, motivate, take responsibility"),
        ("Salary negotiation?", "Don't ask early, research market, give range, focus on learning first"),
        ("Any questions for us?", "Always ask: Growth path, Tech stack, Team culture, Learning opportunities - never say no")
    ]
}

choice = st.selectbox("👉 Select Company Bank", ["--Choose--"] + list(company_qa.keys()))

if choice!= "--Choose--":
    st.markdown(f"### 🔥 {choice} - Full Q&A Bank")
    for idx, (q, a) in enumerate(company_qa[choice], 1):
        with st.expander(f"{idx}. Q: {q}"):
            st.success(f"Ans: {a}")

st.markdown("---")
st.markdown("### 📚 BhavPath Materials")
all_pdfs = sorted(list(set(glob.glob("*.pdf") + glob.glob("*.PDF"))))
st.write(f"Total Found: {len(all_pdfs)} PDFs")
for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 {fname}", f, file_name=fname, key=f"mega_{i}", use_container_width=True)
