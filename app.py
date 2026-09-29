import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io, textwrap, csv, os, random
from datetime import datetime

st.set_page_config(page_title="BhavPath", layout="wide")
DB_FILE = "bhavpath_data.csv"

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except: return ImageFont.load_default()

def make_pdf(skill):
    W,H=1240,1754
    img=Image.new("RGB",(W,H),"white")
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,W,90], fill="#0a1628")
    d.text((40,25), f"BhavPath - {skill}", font=get_font(26,True), fill="#6cb6ff")
    data={
        "Python": "Python:\n- Variables, Loops, If Else, Functions\n- List, Dict, Tuple\n- OOP, File Handling\n- Programs: Palindrome, Fibonacci, Factorial\n- Interview Q: List vs Tuple",
        "SQL": "SQL:\n- SELECT, WHERE, JOINS\n- GROUP BY, Subquery\n- Important Queries",
        "DBMS": "DBMS:\n- ER Diagram, Keys\n- Normalization, ACID",
        "Java": "Java:\n- OOP, Collections\n- Exception Handling",
        "C": "C:\n- Pointers, Structures",
        "C++": "C++:\n- OOP, STL",
        "Aptitude": "Aptitude:\n- %, Profit Loss, Time Speed\n- Blood Relation, Series"
    }
    y=130
    for line in data.get(skill,data["Python"]).split("\n"):
        for wl in textwrap.wrap(line, width=80):
            d.text((40,y), wl, font=get_font(20), fill="black")
            y+=34
    buf=io.BytesIO()
    img.save(buf, format="PDF")
    return buf.getvalue()

def make_animation(skill):
    frames=[]
    W,H=640,360
    for i in range(20):
        img=Image.new("RGB",(W,H),(10,22,40))
        d=ImageDraw.Draw(img)
        # moving circle
        x=50+i*20
        d.ellipse([x,100,x+80,180], fill="#6cb6ff")
        d.text((20,20), f"BhavPath - {skill} Animation", font=get_font(22,True), fill="white")
        d.text((20,250), f"Own Animated Video - {skill} - Frame {i+1}", font=get_font(18), fill="#a0c8ff")
        d.rectangle([20,300,W-20,310], fill="#333")
        d.rectangle([20,300,20+i*30,310], fill="#6cb6ff")
        frames.append(img)
    buf=io.BytesIO()
    frames[0].save(buf, format="GIF", save_all=True, append_images=frames[1:], duration=150, loop=0)
    return buf.getvalue()

# QUESTIONS FOR ONLINE TEST
QUESTIONS = {
    "Python": [
        ("What is output of print(2**3)?", ["6","8","9","Error"], "8"),
        ("Which is mutable?", ["Tuple","String","List","Int"], "List"),
        ("TCS NQT eligibility %?", ["50%","58%","60%","75%"], "58%"),
        ("Keyword to define function?", ["func","def","function","define"], "def"),
        ("Ex: Bhavya list? ", ["( )","{ }","[ ]","< >"], "[ ]")
    ],
    "SQL": [
        ("SELECT is used to?", ["Delete","Fetch data","Update","Create"], "Fetch data"),
        ("Which JOIN returns all?", ["INNER","LEFT","FULL OUTER","RIGHT"], "FULL OUTER"),
        ("Primary key can be null?", ["Yes","No","Sometimes","Depends"], "No")
    ],
    "Aptitude": [
        ("50% of 200?", ["50","100","150","200"], "100"),
        ("Profit if CP 100 SP 120?", ["10%","20%","30%","50%"], "20%")
    ]
}

# TOP - ONLY 2 LINES
st.markdown("<h1 style='text-align:center; margin-bottom:0px'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#6cb6ff; font-weight:400; margin-top:5px'>What's Your Placement Story..?</h3>", unsafe_allow_html=True)
st.divider()

# 1. FORM
with st.container(border=True):
    c1,c2,c3=st.columns(3)
    name=c1.text_input("Name", placeholder="Ex: Bhavya Ponduri")
    perc=c2.slider("Percentage", 40, 100, 58)
    branch=c3.selectbox("Branch", ["CSE","ECE","EEE","MECH","CIVIL"])
    skills=st.multiselect("Skills", ["Python","SQL","DBMS","Java","C","C++","Aptitude"], default=["Python"])
    if st.button("Save Story"):
        ex=os.path.exists(DB_FILE)
        with open(DB_FILE,"a",newline="") as f:
            w=csv.writer(f)
            if not ex: w.writerow(["time","name","%","branch","skills"])
            w.writerow([datetime.now(),name,perc,branch,",".join(skills)])
        st.success(f"Saved {name}")

# 2. Eligibility
with st.expander("Eligibility Check", expanded=True):
    if perc>=58: st.success(f"{perc}% - Eligible for TCS NQT (58% criteria)")
    else: st.warning(f"{perc}% - Focus on skill based companies")
    st.write(f"Name: {name} | Skills: {', '.join(skills)}")

# 3. Details
with st.expander("Details As Per Placements"):
    st.table([{"Stage":"Aptitude","Time":"30 min daily"},{"Stage":"Coding","Time":"1 language strong - Python"},{"Stage":"Interview","Time":"Story: Bhavya Ponduri example"}])

# 4. PDFs
with st.expander("PDFs - Python, SQL, DBMS, Java, C, C++, Aptitude", expanded=True):
    cols=st.columns(4)
    for i,sk in enumerate(["Python","SQL","DBMS","Java","C","C++","Aptitude"]):
        with cols[i%4]:
            pdf=make_pdf(sk)
            st.download_button(f"📄 {sk} PDF", pdf, f"{sk}.pdf", key=f"pdf_{sk}")

# 5. ANIMATED VIDEOS - OWN - NOT EMPTY
with st.expander("Animated Videos - Own - Telugu", expanded=True):
    st.write("Own created animations - No YouTube - Host lo ne")
    v1,v2=st.columns(2)
    sel=v1.selectbox("Select Subject", ["Python","SQL","Java","DBMS"])
    if v2.button(f"Generate {sel} Animation"):
        with st.spinner("Making animation..."):
            gif=make_animation(sel)
            st.image(gif, caption=f"{sel} - Own Animation - BhavPath")
            st.download_button(f"Download {sel} Animation", gif, f"{sel}_animation.gif", key=f"gif_{sel}")

    st.divider()
    # Show all animations preview
    c1,c2,c3=st.columns(3)
    for idx,sk in enumerate(["Python","SQL","Java"]):
        with [c1,c2,c3][idx]:
            gif=make_animation(sk)
            st.image(gif, caption=f"{sk}")

# 6. ONLINE TEST - NOT EMPTY NOW
with st.expander("Online Test - Weekly Tests", expanded=True):
    st.subheader("Online Test - Real Quiz")
    test_sub=st.selectbox("Choose Test", ["Python","SQL","Aptitude"])
    if f"score_{test_sub}" not in st.session_state:
        st.session_state[f"score_{test_sub}"]=0
        st.session_state[f"q_{test_sub}"]=0

    qs=QUESTIONS.get(test_sub, QUESTIONS["Python"])
    q_idx=st.session_state[f"q_{test_sub}"]

    if q_idx < len(qs):
        q, opts, ans = qs[q_idx]
        st.write(f"Q{q_idx+1}: {q}")
        choice=st.radio("Select", opts, key=f"opt_{test_sub}_{q_idx}")
        if st.button("Submit Answer", key=f"sub_{test_sub}_{q_idx}"):
            if choice==ans:
                st.success("Correct!")
                st.session_state[f"score_{test_sub}"]+=1
            else:
                st.error(f"Wrong! Correct: {ans}")
            st.session_state[f"q_{test_sub}"]+=1
            st.rerun()
    else:
        st.success(f"Test Completed! Score: {st.session_state[f'score_{test_sub}']}/{len(qs)}")
        if st.button("Retake Test", key=f"retake_{test_sub}"):
            st.session_state[f"q_{test_sub}"]=0
            st.session_state[f"score_{test_sub}"]=0
            st.rerun()

# 7. Companies
with st.expander("Recommended Companies", expanded=True):
    if perc>=58: st.write("✅ TCS NQT - Eligible (58%)")
    if "Python" in skills: st.write("✅ Accenture - Python")
    if "SQL" in skills: st.write("✅ Wipro - SQL + DBMS")
    if "Java" in skills: st.write("✅ Capgemini - Java")
    if perc<58: st.write("⚠️ Focus: Startup + Skill based companies")
