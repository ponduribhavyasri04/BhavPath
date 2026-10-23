import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="BhavPath Premium", page_icon="🚀", layout="wide")

# ================= ADV GRAPHICS CSS - FULL PREMIUM =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { 
    background: radial-gradient(ellipse at top left, #0f0c29 0%, #302b63 40%, #24243e 80%, #000000 100%) !important;
    background-attachment: fixed !important;
}
.stApp::before {
    content: ''; position: fixed; top:0; left:0; width:100%; height:100%;
    background: 
        radial-gradient(circle at 20% 30%, rgba(102,126,234,0.18) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(118,75,162,0.18) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(240,147,251,0.12) 0%, transparent 60%);
    pointer-events: none; z-index: -1;
}
.welcome-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important;
    padding: 80px 20px !important; border-radius: 30px !important; text-align: center !important; color: white !important;
    box-shadow: 0 20px 60px rgba(102,126,234,0.6), inset 0 1px 0 rgba(255,255,255,0.3) !important;
    border: 2px solid rgba(255,255,255,0.2) !important; position: relative; overflow: hidden;
    animation: float 3s ease-in-out infinite;
}
@keyframes float { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } }
.login-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    padding: 22px !important; border-radius: 20px !important; text-align: center !important; color: white !important;
    box-shadow: 0 10px 30px rgba(102,126,234,0.5) !important; border: 1px solid rgba(255,255,255,0.2) !important;
}
.glass-premium {
    background: rgba(255,255,255,0.08) !important; backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255,255,255,0.15) !important; border-radius: 20px !important;
    padding: 20px !important; box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important; transition: 0.3s !important;
}
.glass-premium:hover { transform: translateY(-2px); box-shadow: 0 15px 40px rgba(102,126,234,0.4) !important; }
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important; border-radius: 15px !important; font-weight: 700 !important; font-size: 15px !important;
    box-shadow: 0 5px 20px rgba(102,126,234,0.4) !important; height: 75px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}
div[data-testid="stButton"] > button:hover { transform: translateY(-2px) scale(1.02) !important; box-shadow: 0 12px 30px rgba(102,126,234,0.6) !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, rgba(15,12,41,0.98) 0%, rgba(48,43,99,0.98) 100%) !important; border-right: 1px solid rgba(255,255,255,0.1) !important; }
.material-heading-main {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white;
    box-shadow: 0 10px 30px rgba(102,126,234,0.4); margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

# --- SESSION ---
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'completed' not in st.session_state: st.session_state.completed = []
if 'name' not in st.session_state: st.session_state.name = ""
if 'email' not in st.session_state: st.session_state.email = ""
if 'college' not in st.session_state: st.session_state.college = ""
if 'purpose' not in st.session_state: st.session_state.purpose = ""
if 'test_skill' not in st.session_state: st.session_state.test_skill = None
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'test_answers' not in st.session_state: st.session_state.test_answers = {}
if 'game_unlocked' not in st.session_state: st.session_state.game_unlocked = False
if 'game_score' not in st.session_state: st.session_state.game_score = 0
if 'cert_skill' not in st.session_state: st.session_state.cert_skill = None
if 'cert_stage' not in st.session_state: st.session_state.cert_stage = "select"
if 'cert_questions' not in st.session_state: st.session_state.cert_questions = []
if 'cert_answers' not in st.session_state: st.session_state.cert_answers = {}
if 'cert_score' not in st.session_state: st.session_state.cert_score = 0

# ONLY 4 SKILLS - C,C++ REMOVED
TOPICS = {
    "Python": ["Intro", "Variables", "Loops", "Functions", "Lists", "OOPS", "File Handling", "Final Boss"],
    "Java": ["Intro", "OOP", "Collections", "Threads", "Final Boss"],
    "SQL": ["Basics", "Joins", "Group By", "Having", "Window Functions", "Final Boss"],
    "DSA": ["Arrays", "Stack", "Queue", "Binary Search", "Linked List", "Final Boss"]
}

# ================= 1ST PAGE: WELCOME =================
if st.session_state.page == "welcome":
    st.markdown("""
    <div class="welcome-box">
        <div style="font-size:70px">🚀</div>
        <div style="font-size:60px; font-weight:900; text-shadow: 0 2px 20px rgba(0,0,0,0.3)">BhavPath</div>
        <div style="font-size:28px; margin-top:10px; font-weight:600">Welcome to your placement story</div>
        <div style="margin-top:10px; font-size:18px; opacity:0.9">Learn. Grind. Game. Get Placed.</div>
        <div style="margin-top:20px"><span style="background:rgba(255,255,255,0.2); padding:8px 16px; border-radius:20px; margin:5px; border:1px solid rgba(255,255,255,0.2)">🎮 Real Game</span><span style="background:rgba(255,255,255,0.2); padding:8px 16px; border-radius:20px; margin:5px">📜 AI Certificate</span><span style="background:rgba(255,255,255,0.2); padding:8px 16px; border-radius:20px; margin:5px">💼 10 LPA</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>")
    c1,c2,c3 = st.columns(3)
    with c1: st.metric("4 Skills", "Python, Java, SQL, DSA")
    with c2: st.metric("32 Modules", "Premium Content")
    with c3: st.metric("Game + Certificate", "Placement Ready")
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.page = "login"; st.rerun()
    st.stop()

# ================= 2ND PAGE: LOGIN =================
if st.session_state.page == "login":
    st.markdown('<div class="login-header"><div style="font-size:35px; font-weight:800">🚀 BhavPath</div><div>Welcome to your placement story - Premium</div></div>', unsafe_allow_html=True)
    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:white; text-align:center">🔐 Login</h3>', unsafe_allow_html=True)
        name = st.text_input("Full Name", value=st.session_state.name, placeholder="Bhavya")
        email = st.text_input("Email", value=st.session_state.email, placeholder="bhavya@college.com")
        college = st.text_input("College Name", value=st.session_state.college, placeholder="Rise College, Ongole")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if name and email and college:
                st.session_state.name = name; st.session_state.email = email; st.session_state.college = college
                st.session_state.page = "purpose"; st.rerun()
            else: st.error("Please fill all fields")
        if st.button("Back"): st.session_state.page = "welcome"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================= 3RD PAGE: PURPOSE - SHUFFLED 1ST PLACEMENT =================
if st.session_state.page == "purpose":
    st.markdown(f'<div class="login-header"><div style="font-size:30px; font-weight:800">🚀 BhavPath</div><div>Hi {st.session_state.name} - Select Your Purpose</div></div>', unsafe_allow_html=True)
    st.markdown('<h4 style="color:white">Why did you come to this link? Select Purpose:</h4>', unsafe_allow_html=True)
    st.markdown("")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("📊 Placement Percentage", use_container_width=True):
            st.session_state.purpose = "placement"; st.session_state.page = "main"; st.rerun()
    with col2:
        if st.button("📚 Skill Learning", use_container_width=True):
            st.session_state.purpose = "skill"; st.session_state.page = "main"; st.rerun()
    st.markdown("")
    col3, col4 = st.columns(2, gap="large")
    with col3:
        if st.button("📝 Test Zone", use_container_width=True):
            st.session_state.purpose = "test"; st.session_state.page = "main"; st.rerun()
    with col4:
        if st.button("📜 Certificate Zone", use_container_width=True):
            st.session_state.purpose = "certificate"; st.session_state.page = "main"; st.rerun()
    st.markdown("")
    _, mid, _ = st.columns([1,1,1])
    with mid:
        if st.button("💼 Interview Questions", use_container_width=True):
            st.session_state.purpose = "interview"; st.session_state.page = "main"; st.rerun()
        st.markdown("")
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"; st.rerun()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.markdown(f'<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 15px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 5px 20px rgba(102,126,234,0.4)"><div style="font-size:22px; font-weight:800">🚀 BhavPath Premium</div><div style="font-size:11px">Rise College</div></div>', unsafe_allow_html=True)
st.sidebar.markdown(f'<div class="glass-premium" style="margin-top:15px"><div style="color:white">👤 {st.session_state.name}</div><div style="color:#aaa; font-size:11px">📧 {st.session_state.email}</div><div style="color:#aaa; font-size:11px">🎓 {st.session_state.college}</div><div style="color:#4ade80; font-size:12px; margin-top:8px">🎯 {st.session_state.purpose}</div></div>', unsafe_allow_html=True)
st.sidebar.metric("XP", st.session_state.xp)
st.sidebar.metric("Game Score", st.session_state.game_score)
if st.sidebar.button("Change Purpose"): st.session_state.page = "purpose"; st.rerun()
if st.sidebar.button("Logout"): st.session_state.page = "welcome"; st.rerun()

# ================= 4TH PAGE: SKILL LEARNING - MATERIAL HEADING ADV GRAPHICS =================
if st.session_state.purpose == "skill":
    st.markdown("""
    <div class="material-heading-main">
        <div style="font-size:36px; font-weight:900">📚 Skill Learning Material</div>
        <div style="font-size:15px; margin-top:8px; opacity:0.9">Premium Study Materials - Python, Java, SQL, DSA - Placement Ready Content</div>
        <div style="margin-top:12px">
            <span style="background:rgba(255,255,255,0.2); padding:6px 12px; border-radius:15px; margin:3px; font-size:12px; border:1px solid rgba(255,255,255,0.2)">📖 Theory</span>
            <span style="background:rgba(255,255,255,0.2); padding:6px 12px; border-radius:15px; margin:3px; font-size:12px">💻 Code Examples</span>
            <span style="background:rgba(255,255,255,0.2); padding:6px 12px; border-radius:15px; margin:3px; font-size:12px">🎯 Interview Qs</span>
            <span style="background:rgba(255,255,255,0.2); padding:6px 12px; border-radius:15px; margin:3px; font-size:12px">🏆 Placement</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    left, middle, right = st.columns([1,2,1.2], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<h4 style="color:white; text-align:center">📁 Material List</h4>', unsafe_allow_html=True)
        selected_topic = st.radio("Select Skill", ["Python", "Java", "SQL", "DSA"])
        selected_module = st.radio(f"Materials in {selected_topic}", TOPICS[selected_topic])
        st.markdown('</div>', unsafe_allow_html=True)
    with middle:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background: rgba(102,126,234,0.15); padding: 15px; border-radius: 12px; border-left: 4px solid #667eea; margin-bottom: 15px;">
            <div style="color:#667eea; font-size:11px; font-weight:700; letter-spacing:1px">MATERIAL HEADING</div>
            <div style="color:white; font-size:22px; font-weight:800">{selected_topic} - {selected_module}</div>
            <div style="color:#aaa; font-size:11px; margin-top:5px">Topic: {selected_module} | Skill: {selected_topic} | Level: Premium | Asked: TCS, Infosys, Amazon</div>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"**What is {selected_module}?** {selected_module} is a core concept in {selected_topic}. It is frequently asked in placement interviews for Data Engineer and Software roles at TCS NQT, Infosys, Amazon for 7-15 LPA packages.")
        st.divider()
        st.markdown("##### 📖 Material Content")
        st.write(f"Detailed explanation for {selected_module}. Covers theory, practical implementation, and interview importance with real company examples.")
        st.markdown("##### 💻 Code Example With Output")
        st.code(f"# {selected_topic} - {selected_module} Example\nfor i in range(0,10,3):\n    print(i)\n\n# Output:\n# 0\n# 3\n# 6\n# 9", language="python")
        st.info("⏱️ Time: O(n) | 💾 Space: O(1) | 🎯 Interview: Frequently Asked")
        key = f"{selected_topic}-{selected_module}"
        if key not in st.session_state.completed:
            if st.button(f"✅ Mark {selected_module} Completed +50 XP", type="primary", use_container_width=True):
                st.session_state.completed.append(key); st.session_state.xp+=50; st.balloons()
        else: st.success("✅ Completed - Material Finished")
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="text-align:center; margin-bottom:15px; background: rgba(102,126,234,0.1); padding:10px; border-radius:10px">
            <div style="color:white; font-weight:700">📖 Material Details</div>
            <div style="color:#aaa; font-size:11px">Heading Info</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"- **Skill:** {selected_topic}")
        st.markdown(f"- **Heading:** {selected_module}")
        st.markdown(f"- **Level:** Premium")
        st.markdown(f"- **Placement:** TCS, Infosys")
        st.divider()
        st.markdown("##### 💻 Practice Editor")
        practice_code = st.text_area("Your Code", "for i in range(0,10,3):\n    print(i)", height=150)
        if st.button("▶️ Run Code", use_container_width=True):
            try:
                import io, sys
                old_stdout = sys.stdout; sys.stdout = buffer = io.StringIO()
                exec(practice_code); sys.stdout = old_stdout
                st.code(buffer.getvalue() or "No output")
            except Exception as e: st.error(e)
        st.markdown('</div>', unsafe_allow_html=True)

# ================= PLACEMENT =================
elif st.session_state.purpose == "placement":
    st.markdown('<div class="material-heading-main"><div style="font-size:32px; font-weight:900">📊 Placement Percentage Checker</div><div style="font-size:14px; opacity:0.9">Enter B.Tech % + Skills → Get Company List Offering Jobs</div></div>', unsafe_allow_html=True)
    COMPANIES_DB = [
        {"name": "TCS NQT", "min_btech": 60, "skills": ["Python", "SQL", "Aptitude"], "package": "3.5-7 LPA", "role": "Ninja / Digital"},
        {"name": "Infosys SP", "min_btech": 65, "skills": ["Python", "Java", "SQL"], "package": "5-9 LPA", "role": "Systems Engineer"},
        {"name": "Wipro Elite", "min_btech": 60, "skills": ["Java", "SQL"], "package": "3.5-6.5 LPA", "role": "Project Engineer"},
        {"name": "Amazon Data Engineer", "min_btech": 70, "skills": ["Python", "SQL", "Pandas"], "package": "10-15 LPA", "role": "Data Engineer"},
    ]
    left,right = st.columns([1,2], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<h4 style="color:white">📝 Enter Details</h4>', unsafe_allow_html=True)
        btech = st.number_input("B.Tech %", min_value=0, max_value=100, value=81)
        inter = st.number_input("Inter %", min_value=0, max_value=100, value=85)
        tenth = st.number_input("10th %", min_value=0, max_value=100, value=90)
        st.divider()
        skill_python = st.checkbox("Python", value=True)
        skill_java = st.checkbox("Java")
        skill_sql = st.checkbox("SQL", value=True)
        skill_pandas = st.checkbox("Pandas")
        my_skills = []
        if skill_python: my_skills.append("Python")
        if skill_java: my_skills.append("Java")
        if skill_sql: my_skills.append("SQL")
        if skill_pandas: my_skills.append("Pandas")
        check_btn = st.button("Check My Companies List", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        if check_btn:
            eligible = []
            for comp in COMPANIES_DB:
                if btech >= comp["min_btech"]:
                    match_count = len(set(my_skills) & set(comp["skills"]))
                    comp["match"] = match_count
                    comp["match_percent"] = int((match_count / len(comp["skills"]))*100) if comp["skills"] else 0
                    eligible.append(comp)
            eligible = sorted(eligible, key=lambda x: x["match_percent"], reverse=True)
            st.success(f"Eligible for {len(eligible)} companies")
            for comp in eligible:
                st.markdown('<div class="glass-premium" style="margin-bottom:12px; border-left:4px solid #4ade80">', unsafe_allow_html=True)
                st.markdown(f"### {comp['name']} - ✅ Eligible")
                st.write(f"Role: {comp['role']} | Package: {comp['package']} | Need: {comp['min_btech']}% | Yours: {btech}%")
                st.write(f"Skills: {', '.join(comp['skills'])} | Match: {comp['match_percent']}%")
                st.markdown('</div>', unsafe_allow_html=True)
        else: st.markdown('<div class="glass-premium"><div style="color:white">👈 Enter B.Tech % and Skills on left → Get premium company list offering</div></div>', unsafe_allow_html=True)

# ================= TEST + REAL GAME =================
elif st.session_state.purpose == "test":
    TEST_BANK = {
        "Python": [{"q": "What is output of range(0,10,3)?", "o": ["0,3,6,9", "0,1,2,3"], "a": "0,3,6,9"}],
        "Java": [{"q": "Java is?", "o": ["Platform Independent", "Dependent"], "a": "Platform Independent"}],
        "SQL": [{"q": "Which returns average B.Tech %?", "o": ["AVG(btech)", "SUM(btech)"], "a": "AVG(btech)"}],
        "DSA": [{"q": "Which uses LIFO?", "o": ["Stack", "Queue"], "a": "Stack"}],
    }
    st.markdown('<div class="material-heading-main"><div style="font-size:32px; font-weight:900">📝 Test Zone + 🎮 Real Game</div><div style="font-size:14px; opacity:0.9">Python, Java, SQL, DSA - Test → Unlock Premium Real Game - 0,3,6,9 Logic</div></div>', unsafe_allow_html=True)
    if not st.session_state.test_started and not st.session_state.game_unlocked:
        st.markdown('<div class="glass-premium"><h4 style="color:white">Step 1: Select Skill For Test - Python, Java, SQL, DSA</h4></div>', unsafe_allow_html=True)
        st.markdown("")
        c1,c2 = st.columns(2, gap="large")
        with c1:
            if st.button("🐍 Python", use_container_width=True): st.session_state.test_skill="Python"
            if st.button("🗄️ SQL", use_container_width=True): st.session_state.test_skill="SQL"
        with c2:
            if st.button("☕ Java", use_container_width=True): st.session_state.test_skill="Java"
            if st.button("🧠 DSA", use_container_width=True): st.session_state.test_skill="DSA"
        if st.session_state.test_skill:
            st.info(f"Selected: {st.session_state.test_skill}")
            if st.button(f"Start {st.session_state.test_skill} Test →", type="primary", use_container_width=True):
                st.session_state.test_started=True; st.session_state.test_answers={}; st.rerun()
    elif st.session_state.test_started and not st.session_state.game_unlocked:
        skill = st.session_state.test_skill
        questions = TEST_BANK.get(skill, TEST_BANK["Python"])
        for i,q in enumerate(questions):
            st.markdown('<div class="glass-premium" style="margin-top:10px">', unsafe_allow_html=True)
            st.markdown(f"**Q{i+1}. {q['q']}**")
            ans = st.radio(f"Select", q['o'], key=f"tq_{skill}_{i}", index=None)
            if ans: st.session_state.test_answers[i]=ans
            st.markdown('</div>', unsafe_allow_html=True)
        if st.button("Submit Test & Unlock Real Game Zone 🎮", type="primary", use_container_width=True):
            correct = sum(1 for idx,q in enumerate(questions) if st.session_state.test_answers.get(idx)==q['a'])
            st.session_state.xp+=correct*20
            st.session_state.game_unlocked=True
            st.session_state.test_started=False
            st.balloons()
            st.success(f"Score {correct}/{len(questions)} - Game Zone Unlocked!")
            st.rerun()
    else:
        skill = st.session_state.test_skill or "Python"
        st.success(f"Test Completed! Real Game Zone Unlocked - Skill: {skill}")
        game_html = """<!DOCTYPE html><html><head><style>body{margin:0;background: radial-gradient(ellipse at center, #1a1a4e 0%, #0f0c29 100%);display:flex;justify-content:center;align-items:center;flex-direction:column;font-family:Poppins}#gameCanvas{border:4px solid #667eea;border-radius:20px;background: radial-gradient(ellipse at center, #16213e 0%, #0f0c29 100%);box-shadow: 0 0 40px rgba(102,126,234,0.6);}#info{color:white;margin:10px;text-align:center;background:rgba(255,255,255,0.1);padding:12px 24px;border-radius:15px;backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.2)}</style></head><body><div id="info"><div>🏆 Score: <span id="score" style="color:#4ade80; font-weight:800">0</span> | 🎯 Target: <b style="color:#4ade80">0, 3, 6, 9</b> in order | ❤️ Lives: <span id="lives">3</span></div><div>Collected: <span id="collected" style="color:#fbbf24">[]</span></div></div><canvas id="gameCanvas" width="600" height="400"></canvas><div style="color:#aaa; font-size:11px; margin-top:8px">🎮 Arrow Keys / WASD / Touch Drag - GREEN 0,3,6,9 Collect - RED Bomb Avoid</div><div id="message" style="color:#fbbf24; font-weight:bold; margin-top:10px; font-size:16px; text-shadow:0 0 10px currentColor"></div><script>const canvas=document.getElementById('gameCanvas');const ctx=canvas.getContext('2d');const scoreEl=document.getElementById('score');const livesEl=document.getElementById('lives');const collectedEl=document.getElementById('collected');const messageEl=document.getElementById('message');let player={x:300,y:200,size:22,speed:6,color:'#667eea'};let keys={};let score=0;let lives=3;let collected=[];let targetSequence=[0,3,6,9];let coins=[];let gameOver=false;let win=false;function spawnCoins(){coins=[];[0,3,6,9].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:true,size:20,color:'#4ade80',collected:false})});[1,2,4,5,7,8].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:false,size:17,color:'#ef4444',collected:false})});}function drawPlayer(){ctx.shadowColor=player.color;ctx.shadowBlur=20;ctx.fillStyle=player.color;ctx.beginPath();ctx.arc(player.x,player.y,player.size,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='white';ctx.beginPath();ctx.arc(player.x-6,player.y-6,4,0,Math.PI*2);ctx.arc(player.x+6,player.y-6,4,0,Math.PI*2);ctx.fill();}function drawCoins(){coins.forEach(coin=>{if(!coin.collected){ctx.shadowColor=coin.color;ctx.shadowBlur=coin.isCorrect?15:5;ctx.fillStyle=coin.color;ctx.beginPath();ctx.arc(coin.x,coin.y,coin.size,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;ctx.strokeStyle='white';ctx.lineWidth=2;ctx.stroke();ctx.fillStyle='white';ctx.font='bold 14px Poppins';ctx.textAlign='center';ctx.fillText(coin.value,coin.x,coin.y+5);}});}function checkCollision(){coins.forEach(coin=>{if(!coin.collected){let dx=player.x-coin.x,dy=player.y-coin.y,dist=Math.sqrt(dx*dx+dy*dy);if(dist<player.size+coin.size){coin.collected=true;if(coin.isCorrect){if(collected.length<targetSequence.length&&coin.value===targetSequence[collected.length]){collected.push(coin.value);score+=25;messageEl.textContent=`✅ Correct! ${coin.value} - range(0,10,3)!`;messageEl.style.color='#4ade80';}else{messageEl.textContent=`❌ Wrong order! Need ${targetSequence[collected.length]}`;messageEl.style.color='#ef4444';lives--;}}else{score=Math.max(0,score-10);lives--;messageEl.textContent=`💥 BOMB! ${coin.value} wrong!`;messageEl.style.color='#ef4444';canvas.style.transform='translate(5px,5px)';setTimeout(()=>canvas.style.transform='translate(0,0)',100);}updateUI();checkWin();}}});}function updateUI(){scoreEl.textContent=score;livesEl.textContent=lives;collectedEl.textContent='['+collected.join(', ')+']';}function checkWin(){if(JSON.stringify(collected)===JSON.stringify(targetSequence)){win=true;messageEl.textContent='🎉 LEGENDARY WIN! 0,3,6,9 Mastered! +100 XP!';messageEl.style.color='#4ade80';for(let i=0;i<60;i++){setTimeout(()=>{ctx.fillStyle=`hsl(${Math.random()*360},100%,60%)`;ctx.beginPath();ctx.arc(Math.random()*600,Math.random()*400,6,0,Math.PI*2);ctx.fill();},i*20);}}if(lives<=0&&!win){gameOver=true;messageEl.textContent='💀 Game Over! Retry!';}}function update(){if(gameOver||win)return;if(keys['ArrowUp']||keys['w']||keys['W'])player.y-=player.speed;if(keys['ArrowDown']||keys['s']||keys['S'])player.y+=player.speed;if(keys['ArrowLeft']||keys['a']||keys['A'])player.x-=player.speed;if(keys['ArrowRight']||keys['d']||keys['D'])player.x+=player.speed;player.x=Math.max(player.size,Math.min(canvas.width-player.size,player.x));player.y=Math.max(player.size,Math.min(canvas.height-player.size,player.y));ctx.clearRect(0,0,canvas.width,canvas.height);drawCoins();drawPlayer();checkCollision();requestAnimationFrame(update);}window.addEventListener('keydown',e=>{keys[e.key]=true;});window.addEventListener('keyup',e=>{keys[e.key]=false;});canvas.addEventListener('touchmove',e=>{e.preventDefault();let r=canvas.getBoundingClientRect();let t=e.touches[0];player.x=t.clientX-r.left;player.y=t.clientY-r.top;});spawnCoins();update();</script></body></html>"""
        components.html(game_html, height=580, width=650)
        st.markdown("")
        c1,c2,c3 = st.columns(3)
        with c1: st.success("GREEN: 0,3,6,9 in order +25 XP")
        with c2: st.error("RED: 1,2,4,5,7,8 Bomb -10 XP")
        with c3: st.info("Arrow Keys / WASD / Touch")
        if st.button("Claim Win +100 XP 🏆", use_container_width=True): st.session_state.xp+=100; st.session_state.game_score+=100; st.balloons()
        if st.button("Go to Certificate →", use_container_width=True): st.session_state.purpose="certificate"; st.session_state.cert_stage="select"; st.rerun()

# ================= CERTIFICATE =================
elif st.session_state.purpose == "certificate":
    st.markdown('<div class="material-heading-main"><div style="font-size:32px; font-weight:900">📜 Certificate Zone - Premium</div><div style="font-size:14px; opacity:0.9">Random AI Interview → Premium Certificate - Placement Ready</div></div>', unsafe_allow_html=True)
    if st.session_state.cert_stage == "select":
        st.markdown('<div class="glass-premium"><h4 style="color:white">Select Skill for Certificate - Python, Java, SQL, DSA</h4></div>', unsafe_allow_html=True)
        st.markdown("")
        c1,c2 = st.columns(2, gap="large")
        with c1:
            if st.button("🐍 Python Certificate", use_container_width=True): st.session_state.cert_skill="Python"
            if st.button("☕ Java Certificate", use_container_width=True): st.session_state.cert_skill="Java"
        with c2:
            if st.button("🗄️ SQL Certificate", use_container_width=True): st.session_state.cert_skill="SQL"
            if st.button("🧠 DSA Certificate", use_container_width=True): st.session_state.cert_skill="DSA"
        if st.session_state.cert_skill:
            if st.button(f"Start AI Interview for {st.session_state.cert_skill} →", type="primary", use_container_width=True):
                qs = ["Explain range(0,10,3)?", "List vs Tuple?", "Tell about yourself?", "Why hire you?", "OOPS?", "Project?"]
                st.session_state.cert_questions=random.sample(qs, 5)
                st.session_state.cert_stage="interview"; st.session_state.cert_answers={}; st.rerun()
    elif st.session_state.cert_stage == "interview":
        for i,q in enumerate(st.session_state.cert_questions):
            st.markdown(f'<div class="glass-premium" style="margin-top:10px"><div style="color:#fbbf24">🤖 Q{i+1}: {q}</div></div>', unsafe_allow_html=True)
            ans = st.text_area(f"Answer Q{i+1}", key=f"cert_{i}", placeholder="Min 20 chars")
            if ans and len(ans)>10: st.session_state.cert_answers[i]=ans
        if len(st.session_state.cert_answers)>=3:
            if st.button("Submit & Generate Certificate", type="primary", use_container_width=True):
                score = min(100, 50 + len(st.session_state.cert_answers)*10)
                st.session_state.cert_score=score; st.session_state.cert_stage="result"; st.rerun()
    else:
        score = st.session_state.cert_score
        st.balloons()
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #fff 0%, #f0f4ff 100%); border-radius:20px; padding:40px; text-align:center; box-shadow: 0 20px 60px rgba(102,126,234,0.4); border:4px solid transparent; background-clip: padding-box; position: relative;">
            <div style="font-size:50px">🏆</div>
            <div style="font-size:36px; font-weight:900; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">BHAVPATH PREMIUM</div>
            <div style="letter-spacing:3px; color:#666; font-size:12px">CERTIFICATE OF EXCELLENCE - ADV GRAPHICS</div>
            <div style="height:3px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb); margin:20px 0; border-radius:10px"></div>
            <div style="font-size:28px; font-weight:800; color:#000">{st.session_state.name}</div>
            <div style="color:#555; font-size:13px">{st.session_state.college} | {st.session_state.email}</div>
            <div style="margin:20px; color:#333">For <b>{st.session_state.cert_skill}</b> | AI Score: <b>{score}%</b></div>
            <div style="background:#f0f4ff; padding:15px; border-radius:15px; border:1px solid #e0e7ff; color:green; font-weight:800">PLACEMENT READY - {st.session_state.cert_skill} EXPERT</div>
        </div>
        """, unsafe_allow_html=True)
        st.download_button("📥 Download Certificate", data=f"BHAVPATH PREMIUM\nName: {st.session_state.name}\nSkill: {st.session_state.cert_skill}\nScore: {score}%", file_name="BhavPath_Certificate.txt", type="primary")

# ================= INTERVIEW =================
else:
    st.markdown('<div class="material-heading-main"><div style="font-size:32px; font-weight:900">💼 Interview Questions</div><div style="font-size:14px">TCS NQT, Infosys, Wipro - Premium Q&A</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-premium"><div style="color:#4ade80; line-height:1.8">Q1: range(0,10,3) output?<br>Ans: 0,3,6,9 - Step logic<br><br>Q2: SQL AVG(btech)?<br>Ans: SELECT AVG(btech) FROM students;<br><br>Q3: OOPS 4 pillars?<br>Ans: Inheritance, Polymorphism, Encapsulation, Abstraction<br><br>Q4: Data Engineer role?<br>Ans: Python + SQL + ETL + Pandas</div></div>', unsafe_allow_html=True)
