import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image, ImageDraw
import io

def make_pdf_bytes(title, sections, watermark="From BhavPath - Bhavya Ponduri"):
    W, H = 850, 1150
    pages = []
    def new_page(pn):
        img = Image.new("RGB", (W, H), "#0F0F0F")
        d = ImageDraw.Draw(img)
        d.rectangle([(0,0),(W,85)], fill="#6C5CE7")
        d.text((40, 20), "B H A V P A T H", fill="white")
        d.text((W-40, 20), "BOUTIQUE EDITION", fill="#FFEAA7", anchor="ra")
        d.text((40, 105), title, fill="white")
        d.line([(40, 140), (810, 140)], fill="#6C5CE7", width=3)
        # UBQUE WATERMARK
        d.text((W//2, H//2), watermark, fill="#1A1A1A", anchor="mm")
        d.text((W//2, H//2-30), "BOUTIQUE • UBIQUE", fill="#1F1F1F", anchor="mm")
        d.rectangle([(0,H-55),(W,H)], fill="#1A1A1A")
        d.text((40, H-35), f"{watermark} | Page {pn} | UBIQUE DESIGN", fill="#6C5CE7")
        return img, d, 165
    pn=1
    img, d, y = new_page(pn)
    for head, lines in sections:
        if y>850:
            pages.append(img); pn+=1; img,d,y=new_page(pn)
        d.rectangle([(30,y-4),(820,y+26)], fill="#FFEAA7")
        d.text((45,y), head.upper(), fill="#0F0F0F")
        y+=38
        for line in lines:
            if y>970:
                pages.append(img); pn+=1; img,d,y=new_page(pn)
            d.ellipse([(45,y+8),(55,y+18)], fill="#6C5CE7")
            d.text((68,y), line, fill="#E0E0E0")
            y+=26
        y+=12
    pages.append(img)
    buf=io.BytesIO()
    pages[0].save(buf, format="PDF", save_all=True, append_images=pages[1:] if len(pages)>1 else [])
    return buf.getvalue()

st.set_page_config(page_title="BhavPath • Ubique by Bhavya Ponduri", page_icon="💎", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@300;400&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background: #0a0a0a; }
h1, h2 { font-family: 'Syne', sans-serif; }
.main { background: #0a0a0a!important; }
div[data-testid="stForm"] {
  background: rgba(255,255,255,0.05)!important;
  border: 1px solid rgba(255,255,255,0.1)!important;
  border-radius: 40px!important;
  padding: 35px!important;
  backdrop-filter: blur(20px);
  box-shadow: 0 0 80px rgba(108,92,231,0.15);
}
.stTextInput>div>div>input,.stSelectbox>div>div>div {
  background: rgba(255,255,255,0.07)!important;
  color: white!important;
  border-radius: 15px!important;
  border: 1px solid rgba(255,255,255,0.1)!important;
}
.stButton>button {
  background: linear-gradient(90deg, #6C5CE7 0%, #FF7675 100%)!important;
  color: white!important;
  border-radius: 50px!important;
  padding: 15px 40px!important;
  font-family: 'Syne'!important;
  font-weight: 800!important;
  letter-spacing: 1px;
  border: none!important;
  box-shadow: 0 10px 30px rgba(108,92,231,0.4);
}
.stSlider,.stMultiSelect label,.stRadio label { color: #dfe6e9!important; }
</style>
""", unsafe_allow_html=True)

# --- UBIQUE HEADER ---
st.markdown("""
<div style="text-align:center; padding: 30px 20px 10px 20px;">
<p style="color:#6C5CE7; letter-spacing:8px; font-size:12px; margin-bottom:10px;">BOUTIQUE • ELITE • UBIQUE</p>
<h1 style="font-size: 68px; color: white; margin:0; letter-spacing:-3px; line-height:0.9;">BhavPath</h1>
<h2 style="font-size: 38px; background: linear-gradient(90deg, #6C5CE7, #FF7675); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top:10px; font-weight:800;">What's your placement story?</h2>
<p style="color:#636e72; font-size:14px; margin-top:15px; letter-spacing:1px;">An ubique placement atelier by <span style="color:white; font-weight:700;">Bhavya Ponduri</span> • Not a portal, it's a vibe</p>
<div style="margin-top:25px;">
<span style="border:1px solid rgba(255,255,255,0.2); color:rgba(255,255,255,0.6); padding:8px 18px; border-radius:30px; font-size:11px; margin:5px;">✦ EST. 2026 ONGOLE</span>
<span style="border:1px solid rgba(255,255,255,0.2); color:rgba(255,255,255,0.6); padding:8px 18px; border-radius:30px; font-size:11px; margin:5px;">✦ 50-POINT VAULT</span>
<span style="border:1px solid rgba(255,255,255,0.2); color:rgba(255,255,255,0.6); padding:8px 18px; border-radius:30px; font-size:11px; margin:5px;">✦ UBIQUE DESIGN</span>
</div>
</div>
""", unsafe_allow_html=True)

l,c,r = st.columns([1,2.3,1])
with c:
    with st.form("ubique_form"):
        st.markdown("<h3 style='color:white; text-align:center;'>Tell your story, darling</h3>", unsafe_allow_html=True)
        name = st.text_input("Full Name", value="Bhavya Ponduri")
        col1,col2 = st.columns(2)
        with col1:
            btech = st.slider("B.Tech %", 40,100,75)
            branch = st.selectbox("Branch", ["CSE","IT","ECE","EEE","AI/ML","Others"])
        with col2:
            backlogs = st.selectbox("Backlogs", [0,1,2,"2+"])
            year = st.selectbox("Grad Year", [2024,2025,2026,2027])
        skills = st.multiselect("Stack", ["Python","Java","C","SQL","DSA","OOPS","DBMS","CN","OS","Aptitude","Communication"], default=["Python","SQL"])
        comm = st.slider("Communication 1-10", 1,10,7)
        goal = st.radio("Dream House", ["TCS","Infosys","Wipro","Accenture","Product"], horizontal=True)
        btn = st.form_submit_button("✦ CREATE MY UBIQUE STORY ✦")

if btn:
    new_data = {"Time":str(datetime.now()), "Name":name, "Branch":branch, "BTech":btech, "Backlogs":backlogs, "Skills":", ".join(skills), "Year":year, "Goal":goal, "Score":int(btech*0.5+len(skills)*6+comm*3)}
    df_new = pd.DataFrame([new_data])
    if os.path.exists("bhavpath_users.csv"):
        pd.concat([pd.read_csv("bhavpath_users.csv"), df_new]).to_csv("bhavpath_users.csv", index=False)
    else:
        df_new.to_csv("bhavpath_users.csv", index=False)
    if "all_users" not in st.session_state: st.session_state.all_users=[]
    st.session_state.all_users.append(new_data)

    st.markdown(f"<div style='text-align:center; padding:20px; background:rgba(108,92,231,0.1); border-radius:20px; border:1px solid #6C5CE7;'><h3 style='color:white;'>Welcome to the atelier, {name} ✨</h3><p style='color:#dfe6e9;'>Vibe Score: {new_data['Score']}/100 • Story Saved as Bhavya Ponduri Example</p></div>", unsafe_allow_html=True)
    st.balloons()

    t1,t2 = st.tabs(["🏢 ELIGIBILITY • UBIQUE CHECK", "💎 50-POINT BOUTIQUE VAULT"])
    with t1:
        st.markdown(f"<h4 style='color:white;'>Real talk for {name}</h4>", unsafe_allow_html=True)
        has_coding = any(s in skills for s in ["Python","Java","C"])
        has_sql = "SQL" in skills
        a,b = st.columns(2)
        with a:
            if btech>=60 and str(backlogs) in ["0","1"] and has_coding: st.success("TCS NQT + Digital: IN • UBIQUE")
            else: st.error("TCS: Need 60% + Code")
            if btech>=60 and str(backlogs)=="0" and has_sql: st.success("Infosys SP: You are THAT girl!")
            else: st.warning("Infosys: Need SQL + 0 backlogs")
        with b:
            if btech>=60: st.success("Wipro & Cognizant: Green flag")
            if btech>=65 and comm>=6: st.success("Accenture: Ate & left no crumbs")

    with t2:
        py = [f"{i}. {c}" for i,c in enumerate(["What is Python?","print()","input()","Variables","Data Types","Type Cast","Operators","If else","Elif","For loop","While","Break Continue","List mutable","Tuple immutable","Dict","Set","Functions def","Return","args kwargs","Lambda","Map Filter","List Comp","String methods","File handling","Try Except","Modules","Class Object","__init__","Inheritance","Polymorphism","Encapsulation","Decorators","Generators","Recursion","Sorting","Searching","Big O","LeetCode","Example name='Bhavya Ponduri'","Example print(name)","Project Calculator","ToDo","DSA in Python","Time Comp","Space Comp","Final Tip","Motivation","Bonus","Watermark","Ubique"],1)]
        dsa = [f"{i}. {c}" for i,c in enumerate(["What is DSA?","Array","Linked List","Stack LIFO","Queue FIFO","HashMap O(1)","Big O","Sorting","Bubble","Selection","Insertion","Merge O(n log n)","Quick","Binary Search O(log n)","Linear","Recursion","Two Pointers","Sliding Window","Prefix Sum","Binary Tree","BST","Traversal","Graph BFS DFS","Heap","Greedy","DP","Memoization","Tabulation","Backtracking","String DSA","Palindrome","Anagram","List vs Tuple","Stack Example","Queue Example","HashMap Example","LeetCode 1-10","11-20","21-30","31-40","41-50","FAANG","Reverse String","Prime","LRU Cache","System Design","Final","Motivation","Bonus","Ubique"],1)]
        sql = [f"{i}. {c}" for i,c in enumerate(["What is SQL?","DBMS vs RDBMS","SELECT *","WHERE","AND OR","ORDER BY","GROUP BY","HAVING","COUNT SUM AVG","DISTINCT","LIMIT","LIKE %","IN","BETWEEN","NULL","INNER JOIN","LEFT JOIN","RIGHT JOIN","FULL JOIN","SELF JOIN","UNION","Subquery","2nd Highest","Nth Highest","Duplicate","DELETE vs TRUNCATE","Primary Key","Foreign Key","Index","View","Procedure","Trigger","ACID","COMMIT ROLLBACK","Normalization","Example WHERE Name='Bhavya Ponduri'","Emp Table","Dept Table","Joins Q","Rank Q","ROW_NUMBER","RANK vs DENSE_RANK","CASE WHEN","Date Func","String Func","Practice 50 Qs","Motivation","Bonus","Watermark","Ubique"],1)]
        tcs = [f"{i}. {c}" for i,c in enumerate(["Pattern Apt 20Q Email 1Q Coding 1Q","Time 90 mins","Work & Time","Percentages","Profit Loss","Speed Distance","Permutation","Blood Relation","Coding Decoding","Synonyms","Email Format","Email Apologize","Reverse String","Prime Check","Armstrong","Palindrome","Fibonacci","PYQ 2023 Q1","PYQ 2023 Q2","PYQ 2024 Q1","PYQ 2024 Q2","Digital LeetCode Medium","OOPS","DBMS","CN & OS","Cutoff 60%","Backlog Max 1","Interview I am Bhavya Ponduri","Why TCS?","HR Qs","Tech Python","Tech Java","Salary 3.36 NQT 7 Digital","Prep Day 1-5","Day 6-10","Day 11-20","Day 21-25","Day 26-30","FacePrep","Prepinsta","Email scoring","Code must run","No negative","Bhavya Ponduri Selected","Checklist","Motivation","Watermark","Bonus","Ubique"],1)]
        infy = [f"{i}. {c}" for i,c in enumerate(["Pattern Apt 10 Reason 10 Tech 40","Eligibility 60% 0 backlogs","SP 5 LPA SE 3.6","Cryptarithmetic","Time & Work","Puzzles","Syllogism","OOPS 4 pillars","Inheritance","Polymorphism","Normalization","ACID","2nd highest MUST","Joins","Group By Having","List vs Tuple","Dict vs Set","String vs StringBuilder","OSI Model","Deadlock","Paging","PYQ 2023 Inheritance","PYQ 2023 SQL","PYQ 2024 DBMS","PYQ 2024 OOPS","Project BhavPath by Bhavya Ponduri","Why Infosys?","Tech 30 mins","String reverse","Array rotation","Cutoff High","Focus Tech 50%","Day 1-10","Day 11-25","Day 26-30","Previous papers","Tech is key","Comms matters","Salary Growth","Bond 1 year","Select Bhavya Ponduri","Mysore Training","50 Qs List","Motivation","Watermark","System Design","Cloud intro","Checklist","Final","Ubique"],1)]
        wipro = [f"{i}. {c}" for i,c in enumerate(["Wipro Pattern Pseudo 20Q Verbal 20Q Apt 20Q","Elite 3.5 LPA","Pseudo What is output?","Loops","Arrays","Synonyms","Antonyms","Para jumble","Aptitude Easy","Cutoff 60%","Backlogs 0","PYQ Pseudo Q1","PYQ Pseudo Q2","PYQ Verbal","Coding Tech","Tech OOPS","Tech DBMS","Accenture Cognitive + Tech","Email Writing","Critical Reasoning","Abstract Reasoning","Common Apps","MS Office","Networking","Salary 4.5 LPA","Eligibility 65% + comms","Comms Round Imp","Email Formal","Example Email by Bhavya Ponduri","Wipro Selected Bhavya Ponduri","Training Pune","Training Bangalore","Pseudo scoring","Verbal 10 days","Apt 10 days","Mock 5 tests","Wipro easy","Accenture needs English","HR Wipro","HR Accenture","Bond None","Growth","Tell me about yourself","BhavPath project","Final 50 Qs","Watermark From BhavPath - Bhavya Ponduri","Cognizant pattern","Capgemini pattern","Motivation","Checklist"],1)]

        pdf_py = make_pdf_bytes("Python • 50 Concepts • Ubique", [("Basics (1-25)", py[:25]), ("Advanced (26-50)", py[25:])])
        pdf_dsa = make_pdf_bytes("DSA • 50 Concepts • Ubique", [("Fundamentals (1-25)", dsa[:25]), ("FAANG (26-50)", dsa[25:])])
        pdf_sql = make_pdf_bytes("SQL • 50 Concepts • Ubique", [("Core (1-25)", sql[:25]), ("Interview (26-50)", sql[25:])])
        pdf_tcs = make_pdf_bytes("TCS NQT • 50 Qs • Ubique Vault", [("Pattern (1-25)", tcs[:25]), ("Interview (26-50)", tcs[25:])])
        pdf_infy = make_pdf_bytes("Infosys • 50 Qs • Ubique Vault", [("Tech (1-25)", infy[:25]), ("Prep (26-50)", infy[25:])])
        pdf_wipro = make_pdf_bytes("Wipro+Acc • 50 Qs • Ubique Vault", [("Wipro (1-25)", wipro[:25]), ("Accenture (26-50)", wipro[25:])])

        c1,c2,c3 = st.columns(3)
        with c1:
            st.download_button("💎 Python 50 • Ubique", pdf_py, f"{name}_Python_Ubique.pdf", "application/pdf", use_container_width=True)
            st.download_button("💎 TCS 50 Qs • Ubique", pdf_tcs, f"{name}_TCS_Ubique.pdf", "application/pdf", use_container_width=True)
        with c2:
            st.download_button("💎 DSA 50 • Ubique", pdf_dsa, f"{name}_DSA_Ubique.pdf", "application/pdf", use_container_width=True)
            st.download_button("💎 Infosys 50 Qs • Ubique", pdf_infy, f"{name}_Infosys_Ubique.pdf", "application/pdf", use_container_width=True)
        with c3:
            st.download_button("💎 SQL 50 • Ubique", pdf_sql, f"{name}_SQL_Ubique.pdf", "application/pdf", use_container_width=True)
            st.download_button("💎 Wipro+Acc 50 Qs • Ubique", pdf_wipro, f"{name}_Wipro_Acc_Ubique.pdf", "application/pdf", use_container_width=True)

with st.sidebar:
    st.markdown("### 💎 Atelier Access")
    if st.text_input("Password", type="password") == "bhavya123":
        if os.path.exists("bhavpath_users.csv"):
            df = pd.read_csv("bhavpath_users.csv")
            st.metric("Total Ubique Stories", len(df))
            st.dataframe(df.tail(20))
            st.download_button("📥 Download All Stories", df.to_csv(index=False).encode('utf-8'), "BhavPath_Ubique_All_Bhavya_Ponduri.csv", "text/csv", use_container_width=True)
 
