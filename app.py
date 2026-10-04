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
    st.sidebar.title("🔐 Admin Panel")
    admin_name = st.sidebar.text_input("Admin Name")
    admin_pass = st.sidebar.text_input("Password", type="password")
    if admin_name == "Bhavya Ponduri" and admin_pass == "1234Bhav":
        st.sidebar.success("Welcome Boss!")
        if os.path.exists("saved_answers.csv"):
            import pandas as pd
            df = pd.read_csv("saved_answers.csv")
            st.subheader(f"👁️ Saved Answers - {len(df)}")
            st.dataframe(df, use_container_width=True)
            with open("saved_answers.csv", "rb") as f:
                st.download_button("📥 Download", f, "Bhavya_Saved_Answers.csv", type="primary", use_container_width=True)

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
            "TCS NQT": [("Tell me about yourself?","I'm Bhavya from Data Science, Rise Krishna Sai Group of Institutions. Strong in Python, SQL, DBMS. Did project on Student Management."),("What is OOPs? 4 Pillars?","OOPs = Object Oriented Programming. 4 Pillars: Encapsulation, Abstraction, Inheritance, Polymorphism."),("C vs Java?","C procedural manual memory. Java OOPs automatic GC platform independent."),("What is SDLC?","Requirement, Design, Coding, Testing, Deployment, Maintenance."),("Reverse a string Python?","s[::-1]"),("What is DBMS?","Software to store/manage data MySQL."),("Primary vs Foreign Key?","PK unique not null, FK refers other table."),("What is Normalization?","Remove redundancy 1NF atomic 2NF 3NF."),("Stack vs Queue?","Stack LIFO Queue FIFO"),("What is Recursion?","Function calling itself base case needed."),("What is Inheritance?","Child gets parent properties."),("What is Polymorphism?","Many forms overloading overriding."),("SQL Joins?","INNER LEFT RIGHT FULL CROSS"),("Exception Handling?","try except finally"),("Why TCS?","No.1 IT company great learning")],
            "Infosys": [("DBMS & Normalization?","DBMS manages data Normalization reduces redundancy"),("List vs Tuple vs Set?","List mutable Tuple immutable Set unique"),("Python Decorator?","Adds extra functionality @ symbol"),("Exception Handling Python?","try/except/finally"),("What is OOPs?","Class Object Encapsulation Abstraction Inheritance Polymorphism"),("Puzzle 3 Bulbs?","Switch1 ON 5 mins OFF Switch2 ON"),("What is SDLC?","Requirement Design Implementation Testing Deployment"),("Agile Methodology?","Iterative sprints 2 weeks"),("Cloud Computing?","Services over internet AWS Azure GCP"),("Prime Number Program?","def is_prime(n): for i in range(2,int(n**0.5)+1)"),("Constructor?","__init__ called when object created"),("Abstract vs Interface?","Abstract 0-100% Interface 100%"),("Indexing in SQL?","Speeds up SELECT"),("Tell about your project?","My project using Python/SQL"),("Constructor Overloading?","Use default args")],
            "Wipro": [("Stack vs Queue?","Stack LIFO Queue FIFO"),("SQL Joins?","INNER LEFT RIGHT FULL"),("Agile Scrum?","PO Scrum Master Team Sprint Standup"),("Why hire you?","Python/SQL projects quick learner"),("What is OS?","Interface hardware user Windows Linux"),("Process vs Thread?","Process own memory Thread shares"),("Data Structure?","Store data efficiently Array List Stack Queue Tree Graph"),("Linked List vs Array?","Array fixed contiguous Linked dynamic"),("What is API?","Allows two softwares communicate REST JSON"),("What is Git?","Version control init add commit push pull"),("OOPs Concepts?","Class Object Encapsulation Abstraction Inheritance Polymorphism"),("Where 5 years?","Skilled developer tech lead"),("Final Year Project?","Title Objective Tech Architecture Challenges")],
            "Accenture": [("Cloud Computing?","On-demand IT AWS EC2 S3"),("SDLC Models?","Waterfall Agile V-Model Spiral"),("Pseudo-code Round?","Tests logic reverse string prime"),("Email Writing Test?","Subject clear Greeting Body Regards"),("What is Networking?","IP DNS TCP/IP HTTP LAN WAN"),("AI vs ML?","AI mimics human ML learns from data"),("Communication Test?","Spoken English pronunciation"),("What is DevOps?","Dev+Ops CI/CD Git Jenkins Docker"),("SQL Queries?","SELECT WHERE GROUP BY HAVING JOIN"),("Aptitude Time & Work?","mn/(m+n)"),("Why Accenture?","Global leader innovation AI Cloud")],
            "Capgemini": [("Java vs Python?","Java compiled verbose Python simple AI/ML"),("Inheritance Example?","class Dog(Animal):"),("SQL Injection?","Hacker injects ' OR '1'='1 prevention parameterized"),("Encapsulation?","Wrapping data methods private __var"),("Abstraction?","Hiding complex showing essential"),("Fibonacci Series?","0,1,1,2,3,5,8 a,b=b,a+b"),("Testing?","Find bugs Unit Integration System UAT"),("Manual vs Automation?","Manual human slow Automation Selenium fast"),("HTML/CSS?","HTML structure CSS styling"),("Profit Loss Aptitude?","CP SP Profit=SP-CP"),("Why Capgemini?","Leader Cloud Digital work-life")]
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
                def save_cb(q_text=q):
                    auto_save(st.session_state.name, sel, q_text, st.session_state.get(f"prac_{sel}_{q_text}", ""))
                st.text_area("Practice Your Answer (Auto Saves)", key=f"prac_{sel}_{q}", placeholder="Type here... auto saves", on_change=save_cb)
                if st.session_state.get(f"prac_{sel}_{q}", "").strip():
                    st.caption("✅ Auto Saved!")

    with tab3:
        st.subheader("📝 Weekly Tests")
        weekly_bank = {
            "Week 1 - Aptitude": [("A does work in 10 days, B in 15 days, together?", ["6 days","5 days","8 days"], 0),("Profit 20% on 500?", ["100","120","80"], 0),("15% of 200?", ["30","25","40"], 0),("Ratio 2:3 sum 50?", ["20,30","10,40","25,25"], 0),("Speed 60kmph, time 2hr, distance?", ["120km","100km","60km"], 0),("SI 10% for 2y on 1000?", ["200","100","300"], 0),("Average of 10,20,30?", ["20","25","15"], 0),("2,4,8,16 next?", ["32","24","20"], 0),("If SP=600 Profit 20% CP?", ["500","400","550"], 0),("LCM of 4,6?", ["12","24","6"], 0),("HCF of 12,18?", ["6","3","9"], 0),("50% of 50% of 100?", ["25","50","20"], 0),("A+B=10, A-B=2, A?", ["6","4","8"], 0),("Triangle sum angles?", ["180","90","360"], 0),("Area of square side 5?", ["25","20","10"], 0),("If x=2, x^2+3?", ["7","5","8"], 0),("10% discount on 1000?", ["900","800","950"], 0),("2:5 = x:20, x?", ["8","10","6"], 0),("Even number?", ["2","3","5"], 0),("Probability of head?", ["0.5","1","0"], 0)],
            "Week 2 - Python + SQL": [("List is mutable?", ["Yes","No"], 0),("Primary key allows null?", ["Yes","No"], 1),("Tuple mutable?", ["Yes","No"], 1),("SQL full form?", ["Structured Query Language","Simple Query","None"], 0),("len([1,2,3])?", ["3","2","1"], 0),("SELECT * FROM table is?", ["DQL","DDL","DML"], 0),("Python used for?", ["Both AI & Web","Only Web","Only AI"], 0),("DROP vs DELETE?", ["DROP deletes table, DELETE row","Same","Opposite"], 0),("What is None in Python?", ["Null value","Zero","Empty"], 0),("JOIN types count?", ["4 major","2","1"], 0),("GROUP BY used with?", ["Aggregate","WHERE","ORDER"], 0),("Python dict uses?", ["Key-Value","Only Value","Only Key"], 0),("pip used for?", ["Install packages","Run code","Delete"], 0),("SQL WHERE filters?", ["Rows","Columns","Table"], 0),("is vs ==?", ["is checks identity, == value","Same","Opposite"], 0),("List slicing [::-1]?", ["Reverse","Copy","Delete"], 0),("VARCHAR vs CHAR?", ["VARCHAR variable length","Same","Opposite"], 0),("Python loop?", ["for & while","only for","only while"], 0),("UNIQUE key allows null?", ["Yes","No"], 0),("print(type([]))?", ["list","array","tuple"], 0)],
            "Week 3 - OOPs + DBMS": [("How many pillars in OOPs?", ["4","3","5"], 0),("Encapsulation means?", ["Wrapping data","Inheritance","Both"], 0),("Inheritance example?", ["Child gets parent property","Opposite","None"], 0),("Polymorphism means?", ["Many forms","One form","No form"], 0),("Abstraction hides?", ["Complexity","Data","Nothing"], 0),("DBMS full form?", ["Database Management System","Data...","None"], 0),("Normalization removes?", ["Redundancy","Data","Table"], 0),("1NF rule?", ["Atomic values","Non atomic","Both"], 0),("Primary key?", ["Unique + Not Null","Null allowed","Both"], 0),("Foreign key refers to?", ["Other table PK","Same table","None"], 0),("Class vs Object?", ["Class blueprint, Object instance","Same","Opposite"], 0),("Constructor called when?", ["Object creation","Deletion","Anytime"], 0),("SQL Index speeds?", ["Retrieval","Insertion","Both"], 0),("ACID properties?", ["Atomicity Consistency Isolation Durability","Only 2","Only 1"], 0),("RDBMS example?", ["MySQL","MongoDB","Both"], 0),("Method overloading?", ["Same name diff params","Diff name","Same everything"], 0),("Method overriding?", ["Child changes parent method","Parent changes","None"], 0),("What is Interface?", ["100% abstraction","0%","50%"], 0),("What is Super key?", ["Superset of candidate key","Subset","None"], 0),("Candidate key?", ["Minimal super key","Maximal","None"], 0)],
            "Week 4 - Mock Placement": [("Tell me about yourself should have?", ["Project + Skills + Strength","Only name","Only college"], 0),("Why should we hire you?", ["Skills + Project + Attitude","Because I need job","Don't know"], 0),("Where do you see yourself in 5 years?", ["Growth in company","No idea","Leave company"], 0),("Strength?", ["Problem solving","Lazy","Angry"], 0),("What is SDLC?", ["Software Development Life Cycle","System...","None"], 0),("Agile is?", ["Iterative development","Waterfall","Both"], 0),("Cloud Computing example?", ["AWS","MS Paint","Notepad"], 0),("API full form?", ["Application Programming Interface","App...","None"], 0),("Git used for?", ["Version control","Gaming","Browsing"], 0),("What is AI?", ["Machine intelligence","Human","None"], 0),("What is ML?", ["Subset of AI","Opposite","Same"], 0),("Resume should be?", ["1-2 pages crisp","10 pages","No resume"], 0),("Interview dress?", ["Formal","Casual","Anything"], 0),("Eye contact?", ["Maintain confidence","Avoid","Stare"], 0),("If you don't know answer?", ["Try logically + Accept","Lie","Silent"], 0),("Teamwork means?", ["Collaboration","Work alone","Fight"], 0),("Leadership?", ["Guide team","Order only","Do nothing"], 0),("Why this company?", ["Skills match + Growth","No reason","Near home only"], 0),("Expected CTC?", ["As per company norms","10 crores","1 rupee"], 0),("Do you have questions for us?", ["Yes ask about growth/tech","No","Salary only"], 0)]
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
