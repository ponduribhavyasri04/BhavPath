import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io, textwrap, csv, os
from datetime import datetime

st.set_page_config(page_title="BhavPath", layout="wide")
DB_FILE = "bhavpath_data.csv"

def get_font(size, bold=False):
    try:
        path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# 50 PAGES PDF - EASY ENGLISH
def make_pdf_50_pages(skill):
    pages = []
    W, H = 1240, 1754

    # Content for 50 pages - easy english
    topics = {
        "Python": ["What is Python - Simple language", "Variables - How to store data", "Loops - Repeat work", "If Else - Decision making", "Functions - Reusable code", "List, Tuple, Dictionary", "File Handling - Easy", "OOPS Basics", "Important Programs", "Interview Questions"],
        "SQL": ["What is SQL", "Select Statement", "Where Filter", "Joins - Easy", "Group By", "Functions", "Subquery", "Index", "Important Queries", "Interview Q&A"],
        "DBMS": ["What is DBMS", "ER Diagram Easy", "Normalization Simple", "Transactions", "Keys - Primary, Foreign", "SQL vs DBMS", "ACID Properties", "Indexing", "Important Questions", "Real Examples"],
        "Java": ["What is Java", "Variables", "Loops", "OOPS - Class Object", "Inheritance Easy", "Polymorphism", "Collections", "Exception Handling", "Important Programs", "Interview Q&A"],
        "C": ["What is C", "Variables", "Loops", "Functions", "Pointers Easy", "Arrays", "Strings", "Structures", "Important Programs", "Interview Q&A"],
        "C++": ["What is C++", "Basics", "OOPS in C++", "Class Object", "Inheritance", "Polymorphism", "STL Easy", "Pointers", "Important Programs", "Interview"],
        "Aptitude": ["What is Aptitude", "Percentage Easy Tricks", "Profit Loss Simple", "Time Speed", "Ratio", "Coding Decoding", "Blood Relation", "Series", "Important Formulas", "Shortcuts"]
    }

    skill_topics = topics.get(skill, topics["Python"])

    for page_no in range(1, 51):
        img = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(img)

        # Header
        d.rectangle([0,0,W,100], fill="#0a1628")
        d.text((40,30), f"BhavPath - {skill} - Page {page_no}/50", font=get_font(28, True), fill="#6cb6ff")
        d.rectangle([0,100,W,105], fill="#6cb6ff")

        y = 140
        d.text((40, y), f"Topic {((page_no-1)//5)+1}: {skill_topics[((page_no-1)//5)]}", font=get_font(26, True), fill="#0a1628")
        y += 60

        # Easy English content - 20 lines per page
        content_lines = [
            f"This is page {page_no} of {skill}. Easy English.",
            f"",
            f"1. What is {skill}? It is very easy to learn.",
            f"2. We use {skill} in placements and jobs.",
            f"3. This point is explained in simple words.",
            f"4. No hard English. Only easy sentences.",
            f"5. Example: If you learn {skill}, you get job easily.",
            f"",
            f"Important Points for Page {page_no}:",
            f"- Point A: Simple and easy to remember",
            f"- Point B: Used in TCS, Wipro, Infosys",
            f"- Point C: Interviewer asks this",
            f"- Point D: Practice this daily 10 minutes",
            f"",
            f"Example Code / Example:",
            f" Example {page_no}: See how easy it is.",
            f" Input -> Process -> Output",
            f" This is very simple logic.",
            f"",
            f"Revision: Page {page_no} is about {skill_topics[((page_no-1)//5)]}",
            f"Remember this for interview."
        ]

        for line in content_lines:
            wrapped = textwrap.wrap(line, width=85) if line else [""]
            for wl in wrapped:
                d.text((50, y), wl, font=get_font(20), fill="black")
                y += 32
                if y > H-100:
                    break

        # Footer
        d.text((50, H-50), f"BhavPath | {skill} Notes | Easy English | Page {page_no}", font=get_font(16), fill="#888")
        pages.append(img)

    buf = io.BytesIO()
    pages[0].save(buf, format="PDF", save_all=True, append_images=pages[1:])
    return buf.getvalue()

# TOP - ONLY 2 LINES
st.markdown("<h1 style='text-align:center; margin-bottom:0px'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#6cb6ff; font-weight:400; margin-top:5px'>What's Your Placement Story..?</h3>", unsafe_allow_html=True)
st.divider()

# Form
with st.container(border=True):
    c1,c2,c3 = st.columns(3)
    name = c1.text_input("Name", placeholder="Ex: Bhavya Ponduri")
    perc = c2.slider("Percentage", 40, 100, 58)
    branch = c3.selectbox("Branch", ["CSE","ECE","EEE","MECH"])
    skills = st.multiselect("Skills", ["Python","SQL","DBMS","Java","C","C++","Aptitude"], default=["Python"])

    if st.button("Save"):
        exists = os.path.exists(DB_FILE)
        with open(DB_FILE, "a", newline="") as f:
            w = csv.writer(f)
            if not exists: w.writerow(["time","name","%","branch","skills"])
            w.writerow([datetime.now(), name, perc, branch, ",".join(skills)])
        st.success("Saved")

# Eligibility
with st.expander("Eligibility Check", expanded=True):
    if perc >= 58:
        st.success(f"{perc}% - Eligible for TCS NQT (58% criteria)")
    else:
        st.warning(f"{perc}% - Skill based companies")

# Details
with st.expander("Details As Per Placements"):
    st.write("Aptitude -> Coding -> Interview")

# PDFs - 50 PAGES
with st.expander("PDFs - 50 Pages Each - Easy English"):
    for sk in ["Python","SQL","DBMS","Java","C","C++","Aptitude"]:
        if st.button(f"Generate {sk} - 50 Pages PDF", key=f"pdf_{sk}"):
            with st.spinner(f"{sk} 50 pages making... 10 sec wait"):
                pdf = make_pdf_50_pages(sk)
                st.download_button(f"Download {sk} - 50 Pages PDF", pdf, f"{sk}_50_Pages_Easy.pdf", key=f"dl_{sk}")

# Videos
with st.expander("Animated Videos - Own"):
    st.write("Own animated videos")

# Tests
with st.expander("Weekly Tests"):
    ans = st.radio("TCS eligibility %?", ["58%","60%"], key="test1")
    if st.button("Submit Test"):
        st.write("Correct: 58%" if ans=="58%" else "Check again")

# Companies
with st.expander("Recommended Companies", expanded=True):
    if perc>=58: st.write("✅ TCS NQT")
    if "Python" in skills: st.write("✅ Accenture - Python")
    if "SQL" in skills: st.write("✅ Wipro - SQL")
    if "Java" in skills: st.write("✅ Capgemini - Java")
