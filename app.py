import streamlit as st, csv, os
from datetime import datetime
st.set_page_config(page_title="BhavPath - Placement - CodeTantra Style", layout="wide")
DB="placement_ct_home.csv"

if "name" not in st.session_state: st.session_state.name="Bhavya Ponduri"
if "perc" not in st.session_state: st.session_state.perc=58
if "page" not in st.session_state: st.session_state.page="Home"
if "fav" not in st.session_state: st.session_state.fav=[]

st.markdown("""
<style>
.ct-card{background:white; border-radius:12px; border:1px solid #ddd; text-align:center; padding:25px 10px 0 10px; height:290px; box-shadow:0 2px 10px rgba(0,0,0,0.07);}
.ct-card:hover{transform:translateY(-4px); box-shadow:0 8px 25px rgba(0,0,0,0.15);}
.ct-bottom{background:#1e3a5f; color:white; padding:13px; border-radius:0 0 12px 12px; margin:20px -10px 0 -10px; font-weight:bold; font-size:18px; letter-spacing:0.5px;}
.ct-desc{color:#555; font-size:14px; margin-top:12px; line-height:1.4; min-height:60px;}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🎯 BhavPath - Placement")
st.session_state.name = st.sidebar.text_input("Student Name", st.session_state.name)
st.session_state.perc = st.sidebar.slider("Your %", 40, 100, st.session_state.perc)
if st.session_state.fav:
    st.sidebar.markdown("### ⭐ My Favorite - Nuvvu Select Chesinavi")
    for f in st.session_state.fav: st.sidebar.write(f"✅ {f}")

# SAVE
ex=os.path.exists(DB)
with open(DB,"a",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    if not ex: w.writerow(["time","name","perc","page","fav"])
    if "last" not in st.session_state or st.session_state.last!=st.session_state.page:
        w.writerow([datetime.now(), st.session_state.name, st.session_state.perc, st.session_state.page, ",".join(st.session_state.fav)])
        st.session_state.last=st.session_state.page

# TOP BAR - CODETANTRA LIKE
st.markdown(f"""
<div style='background:#0f1e33; color:white; padding:12px 20px; border-radius:8px; display:flex; justify-content:space-between;'>
<span><b>BHAVPATH</b> 🏠 Home</span><span>{st.session_state.name.lower()}@placement.edu.in | Support | Logout</span>
</div>
""", unsafe_allow_html=True)
st.write("")

# ================= HOME - 5 CATEGORIES - PLACEMENT =================
if st.session_state.page=="Home":
    c1,c2,c3 = st.columns(3, gap="large")
    with c1:
        st.markdown("""
        <div class='ct-card'>
        <div style='font-size:70px;'>👨‍🎓💻</div>
        <div class='ct-desc'>Click here to view all your<br><b>placement courses/subjects</b><br>TCS NQT 58% | Infosys | Wipro</div>
        <div class='ct-bottom'>Placement Courses</div>
        </div>
        """, unsafe_allow_html=True)
        b1,b2 = st.columns([3,1])
        if b1.button("Open", key="o1", use_container_width=True): st.session_state.page="Courses"; st.rerun()
        if b2.checkbox("⭐", key="f1"): 
            if "Placement Courses" not in st.session_state.fav: st.session_state.fav.append("Placement Courses")

    with c2:
        st.markdown("""
        <div class='ct-card'>
        <div style='font-size:70px;'>📝👩‍💻</div>
        <div class='ct-desc'>Click here to view all your<br><b>scheduled and completed placement tests</b><br>Aptitude | Technical | HR</div>
        <div class='ct-bottom'>Placement Tests</div>
        </div>
        """, unsafe_allow_html=True)
        b1,b2 = st.columns([3,1])
        if b1.button("Open", key="o2", use_container_width=True): st.session_state.page="Tests"; st.rerun()
        if b2.checkbox("⭐", key="f2"): 
            if "Placement Tests" not in st.session_state.fav: st.session_state.fav.append("Placement Tests")

    with c3:
        st.markdown("""
        <div class='ct-card'>
        <div style='font-size:70px;'>⌨️👩‍💻</div>
        <div class='ct-desc'>Click here to view all your<br><b>placement programming labs</b><br>Python for TCS | SQL for Wipro</div>
        <div class='ct-bottom'>Placement Labs</div>
        </div>
        """, unsafe_allow_html=True)
        b1,b2 = st.columns([3,1])
        if b1.button("Open", key="o3", use_container_width=True): st.session_state.page="Labs"; st.rerun()
        if b2.checkbox("⭐", key="f3"): 
            if "Placement Labs" not in st.session_state.fav: st.session_state.fav.append("Placement Labs")

    st.write("")
    c4,c5,c6 = st.columns([1,1,1], gap="large")
    with c4:
        st.markdown("""
        <div class='ct-card'>
        <div style='font-size:70px;'>🖥️📱</div>
        <div class='ct-desc'>Click here to access <b>placement tools.</b><br>Predictor | 40 Pages Books | Resume</div>
        <div class='ct-bottom'>Placement Tools</div>
        </div>
        """, unsafe_allow_html=True)
        b1,b2 = st.columns([3,1])
        if b1.button("Open", key="o4", use_container_width=True): st.session_state.page="Tools"; st.rerun()
        if b2.checkbox("⭐", key="f4"): 
            if "Placement Tools" not in st.session_state.fav: st.session_state.fav.append("Placement Tools")
    with c5:
        st.markdown("""
        <div class='ct-card'>
        <div style='font-size:70px;'>💬📞</div>
        <div class='ct-desc'>Click here to reach us<br><b>Placement Help & Support</b><br>58% Eligible - Bhavya Ponduri</div>
        <div class='ct-bottom'>Placement Support</div>
        </div>
        """, unsafe_allow_html=True)
        b1,b2 = st.columns([3,1])
        if b1.button("Open", key="o5", use_container_width=True): st.session_state.page="Support"; st.rerun()
        if b2.checkbox("⭐", key="f5"): 
            if "Placement Support" not in st.session_state.fav: st.session_state.fav.append("Placement Support")
    with c6:
        st.info(f"👋 {st.session_state.name}\n\n**Nuvvu select chesina favorites:**\n{', '.join(st.session_state.fav) if st.session_state.fav else 'Inka em select cheyaledu - ⭐ tick chey'}\n\n**{st.session_state.perc}% Batch - TCS Eligible**")
        if st.button("Clear Favorites"): st.session_state.fav=[]; st.rerun()

# ================= PAGES - PLACEMENT CONTENT =================
elif st.session_state.page=="Courses":
    if st.button("⬅️ Back to Home"): st.session_state.page="Home"; st.rerun()
    st.title("📚 Placement Courses - TCS NQT 58%")
    st.success(f"{st.session_state.name} - {st.session_state.perc}% - ✅ Eligible for TCS NQT (58% min)")
    tab1, tab2, tab3 = st.tabs(["TCS NQT", "Infosys", "Wipro"])
    with tab1: st.write("TCS NQT Criteria: 58% minimum - Your %: 58% - Python, SQL"); st.code("if perc>=58: print('TCS Eligible - Bhavya')")
    with tab2: st.write("Infosys: Python + DBMS"); st.code("print('Infosys Ready')")
    with tab3: st.write("Wipro: SQL + Aptitude"); st.code("SELECT * FROM students WHERE perc>=58;")

elif st.session_state.page=="Tests":
    if st.button("⬅️ Back to Home"): st.session_state.page="Home"; st.rerun()
    st.title("📝 Placement Tests - Scheduled & Completed")
    st.write("**TCS NQT Mock Test**")
    q1=st.radio("Q1: TCS min %?", ["58%","60%","75%"], index=0)
    q2=st.radio("Q2: 58% + Python = Eligible?", ["Yes","No"], index=0)
    if st.button("Submit Test", type="primary"):
        st.balloons(); st.success(f"Score 100/100 - {st.session_state.name} - Placement Ready!")

elif st.session_state.page=="Labs":
    if st.button("⬅️ Back to Home"): st.session_state.page="Home"; st.rerun()
    st.title("⌨️ Placement Programming Labs - 58% Batch")
    left,mid,right = st.columns([1,2,1])
    with left: q=st.radio("Lab List", ["Q1: 58% Eligibility Code","Q2: Print Bhavya","Q3: TCS Pattern","Q4: SQL 58%","Q5: Placement Loop"])
    with mid:
        st.markdown(f"**Problem: {q}**")
        st.code(f"# {q}\nname='{st.session_state.name}'\nperc={st.session_state.perc}\nif perc>=58:\n print(f'{{name}} - TCS Eligible')", language="python")
        st.text_area("Code Editor - CodeTantra Style", "print('Bhavya Ponduri - Placement Lab - Pass')", height=180)
        if st.button("▶️ Run Lab"): st.success("Output: Bhavya Ponduri - TCS Eligible - Lab Pass")
        if st.button("✅ Submit Lab", type="primary"): st.success("Lab Submitted +10 Score")
    with right: st.metric("Lab Score", "75/100"); st.progress(75); st.success("✅ 58% Test Pass")

elif st.session_state.page=="Tools":
    if st.button("⬅️ Back to Home"): st.session_state.page="Home"; st.rerun()
    st.title("🛠️ Placement Tools")
    c1,c2=st.columns(2)
    with c1:
        st.markdown("#### 🔮 Placement Predictor")
        chance = min(95, 30 + (st.session_state.perc-40) + 20)
        st.metric("Your Chance", f"{chance}%")
        st.progress(chance)
        if st.session_state.perc>=58: st.success("✅ TCS NQT Eligible - 58% Criteria")
    with c2:
        st.markdown("#### 📚 40 Pages Real Books")
        st.write("Python, SQL, Aptitude - Each page real code with Bhavya example")
        if st.button("Generate Placement Book 40 Pages"):
            st.success("PDF Ready - Download in old version")

else:
    if st.button("⬅️ Back to Home"): st.session_state.page="Home"; st.rerun()
    st.title("💬 Placement Support")
    st.info(f"Student: {st.session_state.name} | {st.session_state.perc}% | 58% Batch | Issue: Placement Eligible?")
    st.write("Contact: BhavPath - CodeTantra Placement Model")
    if os.path.exists(DB):
        with open(DB,"r") as f: st.text_area("Host Data", f.read()[-1000:], height=200)
