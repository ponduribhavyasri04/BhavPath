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

def make_pdf(skill):
    W, H = 1240, 1754
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,90], fill="#0a1628")
    d.text((40,25), f"BhavPath - {skill}", font=get_font(26, True), fill="#6cb6ff")
    y = 130
    content = f"{skill} Placement Notes\n1. Basics\n2. Important Questions\n3. Interview Points"
    for line in textwrap.wrap(content, 80):
        d.text((40,y), line, font=get_font(20), fill="black")
        y+=35
    buf=io.BytesIO()
    img.save(buf, format="PDF")
    return buf.getvalue()

# 1. TOP - ONLY 2 LINES
st.markdown("<h1 style='text-align:center; margin-bottom:0px'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#6cb6ff; font-weight:400; margin-top:5px'>What's Your Placement Story..?</h3>", unsafe_allow_html=True)
st.divider()

# 2. Form
with st.container(border=True):
    c1,c2,c3 = st.columns(3)
    name = c1.text_input("Name", placeholder="Enter name")
    perc = c2.slider("Percentage", 40, 100, 58)
    branch = c3.selectbox("Branch", ["CSE","ECE","EEE","MECH"])
    skills = st.multiselect("Skills", ["Python","SQL","DBMS","Java","C","C++","Aptitude"], default=["Python"])
    
    # 3. Host save
    if st.button("Save"):
        exists = os.path.exists(DB_FILE)
        with open(DB_FILE, "a", newline="") as f:
            w = csv.writer(f)
            if not exists: w.writerow(["time","name","%","branch","skills"])
            w.writerow([datetime.now(), name, perc, branch, ",".join(skills)])
        st.success("Saved in Host")

# 4. Eligibility
with st.expander("Eligibility Check", expanded=True):
    if perc >= 58:
        st.success(f"{perc}% - Eligible for TCS NQT (58% criteria)")
    else:
        st.warning(f"{perc}% - Skill based companies")
    st.write(f"Skills: {', '.join(skills)}")

# 5. Details
with st.expander("Details As Per Placements"):
    st.write("Aptitude -> Coding -> Interview")

# 6. PDFs - 7 subjects
with st.expander("PDFs"):
    for sk in ["Python","SQL","DBMS","Java","C","C++","Aptitude"]:
        pdf = make_pdf(sk)
        st.download_button(f"{sk} PDF", pdf, f"{sk}.pdf", key=sk)

# 7. Videos
with st.expander("Animated Videos - Own"):
    st.write("Own animated videos - Telugu voice")

# 8. Weekly Tests
with st.expander("Weekly Tests"):
    ans = st.radio("TCS eligibility % ?", ["58%","60%"], key="test1")
    if st.button("Submit Test"):
        st.write("Correct: 58%" if ans=="58%" else "Check again")

# 9. Recommended Companies
with st.expander("Recommended Companies", expanded=True):
    if perc>=58: st.write("✅ TCS NQT")
    if "Python" in skills: st.write("✅ Accenture - Python")
    if "SQL" in skills: st.write("✅ Wipro - SQL")
    if "Java" in skills: st.write("✅ Capgemini - Java")

# 10. Host Data
with st.expander("Host Data"):
    if os.path.exists(DB_FILE):
        st.code(open(DB_FILE).read())
    else:
        st.write("No data yet")
