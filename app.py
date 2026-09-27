import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image, ImageDraw
import io

# --- 50 PAGE PDF GENERATOR ---
def make_50_page_pdf(title, points):
    W, H = 850, 1150
    pages = []
    watermark = "From BhavPath - Bhavya Ponduri"
    for i in range(1, 51):
        img = Image.new("RGB", (W, H), "#FFFFFF")
        d = ImageDraw.Draw(img)
        # Header
        d.rectangle([(0,0),(W,80)], fill="#6C5CE7")
        d.text((30, 25), f"BhavPath by Bhavya Ponduri | {title} | Page {i}/50", fill="white")
        # Title Box
        d.rectangle([(30, 100),(820, 150)], fill="#FFEAA7")
        d.text((45, 115), f"Point {i}: {title}", fill="#2D3436")
        # Watermark
        d.text((W//2, H//2), watermark, fill="#EFEFEF", anchor="mm")
        # Content
        point_text = points[i-1] if i-1 < len(points) else f"Important Topic {i} for {title}"
        d.text((45, 190), f"{i}. {point_text}", fill="#000000")
        d.text((45, 250), "Explanation:", fill="#6C5CE7")
        d.text((45, 285), "This topic is very important for placement.", fill="#2D3436")
        d.text((45, 315), f"Example for {title}:", fill="#2D3436")
        d.text((45, 345), f"If you are {title} student, remember this.", fill="#636e72")
        d.text((45, 400), "Previous Year Question:", fill="#E17055")
        d.text((45, 430), f"Q{i}: Explain {point_text}?", fill="#2D3436")
        d.text((45, 480), "Tip: Revise this 2 times daily!", fill="#00B894")
        # Footer
        d.rectangle([(0,H-50),(W,H)], fill="#2D3436")
        d.text((30, H-30), f"{watermark} | {title} | Page {i} of 50", fill="white")
        pages.append(img)
    buf = io.BytesIO()
    pages[0].save(buf, format="PDF", save_all=True, append_images=pages[1:])
    return buf.getvalue()

# --- PAGE SETUP ---
st.set_page_config(page_title="BhavPath by Bhavya Ponduri", page_icon="📘", layout="wide")
st.markdown("""
<style>
.stButton>button { background: linear-gradient(90deg, #6C5CE7, #A29BFE); color: white; border-radius: 25px; padding: 12px 28px; font-weight: 700; border: none; width: 100%; }
div[data-testid="stForm"] { border-radius: 20px; padding: 25px; background: white; box-shadow: 0 8px 30px rgba(0,0,0,0.07); }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#6C5CE7;'>✨ BhavPath</h1><p style='text-align:center;'>Crafted by Bhavya Ponduri | 50 Pages Books</p>", unsafe_allow_html=True)

# --- FORM ---
left, center, right = st.columns([1,2.2,1])
with center:
    with st.form("final_form"):
        name = st.text_input("Full Name", value="Bhavya Ponduri")
        col1, col2 = st.columns(2)
        with col1:
            btech = st.slider("B.Tech %", 40, 100, 58)
            branch = st.selectbox("Branch", ["CSE","IT","ECE","AI/ML","Others"])
        with col2:
            backlogs = st.selectbox("Backlogs", [0,1,2,"2+"])
            year = st.selectbox("Year", [2024,2025,2026,2027])
        goal = st.radio("Dream Company", ["TCS","Infosys","Wipro","Accenture"], horizontal=True)
        submit = st.form_submit_button("🚀 Check Eligibility & Get 50 Page PDFs")

if submit:
    # Save user
    data = {"Time":str(datetime.now()), "Name":name, "BTech":btech, "Backlogs":backlogs, "Goal":goal, "Branch":branch, "Year":year}
    if os.path.exists("bhavpath_users.csv"):
        pd.concat([pd.read_csv("bhavpath_users.csv"), pd.DataFrame([data])]).to_csv("bhavpath_users.csv", index=False)
    else:
        pd.DataFrame([data]).to_csv("bhavpath_users.csv", index=False)

    st.divider()
    st.markdown(f"### 📊 Result for {name}")

    # --- CLEAR LOGIC YOU ASKED ---
    if btech < 60:
        st.error(f"⚠️ {name}, you have gotten LOW MARKS ({btech}%) from your B.Tech.")
        st.error(f"You are NOT eligible for {goal} (Company needs minimum 60%).")
        st.warning("So here are the PDFs to improve your skills. Each PDF has 50 PAGES!")
    elif str(backlogs)!= "0":
        st.error(f"⚠️ {name}, you have {backlogs} backlogs. You are NOT eligible.")
        st.warning("So here are the PDFs - clear backlogs and study these 50-page books:")
    else:
        st.success(f"✅ {name}, you are ELIGIBLE for {goal} with {btech}%!")
        st.info("Here are your 50-PAGE PDFs to crack the interview:")

    st.markdown("---")
    st.markdown(f"### 📚 {name}, Here are your PDFs - Because you got {btech}%, study these:")

    # 50 Points Lists
    py = [f"Python - {t}" for t in ["What is Python","print()","input()","Variables","Data Types","Operators","If Else","For Loop","While Loop","List","Tuple","Dictionary","Set","Functions","Return Statement","Lambda","String Methods","File Handling","Exception Handling","Class Object","Inheritance","Polymorphism","Encapsulation","Abstraction","Recursion","Sorting","Searching","Big O Notation","Time Complexity","List Comprehension","Decorators","Generators","Modules","PIP Packages","OOPS Concepts","Project Calculator","LeetCode Easy","LeetCode Medium","Interview Q1","Interview Q2","Interview Q3","Interview Q4","Interview Q5","Resume Tip","Final Project","Communication","Motivation","Bonus","Revision","All The Best"]][:50]
    dsa = [f"DSA - {t}" for t in ["Array","Linked List","Stack LIFO","Queue FIFO","HashMap","Binary Tree","BST","Graph BFS","Graph DFS","Heap","Bubble Sort","Merge Sort","Quick Sort","Binary Search","Linear Search","Two Pointers","Sliding Window","Recursion","Backtracking","Dynamic Programming","DP Knapsack","DP LCS","String Reverse","Palindrome Check","Anagram Check","Linked List Reverse","Stack Example","Queue Example","Tree Traversal Inorder","Tree Preorder","Tree Postorder","Graph Example","LeetCode 1 Two Sum","LeetCode 3 Longest Substring","LeetCode 20 Valid Paranthesis","FAANG Interview Q1","FAANG Q2","FAANG Q3","System Design Intro","LRU Cache","Prime Number","Fibonacci","Factorial","Time Complexity","Space Complexity","Interview Prep","Final Revision","Motivation","Bonus","Last Tip"]][:50]
    sql = [f"SQL - {t}" for t in ["What is SQL","SELECT","WHERE Clause","AND OR","ORDER BY","GROUP BY","HAVING","COUNT","SUM","AVG","DISTINCT","LIKE Operator","IN Operator","BETWEEN","INNER JOIN","LEFT JOIN","RIGHT JOIN","FULL JOIN","UNION","Subquery","2nd Highest Salary","Find Duplicates","Primary Key","Foreign Key","Index","View","ACID Properties","1NF Normalization","2NF","3NF","Example WHERE Name='Bhavya'","ROW_NUMBER","RANK","DENSE_RANK","CASE WHEN","HAVING vs WHERE","Joins Interview Q","TCS PYQ SQL","Infosys PYQ SQL","Wipro PYQ SQL","Complex Query","Easy Query","Medium Query","Hard Query","Interview Q1","Interview Q2","Resume SQL Project","Motivation","Bonus","Final Revision"]][:50]
    tcs = [f"TCS - {t}" for t in ["TCS NQT Pattern","Aptitude 20Q","Email 1Q","Coding 1Q","Time and Work","Speed Distance","Percentages","Profit Loss","Blood Relation","Coding Decoding","Email Writing Format","Coding String Reverse","Coding Prime Number","Coding Palindrome","PYQ 2023 Q1","PYQ 2023 Q2","PYQ 2024 Q1","PYQ 2024 Q2","Digital Open Ended","OOPS Questions","DBMS Questions","Eligibility 60%","Why TCS Interview","Tell me about yourself","Bhavya Ponduri Project","Day 1-5 Aptitude Plan","Day 6-10 Verbal Plan","Day 11-20 Coding Plan","Salary 3.6 LPA","TCS Digital 7 LPA","Preparation Strategy","Time Management","Important Topics","Easy Scoring Areas","Hard Questions","HR Questions","Technical Questions","Managerial Round","Final Mock Test","Resume Tips","Communication Tips","Confidence Tips","Last Day Revision","All The Best","Bonus Tips","Final 5 Qs","TCS Selected Story","Motivation","Final Checklist","Success Mantra"]][:50]
    infy = [f"Infosys - Topic {i}" for i in range(1,51)]
    wipro = [f"Wipro/Accenture - Topic {i}" for i in range(1,51)]

    # Generate 50-page PDFs
    pdf_py = make_50_page_pdf("Python 50", py)
    pdf_dsa = make_50_page_pdf("DSA 50", dsa)
    pdf_sql = make_50_page_pdf("SQL 50", sql)
    pdf_tcs = make_50_page_pdf("TCS NQT 50", tcs)
    pdf_infy = make_50_page_pdf("Infosys 50", infy)
    pdf_wipro = make_50_page_pdf("Wipro+Accenture 50", wipro)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Improve Skills (Because Low Marks):**")
        st.download_button("📘 Python - 50 PAGES", pdf_py, f"{name}_Python_50_PAGES.pdf", "application/pdf", use_container_width=True)
        st.download_button("📗 DSA - 50 PAGES", pdf_dsa, f"{name}_DSA_50_PAGES.pdf", "application/pdf", use_container_width=True)
        st.download_button("📙 SQL - 50 PAGES", pdf_sql, f"{name}_SQL_50_PAGES.pdf", "application/pdf", use_container_width=True)
    with c2:
        st.markdown(f"**Company PYQs (Goal: {goal}):**")
        st.download_button("📕 TCS NQT - 50 PAGES PYQs", pdf_tcs, f"{name}_TCS_50_PAGES.pdf", "application/pdf", use_container_width=True)
        st.download_button("📓 Infosys - 50 PAGES PYQs", pdf_infy, f"{name}_Infosys_50_PAGES.pdf", "application/pdf", use_container_width=True)
        st.download_button("📒 Wipro+Acc - 50 PAGES PYQs", pdf_wipro, f"{name}_Wipro_50_PAGES.pdf", "application/pdf", use_container_width=True)

    st.success("✅ All PDFs are 50 PAGES each + Watermark: From BhavPath - Bhavya Ponduri")

# Sidebar Admin
with st.sidebar:
    if st.text_input("Admin Password", type="password") == "bhavya123":
        if os.path.exists("bhavpath_users.csv"):
            df = pd.read_csv("bhavpath_users.csv")
            st.dataframe(df)
            st.download_button("Download CSV", df.to_csv(index=False).encode('utf-8'), "users.csv", "text/csv")
