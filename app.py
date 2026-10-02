import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import zipfile
import io

st.set_page_config(page_title="BhavPath Placement Predictor", layout="wide", page_icon="🎯")

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except:
        return ImageFont.load_default()

# All 9 Courses Data
ALL_DATA = {
    "Python": [("Python Intro",["Python easy lang"],["print('Hello')"],["Hello"]),("Variables",["Store data"],['name="Bhavya"'],["Bhavya"]),("If Else",["Condition"],['if p>=58:\n print("Eligible")'],["Eligible"]),("Loops",["Repeat"],['for i in range(3): print(i)'],["0 1 2"]),("List",["Many values"],['a=[1,2,3]'],["[1,2,3]"])],
    "SQL": [("SELECT",["Get data"],["SELECT * FROM Students;"],["Rows"]),("WHERE",["Filter"],["WHERE percent>=58;"],["Filtered"]),("JOIN",["Combine"],["JOIN Marks ON id;"],["Joined"])],
    "DBMS": [("DBMS",["Manage data"],["DBMS = Storage"],["Stored"]),("Keys",["Unique ID"],["Primary Key"],["Unique"]),("Normalization",["Remove duplicate"],["1NF 2NF 3NF"],["Clean"])],
    "Java": [("Java Intro",["Java lang"],['System.out.println("Bhavya");'],["Bhavya"]),("If Else",["Check"],['if(p>=58) print("Eligible");'],["Eligible"])],
    "C": [("C Intro",["C lang"],['printf("Bhavya");'],["Bhavya"]),("Pointers",["Address"],['int *p;'],["Pointer"])],
    "Cpp": [("Cpp Intro",["Cpp lang"],['cout<<"Bhavya";'],["Bhavya"]),("OOPs",["Class Object"],['class Student{};'],["Class"])],
    "Aptitude": [("Percentages",["Per 100"],["58% = Pass"], ["Pass"]),("Profit Loss",["SP-CP"],["Profit=SP-CP"],["20"]),("Time Speed",["Speed"], ["Speed=Dist/Time"], ["Result"])],
    "DataScience": [("DS Intro",["Future"],["import pandas"],["Done"]),("Pandas",["Data"],["pd.read_csv()"],["Loaded"]),("ML Basic",["Learn"],["model.fit()"],["Trained"])],
    "AIML": [("AI Intro",["Smart Machine"],["AI = Smart"],["Smart"]),("ML Intro",["Learn"],["ML learns"],["Learns"]),("Deep Learning",["Brain"],["Neural Network"],["AI"])]
}

COMPANIES = {"TCS NQT":58,"Wipro":60,"Infosys":60,"Cognizant":60,"Capgemini":60,"HCL":60,"Tech Mahindra":60,"Accenture":65,"IBM":65,"Deloitte":60,"Amazon":65,"TCS Digital":70,"Microsoft":70,"Infosys SP":68}

def make_one_pdf(course, data, name, percent, branch):
    W,H=800,1100
    pages=[]
    # Page 1 - Student
    img=Image.new("RGB",(W,H),"white")
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,W,60], fill="#0a1628")
    d.text((20,18), f"BhavPath - {name} - {percent}% | {course}", font=get_font(11, True), fill="#6cb6ff")
    y=80
    d.text((25,y), f"Placement Predictor Report", font=get_font(14, True), fill="#0a1628"); y+=35
    d.text((25,y), f"Name: {name} | Branch: {branch} | Percentage: {percent}%", font=get_font(11), fill="black"); y+=35
    d.text((25,y), f"Eligible Companies for {percent}%:", font=get_font(12, True), fill="#2e7d32"); y+=28
    for comp,cut in COMPANIES.items():
        if percent>=cut:
            if y>1000:
                pages.append(img)
                img=Image.new("RGB",(W,H),"white")
                d=ImageDraw.Draw(img)
                y=20
            d.text((35,y), f"✅ {comp} ({cut}%)", font=get_font(10), fill="black"); y+=20
    pages.append(img)
    # Course pages
    for i,(title,theory,code,output) in enumerate(data,2):
        img=Image.new("RGB",(W,H),"white")
        d=ImageDraw.Draw(img)
        d.rectangle([0,0,W,60], fill="#0a1628")
        d.text((20,18), f"BhavPath - {course} - Page {i} | {name}", font=get_font(10, True), fill="#6cb6ff")
        d.rectangle([20,80,W-20,110], fill="#e3f2fd")
        d.text((30,88), f"{title}", font=get_font(12, True), fill="#0a1628")
        y=125
        d.text((25,y), "Theory:", font=get_font(10, True), fill="black"); y+=16
        for t in theory: d.text((25,y), t, font=get_font(9), fill="#222"); y+=14
        y+=5
        d.rectangle([25,y,W-25,y+75], fill="#0a1628")
        d.text((35,y+5), "CODE:", font=get_font(9, True), fill="#6cb6ff")
        d.text((35,y+22), code[0], font=get_font(8), fill="white")
        y+=85
        d.rectangle([25,y,W-25,y+50], fill="#e8f5e9", outline="#4caf50")
        d.text((35,y+5), "OUTPUT:", font=get_font(9, True), fill="#2e7d32")
        d.text((35,y+22), output[0], font=get_font(8), fill="black")
        d.text((25,H-20), f"{name} | {branch} | BhavPath", font=get_font(7), fill="#888")
        pages.append(img)
    fname=f"{course}_{name}.pdf"
    pages[0].save(fname, save_all=True, append_images=pages[1:])
    return fname

# ===== UI =====
st.title("BhavPath Placement Predictor")
st.subheader("What is your Placement Story..? 🚀")
st.write("")

c1,c2,c3 = st.columns(3)
with c1:
    name = st.text_input("Your Name", placeholder="Ex : Bhavya Ponduri")
with c2:
    percent_str = st.text_input("Your Percentage", placeholder="Ex : 58")
with c3:
    branch = st.text_input("Your Branch", placeholder="Ex : CSE / AIML")

try: percent = int(percent_str) if percent_str else 58
except: percent = 58

st.divider()

tab1, tab2 = st.tabs(["📘 Single Course PDF", "📦 All 9 PDFs ZIP"])

with tab1:
    course = st.selectbox("Select Course", list(ALL_DATA.keys()), placeholder="Ex : Python")
    data = (ALL_DATA[course]*8)[:15]
    if st.button(f"Generate {course} PDF", type="primary", use_container_width=True):
        if not name: st.error("Name enter chey!")
        else:
            pdf = make_one_pdf(course, data, name, percent, branch or "CSE")
            with open(pdf,"rb") as f:
                st.download_button(f"📥 Download {course} PDF for {name}", f, file_name=pdf, mime="application/pdf", use_container_width=True)
            st.success("Done!")
            st.subheader(f"🎯 {name} ({percent}%) Eligible For:")
            for n,c in COMPANIES.items():
                if percent>=c: st.write(f"✅ {n} ({c}%)")
            st.balloons()

with tab2:
    st.write("Generate All 9 Courses at once with your details")
    if st.button("Generate All 9 PDFs ZIP", type="primary", use_container_width=True):
        if not name: st.error("Name enter chey!")
        else:
            files=[]
            for course in ALL_DATA.keys():
                data=(ALL_DATA[course]*8)[:15]
                fname=make_one_pdf(course, data, name, percent, branch or "CSE")
                files.append(fname)
            # Create ZIP
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as z:
                for f in files:
                    z.write(f)
            zip_buffer.seek(0)
            st.download_button("📦 Download All 9 PDFs ZIP", zip_buffer, file_name=f"BhavPath_All_{name}.zip", mime="application/zip", use_container_width=True)
            st.success(f"All 9 PDFs Generated for {name}!")
            for course in ALL_DATA.keys():
                with open(f"{course}_{name}.pdf","rb") as f:
                    st.download_button(f"Download {course}", f, file_name=f"{course}_{name}.pdf", key=f"dl_{course}")

st.caption("BhavPath | Bhavya Ponduri | Placement Predictor 2026")
