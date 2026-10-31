Idhe rey FINAL over all code! Nee paper lo flow motham same - *Welcome -> Login -> Purpose -> Placement + Technical Skills Welcome + Graph* - motham okate `app.py` file lo.

*Pages folder unte delete chesi, okka `app.py` matrame pettu, idhi paste chey:*
import streamlit as st
import pandas as pd

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

# --- SESSION ---
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'selected_skill' not in st.session_state: st.session_state.selected_skill = "C"
if 'topic' not in st.session_state: st.session_state.topic = ""

# --- COMMON BACKGROUND (Nee Blue-Pink Graphics) ---
st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:25px;border-radius:22px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def header(title, sub=""):
    st.markdown(f"<div class='center'><h1 style='color:white;font-size:42px;font-weight:900;'>{title}</h1><p style='color:#a78bfa;'>{sub}</p></div>", unsafe_allow_html=True)

# ================= 1. WELCOME PAGE =================
if st.session_state.page == "welcome":
    st.markdown("""
    <div class='center' style='padding-top:20vh'>
        <h1 style='color:#c7f0ff;font-size:78px;font-weight:900;'>Welcome to BhavPath</h1>
        <div class='glass' style='display:inline-block;margin-top:20px;'><h2 style='margin:0;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:34px;'>What is Your Placement Story..??</h2></div>
    </div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c: 
        st.write(""); st.write("")
        if st.button("Next →", use_container_width=True): st.session_state.page="login"; st.rerun()

# ================= 2. LOGIN PAGE =================
elif st.session_state.page == "login":
    header("Login to BhavPath", "As per your paper - Step 2")
    _,col,_=st.columns([1.2,1,1.2])
    with col:
        st.write("")
        email=st.text_input("Email"); college=st.text_input("College Name")
        st.write("")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if email and college: st.session_state.college=college; st.session_state.page="purpose"; st.rerun()
            else: st.error("Enter Email & College")
        if st.button("← Back"): st.session_state.page="welcome"; st.rerun()

# ================= 3. WHAT IS THE PURPOSE =================
elif st.session_state.page == "purpose":
    header("What is the purpose?", "Your paper Step 3")
    _,col,_=st.columns([1,1.5,1])
    with col:
        st.write("")
        c1,c2=st.columns(2)
        with c1:
            if st.button("📈 Placement Prediction", use_container_width=True): st.session_state.page="placement_welcome"; st.rerun()
            st.write("")
            if st.button("🧠 Test Zone", use_container_width=True): st.session_state.page="coming_soon"; st.rerun()
        with c2:
            if st.button("💻 Technical Skills", use_container_width=True): st.session_state.page="tech_welcome"; st.rerun()
            st.write("")
            if st.button("💼 Interview + Code", use_container_width=True): st.session_state.page="coming_soon"; st.rerun()

# ================= 4A. PLACEMENT - WELCOMING PAGE =================
elif st.session_state.page == "placement_welcome":
    header("Welcome to Placement Prediction", f"Hello {st.session_state.college} Student!")
    st.markdown("<div class='center glass' style='width:600px;margin:30px auto;'>We will predict eligible companies based on % + Skills</div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        if st.button("Next → Enter Details", use_container_width=True, type="primary"): st.session_state.page="placement_form"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

# ================= 4B. PLACEMENT FORM =================
elif st.session_state.page == "placement_form":
    header("Enter Your Details", "1.Name 2.10th 3.Inter 4.BTech 5.Skills")
    _,col,_=st.columns([1,1.3,1])
    with col:
        name=st.text_input("1. Name"); tenth=st.number_input("2. 10th %",0.0,100.0,85.0); inter=st.number_input("3. Inter %",0.0,100.0,80.0); btech=st.number_input("4. B.Tech %",0.0,100.0,75.0); skills=st.text_input("5. Skills known?", placeholder="Python, Java, SQL")
        if st.button("Continue → Show Companies", use_container_width=True, type="primary"): st.session_state.pdata=(name,tenth,inter,btech,skills); st.session_state.page="placement_result"; st.rerun()

# ================= 4C. COMPANY LIST + GRAPH =================
elif st.session_state.page == "placement_result":
    name,tenth,inter,btech,skills=st.session_state.pdata; avg=(tenth+inter+btech)/3
    header(f"Company Eligibility for {name}", f"Avg: {avg:.1f}% + Skills: {skills}")
    companies=[]
    if avg>=75: companies.append(["Google/Amazon","75%+ + Python","High"])
    if avg>=70: companies.append(["TCS Digital","70%+","Medium"])
    if avg>=65: companies.append(["TCS Ninja/Wipro","65%+","Easy"])
    if avg>=60: companies.append(["Capgemini","60%+","Easy"])
    df=pd.DataFrame(companies, columns=["Company","Eligibility","Chance"])
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        st.write(""); st.dataframe(df, use_container_width=True)
        st.write(""); st.write("**Nenu Graph Chesi Cheptha:**")
        st.bar_chart(pd.DataFrame({"Score":[tenth,inter,btech]}, index=["10th","Inter","BTech"]))
        st.progress(int(avg))
        if st.button("← Start Again"): st.session_state.page="welcome"; st.rerun()

# ================= 5A. WELCOMING TO BHAVPATH TECHNICAL SKILLS =================
elif st.session_state.page == "tech_welcome":
    st.markdown("""
    <div class='center' style='padding-top:16vh'>
        <h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1>
        <div class='glass' style='display:inline-block;margin-top:25px;max-width:700px;'><p style='color:#c7f0ff;font-size:18px;margin:0;'>Master <b>C, C++, Java, Python, SQL, DSA</b> with Topic-wise Info, Diagrams & Code</p><p style='color:#fef08a;margin-top:10px;font-weight:600;'>Your Coding Journey Starts Here 🚀</p></div>
    </div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Explore Skills →", use_container_width=True, type="primary"): st.session_state.page="tech_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

# ================= 5B. TECHNICAL SKILLS LIST =================
elif st.session_state.page == "tech_skills":
    header("BhavPath Technical Skill Page", "Select a skill")
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        st.write("")
        c1,c2,c3,c4=st.columns(4)
        if c1.button("C", use_container_width=True): st.session_state.selected_skill="C"; st.session_state.page="skill_detail"; st.rerun()
        if c2.button("C++", use_container_width=True): st.session_state.selected_skill="C++"; st.session_state.page="skill_detail"; st.rerun()
        if c3.button("Java", use_container_width=True): st.session_state.selected_skill="Java"; st.session_state.page="skill_detail"; st.rerun()
        if c4.button("Python", use_container_width=True): st.session_state.selected_skill="Python"; st.session_state.page="skill_detail"; st.rerun()
        st.write("")
        c5,c6=st.columns(2)
        if c5.button("SQL", use_container_width=True): st.session_state.selected_skill="SQL"; st.session_state.page="skill_detail"; st.rerun()
        if c6.button("DSA", use_container_width=True): st.session_state.selected_skill="DSA"; st.session_state.page="skill_detail"; st.rerun()
        st.write("")
        if st.button("← Back to Welcome"): st.session_state.page="tech_welcome"; st.rerun()

# ================= 5C. SKILL DETAIL - TOPICS + DIAGRAMS =================
elif st.session_state.page == "skill_detail":
    skill=st.session_state.selected_skill
    header(f"{skill} - Topics & Explanation", "Incase select [C] -> C Topics 1-8 & Explanation with Info & Diagrams")
    topics={"C":["Intro","Data Types","Loops","Functions","Pointers","Arrays","Structures","File Handling"],"Python":["Basics","Loops","Functions","OOP","Libraries","File Handling","Django","Projects"],"Java":["Basics","OOP","Collections","Exception","Multithreading","JDBC","Spring","Projects"],"C++":["Basics","OOP","STL","Pointers","Inheritance","Polymorphism","Templates","Projects"],"SQL":["SELECT","JOINS","GROUP BY","Subqueries","Indexing","Normalization","Procedures","Projects"],"DSA":["Arrays","Linked List","Stack & Queue","Trees","Graphs","Sorting","DP","Greedy"]}
    _,c,_=st.columns([0.2,3,0.2])
    with c:
        col1,col2=st.columns([1,2])
        with col1:
            st.markdown(f"<div class='glass'><h3>{skill} Topics (1-8)</h3></div>", unsafe_allow_html=True)
            for i,t in enumerate(topics.get(skill, topics["C"]),1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True): st.session_state.topic=t
        with col2:
            st.markdown(f"<div class='glass'><h3>Explanation with Info & Diagrams</h3><p>Selected: <b>{st.session_state.topic or 'Select a topic left side'}</b></p><p>This is {skill} explanation area. Here you add Info + Diagrams + Code. Same for all Skills as per your paper.</p><br><code>Example code for {skill}...</code></div>", unsafe_allow_html=True)
        st.write("")
        if st.button("← Back to Skills"): st.session_state.page="tech_skills"; st.rerun()

else:
    header("Coming Soon 🚀")
    if st.button("← Back"): st.session_state.page="purpose"; st.rerun()
*Nee paper flow motham set:*
- Welcome -> Login -> Purpose (4 options)
- Placement -> Welcome -> Form (Name,10th,Inter,BTech,Skills) -> Company list + Graph
- Technical Skills -> *Welcoming to BhavPath Technical Skills* -> C,C++,Java,Python,SQL,DSA -> Topics 1-8 + Explanation with Diagrams

Commit kottu, full neat ga same alane vastadi!
