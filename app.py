import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #FFFFFF !important; }
h1,h2,h3,p,div,span,label { color: #0F172A !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 18px; border: 1px solid #E2E8F0; margin-bottom: 14px; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 12px; padding: 14px; }
.blue-card b { color: #FFFFFF !important; }
.help-card { background: #EFF6FF !important; border: 1px solid #BFDBFE; border-radius: 12px; padding: 14px; margin-bottom: 12px; }
.content-card { background: #F8FAFC !important; border-left: 4px solid #2563EB; border-radius: 8px; padding: 14px; margin-bottom: 12px; }
.syntax-card { background: #F0FDF4 !important; border-left: 4px solid #22C55E; border-radius: 8px; padding: 14px; margin-bottom: 12px; }
.feature-card { background: #FFFBEB !important; border-left: 4px solid #F59E0B; border-radius: 8px; padding: 14px; margin-bottom: 12px; }
.cert-card { background: #FFFBEB !important; border: 3px solid #FFB300; border-radius: 16px; padding: 20px; text-align: center; }
div[data-baseweb="select"] > div { background-color: #FFFFFF !important; color: #000000 !important; border: 1px solid #CBD5E1 !important; }
.stCodeBlock { background-color: #F8FAFC !important; }
.stButton>button { background: #2563EB !important; color: white !important; border-radius: 10px; font-weight: 700 !important; height: 42px; }
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state: st.session_state.logged = False
if 'user' not in st.session_state: st.session_state.user = {}
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'topic' not in st.session_state: st.session_state.topic = "Python - 8 Modules"
if 'mod' not in st.session_state: st.session_state.mod = 0
if 'done' not in st.session_state: st.session_state.done = {}
if 'won' not in st.session_state: st.session_state.won = False

TOPICS = {
    "Python - 8 Modules": {
        "short": "Python", "title": "Python - 8 Modules - Data Science", "about": "Guido 1991. Easy, trending 2025.",
        "modules": [
            {"name": "1. Intro to Python", "what_is": "Python high-level, easy syntax, interpreted. No semicolon, only indentation! Libraries: Pandas, Numpy, TensorFlow.", "syntax": "print('Hello Python')\n# No #include needed", "features": "Easy, huge libraries, interpreted, dynamic typing, 8-15 LPA", "applications": "Data Science, AI/ML, Web - For 81% MUST", "code": "print('Hello BhavPath!')\nname='Bhav'\nbtech=81\nprint(f'{name} - {btech}% - Rise College')", "interview_q": "Q: Who invented Python? A: Guido van Rossum 1991", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum"},
            {"name": "2. Variables", "what_is": "Variable = memory name. No declaration needed - Dynamic! btech=81, name='Bhav'", "syntax": "btech=81\nname='Bhav'\ncollege='Rise College'", "features": "No int needed, dynamic typing, f-string", "applications": "Store student data, Data Science df['btech']=81", "code": "btech=81\nname='Bhav'\nprint(f'{name} - {btech}%')", "interview_q": "Q: Dynamic typing? A: Same var can hold int then string", "q": "Python var?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81"},
            {"name": "3. List & Dict", "what_is": "list Mutable [] marks=[81,75,80] Can change. dict Key-value {} student={'name':'Bhav','btech':81} Fast lookup!", "syntax": "marks=[81,75,80]\nstudent={'name':'Bhav','btech':81}", "features": "list mutable [], dict key-value {}, df is list of dicts", "applications": "Marks avg, student data, Data Science", "code": "marks=[81,75,80,85]\nstudent={'name':'Bhav','btech':81}\nprint(f'Avg: {sum(marks)/len(marks)}%')", "interview_q": "Q: List vs tuple? A: list mutable [] can change", "q": "Mutable?", "opts": ["list", "tuple"], "ans": "list"},
            {"name": "4. Loops - Final Boss", "what_is": "Loop = Repeat. for i in range(0,10,3): -> 0 3 6 9 coins! Final Boss logic! range(0,10,1) -> 0-9 all", "syntax": "for i in range(0,10,3):\n    print(i, end=' ') # 0 3 6 9", "features": "range(start, stop, step) 0 3 6 9 optimal for Final Boss", "applications": "Final Boss coins at 0,3,6,9, loop marks", "code": "print('Final Boss - Coins at 0,3,6,9')\nfor i in range(0,10,3):\n    print(i, end=' ') # 0 3 6 9", "interview_q": "Q: range(0,10,3)? A: 0 3 6 9 start 0 stop 10 exclusive step 3", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9"},
            {"name": "5. Pandas - DE Must", "what_is": "Pandas for DE! pd.read_csv, df['btech'].mean(), groupby. Must for 8-15 LPA", "syntax": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75,80]})", "features": "DataFrame table, Series column, read_csv, mean, groupby", "applications": "Eligible filter df[df['btech']>=60], avg per college", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75,80]})\nprint(f'Mean: {df[\"btech\"].mean()}%')", "interview_q": "Q: DataFrame? A: Table rows and columns", "q": "Pandas mean?", "opts": ["df['btech'].mean()", "mean(df)"], "ans": "df['btech'].mean()"},
        ]
    },
    "C Programming": {"short": "C", "title": "C - Mother Language", "about": "Dennis Ritchie 1972", "modules": [{"name": "1. Intro", "what_is": "C procedural by Dennis Ritchie 1972 Mother language", "syntax": "#include <stdio.h>\nint main(){ printf('Hello C'); return 0; }", "features": "Procedural, fast, foundation", "applications": "OS, Embedded", "code": "printf('Hello C');", "interview_q": "Q: Who invented C? A: Dennis Ritchie 1972", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie"}]},
    "Data Engineering": {"short": "Data Eng", "title": "Data Engineering - 8-15 LPA", "about": "SQL, Python, ETL, Spark", "modules": [{"name": "1. SQL", "what_is": "SELECT, WHERE filter, GROUP BY group, ORDER BY sort 80% interviews", "syntax": "SELECT name, btech FROM students WHERE btech>=60", "features": "SELECT, WHERE, GROUP BY, ORDER BY", "applications": "Eligible SELECT * WHERE btech>=60", "code": "SELECT * FROM students WHERE btech>=60 ORDER BY btech DESC;", "interview_q": "Q: WHERE vs HAVING? A: WHERE before GROUP BY", "q": "WHERE for?", "opts": ["Filter", "Group"], "ans": "Filter"}]},
}
TOPICS["C++ - Gaming"] = TOPICS["C Programming"]
TOPICS["Java - Android"] = TOPICS["C Programming"]
TOPICS["Software Eng"] = TOPICS["Data Engineering"]

ADS = [
    {"title": "TCS NQT 2025", "desc": "60% eligibility? You have 81%! Official TCS NQT apply page - 8 LPA package", "cta": "Apply on TCS Official →", "url": "https://nextstep.tcs.com/campus/"},
    {"title": "Python Docs", "desc": "Official Python docs - Free learning for Data Science", "cta": "Learn on Python.org →", "url": "https://docs.python.org/3/"},
    {"title": "SQL Tutorial", "desc": "Learn SQL free - Must for Data Engineering 8-15 LPA", "cta": "Learn SQL →", "url": "https://www.w3schools.com/sql/"},
]

if not st.session_state.logged:
    st.title("🚀 BhavPath")
    c1, c2 = st.columns([1,1], gap="large")
    with c1:
        email = st.text_input("Email", placeholder="bhav@gmail.com")
        college = st.text_input("College", placeholder="Rise College, Ongole")
        btech = st.slider("BTech %", 0, 100, 81)
        if st.button("Start Learning →", use_container_width=True, type="primary"):
            if email and "@" in email and college:
                st.session_state.user = {"email": email, "college": college, "btech": btech, "name": email.split("@")[0]}
                st.session_state.logged = True
                st.rerun()
    with c2:
        st.markdown("""
        <div class="white-card">
        <h3>🚀 Welcome to BhavPath</h3>
        <p>• 6 Topics - Python, C, C++, Java, Data Eng, Software Eng</p>
        <p>• 8 Modules per topic - Easy to hard - Full content after select</p>
        <p>• What is, Syntax, Features, Applications, Code, Interview Q</p>
        <p>• Practice quiz + Final Boss Game + Certificate</p>
        <p>• Clickable official links - TCS NQT Apply Now -> New tab</p>
        <p>• Clean, spacious, no eruku eruku</p>
        </div>
        """, unsafe_allow_html=True)
    st.stop()

st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | {st.session_state.topic}</b></div>', unsafe_allow_html=True)
done_count = len([k for k in st.session_state.done if st.session_state.done[k]])
st.progress(min(done_count/6, 1.0))
st.caption(f"Progress: {done_count} modules | Game unlocks at 3")

col_left, col_right = st.columns([1, 2.8], gap="large")

with col_left:
    st.subheader("📚 Topics - All List")
    for tname, tdata in TOPICS.items():
        if st.session_state.topic == tname:
            st.markdown(f'<div class="blue-card"><b>📖 {tdata["short"]} ✅</b><br>{tname}</div>', unsafe_allow_html=True)
        else:
            if st.button(f"{tdata['short']}", key=f"btn_{tname}", use_container_width=True):
                st.session_state.topic = tname
                st.session_state.mod = 0
                st.rerun()
    st.divider()
    st.subheader("🔗 Helpful Links")
    st.caption("Click -> Official website new tab lo open")
    for ad in ADS:
        st.markdown(f'<div class="help-card"><b>{ad["title"]}</b><br><span style="font-size:12px;">{ad["desc"]}</span></div>', unsafe_allow_html=True)
        st.link_button(ad["cta"], ad["url"], use_container_width=True)
        st.write("")
    if st.button("Logout", use_container_width=True):
        st.session_state.logged = False
        st.rerun()

with col_right:
    t = TOPICS[st.session_state.topic]
    st.title(f"📘 {t['title']}")
    st.caption(f"{t['about']} | For {st.session_state.user['btech']}% | {len(t['modules'])} Modules")
    
    mod_names = [m["name"] for m in t["modules"]]
    sel = st.selectbox(f"Select Module ({len(mod_names)} total) - Content below will change:", range(len(mod_names)), format_func=lambda x: mod_names[x], index=st.session_state.mod)
    st.session_state.mod = sel
    mod = t["modules"][sel]
    
    st.divider()
    st.subheader(f"📖 Content After Selecting: {mod['name']}")
    st.markdown(f'<div class="content-card"><b>📌 What is {mod["name"]}?</b><br><br>{mod["what_is"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="syntax-card"><b>📝 Syntax - How to write?</b><br><br>{mod["syntax"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="feature-card"><b>⭐ Features - Why important?</b><br><br>{mod["features"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="white-card"><b>🚀 Applications - For {st.session_state.user["btech"]}% profile</b><br><br>{mod["applications"]}</div>', unsafe_allow_html=True)
    
    st.subheader("💻 Code Example")
    st.code(mod["code"], language="python")
    st.markdown(f'<div class="white-card"><b>🎤 Interview Q&A</b><br>{mod["interview_q"]}</div>', unsafe_allow_html=True)
    
    st.divider()
    col_prev, col_done, col_next = st.columns([1,1,1])
    with col_prev:
        if sel>0 and st.button("← Prev", use_container_width=True): st.session_state.mod-=1; st.rerun()
    with col_done:
        key = f"{st.session_state.topic}_{sel}"
        if st.session_state.done.get(key): st.success("✅ Done +50 XP")
        else:
            if st.button(f"Mark Done +50 XP 🔥", use_container_width=True, type="primary"): st.session_state.done[key]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
    with col_next:
        if sel < len(mod_names)-1 and st.button("Next →", use_container_width=True): st.session_state.mod+=1; st.rerun()
    
    st.divider()
    tab1, tab2 = st.tabs(["🧠 Practice Quiz", "🎮 Final Boss & Certificate"])
    with tab1:
        st.write(f"**Q: {mod['q']}**")
        choice = st.radio("Choose:", mod["opts"], key=f"q_{sel}")
        if st.button("Check Answer", key=f"chk_{sel}"):
            if choice==mod["ans"]: st.success(f"✅ Correct! {mod['ans']} +20 XP"); st.session_state.xp+=20; st.balloons()
            else: st.error(f"❌ Wrong! Correct: {mod['ans']}")
    with tab2:
        if done_count < 3:
            st.warning(f"🔒 Locked - Complete {3-done_count} more modules. Current: {done_count}/3")
        else:
            st.success(f"🔥 Unlocked! {done_count} modules done!")
            st.write("Coins at 0,3,6,9 - Need for loop with step 3 - for(i=0;i<10;i+=3) -> 0 3 6 9")
            step = st.slider("for(i=0; i<10; i+=?)", 1,5,3, key="game")
            if st.button("PLAY FINAL BOSS 🔥", use_container_width=True):
                coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
                st.write(f"Path: {path} | Collected: {coll}/4")
                if coll==4: st.balloons(); st.success(f"SLAYED! +200 XP"); st.session_state.xp+=200; st.session_state.won=True; st.snow()
                else: st.error(f"Need i+=3 - Got {coll}/4")
            if st.session_state.won:
                today = date.today().strftime("%d-%m-%Y")
                st.markdown(f'<div class="cert-card"><div style="font-size:20px;font-weight:900;">🏆 CERTIFICATE 🏆</div><div>BhavPath</div><div style="background:white;border-radius:12px;padding:12px;margin:8px 0;"><div>{st.session_state.user["name"]} - {st.session_state.user["college"]} - {st.session_state.user["btech"]}%</div><div style="font-weight:800;">{st.session_state.topic} - Complete</div><div>XP: {st.session_state.xp} | Date: {today} | Grade: A+ 🔥</div></div></div>', unsafe_allow_html=True)
                cert_text = f"Certificate\nName: {st.session_state.user['name']}\nCollege: {st.session_state.user['college']}\nBTech: {st.session_state.user['btech']}%\nTopic: {st.session_state.topic}\nXP: {st.session_state.xp}\nDate: {today}"
                st.download_button("📥 Download Certificate", data=cert_text, file_name=f"Certificate_{st.session_state.topic}.txt", mime="text/plain", use_container_width=True)
