import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="centered")

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.btech = 70

if not st.session_state.login:
    st.title("🚀 BhavPath")
    st.write("Your Placement Journey Starts Here!")

    full_name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
    branch = st.selectbox("Branch", ["Data Science", "CSE", "ECE", "IT", "Other"], placeholder="Ex: Data Science")
    college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
    btech = st.number_input("BTech Percentage %", 0, 100, 70)

    if st.button("Submit & Get Access", use_container_width=True, type="primary"):
        if full_name and college:
            st.session_state.login = True
            st.session_state.name = full_name
            st.session_state.btech = btech
            st.rerun()
        else:
            st.error("Fill details")

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
                    st.download_button("Download", f, file_name=pdf, key=pdf, use_container_width=True)

    with tab2:
        st.subheader(f"💼 Interview Q&A - BTech {st.session_state.btech}%")
        all_qs = {
            "TCS NQT": ["Tell me about yourself?","What is OOPs?","C vs Java?","SDLC?","Reverse string?","DBMS?","Primary vs Foreign key?","Normalization?","Stack vs Queue?","Recursion?","Inheritance?","Polymorphism?","SQL Joins?","Exception handling?","Why TCS?"],
            "Infosys": ["DBMS Normalization?","List vs Tuple?","Python decorator?","Exception handling?","OOPs?","3 bulbs puzzle?","SDLC?","Agile?","Cloud Computing?","Prime program?","Constructor?","Abstract vs Interface?","Indexing in SQL?","Your project?"],
        }
        sel = st.selectbox("Company", list(all_qs.keys()))
        for i,q in enumerate(all_qs[sel],1):
            with st.container(border=True):
                st.write(f"**Q{i}. {q}**")
                st.text_area("Your Answer", key=f"{sel}_{i}", placeholder="Type here...")

    with tab3:
        st.subheader("📝 Weekly Tests - Auto Changes Every Week (20 Qs)")

        # --- 20 QUESTIONS PER WEEK ---
        weekly_bank = {
            "Week 1 - Aptitude (20 Qs)": [
                ("If A does work in 10 days, B in 15, together?", ["6 days","5 days","8 days"], 0),
                ("Profit 20% on 500?", ["100","120","80"], 0),
                ("15% of 200?", ["30","25","40"], 0),
                ("Ratio 2:3 sum 50, numbers?", ["20,30","10,40","25,25"], 0),
                ("Speed 60kmph, time 2hr, distance?", ["120km","100km","60km"], 0),
                ("Simple Interest 10% for 2y on 1000?", ["200","100","300"], 0),
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
                ("Probability of head in coin?", ["0.5","1","0"], 0),
            ],
            "Week 2 - Python + SQL (20 Qs)": [
                ("List is mutable?", ["Yes","No"], 0),
                ("Primary key allows null?", ["Yes","No"], 1),
                ("Python tuple mutable?", ["Yes","No"], 1),
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
            "Week 3 - OOPs + DBMS (20 Qs)": [
                ("How many pillars OOPs?", ["4","3","5"], 0),
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
            "Week 4 - Mock Placement (20 Qs)": [
                ("Tell me about yourself should have?", ["Project + Skills + Strength","Only name","Only college"], 0),
                ("Why should we hire you?", ["Skills + Project + Attitude","Because I need job","Don't know"], 0),
                ("Where 5 years?", ["Growth in company","No idea","Leave company"], 0),
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
        st.info(f"📅 {week} - 20 Questions - Weekly maaruthundi!")

        score = 0
        answers = {}
        for i, (q, opts, correct) in enumerate(weekly_bank[week]):
            st.write(f"**Q{i+1}. {q}**")
            ans = st.radio(f"Select", opts, key=f"{week}_{i}", index=None)
            if ans is not None and opts.index(ans) == correct:
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
