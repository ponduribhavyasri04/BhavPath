import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - Clean", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #FCFC !important; }
h1,h2,h3,p,div,span { color: #111111 !important; }
h1 { color: #0F172A !important; font-weight: 800 !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 12px; padding: 14px; }
.blue-card b { color: #FFFFFF !important; }
.cert-card { background: #FFFBEB !important; border: 2px solid #F59E0B; border-radius: 16px; padding: 20px; text-align: center; }
.stButton>button { background: #2563EB !important; color: white !important; border-radius: 10px; font-weight: 700 !important; height: 42px; }
.stTabs [data-baseweb="tab-list"] { gap: 8px; }
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state: st.session_state.logged = False
if 'user' not in st.session_state: st.session_state.user = {}
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'topic' not in st.session_state: st.session_state.topic = "Python"
if 'mod' not in st.session_state: st.session_state.mod = 0
if 'done' not in st.session_state: st.session_state.done = {}
if 'won' not in st.session_state: st.session_state.won = False

TOPICS = {
    "Python": {
        "title": "Python - For Data Science",
        "about": "Easy, powerful, trending 2025. For your 81% profile, Python is MUST.",
        "modules": [
            {"name": "Intro", "content": "Python by Guido 1991. No semicolon, only indentation. Used for Data Science, AI. Libraries: Pandas, Numpy.", "code": "print('Hello Python')\nprint('BhavPath - Easy')", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum"},
            {"name": "Variables", "content": "No type needed! btech=81, name='Bhav'. Dynamic. Same variable can hold different types.", "code": "btech=81\nname='Bhav'\nprint(f'{name} {btech}%')", "q": "Python variable?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81"},
            {"name": "List & Dict", "content": "list = [81,75,80] mutable. dict = {'name':'Bhav','btech':81} key-value. Most used in Data Science.", "code": "marks=[81,75,80]\nprint(f'Avg: {sum(marks)/len(marks)}')", "q": "Mutable?", "opts": ["list", "tuple"], "ans": "list"},
            {"name": "Loops - Final Boss", "content": "for i in range(0,10,3): -> 0 3 6 9 coins! This is Final Boss logic! range(0,10,1) -> 0-9 all.", "code": "for i in range(0,10,3):\n    print(i, end=' ') # 0 3 6 9", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9"},
            {"name": "Pandas", "content": "Pandas for DE! pd.read_csv, df['btech'].mean(), groupby. Must for 8-15 LPA role.", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())", "q": "Pandas mean?", "opts": ["df['btech'].mean()", "mean(df)"], "ans": "df['btech'].mean()"},
        ]
    },
    "C Programming": {"title": "C - Mother Language", "about": "Dennis Ritchie 1972. Fast, close to hardware.", "modules": [
        {"name": "Intro", "content": "C is procedural, mother of all languages. Used for OS, Embedded.", "code": "#include <stdio.h>\nint main(){ printf('Hello C'); return 0; }", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie"},
        {"name": "Loops - Final Boss", "content": "for(i=0;i<10;i+=3) -> 0 3 6 9 coins! Final Boss logic from C!", "code": "for(int i=0;i<10;i+=3) printf('%d ', i); // 0 3 6 9", "q": "i+=3?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9"},
    ]},
    "Data Engineering": {"title": "Data Engineering - 8-15 LPA", "about": "Build pipelines. Tools: SQL, Python, Spark, Cloud. Highest demand 2025.", "modules": [
        {"name": "SQL Basics", "content": "SELECT, WHERE filter, GROUP BY group, ORDER BY sort. 80% interviews ask SQL!", "code": "SELECT * FROM students WHERE btech>=60 ORDER BY btech DESC;", "q": "WHERE for?", "opts": ["Filter", "Group"], "ans": "Filter"},
        {"name": "ETL", "content": "Extract: pd.read_csv, Transform: df['eligible']=df['btech']>=60, Load: df.to_csv. BhavPath is ETL!", "code": "df['eligible']=df['btech']>=60\nprint(df)", "q": "ETL Load?", "opts": ["Store to warehouse", "Get data"], "ans": "Store to warehouse"},
    ]},
}
TOPICS["C++"] = TOPICS["C Programming"]
TOPICS["C++"]["title"] = "C++ - Gaming Engines"
TOPICS["Java"] = TOPICS["C Programming"]
TOPICS["Java"]["title"] = "Java - Android + Enterprise"
TOPICS["Software Engineering"] = TOPICS["Data Engineering"]
TOPICS["Software Engineering"]["title"] = "Software Engineering - SDLC"

if not st.session_state.logged:
    st.title("🚀 BhavPath")
    st.caption("Clean, simple, no clumsy - Only 2 pages total")
    c1, c2 = st.columns([1,1], gap="large")
    with c1:
        st.markdown('<div class="white-card"><h2>Login</h2><p>Enter details - Direct main app</p></div>', unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="bhav@gmail.com")
        college = st.text_input("College", placeholder="Rise College, Ongole")
        btech = st.slider("BTech %", 0, 100, 81)
        if st.button("Start Learning →", use_container_width=True):
            if email and college and "@" in email:
                st.session_state.user = {"email": email, "college": college, "btech": btech, "name": email.split("@")[0]}
                st.session_state.logged = True
                st.rerun()
            else:
                st.error("Enter valid email")
    with c2:
        st.markdown("""
        <div class="white-card">
        <h3>✨ Clean Design</h3>
        <p>• No eruku eruku - Lots of space</p>
        <p>• Only 2 pages - Login + Main</p>
        <p>• Left: Topics (6 topics)</p>
        <p>• Right: Content with tabs</p>
        <p>• Game + Certificate at bottom - Same page</p>
        <br>
        <h3>📚 Topics</h3>
        <p>• Python - Data Science</p>
        <p>• C, C++, Java</p>
        <p>• Data Engineering - 8-15 LPA</p>
        <p>• Software Engineering - SDLC</p>
        </div>
        """, unsafe_allow_html=True)
    st.stop()

st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</b></div>', unsafe_allow_html=True)
done_count = len([k for k in st.session_state.done if st.session_state.done[k]])
st.write(f"Progress: {done_count} modules done | Game unlocks at 3 modules")
st.progress(min(done_count/5, 1.0))
col_left, col_right = st.columns([1, 2.5], gap="large")

with col_left:
    st.subheader("Topics")
    for tname in TOPICS.keys():
        is_sel = st.session_state.topic == tname
        if is_sel:
            st.markdown(f'<div class="blue-card"><b>📖 {tname} ✅</b><br>{TOPICS[tname]["title"]}</div>', unsafe_allow_html=True)
        else:
            if st.button(f"{tname}", key=f"btn_{tname}", use_container_width=True):
                st.session_state.topic = tname
                st.session_state.mod = 0
                st.rerun()
    st.divider()
    if st.button("Logout", use_container_width=True):
        st.session_state.logged = False
        st.rerun()
    st.markdown(f'<div class="white-card"><b>For {st.session_state.user["btech"]}% profile</b><br>TCS NQT Eligible? { "Yes ✅" if st.session_state.user["btech"]>=60 else "No ❌"} (60% needed)<br><br>XP: {st.session_state.xp}<br>Modules: {done_count}</div>', unsafe_allow_html=True)

with col_right:
    t = TOPICS[st.session_state.topic]
    st.title(f"{t['title']}")
    st.caption(f"{t['about']} | For {st.session_state.user['btech']}% | {len(t['modules'])} Modules")
    mod_names = [m["name"] for m in t["modules"]]
    sel = st.selectbox("Select Module:", range(len(mod_names)), format_func=lambda x: f"{x+1}. {mod_names[x]}", index=st.session_state.mod)
    st.session_state.mod = sel
    mod = t["modules"][sel]
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Learn", "💻 Code", "🧠 Practice", "🎮 Game & Certificate"])
    with tab1:
        st.markdown(f'<div class="white-card"><h3>Module {sel+1}: {mod["name"]}</h3><p>{mod["content"]}</p><br><p><b>Why for {st.session_state.user["btech"]}%?</b> Helps in TCS NQT and Final Boss game 0,3,6,9 logic!</p></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            if sel>0:
                if st.button("← Prev"): st.session_state.mod-=1; st.rerun()
        with col2:
            key = f"{st.session_state.topic}_{sel}"
            if st.session_state.done.get(key):
                st.success("✅ Done")
            else:
                if st.button(f"Mark Done +50 XP"):
                    st.session_state.done[key]=True
                    st.session_state.xp+=50
                    st.balloons()
                    st.rerun()
        with col3:
            if sel < len(mod_names)-1:
                if st.button("Next →"): st.session_state.mod+=1; st.rerun()
    with tab2:
        st.subheader("Code Example")
        st.code(mod["code"], language="python")
        st.markdown('<div class="white-card"><b>💡 Try yourself:</b> Copy code, change btech=81 to btech=85 and see output!</div>', unsafe_allow_html=True)
        user_code = st.text_area("Write your code here:", value=mod["code"], height=150, key=f"code_{sel}")
        if st.button("▶️ Run Code", key=f"run_{sel}"):
            st.success(f"Output (Simulated):\nHello BhavPath! Welcome to {st.session_state.topic}!\nTask done for {mod['name']}!\n✅ Success!")
    with tab3:
        st.subheader(f"Practice - {mod['name']}")
        st.markdown(f'<div class="white-card"><b>Q: {mod["q"]}</b></div>', unsafe_allow_html=True)
        choice = st.radio("Choose:", mod["opts"], key=f"q_{sel}")
        if st.button("Check Answer", key=f"chk_{sel}"):
            if choice==mod["ans"]:
                st.success(f"✅ Correct! {mod['ans']} - You slayed! +20 XP")
                st.session_state.xp+=20
                st.balloons()
            else:
                st.error(f"❌ Wrong! Correct: {mod['ans']}")
        st.divider()
        st.write("All Modules:")
        for i, mname in enumerate(mod_names):
            mark = "✅" if st.session_state.done.get(f"{st.session_state.topic}_{i}") else "⬜"
            st.write(f"{mark} {i+1}. {mname}")
    with tab4:
        st.subheader("🎮 Final Boss + Certificate")
        if done_count < 3:
            st.warning(f"🔒 Locked - Complete {3-done_count} more modules to unlock game and certificate. Current: {done_count}/3")
            st.progress(done_count/3)
        else:
            st.success(f"🔥 Unlocked! {done_count} modules done - Play game to get certificate!")
            st.markdown('<div class="white-card"><b>Loop Legends - Final Boss</b><br>Coins at 0,3,6,9 - From Loops module - for(i=0;i<10;i+=3) -> 0 3 6 9<br>Win to unlock certificate!</div>', unsafe_allow_html=True)
            step = st.slider("for(i=0; i<10; i+=?)", 1, 5, 3, key="game_slider")
            if st.button("PLAY FINAL BOSS 🔥", key="play"):
                coins=[0,3,6,9]
                path=list(range(0,10,step))
                coll=len([x for x in path if x in coins])
                st.write(f"Path: {path} | Collected: {coll}/4")
                if coll==4:
                    st.balloons()
                    st.success(f"YOU SLAYED FINAL BOSS! +200 XP - Total {st.session_state.xp+200}")
                    st.session_state.xp+=200
                    st.session_state.won=True
                    st.snow()
                else:
                    st.error(f"Need i+=3 for 0,3,6,9 - You got {coll}/4")
            if st.session_state.won:
                st.divider()
                today = date.today().strftime("%d-%m-%Y")
                st.markdown(f"""
                <div class="cert-card">
                <div style="font-size: 24px; font-weight: 900;">🏆 CERTIFICATE 🏆</div>
                <div>BhavPath - Gamified Learning Platform</div>
                <div style="background: white; border-radius: 12px; padding: 16px; margin: 12px 0;">
                <div>This is to certify that</div>
                <div style="font-size: 22px; font-weight: 900; color: #2563EB;">{st.session_state.user['name']}</div>
                <div>from {st.session_state.user['college']} - {st.session_state.user['btech']}%</div>
                <div style="font-size: 18px; font-weight: 800; margin-top: 8px;">{st.session_state.topic} - Complete</div>
                <div style="margin-top: 8px;">XP: {st.session_state.xp} | Date: {today} | Grade: A+ 🔥</div>
                </div>
                <div style="font-size: 11px;">ID: BP-{st.session_state.user['btech']}-{st.session_state.xp}</div>
                </div>
                """, unsafe_allow_html=True)
                cert_text = f"BhavPath Certificate\nName: {st.session_state.user['name']}\nCollege: {st.session_state.user['college']}\nBTech: {st.session_state.user['btech']}%\nTopic: {st.session_state.topic}\nXP: {st.session_state.xp}\nDate: {today}\nID: BP-{st.session_state.user['btech']}-{st.session_state.xp}"
                st.download_button("📥 Download Certificate", data=cert_text, file_name=f"Certificate_{st.session_state.topic}_{st.session_state.user['name']}.txt", mime="text/plain", use_container_width=True)
                st.success("Share on LinkedIn - #BhavPath #Python")
    st.divider()
    st.markdown('<div class="white-card" style="border: 1px dashed #94A3B8; text-align: center;"><b>📢 Ad:</b> TCS NQT 2025 - 60% eligible? You have 81%! Apply now - 8 LPA - <b>Click here</b></div>', unsafe_allow_html=True)
