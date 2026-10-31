import streamlit as st
import pandas as pd

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

# Force welcome as first page
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = ""
    st.session_state.selected_skill = "C"
    st.session_state.topic = ""

# BACKGROUND
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

# ================= 1. STARTING WELCOME PAGE - IDHE FIRST =================
if st.session_state.page == "welcome":
    st.markdown("""
    <div class='center' style='padding-top:22vh'>
        <h1 style='color:#c7f0ff;font-size:82px;font-weight:900;letter-spacing:-1px;'>Welcome to BhavPath</h1>
        <div class='glass' style='display:inline-block;margin-top:25px;padding:28px 50px;'>
            <h2 style='margin:0;font-size:36px;font-weight:800;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>
            What is Your Placement Story..??
            </h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    _,c,_=st.columns([1.4,1,1.4])
    with c:
        st.write(""); st.write(""); st.write("")
        if st.button("Next →", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

# ================= 2. LOGIN =================
elif st.session_state.page == "login":
    st.markdown("<div class='center'><h1 style='color:white;font-size:42px;'>Login to BhavPath</h1><p style='color:#a78bfa;'>Continue your story</p></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1.2,1,1.2])
    with col:
        st.write(""); email=st.text_input("Email"); college=st.text_input("College Name")
        st.write("")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if email and college:
                st.session_state.college=college
                st.session_state.page="purpose"; st.rerun()
            else: st.error("Enter both")
        if st.button("← Back"): st.session_state.page="welcome"; st.rerun()

# ================= 3. PURPOSE =================
elif st.session_state.page == "purpose":
    st.markdown("<div class='center'><h1 style='color:white;font-size:42px;'>What is the purpose?</h1></div>", unsafe_allow_html=True)
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

# ================= 4A. PLACEMENT WELCOME =================
elif st.session_state.page == "placement_welcome":
    st.markdown(f"<div class='center'><h1 style='color:white;'>Welcome to Placement Prediction</h1><p style='color:#a78bfa;'>{st.session_state.college}</p></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        if st.button("Next → Enter Details", use_container_width=True, type="primary"): st.session_state.page="placement_form"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

# ================= 4B. PLACEMENT FORM =================
elif st.session_state.page == "placement_form":
    st.markdown("<div class='center'><h1 style='color:white;font-size:38px;'>Enter Your Details</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.3,1])
    with col:
        name=st.text_input("1. Name"); tenth=st.number_input("2. 10th %",0.0,100.0,85.0); inter=st.number_input("3. Inter %",0.0,100.0,80.0); btech=st.number_input("4. B.Tech %",0.0,100.0,75.0); skills=st.text_input("5. Skills?", placeholder="Python, Java")
        if st.button("Continue →", use_container_width=True, type="primary"): st.session_state.pdata=(name,tenth,inter,btech,skills); st.session_state.page="placement_result"; st.rerun()

# ================= 4C. RESULT + GRAPH =================
elif st.session_state.page == "placement_result":
    name,tenth,inter,btech,skills=st.session_state.pdata; avg=(tenth+inter+btech)/3
    st.markdown(f"<div class='center'><h1 style='color:white;'>Company List for {name} - {avg:.1f}%</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        df=pd.DataFrame([["Google/Amazon","75%+"],["TCS Digital","70%+"],["Wipro","65%+"]], columns=["Company","Eligibility"])
        st.dataframe(df, use_container_width=True)
        st.bar_chart(pd.DataFrame({"Score":[tenth,inter,btech]}, index=["10th","Inter","BTech"]))
        st.progress(int(avg))
        if st.button("← Home"): st.session_state.page="welcome"; st.rerun()

# ================= 5A. WELCOMING TO TECHNICAL SKILLS =================
elif st.session_state.page == "tech_welcome":
    st.markdown("""
    <div class='center' style='padding-top:16vh'>
        <h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1>
        <div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>Master C, C++, Java, Python, SQL, DSA with Info & Diagrams</p></div>
    </div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Explore Skills →", use_container_width=True, type="primary"): st.session_state.page="tech_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

# ================= 5B. SKILLS LIST =================
elif st.session_state.page == "tech_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>BhavPath Technical Skill Page</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        c1,c2,c3,c4=st.columns(4)
        if c1.button("C", use_container_width=True): st.session_state.selected_skill="C"; st.session_state.page="skill_detail"; st.rerun()
        if c2.button("C++", use_container_width=True): st.session_state.selected_skill="C++"; st.session_state.page="skill_detail"; st.rerun()
        if c3.button("Java", use_container_width=True): st.session_state.selected_skill="Java"; st.session_state.page="skill_detail"; st.rerun()
        if c4.button("Python", use_container_width=True): st.session_state.selected_skill="Python"; st.session_state.page="skill_detail"; st.rerun()
        st.write("")
        c5,c6=st.columns(2)
        if c5.button("SQL", use_container_width=True): st.session_state.selected_skill="SQL"; st.session_state.page="skill_detail"; st.rerun()
        if c6.button("DSA", use_container_width=True): st.session_state.selected_skill="DSA"; st.session_state.page="skill_detail"; st.rerun()
        if st.button("← Back"): st.session_state.page="tech_welcome"; st.rerun()

# ================= 5C. SKILL DETAIL =================
elif st.session_state.page == "skill_detail":
    skill=st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Topics & Diagrams</h1></div>", unsafe_allow_html=True)
    topics={"C":["Intro","Data Types","Loops","Functions","Pointers","Arrays","Structures","File Handling"],"Python":["Basics","Loops","Functions","OOP","Libraries","File Handling","Django","Projects"],"Java":["Basics","OOP","Collections","Exception","Multithreading","JDBC","Spring","Projects"],"C++":["Basics","OOP","STL","Pointers","Inheritance","Polymorphism","Templates","Projects"],"SQL":["SELECT","JOINS","GROUP BY","Subqueries","Indexing","Normalization","Procedures","Projects"],"DSA":["Arrays","Linked List","Stack","Trees","Graphs","Sorting","DP","Greedy"]}
    _,c,_=st.columns([0.2,3,0.2])
    with c:
        col1,col2=st.columns([1,2])
        with col1:
            for i,t in enumerate(topics.get(skill, topics["C"]),1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True): st.session_state.topic=t
        with col2:
            st.markdown(f"<div class='glass'><h3>{st.session_state.topic or 'Select a topic'}</h3><p>Info & Diagrams for {skill} here...</p><code>Example code for {skill}</code></div>", unsafe_allow_html=True)
        if st.button("← Back"): st.session_state.page="tech_skills"; st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon 🚀</h1></div>", unsafe_allow_html=True)
    if st.button("← Back"): st.session_state.page="purpose"; st.rerun()
