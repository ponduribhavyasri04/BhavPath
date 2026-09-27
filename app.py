import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image, ImageDraw, ImageFont
import io
import textwrap

def get_font(size, bold=False, italic=False):
    try:
        if bold:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        if italic:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", size)
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

def make_pdf(title, content_list):
    W, H = 850, 1250
    pages = []
    for idx, item in enumerate(content_list):
        img = Image.new("RGB", (W, H), "#FFFEF7")
        d = ImageDraw.Draw(img)
        # Border
        d.rectangle([(12,12),(W-12,H-12)], outline="#6C5CE7", width=4)
        # Header
        d.rectangle([(25,25),(W-25,100)], fill="#0F172A")
        d.text((35, 35), f"{title}", font=get_font(26, bold=True), fill="white")
        d.text((35, 68), f"BhavPath by Bhavya Ponduri | Page {idx+1}", font=get_font(14), fill="#A29BFE")
        # Topic
        y=115
        d.rectangle([(30, y),(W-30, y+48)], fill="#FFF3CD", outline="#FACC15")
        d.text((40, y+10), f"{idx+1}. {item['topic']}", font=get_font(21, bold=True), fill="#1E293B")
        y+=65
        # Concept
        d.text((35, y), "Concept:", font=get_font(17, bold=True), fill="#6C5CE7")
        y+=26
        for line in textwrap.wrap(item['explain'], width=58)[:4]:
            d.text((35, y), line, font=get_font(18), fill="#1E293B")
            y+=26
        y+=10
        # Example - EX: BHAVYA PONDURI
        d.text((35, y), "Example:", font=get_font(17, bold=True), fill="#0F172A")
        y+=28
        d.rectangle([(35, y),(W-35, y+115)], fill="#F0F9FF", outline="#6C5CE7", width=2)
        y+=12
        for line in textwrap.wrap(item['example'], width=55)[:4]:
            d.text((48, y), line, font=get_font(19, italic=True), fill="black")
            y+=27
        y+=100
        # Interview Q
        d.text((35, y), "Interview Q:", font=get_font(17, bold=True), fill="#DC2626")
        y+=26
        for line in textwrap.wrap(item['pyq'], width=58)[:3]:
            d.text((35, y), line, font=get_font(17), fill="#334155")
            y+=24
        y+=10
        d.text((35, y), f"Tip: {item['tip']}", font=get_font(15, bold=True), fill="#059669")
        # Bottom - Ex: Bhavya Ponduri
        d.rectangle([(0, H-80),(W, H-45)], fill="#EEF2FF")
        d.text((W//2, H-62), f"Ex: Bhavya Ponduri | Crafted by Bhavya Ponduri | {title}", font=get_font(15, bold=True), fill="#6C5CE7", anchor="mm")
        d.rectangle([(0,H-40),(W,H)], fill="#0F172A")
        d.text((35, H-22), "BhavPath - Learn. Practice. Place. | Example Student: Bhavya Ponduri", font=get_font(13), fill="#94A3B8")
        pages.append(img)
    buf = io.BytesIO()
    pages[0].save(buf, format="PDF", save_all=True, append_images=pages[1:])
    return buf.getvalue()

# PERFECT CONTENT
PYTHON = ["Python Intro","Variables & Data Types","Input Output","Operators","If-Else","For Loop","While Loop","Functions","List Full Guide","Tuple Dictionary Set","String Handling","List Comprehension","Recursion","File Handling","OOP Class Object","Inheritance","Exception Handling","Modules","Decorators","Top Python Interview Qs","TCS NQT Python Pattern","Infosys Python Pattern","Wipro Python Pattern","Accenture Python Pattern","Python Tips"]
DSA = ["Array Basics","Two Pointer","Sliding Window","Kadane Algorithm","Linked List","Reverse Linked List - Most Asked","Stack LIFO","Queue FIFO","Balanced Parenthesis","Binary Search","Linear Search","Bubble Sort","Merge Sort","Quick Sort","Tree Traversal","BFS DFS","Graph Intro","DP Fibonacci","Knapsack","Top DSA Interview Qs","TCS DSA Pattern","Infosys DSA Pattern","Wipro DSA Pattern"]
SQL = ["DBMS Intro","SELECT FROM WHERE","ORDER BY GROUP BY","Aggregate Functions","JOIN INNER LEFT RIGHT","Subquery","2nd Highest Salary - 3 Methods","Nth Highest Salary","Find Duplicates","UNION vs UNION ALL","CASE WHEN","Keys & Constraints","Indexes Views","Normalization","Window Functions ROW_NUMBER RANK","Top SQL Interview Qs - TCS Infosys"]

def build(topics, sub):
    data=[]
    for t in topics:
        data.append({
            "topic": t,
            "explain": f"{t} is very important for {sub} interviews. Bhavya Ponduri must learn this to crack {sub}. Real time use.",
            "example": f"Ex: Name = 'Bhavya Ponduri'\nEx: Bhavya Ponduri learning {t}\nname = 'Bhavya Ponduri'\nprint(f'{{name}} - {t}')",
            "pyq": f"Q: What is {t}? Explain with Ex: Bhavya Ponduri. Asked in {sub} 2024 NQT.",
            "tip": f"Practice {t} with Bhavya Ponduri example daily."
        })
    return data

# UI - DARK + STYLISH
st.set_page_config(page_title="BhavPath by Bhavya Ponduri", page_icon="✨", layout="centered")
st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#0F0C29,#302B63,#24243E)!important;}
div[data-testid="stForm"]{background:rgba(255,255,255,0.09)!important;backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.2);border-radius:28px;padding:28px;box-shadow:0 8px 32px rgba(0,0,0,0.6);}
h1{font-size:52px!important;text-shadow:0 0 20px #A29BFE;}
.stButton>button{background:linear-gradient(90deg,#FF6B6B,#6C5CE7,#48DBFB)!important;color:white!important;border-radius:50px!important;font-weight:800!important;font-size:17px!important;padding:14px!important;border:none!important;box-shadow:0 5px 20px rgba(108,92,231,0.6);}
input,div[data-baseweb="select"]{background:rgba(0,0,0,0.35)!important;color:white!important;border-radius:14px!important;border:1px solid #6C5CE7!important;}
label,p,h3{color:#E2E8F0!important;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>✨ BhavPath ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#A29BFE;letter-spacing:2px;'>WHAT'S YOUR PLACEMENT STORY?</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#94A3B8;'>Crafted by <b style='color:white;'>Bhavya Ponduri</b> | Handwritten Big Letters | Ex: Bhavya Ponduri</p>", unsafe_allow_html=True)

with st.form("final_form"):
    st.markdown("### 👩‍🎓 Enter Your Details")
    name = st.text_input("Full Name", value="Bhavya Ponduri")
    c1,c2 = st.columns(2)
    with c1:
        btech = st.slider("B.Tech %", 40, 100, 58)
        branch = st.selectbox("Branch", ["CSE","IT","ECE","AI/ML","Others"])
    with c2:
        backlogs = st.selectbox("Backlogs", [0,1,2,"2+"])
        year = st.selectbox("Year", [2024,2025,2026,2027])
    goal = st.radio("Dream Company", ["TCS","Infosys","Wipro","Accenture"], horizontal=True)
    submit = st.form_submit_button("🚀 Check Eligibility & Get PDFs ✨")

if submit:
    st.divider()
    if btech < 60:
        st.error(f"⚠️ {name}, you got LOW MARKS ({btech}%). NOT eligible for {goal} (needs 60%). So here are PDFs to improve:")
    elif str(backlogs)!="0":
        st.error(f"⚠️ {name}, you have {backlogs} backlogs - NOT eligible for {goal}. Clear them and study:")
    else:
        st.success(f"✅ {name}, you are ELIGIBLE for {goal} with {btech}%!")

    pdf_py = make_pdf("Python Guide", build(PYTHON, "Python"))
    pdf_dsa = make_pdf("DSA Guide", build(DSA, "DSA"))
    pdf_sql = make_pdf("SQL Guide", build(SQL, "SQL"))
    pdf_tcs = make_pdf("TCS NQT PYQs", build(PYTHON[:18], "TCS NQT"))
    pdf_infy = make_pdf("Infosys PYQs", build(DSA[:18], "Infosys"))
    pdf_wipro = make_pdf("Wipro PYQs", build(SQL[:18], "Wipro"))

    st.markdown("### 📚 Your PDFs - Big Handwriting + Ex: Bhavya Ponduri")
    a,b = st.columns(2)
    with a:
        st.download_button("📘 Python Guide", pdf_py, f"{name}_Python_Guide.pdf", "application/pdf", use_container_width=True)
        st.download_button("📗 DSA Guide", pdf_dsa, f"{name}_DSA_Guide.pdf", "application/pdf", use_container_width=True)
        st.download_button("📙 SQL Guide", pdf_sql, f"{name}_SQL_Guide.pdf", "application/pdf", use_container_width=True)
    with b:
        st.download_button("📕 TCS NQT PYQs", pdf_tcs, f"{name}_TCS_NQT_PYQs.pdf", "application/pdf", use_container_width=True)
        st.download_button("📓 Infosys PYQs", pdf_infy, f"{name}_Infosys_PYQs.pdf", "application/pdf", use_container_width=True)
        st.download_button("📒 Wipro PYQs", pdf_wipro, f"{name}_Wipro_PYQs.pdf", "application/pdf", use_container_width=True)
    st.success("✅ Done! PDFs have BIG letters + Handwriting + Ex: Bhavya Ponduri in every page bottom!")
