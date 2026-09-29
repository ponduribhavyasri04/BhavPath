import streamlit as st, csv, os, io, textwrap
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

st.set_page_config(page_title="BhavPath", layout="wide")
DB_FILE="bhavpath_data.csv"

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except: return ImageFont.load_default()

def make_easy_pdf(skill):
    db={
        "Python": ["PYTHON - EASY ENGLISH","","What is Python? Easy language for job.","print('Bhavya Ponduri') -> Shows name","perc=58","if perc>=58: print('TCS Eligible')","skills=['Python','SQL'] - List example","for loop: repeat work","def check(p): return 'Eligible' if p>=58","Interview: List mutable, Tuple fixed","Programs: Palindrome, Fibonacci"],
        "SQL": ["SQL - EASY ENGLISH","SQL stores student data","SELECT * FROM students WHERE name='Bhavya Ponduri'","WHERE perc>=58 -> TCS eligible","JOIN: Connect student + company"],
        "DBMS": ["DBMS - EASY ENGLISH","Big box to store data","Primary key = Roll Number","ACID = safe save"],
        "Java": ["JAVA - EASY ENGLISH","Class = design, Object = house","Student class has name Bhavya Ponduri"],
        "C": ["C - EASY ENGLISH","Base language","printf('Bhavya Ponduri')"],
        "C++": ["C++ - EASY ENGLISH","C + OOP","vector<string> skills"],
        "Aptitude": ["APTITUDE - EASY ENGLISH","58% needed for TCS NQT","Profit: 120-100=20","Speed=Distance/Time"]
    }
    lines=db.get(skill, db["Python"])
    W,H=1240,1754
    img=Image.new("RGB",(W,H),"white")
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,W,90], fill="#0a1628")
    d.text((40,25), f"BhavPath - {skill} - Easy English", font=get_font(26,True), fill="#6cb6ff")
    y=120
    for line in lines:
        for wl in textwrap.wrap(line, width=80) if line else [""]:
            d.text((45,y), wl, font=get_font(22), fill="black"); y+=38
    buf=io.BytesIO(); img.save(buf, format="PDF"); return buf.getvalue()

def make_gif(skill):
    texts={
        "Python": ["print('Bhavya Ponduri')","perc=58","if perc>=58:"," print('TCS Eligible')","skills=['Python','SQL']"],
        "SQL": ["SELECT * FROM students","WHERE name='Bhavya Ponduri'","WHERE perc>=58","JOIN company","Eligible"],
        "Aptitude": ["58% = Eligible","Profit = 20","Speed=D/T","TCS NQT","Easy"]
    }
    t=texts.get(skill, texts["Python"])
    frames=[]
    for i, line in enumerate(t*3):
        img=Image.new("RGB",(700,400),(10,22,40))
        d=ImageDraw.Draw(img)
        d.rectangle([0,0,700,60], fill="#0a1628")
        d.text((20,15), f"{skill} - PDF Content Animation", font=get_font(18,True), fill="#6cb6ff")
        d.rectangle([20, 100+i*5, 680, 170+i*5], fill="#1a2f4a", outline="#6cb6ff")
        d.text((30,115+i*5), line, font=get_font(22), fill="white")
        d.rectangle([20,350,20+(i+1)*40,365], fill="#6cb6ff")
        frames.append(img)
    buf=io.BytesIO()
    frames[0].save(buf, format="GIF", save_all=True, append_images=frames[1:], duration=600, loop=0)
    return buf.getvalue()

# SIDEBAR - PAGES LAGA DIVIDE
st.sidebar.title("BhavPath")
page=st.sidebar.radio("Go to", ["🏠 Home","📚 PDFs","🎬 Animations","📝 Online Test","🏢 Companies"])

if "last_saved" not in st.session_state: st.session_state.last_saved=""

# HOME
if page=="🏠 Home":
    st.markdown("<h1 style='text-align:center'>BhavPath</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#6cb6ff; font-weight:400'>What's Your Placement Story..?</h3>", unsafe_allow_html=True)
    st.divider()
    with st.container(border=True):
        c1,c2,c3=st.columns(3)
        name=c1.text_input("Name", placeholder="Ex: Bhavya Ponduri")
        perc=c2.slider("Percentage", 40, 100, 58)
        branch=c3.selectbox("Branch", ["CSE","ECE","EEE","MECH"])
        skills=st.multiselect("Skills", ["Python","SQL","DBMS","Java","C","C++","Aptitude"], default=["Python"])
        if name.strip()!="" and name!=st.session_state.last_saved:
            ex=os.path.exists(DB_FILE)
            with open(DB_FILE,"a",newline="", encoding="utf-8") as f:
                w=csv.writer(f)
                if not ex: w.writerow(["time","name","%","branch","skills"])
                w.writerow([datetime.now(), name, perc, branch, ",".join(skills)])
            st.session_state.last_saved=name
            st.toast(f"✅ Auto Saved to Host: {name}")
            st.success(f"Auto Saved to Host: {name}")

    with st.container(border=True):
        if perc>=58: st.success(f"{perc}% - Eligible for TCS NQT")
        else: st.warning(f"{perc}% - Skill based")

# PDFs
elif page=="📚 PDFs":
    st.title("📚 PDFs - Easy English with Content")
    for sk in ["Python","SQL","DBMS","Java","C","C++","Aptitude"]:
        pdf=make_easy_pdf(sk)
        st.download_button(f"📥 Download {sk} PDF - Easy English Content", pdf, f"{sk}_Easy.pdf", key=sk)

# ANIMATIONS - PDF ki thaginatu
elif page=="🎬 Animations":
    st.title("🎬 Animations - PDF ki Thaginatu")
    sel=st.selectbox("Select Subject", ["Python","SQL","DBMS","Java","C","C++","Aptitude"])
    gif=make_gif(sel)
    st.image(gif, caption=f"{sel} - Same as PDF content - Ex: Bhavya Ponduri")
    st.download_button(f"Download {sel} Animation", gif, f"{sel}.gif", key=f"gif_{sel}")

# ONLINE TEST
elif page=="📝 Online Test":
    st.title("📝 Online Test")
    QUEST={
        "Python": [("print('Bhavya Ponduri') output?", ["Bhavya Ponduri","Error"], "Bhavya Ponduri"), ("TCS %?", ["58%","90%"], "58%"), ("List symbol?", ["[]","()"], "[]")],
        "SQL": [("SQL full form?", ["Structured Query Language","Simple"], "Structured Query Language")]
    }
    sub=st.selectbox("Subject", ["Python","SQL"])
    if f"q_{sub}" not in st.session_state: st.session_state[f"q_{sub}"]=0; st.session_state[f"s_{sub}"]=0
    qs=QUEST[sub]
    idx=st.session_state[f"q_{sub}"]
    if idx < len(qs):
        q,o,a=qs[idx]
        st.write(f"Q{idx+1}: {q}")
        ch=st.radio("Answer", o, key=f"{sub}{idx}")
        if st.button("Submit", key=f"b{sub}{idx}"):
            if ch==a: st.success("Correct!"); st.session_state[f"s_{sub}"]+=1
            else: st.error(f"Correct: {a}")
            st.session_state[f"q_{sub}"]+=1; st.rerun()
    else:
        st.success(f"Score {st.session_state[f's_{sub}']}/{len(qs)}")
        if st.button("Retake"): st.session_state[f"q_{sub}"]=0; st.session_state[f"s_{sub}"]=0; st.rerun()

# COMPANIES
elif page=="🏢 Companies":
    st.title("🏢 Recommended Companies")
    perc=st.slider("Percentage", 40,100,58)
    if perc>=58: st.write("✅ TCS NQT - 58% Eligible")
    st.write("✅ Accenture - Python")
    st.write("✅ Wipro - SQL")
    st.write("✅ Capgemini - Java")
