import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="centered")

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.btech = 70

# ---------- LOGIN ----------
if not st.session_state.login:
    st.title("🚀 BhavPath")
    st.subheader("What's Your Placement Story..??")

    full_name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
    branch = st.selectbox("Branch", ["Data Science", "CSE", "ECE", "IT", "Other"], placeholder="Ex: Data Science")
    college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
    btech = st.number_input("BTech Percentage %", min_value=0, max_value=100, value=70)

    if st.button("Submit & Get Access", use_container_width=True, type="primary"):
        if full_name and college:
            st.session_state.login = True
            st.session_state.name = full_name
            st.session_state.btech = btech
            st.rerun()
        else:
            st.error("Fill all details")

# ---------- MAIN ----------
else:
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
        st.subheader(f"💼 Interview Q&A With Answers")
        all_qs_ans = {
            "TCS NQT": [
                ("Tell me about yourself?","I'm Bhavya from Data Science, Rise Krishna Sai Group of Institutions. Strong in Python, SQL, DBMS. Did project on Student Management. Quick learner, looking to start career with TCS."),
                ("What is OOPs? 4 Pillars?","OOPs = Object Oriented Programming. 4 Pillars: 1) Encapsulation - wrapping data in class, 2) Abstraction - hiding complex details, 3) Inheritance - child inherits parent, 4) Polymorphism - many forms."),
                ("C vs Java?","C is procedural, manual memory, no OOPs. Java is OOPs, automatic GC, platform independent (JVM), secure."),
                ("What is SDLC?","Software Development Life Cycle. Phases: Requirement, Design, Coding, Testing, Deployment, Maintenance. Models: Waterfall, Agile."),
                ("Reverse a string Python?","s='bhavya' => s[::-1] gives 'ayvahb'. Also ''.join(reversed(s))."),
                ("What is DBMS?","DBMS is software to store/manage data. Eg MySQL. Features: ACID, avoids redundancy."),
                ("Primary vs Foreign Key?","Primary Key = unique+not null identifies row. Foreign Key = refers to PK of other table."),
                ("What is Normalization?","To remove redundancy. 1NF atomic, 2NF no partial dependency, 3NF no transitive dependency."),
                ("Stack vs Queue?","Stack LIFO push/pop Undo. Queue FIFO enqueue/dequeue Printer queue, BFS."),
                ("What is Recursion?","Function calling itself. Must have base case. Eg factorial n*fact(n-1). Without base -> stack overflow."),
                ("What is Inheritance?","Child gets parent properties. Types: Single, Multiple, Multilevel, Hierarchical."),
                ("What is Polymorphism?","Many forms. Overloading same name diff params. Overriding child changes parent method."),
                ("SQL Joins?","INNER common, LEFT all left + common, RIGHT all right + common, FULL all both, CROSS cartesian."),
                ("Exception Handling?","try: risky code, except: handle, finally: always runs."),
                ("Why TCS?","TCS No.1 IT company, great learning, job security, my Data Science skills match TCS Digital."),
            ],
            "Infosys": [
                ("DBMS & Normalization?","DBMS manages data. Normalization organizes tables to reduce redundancy using 1NF,2NF,3NF."),
                ("List vs Tuple vs Set?","List [1,2] mutable ordered duplicate allowed. Tuple (1,2) immutable ordered duplicate allowed. Set {1,2} mutable unordered no duplicate."),
                ("Python Decorator?","Adds extra functionality without modifying function. Uses @ symbol. Eg @login_required."),
                ("Exception Handling Python?","try/except/finally. try: a=10/0 except ZeroDivisionError: print Error"),
                ("What is OOPs?","Class blueprint, Object instance, Encapsulation wrapping, Abstraction hiding, Inheritance reusing, Polymorphism many forms."),
                ("Puzzle 3 Bulbs?","Switch1 ON 5 mins OFF, Switch2 ON, go to room. ON=Switch2, OFF HOT=Switch1, OFF COLD=Switch3."),
                ("What is SDLC?","Requirement, Design, Implementation, Testing, Deployment, Maintenance. Agile most used."),
                ("Agile Methodology?","Iterative development in sprints 2 weeks. Daily standup, planning, review, retrospective."),
                ("Cloud Computing?","Services over internet storage, servers. Pay as you use. AWS, Azure, GCP. IaaS, PaaS, SaaS."),
                ("Prime Number Program?","def is_prime(n): if n<2 return False; for i in range(2,int(n**0.5)+1): if n%i==0 return False; return True"),
                ("Constructor?","Special method __init__ called when object created. def __init__(self,name): self.name=name"),
                ("Abstract vs Interface?","Abstract 0-100% abstraction can have concrete methods. Interface 100% abstraction only abstract methods."),
                ("Indexing in SQL?","Index speeds up SELECT. Like book index. Clustered physical order, Non-clustered separate."),
                ("Tell about your project?","My project [Title] using Python/SQL. Problem [Problem]. Solution [Features]. Tech Python, MySQL."),
                ("Constructor Overloading?","Python no direct support, use default args: def __init__(self,a=None,b=None):"),
            ],
            "Wipro": [
                ("Stack vs Queue?","Stack LIFO undo, recursion. Queue FIFO BFS, printer queue."),
                ("SQL Joins?","INNER common, LEFT all left, RIGHT all right, FULL all both, CROSS cartesian."),
                ("Agile Scrum?","Agile philosophy, Scrum framework. Roles PO, Scrum Master, Team. Events Sprint, Standup, Review."),
                ("Why hire you?","Strong Python/SQL, projects, quick learner, good communication, adaptable."),
                ("What is OS?","OS interface between hardware and user. Manages CPU, memory, files. Eg Windows, Linux."),
                ("Process vs Thread?","Process independent program own memory. Thread lightweight shares memory."),
                ("Data Structure?","Way to store data efficiently. Linear Array, List, Stack, Queue. Non-linear Tree, Graph."),
                ("Linked List vs Array?","Array fixed size contiguous fast random access. Linked List dynamic fast insert/delete."),
                ("What is API?","Application Programming Interface allows two softwares to communicate. Eg Google Maps API. REST, JSON."),
                ("What is Git?","Version control tracks code changes. Commands init, add, commit, push, pull, branch, merge."),
                ("OOPs Concepts?","Class blueprint, Object instance, Encapsulation, Abstraction, Inheritance, Polymorphism."),
                ("Where 5 years?","See myself as skilled developer/tech lead in Wipro, learning AI/Cloud."),
                ("Final Year Project?","Explain Title, Objective, Tech stack, Architecture, Challenges, Outcome, Your role."),
            ],
            "Accenture": [
                ("Cloud Computing?","On-demand IT resources over internet. Benefits scalability, cost saving. AWS EC2, S3."),
                ("SDLC Models?","Waterfall sequential, Agile iterative, V-Model testing each phase, Spiral risk."),
                ("Pseudo-code Round?","Tests logic not syntax. Practice reverse string, prime, Fibonacci, palindrome, factorial."),
                ("Email Writing Test?","Formal: Subject clear, Greeting Dear Sir, Purpose first line, Body crisp, Regards."),
                ("What is Networking?","Connecting computers. IP, DNS, TCP/IP, HTTP, LAN/WAN, OSI 7 layers. TCP reliable, UDP fast."),
                ("AI vs ML?","AI machine mimics human. ML subset of AI learns from data. DL subset of ML."),
                ("Communication Test?","Tests spoken English, pronunciation. Speak slowly clearly confident."),
                ("What is DevOps?","Dev + Ops Development + Operations. Automates SDLC via CI/CD. Tools Git, Jenkins, Docker."),
                ("SQL Queries?","Practice SELECT, WHERE, GROUP BY, HAVING, ORDER BY, JOIN, Subquery, Window functions."),
                ("Aptitude Time & Work?","If A m days, B n days, together mn/(m+n). Practice Time-Speed-Distance."),
                ("Why Accenture?","Global leader consulting, innovation AI/Cloud, great learning, my Data Science fits."),
            ],
            "Capgemini": [
                ("Java vs Python?","Java compiled static typed verbose fast enterprise. Python interpreted dynamic simple best for AI/ML."),
                ("Inheritance Example?","class Animal: def sound(): print Sound; class Dog(Animal): def sound(): print Bark -> Dog inherits Animal."),
                ("SQL Injection?","Hacker injects malicious SQL via input. Eg ' OR '1'='1. Prevention parameterized queries."),
                ("Encapsulation?","Wrapping data + methods in class, hiding via private __var. Access via getter/setter."),
                ("Abstraction?","Hiding complex implementation showing only essential. Via abstract class/interface."),
                ("Fibonacci Series?","def fib(n): a,b=0,1; for i in range(n): print(a); a,b=b,a+b. Series 0,1,1,2,3,5,8..."),
                ("Testing?","Process to find bugs. Types Manual vs Automation, Unit, Integration, System, UAT."),
                ("Manual vs Automation?","Manual human tests good exploratory slow. Automation Selenium/Python fast reusable."),
                ("HTML/CSS?","HTML structure tags, CSS styling color layout. HTML skeleton CSS makeup."),
                ("Profit Loss Aptitude?","CP Cost Price, SP Selling Price. Profit=SP-CP Loss=CP-SP Profit%=Profit/CP*100."),
                ("Why Capgemini?","Leader tech services strong Cloud/Digital innovation great work-life."),
            ]
        }
        sel = st.selectbox("Company Select", list(all_qs_ans.keys()))
        need_map = {"TCS NQT":60, "Infosys":65, "Wipro":60, "Accenture":65, "Capgemini":60}
        need = need_map[sel]
        if st.session_state.btech >= need:
            st.success(f"✅ Eligible for {sel} (Need {need}%, You {st.session_state.btech}%)")
        else:
            st.error(f"❌ Not Eligible for {sel} (Need {need}%)")
        for i, (q, a) in enumerate(all_qs_ans[sel], 1):
            with st.container(border=True):
                st.markdown(f"**Q{i}. {q}**")
                with st.expander("👁️ To See Answer"):
                    st.info(a)
                st.text_area("Practice Your Answer", key=f"prac_{sel}_{i}", placeholder="Type your answer here...")

    with tab3:
        st.subheader("📝 Weekly Tests")
        weekly_bank = {
            "Week 1 - Aptitude": [
                ("A does work in 10 days, B in 15 days, together?", ["6 days","5 days","8 days"], 0),
                ("Profit 20% on 500?", ["100","120","80"], 0),
                ("15% of 200?", ["30","25","40"], 0),
                ("Ratio 2:3 sum 50?", ["20,30","10,40","25,25"], 0),
                ("Speed 60kmph, time 2hr, distance?", ["120km","100km","60km"], 0),
                ("SI 10% for 2y on 1000?", ["200","100","300"], 0),
                ("Average of 10,20,30?", ["20","25","15"], 0),
                ("2,4,8,16 next?", ["32","24","20"], 0),
                ("If SP=600 Profit 20% CP?", ["500","400","550"], 0),
                ("LCM of 4,6?", ["12","24","6"], 0),
                ("HCF of 12,18?", ["6","3","9"], 0),
                ("50% of 50% of 100?", ["25","50","20"], 0),
                ("A+B=10, A-B=2, A?", ["6","4","8"], 0),
                ("Triangle sum angles?", ["180","90","360"], 0),
                ("Area of square side 5?", ["25","20","10"], 0),
                ("If x=2, x^2+3?", ["7","5","8"], 0),
                ("10% discount on 1000?", ["900","800","950"], 0),
                ("2:5 = x:20, x?", ["8","10","6"], 0),
                ("Even number?", ["2","3","5"], 0),
                ("Probability of head?", ["0.5","1","0"], 0),
            ],
            "Week 2 - Python + SQL": [
                ("List is mutable?", ["Yes","No"], 0),
                ("Primary key allows null?", ["Yes","No"], 1),
                ("Tuple mutable?", ["Yes","No"], 1),
                ("SQL full form?", ["Structured Query Language","Simple Query","None"], 0),
                ("len([1,2,3])?", ["3","2","1"], 0),
                ("SELECT * FROM table is?", ["DQL","DDL","DML"], 0),
                ("Python used for?", ["Both AI & Web","Only Web","Only AI"], 0),
                ("DROP vs DELETE?", ["DROP deletes table, DELETE row","Same","Opposite"], 0),
                ("What is None in Python?", ["Null value","Zero","Empty"], 0),
                ("JOIN types count?", ["4 major","2","1"], 0),
                ("GROUP BY used with?", ["Aggregate","WHERE","ORDER"], 0),
                ("Python dict uses?", ["Key-Value","Only Value","Only Key"], 0),
                ("pip used for?", ["Install packages","Run code","Delete"], 0),
                ("SQL WHERE filters?", ["Rows","Columns","Table"], 0),
                ("is vs ==?", ["is checks identity, == value","Same","Opposite"], 0),
                ("List slicing [::-1]?", ["Reverse","Copy","Delete"], 0),
                ("VARCHAR vs CHAR?", ["VARCHAR variable length","Same","Opposite"], 0),
                ("Python loop?", ["for & while","only for","only while"], 0),
                ("UNIQUE key allows null?", ["Yes","No"], 0),
                ("print(type([]))?", ["list","array","tuple"], 0),
            ],
            "Week 3 - OOPs + DBMS": [
                ("How many pillars in OOPs?", ["4","3","5"], 0),
                ("Encapsulation means?", ["Wrapping data","Inheritance","Both"], 0),
                ("Inheritance example?", ["Child gets parent property","Opposite","None"], 0),
                ("Polymorphism means?", ["Many forms","One form","No form"], 0),
                ("Abstraction hides?", ["Complexity","Data","Nothing"], 0),
                ("DBMS full form?", ["Database Management System","Data...","None"], 0),
                ("Normalization removes?", ["Redundancy","Data","Table"], 0),
                ("1NF rule?", ["Atomic values","Non atomic","Both"], 0),
                ("Primary key?", ["Unique + Not Null","Null allowed","Both"], 0),
                ("Foreign key refers to?", ["Other table PK","Same table","None"], 0),
                ("Class vs Object?", ["Class blueprint, Object instance","Same","Opposite"], 0),
                ("Constructor called when?", ["Object creation","Deletion","Anytime"], 0),
                ("SQL Index speeds?", ["Retrieval","Insertion","Both"], 0),
                ("ACID properties?", ["Atomicity Consistency Isolation Durability","Only 2","Only 1"], 0),
                ("RDBMS example?", ["MySQL","MongoDB","Both"], 0),
                ("Method overloading?", ["Same name diff params","Diff name","Same everything"], 0),
                ("Method overriding?", ["Child changes parent method","Parent changes","None"], 0),
                ("What is Interface?", ["100% abstraction","0%","50%"], 0),
                ("What is Super key?", ["Superset of candidate key","Subset","None"], 0),
                ("Candidate key?", ["Minimal super key","Maximal","None"], 0),
            ],
            "Week 4 - Mock Placement": [
                ("Tell me about yourself should have?", ["Project + Skills + Strength","Only name","Only college"], 0),
                ("Why should we hire you?", ["Skills + Project + Attitude","Because I need job","Don't know"], 0),
                ("Where do you see yourself in 5 years?", ["Growth in company","No idea","Leave company"], 0),
                ("Strength?", ["Problem solving","Lazy","Angry"], 0),
                ("What is SDLC?", ["Software Development Life Cycle","System...","None"], 0),
                ("Agile is?", ["Iterative development","Waterfall","Both"], 0),
                ("Cloud Computing example?", ["AWS","MS Paint","Notepad"], 0),
                ("API full form?", ["Application Programming Interface","App...","None"], 0),
                ("Git used for?", ["Version control","Gaming","Browsing"], 0),
                ("What is AI?", ["Machine intelligence","Human","None"], 0),
                ("What is ML?", ["Subset of AI","Opposite","Same"], 0),
                ("Resume should be?", ["1-2 pages crisp","10 pages","No resume"], 0),
                ("Interview dress?", ["Formal","Casual","Anything"], 0),
                ("Eye contact?", ["Maintain confidence","Avoid","Stare"], 0),
                ("If you don't know answer?", ["Try logically + Accept","Lie","Silent"], 0),
                ("Teamwork means?", ["Collaboration","Work alone","Fight"], 0),
                ("Leadership?", ["Guide team","Order only","Do nothing"], 0),
                ("Why this company?", ["Skills match + Growth","No reason","Near home only"], 0),
                ("Expected CTC?", ["As per company norms","10 crores","1 rupee"], 0),
                ("Do you have questions for us?", ["Yes ask about growth/tech","No","Salary only"], 0),
            ]
        }
        week = st.selectbox("Select Week", list(weekly_bank.keys()))
        score = 0
        for i, (q, opts, corr) in enumerate(weekly_bank[week]):
            st.write(f"**Q{i+1}. {q}**")
            ans = st.radio("Select", opts, key=f"{week}_{i}", index=None)
            if ans and opts.index(ans) == corr:
                score += 1
        if st.button("Submit Test", type="primary", use_container_width=True):
            st.balloons()
            st.success(f"✅ Your Score: {score} / 20")
            if score >= 18:
                st.success("🔥 Outstanding Bhavya! Placement Ready!")
            elif score >= 15:
                st.info("💪 Good Job! Keep practicing!")
            else:
                st.warning("📚 Revise once more - You can do it!")
