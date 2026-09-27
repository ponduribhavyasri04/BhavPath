import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def get_font(size, bold=False, italic=False):
    try:
        if bold:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        if italic:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", size)
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

def make_pdf(title, topics):
    W, H = 850, 1250
    pages = []
    for idx, t in enumerate(topics):
        img = Image.new("RGB", (W, H), "#FFFEF7")
        d = ImageDraw.Draw(img)
        d.rectangle([(12,12),(W-12,H-12)], outline="#6C5CE7", width=4)
        d.rectangle([(25,25),(W-25,100)], fill="#0F172A")
        d.text((35, 35), title, font=get_font(26, True), fill="white")
        d.text((35, 68), f"BhavPath by Bhavya Ponduri | Page {idx+1}", font=get_font(14), fill="#A29BFE")
        y = 115
        d.rectangle([(30, y),(W-30, y+50)], fill="#FFF3CD")
        d.text((40, y+10), f"{idx+1}. {t}", font=get_font(22, True), fill="#1E293B")
        y += 70
        d.text((35, y), "Concept:", font=get_font(18, True), fill="#6C5CE7")
        y += 28
        d.text((35, y), f"{t} is important for placement. Learn with Ex.", font=get_font(18), fill="#1E293B")
        y += 40
        d.text((35, y), "Example:", font=get_font(18, True), fill="black")
        y += 30
        d.rectangle([(35, y),(W-35, y+105)], fill="#F0F9FF", outline="#6C5CE7", width=2)
        y += 12
        d.text((48, y), f"Ex: Name = 'Bhavya Ponduri'", font=get_font(19, italic=True), fill="black")
        y += 27
        d.text((48, y), f"Ex: Bhavya Ponduri -> {t}", font=get_font(19, italic=True), fill="black")
        y += 27
        d.text((48, y), f"name = 'Bhavya Ponduri' # JS: let name='Bhavya'", font=get_font(18), fill="black")
        y += 90
        d.text((35, y), "Interview Q: Explain with Ex: Bhavya Ponduri", font=get_font(17, True), fill="#DC2626")
        y += 30
        d.rectangle([(0, H-75),(W, H-40)], fill="#EEF2FF")
        d.text((W//2, H-58), f"Ex: Bhavya Ponduri | Crafted by Bhavya Ponduri", font=get_font(15, True), fill="#6C5CE7", anchor="mm")
        d.rectangle([(0, H-35),(W, H)], fill="#0F172A")
        d.text((35, H-15), "BhavPath - Big Handwriting - Ex: Bhavya Ponduri", font=get_font(13), fill="#94A3B8")
        pages.append(img)
    buf = io.BytesIO()
    pages[0].save(buf, format="PDF", save_all=True, append_images=pages[1:])
    return buf.getvalue()

def get_eligible(per, back):
    eligible = []
    b = str(back)
    if per >= 60 and b == "0":
        eligible.append("✅ TCS - 60% Criteria - Eligible")
    if per >= 65 and b == "0":
        eligible.append("✅ Infosys - 65% Criteria - Eligible")
    if per >= 60:
        eligible.append("✅ Wipro - 60% Criteria - Eligible")
    if per >= 65 and b == "0":
        eligible.append("✅ Accenture - 65% Criteria - Eligible")
    if per >= 60:
        eligible.append("✅ Cognizant - 60% Criteria - Eligible")
        eligible.append("✅ Capgemini - 60% Criteria - Eligible")
    if per < 60:
        return []
    return eligible

# UI
st.set_page_config(page_title="BhavPath", page_icon="✨", layout="centered")
st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#0F0C29,#302B63,#24243E)!important;}
div[data-testid="stForm"]{background:rgba(255,255,255,0.09)!important;backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.2);border-radius:28px;padding:28px;box-shadow:0 8px 32px rgba(0,0,0,0.6);}
h1{font-size:52px!important;text-shadow:0 0 20px #A29BFE;}
.stButton>button{background:linear-gradient(90deg,#FF6B6B,#6C5CE7,#48DBFB)!important;color:white!important;border-radius:50px!important;font-weight:800!important;padding:14px!important;border:none!important;}
label,p,h3,span{color:#E2E8F0!important;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>✨ BhavPath ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#A29BFE;letter-spacing:2px;'>WHAT'S YOUR PLACEMENT STORY?</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#94A3B8;'>Crafted by Bhavya Ponduri | Handwritten Big Letters</p>", unsafe_allow_html=True)

with st.form("final"):
    st.markdown("### 👩‍🎓 Enter Your Details")
    name = st.text_input("Full Name (Ex: Bhavya Ponduri)", value="Bhavya Ponduri")
    st.caption("Ex: Bhavya Ponduri")
    c1,c2 = st.columns(2)
    with c1:
        btech = st.slider("B.Tech %", 40, 100, 58)
        branch = st.selectbox("Branch", ["CSE","IT","ECE","AI/ML","Others"])
    with c2:
        backlogs = st.selectbox("Backlogs", [0,1,2,"2+"])
        year = st.selectbox("Year", [2024,2025,2026,2027])
    submit = st.form_submit_button("🚀 Check Eligibility Automatically ✨")

if submit:
    st.divider()
    st.markdown(f"### 📊 Output for Ex: {name}")
    st.markdown(f"**Ex: {name} | B.Tech: {btech}% | Branch: {branch} | Backlogs: {backlogs}**")

    eligible = get_eligible(btech, backlogs)

    if btech < 60:
        st.error(f"⚠️ Ex: {name}, you got LOW MARKS ({btech}%) - NOT Eligible for 60% companies!")
        st.markdown("You need 60%+. Study these PDFs:")
    else:
        if not eligible:
            st.error(f"⚠️ Ex: {name}, Backlogs valla not eligible. Clear backlogs!")
        else:
            st.success(f"✅ Ex: {name}, you got {btech}% - You are Eligible!")
            st.markdown(f"#### 🎉 Ex: {name} is Eligible For {len(eligible)} Companies:")
            for comp in eligible:
                st.success(f"{comp} -> Ex: {name}")

    st.markdown("---")
    st.markdown(f"### 📚 PDFs for Ex: {name} - Big Handwriting")

    py_pdf = make_pdf("Python Guide", ["Python Intro","Variables","Operators","If Else","For Loop","While Loop","Functions","List Full","Dict Set Tuple","String Handling","Recursion","OOP","Top Python Qs"])
    dsa_pdf = make_pdf("DSA Guide", ["Array Basics","Linked List","Reverse LL","Stack LIFO","Queue FIFO","Binary Search","Sorting","Tree Traversal","BFS DFS","DP Basics","Top DSA Qs"])
    sql_pdf = make_pdf("SQL Guide", ["SELECT WHERE","GROUP BY","JOINs","Subquery","2nd Highest Salary","Duplicates","Window Functions","Top SQL Qs"])
    js_pdf = make_pdf("JavaScript Guide", ["JS Intro","let var const","Data Types","If Else","Loops","Functions","Arrow Functions","Array Methods","Object","DOM","Promises Async Await","Fetch API","Top JS Qs"])

    c1,c2 = st.columns(2)
    with c1:
        st.download_button("📘 Python Guide - Ex: Bhavya Ponduri", py_pdf, f"Ex_{name}_Python_Guide.pdf", "application/pdf", use_container_width=True)
        st.download_button("📗 DSA Guide - Ex: Bhavya Ponduri", dsa_pdf, f"Ex_{name}_DSA_Guide.pdf", "application/pdf", use_container_width=True)
        st.download_button("📙 SQL Guide - Ex: Bhavya Ponduri", sql_pdf, f"Ex_{name}_SQL_Guide.pdf", "application/pdf", use_container_width=True)
    with c2:
        st.download_button("📒 JavaScript Guide - Ex: Bhavya Ponduri", js_pdf, f"Ex_{name}_JavaScript_Guide.pdf", "application/pdf", use_container_width=True)
        st.download_button("📕 TCS NQT PYQs", py_pdf, f"Ex_{name}_TCS_NQT.pdf", "application/pdf", use_container_width=True)
        st.download_button("📓 Infosys PYQs", dsa_pdf, f"Ex_{name}_Infosys.pdf", "application/pdf", use_container_width=True)
