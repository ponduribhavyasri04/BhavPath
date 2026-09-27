import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image, ImageDraw
import io
# ================= BEFORE CODE PART - PDF GENERATOR (Monna ledhu, ippudu add chesam) =================
def make_pdf_bytes(title, sections):
    W, H = 800, 1100
    img = Image.new("RGB", (W, H), "#FFFBF7")
    draw = ImageDraw.Draw(img)
    # Header
    draw.text((W//2, 30), "BhavPath by Bhavya", fill="#8a2be2", anchor="mt")
    draw.text((W//2, 55), "India's Cute Learning Ecosystem", fill="#666", anchor="mt")
    y = 110
    draw.text((30, y), title, fill="#1e88e5")
    y += 35
    draw.line([(30, y), (750, y)], fill="#1e88e5", width=3)
    y += 30
    for head, content in sections:
        if y > 950: break
        draw.text((40, y), head, fill="#e91e63")
        y += 28
        for line in content.split("\n"):
            draw.text((55, y), line, fill="#222")
            y += 22
        y += 15
    draw.text((30, H-30), "Tip: Daily 10 Qs practice - BhavPath!", fill="#4caf50")
    buf = io.BytesIO()
    img.save(buf, format="PDF")
    return buf.getvalue()

# ================= APP CONFIG (Before code lo simple ga undedi) =================
st.set_page_config(page_title="BhavPath by Bhavya", page_icon="🚀", layout="centered")
st.markdown("<h1 style='text-align:center; color:#8a2be2;'>🚀 BhavPath</h1><p style='text-align:center;'>by Bhavya | Before + After = Full Ecosystem</p>", unsafe_allow_html=True)

# ================= BEFORE CODE PART - FORM (Monna TCS ke pettav) =================
with st.form("bhavpath_final"):
    st.subheader("👤 Nee Details (Before code laage)")
    name = st.text_input("Name *")
    col1, col2 = st.columns(2)
    with col1:
        btech = st.slider("B.Tech %", 40, 100, 72)
        branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "EEE", "AI/ML", "Others"])
    with col2:
        backlogs = st.selectbox("Active Backlogs", [0, 1, 2, "2+"])
        year = st.selectbox("Passout Year", [2024, 2025, 2026, 2027])
    
    st.subheader("💻 Skills")
    skills = st.multiselect("Skills", ["Python", "Java", "C", "SQL", "DSA", "OOPS", "DBMS", "Communication", "Aptitude"])
    comm = st.slider("English Communication 1-10", 1, 10, 6)
    goal = st.radio("Goal", ["TCS", "Infosys", "Any Service Job", "Product Based"])
    
    btn = st.form_submit_button("🔥 Check Full Eligibility + Get PDFs")

# ================= AFTER CODE PART - FULL LOGIC (Monna TCS mathrame, ippudu anni) =================
if btn:
    if not name:
        st.warning("Name pettu Bhavya!")
        st.stop()

    # ---- SAVE (Before code lo kuda undi, ippudu continue) ----
    has_coding = any(s in skills for s in ["Python", "Java", "C"])
    has_sql = "SQL" in skills
    has_dsa = "DSA" in skills
    score = int(btech*0.5 + len(skills)*6 + comm*3)
    
    row = [[str(datetime.now()), name, branch, btech, backlogs, ", ".join(skills), year, goal, score]]
    df_new = pd.DataFrame(row, columns=["Time","Name","Branch","BTech","Backlogs","Skills","Year","Goal","Score"])
    if os.path.exists("bhavpath_users.csv"):
        df_old = pd.read_csv("bhavpath_users.csv")
        pd.concat([df_old, df_new]).to_csv("bhavpath_users.csv", index=False)
    else:
        df_new.to_csv("bhavpath_users.csv", index=False)
    
    st.success(f"Hey {name}! Data Saved ✅ | Score: {score}/100")
    st.divider()

    # ---- BEFORE: Only TCS undedi ----
    # ---- AFTER: All 5 Companies + Previous Qs Prompt ----
    st.header("🏢 Before: TCS Only | After: All Companies + Prompt")

    # 1. TCS (Before code)
    st.subheader("1. TCS NQT (3.6 LPA) & Digital (7 LPA) - BEFORE CODE")
    if btech >= 60 and str(backlogs) in ["0","1"] and has_coding:
        st.success("✅ Eligible for TCS NQT")
        st.info("**Previous Qs:** Aptitude Work&Time, Email to client, Coding Reverse String/Prime No")
        if btech>=70 and has_dsa:
            st.success("✅ TCS Digital (7 LPA) - Eligible! Prompt: LeetCode Medium 100 Qs")
    else:
        st.error("❌ TCS Not Eligible - Need 60% + Coding")

    # 2. INFOSYS (After code - Nuvvu adigindi)
    st.subheader("2. Infosys SP (5 LPA) - AFTER CODE ADDED")
    if btech>=60 and str(backlogs)=="0" and has_coding and has_sql:
        st.success("✅ Eligible for Infosys SP (5 LPA) & SE (3.6 LPA)")
        st.info("**Previous Qs:** 1. OOPS Inheritance? 2. SQL 2nd highest salary query 3. List vs Tuple 4. DBMS Normalization")
    elif btech>=60 and has_coding:
        st.warning("⚠️ SE only - SP kosam SQL nerchuko")
    else:
        st.error("❌ Infosys Not Eligible - Need 60% + 0 Backlogs + SQL")

    # 3. WIPRO (After)
    st.subheader("3. Wipro Elite (3.5 LPA) - AFTER CODE")
    if btech>=60:
        st.success("✅ Wipro Eligible")
        st.info("**Previous Qs:** Pseudo Code 20Qs + Aptitude + Verbal - Easy pattern")
    else:
        st.error("❌ Wipro Not Eligible")

    # 4. ACCENTURE (After)
    st.subheader("4. Accenture (4.5 LPA) - AFTER CODE")
    if btech>=65 and str(backlogs)=="0" and comm>=6:
        st.success("✅ Accenture Eligible")
        st.info("**Previous Qs:** Email Writing + Critical Reasoning + Communication round")
    else:
        st.error("❌ Accenture Not Eligible - Need 65% + Good English")

    # 5. COGNIZANT (After)
    st.subheader("5. Cognizant GenC (4 LPA) & Next (6.8 LPA) - AFTER CODE")
    if btech>=60:
        st.success("✅ Cognizant GenC Eligible")
        if btech>=70 and has_dsa:
            st.success("✅ GenC Next Eligible - Prompt: Advanced DSA + SQL Joins")
    
    st.divider()

    # ================= AFTER CODE PART - PDFs INSIDE CODE =================
    st.header("📥 After Code: PDFs Inside Code (No External File Needed)")

    pdf_py = make_pdf_bytes("Python Super Skill", [("What is Python?", "Python = instructions to computer\nEasy like English"), ("Variables", "name='Bhavya' -> text box\nage=10 -> number box"), ("print()", "print(name) -> Bhavya")])
    pdf_dsa = make_pdf_bytes("DSA Easy", [("List", "Shopping basket - mutable\n[1,2,3]"), ("Tuple", "Locked box - immutable\n(1,2,3)")])
    pdf_sql = make_pdf_bytes("SQL Mastery", [("2nd Highest Salary", "SELECT MAX(Sal) FROM Emp WHERE Sal < (SELECT MAX(Sal) FROM Emp)"), ("Joins", "INNER, LEFT, RIGHT imp")])
    pdf_tcs = make_pdf_bytes("TCS NQT Previous Qs", [("Pattern", "Apt 20Q, Email 1Q, Code 1Q"), ("Top Qs", "Work&Time, %, Email, Reverse String, Prime")])
    pdf_infy = make_pdf_bytes("Infosys SP Previous Qs", [("Pattern", "Apt 10, Reas 10, Tech 10"), ("Tech", "OOPS, SQL 2nd salary, List vs Tuple, DBMS")])
    pdf_wipro = make_pdf_bytes("Wipro+Accenture Qs", [("Wipro", "Pseudo Code 20Q, Verbal"), ("Accenture", "Email + Critical Reasoning")])

    a,b = st.columns(2)
    with a:
        st.download_button("📘 Python PDF", pdf_py, "BhavPath_Python.pdf", "application/pdf")
        st.download_button("📗 DSA PDF", pdf_dsa, "BhavPath_DSA.pdf", "application/pdf")
        st.download_button("📙 SQL PDF", pdf_sql, "BhavPath_SQL.pdf", "application/pdf")
    with b:
        st.download_button("📕 TCS Q&A PDF", pdf_tcs, "BhavPath_TCS_QA.pdf", "application/pdf")
        st.download_button("📓 Infosys Q&A PDF", pdf_infy, "BhavPath_Infosys_QA.pdf", "application/pdf")
        st.download_button("📒 Wipro+Acc Q&A PDF", pdf_wipro, "BhavPath_Wipro_Acc.pdf", "application/pdf")

# Admin (Before nundi undi)
with st.sidebar:
    st.write("🔒 Admin")
    if st.text_input("Password", type="password") == "bhavya123":
        if os.path.exists("bhavpath_users.csv"):
            df = pd.read_csv("bhavpath_users.csv")
            st.metric("Users", len(df))
            st.dataframe(df.tail(10))
