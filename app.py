import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - Lists Group", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #FCFCFC !important; }
h1,h2,h3,p,div,span { color: #111111 !important; }
h1 { color: #0F172A !important; font-weight: 800 !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 12px; padding: 14px; }
.blue-card b { color: #FFFFFF !important; }
.category-card { background: #F8FAFC !important; border: 1px solid #CBD5E1; border-radius: 10px; padding: 12px; margin-bottom: 8px; }
.cert-card { background: #FFFBEB !important; border: 2px solid #F59E0B; border-radius: 16px; padding: 20px; text-align: center; }
.stButton>button { background: #2563EB !important; color: white !important; border-radius: 10px; font-weight: 700 !important; height: 42px; }
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
        "title": "Python - For Data Science", "about": "Easy, powerful, trending 2025. For your 81% profile, Python is MUST.", "track": "Python Track",
        "modules": [
            {"name": "Intro", "content": "Python by Guido 1991. No semicolon, only indentation. Used for Data Science, AI. Libraries: Pandas, Numpy.", "code": "print('Hello Python')\nprint('BhavPath - Easy')", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum"},
            {"name": "Variables", "content": "No type needed! btech=81, name='Bhav'. Dynamic. Same variable can hold different types.", "code": "btech=81\nname='Bhav'\nprint(f'{name} {btech}%')", "q": "Python variable?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81"},
            {"name": "List & Dict", "content": "list = [81,75,80] mutable. dict = {'name':'Bhav','btech':81} key-value. Most used in Data Science.", "code": "marks=[81,75,80]\nprint(f'Avg: {sum(marks)/len(marks)}')", "q": "Mutable?", "opts": ["list", "tuple"], "ans": "list"},
            {"name": "Loops - Final Boss", "content": "for i in range(0,10,3): -> 0 3 6 9 coins! This is Final Boss logic! range(0,10,1) -> 0-9 all.", "code": "for i in range(0,10,3):\n    print(i, end=' ') # 0 3 6 9", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9"},
            {"name": "Pandas", "content": "Pandas for DE! pd.read_csv, df['btech'].mean(), groupby. Must for 8-15 LPA role.", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())", "q": "Pandas mean?", "opts": ["df['btech'].mean()", "mean(df)"], "ans": "df['btech'].mean()"},
        ]
    },
    "C Programming": {"title": "C - Mother Language", "about": "Dennis Ritchie 1972. Fast, close to hardware.", "track": "C Family", "modules": [
        {"name": "Intro", "content": "C is procedural, mother of all languages. Used for OS, Embedded.", "code": "#include <stdio.h>\nint main(){ printf('Hello C'); return 0; }", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie"},
        {"name": "Loops - Final Boss", "content": "for(i=0;i<10;i+=3) -> 0 3 6 9 coins! Final Boss logic from C!", "code": "for(int i=0;i<10;i+=3) printf('%d ', i); // 0 3 6 9", "q": "i+=3?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9"},
    ]},
    "C++": {"title": "C++ - Gaming Engines", "about": "C++ for gaming, fast, OOP. Unreal Engine.", "track": "C Family", "modules": [
        {"name": "Intro", "content": "C++ is C + OOP. Used for gaming engines.", "code": "#include <iostream>\nint main(){ std::cout<<\"Hello C++\"; }", "q": "C++ invented by?", "opts": ["Bjarne Stroustrup", "Dennis Ritchie"], "ans": "Bjarne Stroustrup"},
    ]},
    "Java": {"title": "Java - Android + Enterprise", "about": "James Gosling 1995. Android, enterprise.", "track": "C Family", "modules": [
        {"name": "Intro", "content": "Java by James Gosling. Write once run anywhere. Android.", "code": "public class Main{ public static void main(String[] args){ System.out.println(\"Hello Java\"); } }", "q": "Who invented Java?", "opts": ["James Gosling", "Guido"], "ans": "James Gosling"},
    ]},
    "Data Engineering": {"title": "Data Engineering - 8-15 LPA", "about": "Build pipelines. Tools: SQL, Python, Spark, Cloud. Highest demand 2025.", "track": "Data Track", "modules": [
        {"name": "SQL Basics", "content": "SELECT, WHERE filter, GROUP BY group, ORDER BY sort. 80% interviews ask SQL!", "code": "SELECT * FROM students WHERE btech>=60 ORDER BY btech DESC;", "q": "WHERE for?", "opts": ["Filter", "Group"], "ans": "Filter"},
        {"name": "ETL", "content": "Extract: pd.read_csv, Transform: df['eligible']=df['btech']>=60, Load: df.to_csv. BhavPath is ETL!", "code": "df['eligible']=df['btech']>=60\nprint(df)", "q": "ETL Load?", "opts": ["Store to warehouse", "Get data"], "ans": "Store to warehouse"},
    ]},
    "Software Engineering": {"title": "Software Engineering - SDLC", "about": "SDLC, Agile, Scrum, Git, Testing. 6-12 LPA.", "track": "Data Track", "modules": [
        {"name": "SDLC", "content": "SDLC = Requirement, Design, Coding, Testing, Deployment. Agile = Scrum sprints.", "code": "# Agile\n# Sprint 1: Requirement\n# Sprint 2: Design", "q": "SDLC first phase?", "opts": ["Requirement", "Coding"], "ans": "Requirement"},
    ]},
}

# LISTS GROUP - CATEGORY WISE - THIS IS THE ONE MODIFICATION!
TRACKS = {
    "🐍 Python Track": ["Python"],
    "💻 C Family": ["C Programming", "C++", "Java"],
    "📊 Data Track": ["Data Engineering", "Software Engineering"]
}

if not st.session_state.logged:
    st.title("🚀 BhavPath")
    st.caption("Clean - Lists group wise - Select chesukoni laaga")
    c1, c2 = st.columns([1,1], gap="large")
    with c1:
        email = st.text_input("Email", placeholder="bhav@gmail.com")
        college = st.text_input("College", placeholder="Rise College, Ongole")
        btech = st.slider("BTech %", 0, 100, 81)
        if st.button("Start Learning →", use_container_width=True):
            if email and college and "@" in email:
                st.session_state.user = {"email": email, "college": college, "btech": btech, "name": email.split("@")[0]}
                st.session_state.logged = True
                st.rerun()
    with c2:
        st.markdown("""
        <div class="white-card">
        <h3>✨ New - Lists Group Modification</h3>
        <p>• <b>🐍 Python Track</b> list - Python</p>
        <p>• <b>💻 C Family</b> list - C, C++, Java</p>
        <p>• <b>📊 Data Track</b> list - Data Eng, Software Eng</p>
        <p>• Select category -> Select topic -> Learn</p>
        <p>• Same select chesukoni laaga - Easy to find</p>
        <p>• Clean, no eruku eruku - Spacious</p>
        </div>
        """, unsafe_allow_html=True)
    st.stop()

st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</b></div>', unsafe_allow_html=True)
done_count = len([k for k in st.session_state.done if st.session_state.done[k]])
st.write(f"Progress: {done_count} modules | Game unlocks at 3")
st.progress(min(done_count/5, 1.0))

col_left, col_right = st.columns([1, 2.5], gap="large")

# LEFT - LISTS GROUP WISE - MODIFIED ONE THING - SELECT CHESUKONI LAAGA
with col_left:
    st.subheader("📚 Languages Lists - Group Wise")
    st.caption("Category select chesuko -> Topic select")
    
    for track_name, topic_list in TRACKS.items():
        with st.expander(f"{track_name} ({len(topic_list)} topics)", expanded=True):
            for tname in topic_list:
                is_sel = st.session_state.topic == tname
                if is_sel:
                    st.markdown(f'<div class="blue-card"><b>📖 {tname} ✅ Selected</b><br>{TOPICS[tname]["title"]}</div>', unsafe_allow_html=True)
                else:
                    if st.button(f"{tname}", key=f"btn_{tname}", use_container_width=True):
                        st.session_state.topic = tname
                        st.session_state.mod = 0
                        st.rerun()
    
    st.divider()
    st.subheader("🔗 Helpful Links - Clickable")
    st.markdown('<div class="white-card"><b>TCS NQT 2025</b><br>60% needed - You have 81%!</div>', unsafe_allow_html=True)
    st.link_button("Apply on TCS Official →", "https://nextstep.tcs.com/campus/", use_container_width=True)
    st.write("")
    st.markdown('<div class="white-card"><b>Python Docs</b><br>Official docs - Free</div>', unsafe_allow_html=True)
    st.link_button("Learn on Python.org →", "https://docs.python.org/3/", use_container_width=True)
    
    st.divider()
    if st.button("Logout", use_container_width=True):
        st.session_state.logged = False
        st.rerun()
    st.markdown(f'<div class="white-card"><b>For {st.session_state.user["btech"]}%</b><br>TCS NQT: {"Yes ✅" if st.session_state.user["btech"]>=60 else "No ❌"}<br>XP: {st.session_state.xp}<br>Done: {done_count}</div>', unsafe_allow_html=True)

# RIGHT - SAME CONTENT - TABS
with col_right:
    t = TOPICS[st.session_state.topic]
    st.title(f"{t['title']}")
    st.caption(f"{t['about']} | For {st.session_state.user['btech']}% | Track: {t['track']} | {len(t['modules'])} Modules")
    
    mod_names = [m["name"] for m in t["modules"]]
    sel = st.selectbox("Select Module - Content below will change:", range(len(mod_names)), format_func=lambda x: f"{x+1}. {mod_names[x]}", index=st.session_state.mod)
    st.session_state.mod = sel
    mod = t["modules"][sel]
    
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Learn", "💻 Code", "🧠 Practice", "🎮 Game & Certificate"])
    
    with tab1:
        st.markdown(f'<div class="white-card"><h3>Module {sel+1}: {mod["name"]}</h3><p>{mod["content"]}</p><br><p><b>Why for {st.session_state.user["btech"]}%?</b> Helps in TCS NQT and Final Boss 0,3,6,9!</p></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            if sel>0 and st.button("← Prev"): st.session_state.mod-=1; st.rerun()
        with col2:
            key = f"{st.session_state.topic}_{sel}"
            if st.session_state.done.get(key): st.success("✅ Done")
            else:
                if st.button(f"Mark Done +50 XP"):
                    st.session_state.done[key]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
        with col3:
            if sel < len(mod_names)-1 and st.button("Next →"): st.session_state.mod+=1; st.rerun()
    
    with tab2:
        st.subheader("Code Example")
        st.code(mod["code"], language="python")
        st.text_area("Write your code here:", value=mod["code"], height=120, key=f"code_{sel}")
        if st.button("▶️ Run Code", key=f"run_{sel}"):
            st.success(f"Output (Simulated): Hello {st.session_state.topic}! Task done for {mod['name']}! ✅")
    
    with tab3:
        st.subheader(f"Practice - {mod['name']}")
        st.markdown(f'<div class="white-card"><b>Q: {mod["q"]}</b></div>', unsafe_allow_html=True)
        choice = st.radio("Choose:", mod["opts"], key=f"q_{sel}")
        if st.button("Check Answer", key=f"chk_{sel}"):
            if choice==mod["ans"]: st.success(f"✅ Correct! {mod['ans']} +20 XP"); st.session_state.xp+=20; st.balloons()
            else: st.error(f"❌ Wrong! Correct: {mod['ans']}")
    
    with tab4:
        st.subheader("🎮 Final Boss + Certificate")
        if done_count < 3:
            st.warning(f"🔒 Locked - Complete {3-done_count} more - Current: {done_count}/3")
            st.progress(done_count/3)
        else:
            st.success(f"🔥 Unlocked! {done_count} modules done!")
            st.markdown('<div class="white-card"><b>Loop Legends - Final Boss</b><br>Coins at 0,3,6,9 - for(i=0;i<10;i+=3) -> 0 3 6 9<br>Win to unlock certificate!</div>', unsafe_allow_html=True)
            step = st.slider("for(i=0; i<10; i+=?)", 1, 5, 3, key="game_slider")
            if st.button("PLAY FINAL BOSS 🔥", key="play"):
                coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
                st.write(f"Path: {path} | Collected: {coll}/4")
                if coll==4: st.balloons(); st.success(f"SLAYED! +200 XP"); st.session_state.xp+=200; st.session_state.won=True; st.snow()
                else: st.error(f"Need i+=3 - Got {coll}/4")
            if st.session_state.won:
                today = date.today().strftime("%d-%m-%Y")
                st.markdown(f"""
                <div class="cert-card">
                <div style="font-size: 24px; font-weight: 900;">🏆 CERTIFICATE 🏆</div>
                <div>BhavPath</div>
                <div style="background: white; border-radius: 12px; padding: 16px; margin: 12px 0;">
                <div>{st.session_state.user['name']} - {st.session_state.user['college']} - {st.session_state.user['btech']}%</div>
                <div style="font-size: 18px; font-weight: 800;">{st.session_state.topic} - Complete</div>
                <div>XP: {st.session_state.xp} | Date: {today} | Grade: A+ 🔥</div>
                </div>
                </div>
                """, unsafe_allow_html=True)
                cert_text = f"Certificate\nName: {st.session_state.user['name']}\nCollege: {st.session_state.user['college']}\nBTech: {st.session_state.user['btech']}%\nTopic: {st.session_state.topic}\nXP: {st.session_state.xp}\nDate: {today}"
                st.download_button("📥 Download Certificate", data=cert_text, file_name=f"Certificate_{st.session_state.topic}.txt", mime="text/plain", use_container_width=True)
