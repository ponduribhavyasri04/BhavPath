import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import zipfile, io

st.set_page_config(page_title="BhavPath Placement Predictor", layout="wide", page_icon="🎯")

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except:
        return ImageFont.load_default() 

ALL_DATA = {
"Python": [("Python Intro",["Created by Guido 1991","High level easy","Used in AI Web DataScience","Fast development"],["print('Hello Bhavya - Welcome to BhavPath')"],["Hello Bhavya"]),("Variables & DataTypes",["Variable stores data","int float str bool list dict","Dynamic typing"],["name='Bhavya'\nperc=58\nprint(name,perc)"],["Bhavya 58"]),("Operators",["+ - * / %","==!= > <","and or not"],["a=58\nb=60\nprint(a>=58)"],["True"]),("If Else",["Decision making","if elif else","Indentation must"],["perc=58\nif perc>=58:\n print('Eligible TCS NQT')\nelse:\n print('Try')"],["Eligible TCS NQT"]),("For & While Loops",["Repeat tasks","range(5)","break continue"],["for i in range(1,6):\n print(i)"],["1 2 3 4 5"]),("Lists",["Mutable [1,2,3]","append pop sort reverse","Slicing"],["marks=[58,60,65,70]\nprint(max(marks))"],["70"]),("Dictionary & Set",["Dict key:value","Set unique","Tuple immutable"],["student={'name':'Bhavya','perc':58}\nprint(student['name'])"],["Bhavya"]),("Strings",["upper lower split","f-string"],["s='BhavPath'\nprint(s.upper())"],["BHAVPATH"]),("Functions",["def reusable","return"],["def eligible(p):\n return p>=58\nprint(eligible(58))"],["True"]),("File Handling",["open read write"],["f=open('a.txt','w')\nf.write('Bhavya')"],["File created"]),("Oops",["Class Object","Inheritance"],["class Student:\n def __init__(self,n):\n self.name=n"],["Object"]),("Exception",["try except finally"],["try:\n x=10/0\nexcept:\n print('Error')"],["Error"]),("Modules",["import math random pandas"],["import math\nprint(math.sqrt(64))"],["8.0"]),("NQT Python",["TCS NQT easy Python","Input output"],["n=int(input())\nif n>=58:\n print('Eligible')"],["Eligible"]),("Project",["BhavPath app","Streamlit project"],["print('Build BhavPath app')"],["Build app"])],
"SQL": [("SQL Intro",["Structured Query Language","RDBMS"],["SELECT * FROM Students;"],["Data"]),("SELECT WHERE",["Get filter"],["SELECT * WHERE perc>=58;"],["Filtered"]),("JOIN",["Combine tables - TCS Fav"],["SELECT * FROM S JOIN M ON id;"],["Joined"]),("GROUP BY",["COUNT SUM AVG"],["SELECT branch, AVG(perc) GROUP BY branch;"],["Grouped"]),("SQL for NQT",["Easy score"],["SELECT COUNT(*) WHERE perc>=58;"],["Count"])],
"DBMS": [("DBMS Intro",["Store manage data"],["DBMS"],["Stored"]),("Keys",["Primary Foreign"],["PRIMARY KEY"],["Key"]),("Normalization",["1NF 2NF 3NF"],["Normalized"],["Clean"]),("ACID",["Safe transaction"],["ACID"],["Safe"])],
"Java": [("Java Intro",["James Gosling WORA OOPs"],["System.out.println(\"Bhavya\");"],["Bhavya"]),("If Else",["Condition"],["if(perc>=58) System.out.println(\"Eligible\");"],["Eligible"])],
"C": [("C Intro",["Dennis Ritchie 1972 Mother language"],["printf(\"Bhavya\");"],["Bhavya"])],
"Cpp": [("Cpp Intro",["Bjarne Stroustrup C+OOPs"],["cout<<\"Bhavya\";"],["Bhavya"])],
"Aptitude": [("Percentages",["Per 100 (Val/Total)*100","58% = 58/100"],["58% to 60% need 2"],["60%"]),("Profit Loss",["SP-CP Profit"],["CP100 SP120 Profit20%"],["20%"]),("Time Speed",["Speed=Dist/Time"],["Dist 120"],["120km"]),("NQT Pattern",["Apt 20 Reas 30 Verbal 20","58% best NQT"],["NQT crack"],["Crack"])],
"DataScience": [("DS Intro",["Data + Science High salary"],["import pandas"],["Done"])],
"AIML": [("AI Intro",["AI human like machine","ML learn from data"],["AI"],["Smart"])],
}
COMPANIES={"TCS NQT":58,"Wipro":60,"Infosys":60,"Cognizant":60,"Capgemini":60,"HCL":60,"Accenture":65,"IBM":65,"Deloitte":60,"Amazon":65,"TCS Digital":70,"Microsoft":70}

def make_pdf(course, data, name, perc, branch):
    W,H=800,1100
    pages=[]
    img=Image.new("RGB",(W,H),"white")
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,W,70], fill="#0a1628")
    d.text((20,22), f"BhavPath - {name} - {perc}% | {course} Notes", font=get_font(11,True), fill="#6cb6ff")
    y=90
    d.text((25,y), "BhavPath Placement Predictor", font=get_font(16,True), fill="#0a1628"); y+=35
    d.text((25,y), f"Where is your Placement Story..? - {name}'s Story", font=get_font(12,True), fill="#1565c0"); y+=30
    d.text((25,y), f"Name: {name} | Branch: {branch} | Percentage: {perc}%", font=get_font(11,True), fill="black"); y+=28
    d.text((25,y), f"Your Placement DNA for {perc}%:", font=get_font(12,True), fill="#2e7d32"); y+=25
    for comp,cut in COMPANIES.items():
        if int(perc)>=cut:
            d.text((35,y), f"✅ {comp} ({cut}%) - ELIGIBLE", font=get_font(10), fill="black"); y+=20
    pages.append(img)
    for i in range(15):
        title,theory,code,out = data[i % len(data)]
        img=Image.new("RGB",(W,H),"white")
        d=ImageDraw.Draw(img)
        d.rectangle([0,0,W,60], fill="#0a1628")
        d.text((20,18), f"BhavPath - {course} - Page {i+2} | {name} | {perc}%", font=get_font(10,True), fill="#6cb6ff")
        d.rectangle([20,75,W-20,108], fill="#e3f2fd")
        d.text((30,83), f"Topic {i+1}: {title}", font=get_font(11,True), fill="#0a1628")
        y=125
        d.text((25,y), "Theory:", font=get_font(10,True), fill="black"); y+=18
        for t in theory[:4]:
            d.text((30,y), f"• {t}", font=get_font(9), fill="#222"); y+=14
        y+=6
        d.rectangle([25,y,W-25,y+75], fill="#0a1628")
        d.text((35,y+5), "CODE:", font=get_font(9,True), fill="#6cb6ff")
        d.text((35,y+22), "\n".join(code)[:250], font=get_font(8), fill="white")
        y+=85
        d.rectangle([25,y,W-25,y+50], fill="#e8f5e9", outline="#4caf50")
        d.text((35,y+5), "OUTPUT:", font=get_font(9,True), fill="#2e7d32")
        d.text((35,y+22), "\n".join(out)[:200], font=get_font(8), fill="black")
        d.text((25,H-18), f"{name} | {branch} | {perc}% | BhavPath | Page {i+2}", font=get_font(7), fill="#888")
        pages.append(img)
    fname=f"{course}_{name}.pdf"
    pages[0].save(fname, save_all=True, append_images=pages[1:])
    return fname

# ===== UI =====
st.markdown("<h1 style='text-align:center;color:#0a1628;'>BhavPath Placement Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#1e88e5;'>Where is your Placement Story..? 🚀</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Enter your details and generate your Placement DNA + Full 15 Pages Notes</p>", unsafe_allow_html=True)
st.write("")

c1,c2,c3 = st.columns(3)
with c1:
    name = st.text_input("Your Name", placeholder="Ex : Bhavya Ponduri")
with c2:
    perc = st.text_input("Your Percentage", placeholder="Ex : 58")
with c3:
    branch = st.text_input("Your Branch", placeholder="Ex : CSE / AIML")

course = st.selectbox("Select Course", list(ALL_DATA.keys()))

st.write("")
if st.button("🧬 Generate Your Placement DNA", type="primary", use_container_width=True):
    if not name or not perc:
        st.error("Name & Percentage enter chey Bhavya!")
    else:
        pdf=make_pdf(course, ALL_DATA[course], name, int(perc) if perc.isdigit() else 58, branch or "CSE")
        with open(pdf,"rb") as f:
            st.download_button(f"📥 Download {course} PDF - Your Placement DNA - {name}", f, file_name=pdf, mime="application/pdf", use_container_width=True)
        st.success(f"Your Placement DNA Generated Bhavya! {perc}% Eligible List inside PDF!")
        st.balloons()

if st.button("📦 Generate All 9 PDFs at Once", use_container_width=True):
    if not name:
        st.error("Name enter chey!")
    else:
        zbuf=io.BytesIO()
        with zipfile.ZipFile(zbuf,"w") as z:
            for c in ALL_DATA.keys():
                f=make_pdf(c, ALL_DATA[c], name, int(perc) if perc and perc.isdigit() else 58, branch or "CSE")
                z.write(f)
        zbuf.seek(0)
        st.download_button("📦 Download All 9 PDFs ZIP", zbuf, file_name=f"BhavPath_All_{name}.zip", mime="application/zip", use_container_width=True)

st.divider()
if perc and perc.isdigit():
    st.subheader(f"🎯 {name or 'You'} ({perc}%) Your DNA Says Eligible For:")
    cols=st.columns(2)
    i=0
    for comp,cut in COMPANIES.items():
        if int(perc)>=cut:
            cols[i%2].write(f"✅ {comp} ({cut}%)")
            i+=1
