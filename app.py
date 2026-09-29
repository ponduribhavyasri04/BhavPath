# app.py - BHAVPATH - ULTIMATE - LONG LASTING - NO EXTERNAL LINKS - BHAVYA PONDURI - 2026-2030
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io, textwrap, csv, os, random, json
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="BhavPath", layout="wide", page_icon="🚀")
DB_FILE = "bhavpath_data.csv"

# --- STABLE FONT ---
def get_font(s,b=False):
    try:
        p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except:
        return ImageFont.load_default()

def make_skill_pdf(skill, content):
    W,H=1240,1754
    img=Image.new("RGB",(W,H),"white")
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,W,120], fill="#0a1628")
    d.text((40,30), f"BhavPath - {skill} - Bhavya Ponduri", font=get_font(32,True), fill="#6cb6ff")
    d.text((40,80), "Long Lasting Notes 2026-2030", font=get_font(18), fill="white")
    y=160
    for para in content.split("\n"):
        for line in textwrap.wrap(para, width=75):
            d.text((40,y), line, font=get_font(22), fill="black")
            y+=32
    buf=io.BytesIO(); img.save(buf, format="PDF"); return buf.getvalue()

def make_animated_video(skill):
    # Own animated video - PIL frames as GIF - No external link
    frames=[]
    W,H=640,360
    for i in range(15):
        img=Image.new("RGB",(W,H), (10,22,40))
        d=ImageDraw.Draw(img)
        x = int(50 + i*35)
        d.ellipse([x, 100, x+80, 180], fill="#6cb6ff")
        d.text((20,20), f"{skill} Animation - Bhavya Ponduri - Frame {i}", font=get_font(18,True), fill="white")
        d.text((20,280), f"Code running... {skill} -> Placement!", font=get_font(16), fill="#a0d8ff")
        frames.append(img)
    buf=io.BytesIO()
    frames[0].save(buf, format="GIF", save_all=True, append_images=frames[1:], duration=200, loop=0)
    return buf.getvalue()

def save_data(name, perc, branch, skills):
    file_exists = os.path.exists(DB_FILE)
    with open(DB_FILE, "a", newline="") as f:
        w=csv.writer(f)
        if not file_exists:
            w.writerow(["timestamp","name","percentage","branch","skills"])
        w.writerow([datetime.now(), name, perc, branch, ",".join(skills)])

def recommend_companies(perc, skills):
    comps=[]
    if perc>=58 or "Python" in skills: comps.append("TCS NQT (58% eligible - Bhavya Ponduri example)")
    if perc>=60: comps.append("Infosys - 60% - CSE")
    if "SQL" in skills and "DBMS" in skills: comps.append("Wipro - DBMS + SQL")
    if "Java" in skills: comps.append("Capgemini - Java")
    if "Python" in skills: comps.append("Accenture - Python + Aptitude")
    if perc<60: comps.append("Startups + BhavPath Internships - Skill based - No % criteria")
    return comps

# --- 1. TOP HEADER ---
st.markdown("<h1 style='text-align:center; font-size:60px'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#6cb6ff'>What's Your Placement Story..? ✨</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Ex: Bhavya Ponduri - 58% - CSE - TCS Target - Long Lasting - Neat - Animated - Simple English - Telugu Video</p>", unsafe_allow_html=True)
st.divider()

# --- 2. MAIN STORY FORM - Host saving ---
with st.container(border=True):
    st.subheader("📝 Tell Your Story - We Save As Host")
    c1,c2,c3=st.columns(3)
    name = c1.text_input("Your Name", value="Bhavya Ponduri")
    perc = c2.slider("Percentage", 40, 100, 58)
    branch = c3.selectbox("Branch", ["CSE","ECE","EEE","MECH","CIVIL"], index=0)
    skills_sel = st.multiselect("Select Skills - PDFs will generate", ["Python","SQL","DBMS","Java","C","C++","Aptitude"], default=["Python","SQL"])

    if st.button("🚀 Save My Story + Check Eligibility"):
        save_data(name, perc, branch, skills_sel)
        st.success(f"Saved! {name} - {perc}% - Host lo save ayindi - BhavPath DB")
        st.balloons()

# --- 3. ELIGIBILITY - BHAVYA EXAMPLE ENABLE ---
with st.expander("3. ✅ Eligibility Check - Example: Bhavya Ponduri Enable", expanded=True):
    st.write(f"**Example Enabled:** Name = Bhavya Ponduri | {perc}% | {branch} | Skills: {', '.join(skills_sel)}")
    if perc>=58:
        st.success(f"✅ {name} Eligible for TCS NQT - 58% criteria - Bhavya Ponduri example lo ok - Neat!")
    else:
        st.error("Not eligible for TCS but eligible for skill-based companies - BhavPath will guide")
    st.json({"name": name, "percentage": perc, "branch": branch, "eligible_companies": recommend_companies(perc, skills_sel)})

# --- 4. ALL DETAILS AS PER PLACEMENTS ---
with st.expander("4. 📋 All Details As Per Placements - Unique"):
    st.table([
        {"Stage":"Aptitude","What to do":"58% ok but practice daily 30 min - Bhavya 58% example","BhavPath Tool":"Aptitude PDF + Test"},
        {"Stage":"Coding","What to do":"Python/Java any 1 strong - projects must","BhavPath Tool":"Animated Video + PDF"},
        {"Stage":"Interview","What to do":"Story telling - What's Your Placement Story","BhavPath Tool":"Company List"}
    ])

# --- 5. PDFs FOR ALL SKILLS ---
with st.expander("5. 📄 PDFs For All Students - Python, SQL, DBMS, Java, C, C++, Aptitude", expanded=True):
    cols=st.columns(4)
    pdf_contents={
        "Python":"Python Basics:\n1. Variables, loops, functions\n2. OOP - class\n3. For Placements: List, Dict, String - 90% questions\nBhavya Ponduri Notes - Long lasting",
        "SQL":"SQL Notes:\n1. SELECT, WHERE, JOIN\n2. GROUP BY, HAVING\n3. TCS asks JOIN + Subquery\nBhavya Ponduri",
        "DBMS":"DBMS:\n1. ACID, Normalization\n2. Indexing\n3. Example: Bhavya Ponduri 58% story",
        "Java":"Java:\n1. OOP, Inheritance\n2. Collections\n3. Placement focus",
        "C":"C:\n1. Pointers, Arrays\n2. Structures\n3. Basics for all",
        "C++":"C++:\n1. OOP + STL\n2. Vector, Map\n3. Competitive",
        "Aptitude":"Aptitude:\n1. % - Bhavya 58% example\n2. Time & Work\n3. Simple English + Telugu video style"
    }
    for i, (skill, content) in enumerate(pdf_contents.items()):
        with cols[i%4]:
            if st.button(f"Download {skill} PDF"):
                pdf = make_skill_pdf(skill, content)
                st.download_button(f"Save {skill} PDF", pdf, f"{skill}_BhavyaPonduri_BhavPath.pdf", key=f"pdf{skill}")

# --- 6. ANIMATED VIDEOS OWN ---
with st.expander("6. 🎬 Own Animated Videos - Python / Java - As Per Content"):
    s=st.selectbox("Choose skill animation", ["Python","Java","SQL"])
    if st.button(f"Generate {s} Animated Video"):
        gif = make_animated_video(s)
        st.image(gif, caption=f"{s} - Own Animation - BhavPath - Bhavya Ponduri - No external link")
        st.download_button("Download GIF Video", gif, f"{s}_animation_Bhavya.gif")

# --- 7. WEEKLY TESTS ---
with st.expander("7. 📝 Weekly Tests - Unique"):
    q=st.radio("Weekly Test - Aptitude (Bhavya 58% example): If Bhavya gets 58%, 75 coding, eligible?", ["Yes - TCS 58% criteria", "No"], index=0)
    if st.button("Submit Test"):
        if q.startswith("Yes"):
            st.success("Correct! Bhavya Ponduri example - 58% eligible - You know placement story!")
            save_data(name+"_TEST", perc, branch, ["Test_Pass"])
        else:
            st.error("Wrong - TCS NQT 58% - Check Eligibility tab")

# --- 8. HOST DATA SAVING ---
with st.expander("8. 💾 Saving Everyone Data As Host - Me"):
    if os.path.exists(DB_FILE):
        st.write("Host lo save ayina data:")
        with open(DB_FILE) as f:
            st.code(f.read(), language="csv")
    else:
        st.info("No data yet - First story save chey Bhavya")

# --- 9. RECOMMENDED COMPANY LISTS ---
with st.expander("9. 🏢 Recommended Company List - After Details", expanded=True):
    recs = recommend_companies(perc, skills_sel)
    for r in recs:
        st.success(f"✅ {r}")
    st.caption("Unique Logic: % + Skills + Bhavya Ponduri example = Company")

st.divider()
st.markdown("<center><b>10. All in Unique Way - BhavPath - Bhavya Ponduri - Stable 2026-2030 - Long Lasting - Neat</b></center>", unsafe_allow_html=True)
