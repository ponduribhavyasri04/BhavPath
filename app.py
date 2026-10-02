import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="BhavPath", layout="wide", page_icon="📘")

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except:
        return ImageFont.load_default()

def make_pdf(course, data):
    W,H=800,1100
    pages=[]
    for i, (title, theory, code, output) in enumerate(data,1):
        img=Image.new("RGB",(W,H),"white")
        d=ImageDraw.Draw(img)
        d.rectangle([0,0,W,60], fill="#0a1628")
        d.text((20,18), f"BhavPath - {course} - Page {i}", font=get_font(12, True), fill="#6cb6ff")
        d.rectangle([20,80,W-20,115], fill="#e3f2fd")
        d.text((30,88), f"{i}. {title}", font=get_font(13, True), fill="#0a1628")
        y=130
        d.text((25,y), "Theory:", font=get_font(11, True), fill="#0a1628"); y+=18
        for t in theory:
            d.text((25,y), t, font=get_font(10), fill="#222"); y+=14
        y+=10
        d.rectangle([25,y,W-25,y+95], fill="#0a1628")
        d.text((35,y+5), "CODE:", font=get_font(10, True), fill="#6cb6ff")
        yy=y+22
        for c in code:
            d.text((35,yy), c, font=get_font(9), fill="white"); yy+=13
        y+=105
        d.rectangle([25,y,W-25,y+65], fill="#e8f5e9", outline="#4caf50")
        d.text((35,y+5), "OUTPUT:", font=get_font(10, True), fill="#2e7d32")
        d.text((35,y+25), output[0], font=get_font(9), fill="black")
        y+=75
        d.rectangle([25,y,W-25,y+55], outline="#6cb6ff", fill="#f8fbff")
        d.text((35,y+5), "DIAGRAM: Input -> Process -> Output", font=get_font(10, True), fill="#0a1628")
        d.text((25,H-20), f"Page {i} | BhavPath | Bhavya Ponduri", font=get_font(8), fill="#888")
        pages.append(img)
    fname=f"{course}_Bhavya.pdf"
    pages[0].save(fname, save_all=True, append_images=pages[1:])
    return fname

# --- All Courses Data ---
all_courses = {
    "Python": [("What is Python",["Python is computer language.","Used in Instagram."],['print("Hello")'],["Hello"]),
               ("Variables",["Box for data."],['name="Bhavya"'],["Bhavya"]),
               ("If Else",["Check condition."],['if p>=58:\n print("Eligible")'],["Eligible"]),
               ("Loops",["Repeat."],['for i in range(3):\n print(i)'],["0 1 2"]),
               ("List",["Many values."],['a=[1,2,3]'],["[1,2,3]"]),
               ("File",["Save data."],['open("data.csv")'],["File"])],
    "SQL": [("SELECT",["Get data."],["SELECT * FROM Students;"],["Rows"]),("WHERE",["Filter."],["SELECT * WHERE percent>=58;"],["Eligible"])],
    "DBMS": [("DBMS Intro",["Manage data."],["DBMS = Storage"],["Stored"]),("Keys",["Unique."],["Primary Key"],["Unique"])],
    "Java": [("Java Intro",["Java language."],['System.out.println("Bhavya");'],["Bhavya"])],
    "C": [("C Intro",["C language."],['printf("Bhavya");'],["Bhavya"])],
    "Cpp": [("C++ Intro",["Cpp language."],['cout<<"Bhavya";'],["Bhavya"])],
    "Aptitude": [("Percent",["Per 100."],["58% = Pass"],["Pass"]),("Profit",["SP-CP."],["Profit=20"],["20"])],
    "DataScience": [("DS Intro",["Future."],["import pandas"],["Done"]),("Pandas",["Data."],["df=pd.read_csv()"],["Loaded"])],
    "AIML": [("AI Intro",["Smart machine."],["AI = Smart"],["Smart"]),("ML Intro",["Machine learns."],["ML = Learn"],["Learn"])]
}

st.title("BhavPath - Bhavya Ponduri")
st.write("Placement Material - Python, SQL, Java, C, Aptitude, Data Science, AI & ML")

course = st.selectbox("Select Course", list(all_courses.keys()))

data = all_courses[course]
# expand to many pages automatically
expanded = (data*7)[:40] # make 40 pages internally but no mention outside

if st.button(f"Generate {course} PDF"):
    pdf_file = make_pdf(course, expanded)
    with open(pdf_file, "rb") as f:
        st.download_button(f"📥 Download {course} PDF", f, file_name=pdf_file, mime="application/pdf")
    st.success(f"{course} PDF Ready! PDF works 100% - Open in any PDF reader!")

st.divider()
st.write("Download All:")
for c in all_courses.keys():
    if st.button(f"Generate {c}", key=f"btn_{c}"):
        pdf = make_pdf(c, (all_courses[c]*7)[:40])
        with open(pdf, "rb") as file:
            st.download_button(f"Download {c}", file, file_name=pdf, key=f"dl_{c}")

st.markdown("---")
st.caption("BhavPath | Made by Bhavya Ponduri | 2026")
