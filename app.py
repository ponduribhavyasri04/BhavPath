import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - No Percentage Page", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #F8FAFC !important; }
h1,h2,h3,p,div,span,label,li { color: #000000 !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; font-size: 24px !important; }
.white-card { background: #FFFFFF !important; border-radius: 10px; padding: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-bottom: 8px; border: 1px solid #E2E8F0; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 10px; padding: 12px; }
.blue-card b { color: #FFFFFF !important; }
.ad-card { background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important; color: #FFFFFF !important; border-radius: 10px; padding: 12px; margin-bottom: 8px; }
.ad-card b { color: #FFFFFF !important; }
.cert-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFE082 100%) !important; border: 3px solid #FFB300 !important; border-radius: 16px; padding: 20px; text-align: center; }
.practice-card { background: #FFFBEB !important; border: 1px solid #F59E0B; border-radius: 8px; padding: 10px; margin-bottom: 8px; }
.run-card { background: #1E293B !important; color: #FFFFFF !important; border-radius: 8px; padding: 10px; }
.run-card b { color: #FFFFFF !important; }
.locked-card { background: #E2E8F0 !important; border-radius: 8px; padding: 10px; }
.stButton>button { background: #2563EB !important; color: #FFFFFF !important; border-radius: 8px; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state: st.session_state.logged = False
if 'user' not in st.session_state: st.session_state.user = {"btech": 81}
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'selected_topic' not in st.session_state: st.session_state.selected_topic = "Python"
if 'completed' not in st.session_state: st.session_state.completed = {}
if 'current_mod' not in st.session_state: st.session_state.current_mod = 0
if 'cert_unlocked' not in st.session_state: st.session_state.cert_unlocked = False
if 'final_boss_won' not in st.session_state: st.session_state.final_boss_won = False
if 'purpose_done' not in st.session_state: st.session_state.purpose_done = False

TOPICS = {
    "Python": {"title": "Python - 8 Modules", "desc": "Easy + Data Science", "modules": [
        {"name": "Intro", "content": "Python by Guido 1991. Easy syntax. Pandas for Data Science.", "code": "print(\"Hello Python\")", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum", "task": "Print Hello Python"},
        {"name": "Variables", "content": "No type needed! btech=81, name='Bhav'.", "code": "btech=81\nname='Bhav'\nprint(f\"{name} {btech}%\")", "q": "Python var?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81", "task": "Declare btech=81"},
        {"name": "List & Dict", "content": "list [81,75,80] mutable, dict {'name':'Bhav'} key-value.", "code": "marks=[81,75,80]\nprint(sum(marks)/len(marks))", "q": "Mutable?", "opts": ["list", "tuple"], "ans": "list", "task": "Create list and avg"},
        {"name": "Loops Final Boss", "content": "for i in range(0,10,3): print(i) -> 0 3 6 9 coins! Final Boss!", "code": "for i in range(0,10,3):\n    print(i, end=\" \") # 0 3 6 9", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run range 0-10 step 3"},
        {"name": "Pandas", "content": "Pandas: df=pd.DataFrame, mean() - Must for DE!", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())", "q": "Pandas mean?", "opts": ["df['btech'].mean()", "mean(df)"], "ans": "df['btech'].mean()", "task": "Calculate mean"},
    ]},
    "C": {"title": "C - Mother Language", "desc": "Dennis Ritchie 1972", "modules": [
        {"name": "Intro", "content": "C by Dennis Ritchie. Fast.", "code": "printf(\"Hello C\");", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie", "task": "Print Hello C"},
        {"name": "Loops Final Boss", "content": "for(i=0;i<10;i+=3) -> 0 3 6 9", "code": "for(int i=0;i<10;i+=3) printf(\"%d \", i);", "q": "i+=3?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run loop"},
    ]},
    "Data Engineering": {"title": "Data Engineering - 8-15 LPA", "desc": "Build pipelines", "modules": [
        {"name": "SQL Basics", "content": "SELECT, WHERE filter, GROUP BY", "code": "SELECT * FROM students WHERE btech>=60;", "q": "WHERE for?", "opts": ["Filter", "Group"], "ans": "Filter", "task": "SELECT with WHERE"},
        {"name": "ETL", "content": "Extract pd.read_csv, Transform eligible, Load to warehouse", "code": "df['eligible']=df['btech']>=60", "q": "Transform?", "opts": ["Clean/filter", "Get data"], "ans": "Clean/filter", "task": "Add eligible column"},
    ]},
}
TOPICS["C++"] = TOPICS["C"]
TOPICS["C++"]["title"] = "C++ - Gaming Engines"
TOPICS["Java"] = TOPICS["C"]
TOPICS["Java"]["title"] = "Java - Android + Enterprise"
TOPICS["Software Engineering"] = TOPICS["Data Engineering"]
TOPICS["Software Engineering"]["title"] = "Software Engineering - SDLC, Agile"

ADS = [
    {"title": "🔥 TCS NQT 2025 - Apply Now!", "desc": "60% eligibility? You have 81%! 8 LPA package!", "cta": "Apply Now →", "color": "#FF6B6B"},
    {"title": "📚 Data Engineering Course - 50% OFF!", "desc": "SQL + Python + Spark + AWS - Coupon: BHAV50", "cta": "Enroll Now →", "color": "#4ECDC4"},
]

def generate_certificate(name, college, btech, topic, xp, date_str):
    return f"""
    <div class="cert-card">
        <div style="font-size: 28px; font-weight: 900; color: #0F2C61;">🏆 CERTIFICATE OF COMPLETION 🏆</div>
        <div style="font-size: 14px; color: #64748B; margin-bottom: 12px;">BhavPath - Gamified Learning Platform</div>
        <div style="border: 2px solid #FFB300; border-radius: 12px; padding: 16px; background: white;">
            <div style="font-size: 16px;">This is to certify that</div>
            <div style="font-size: 26px; font-weight: 900; color: #2563EB;">{name}</div>
            <div style="font-size: 14px;">from <b>{college}</b> with <b>{btech}% BTech</b></div>
            <div style="font-size: 18px; font-weight: 800; color: #0F2C61; margin-top: 8px;">{topic} - Complete Tutorial</div>
            <div style="font-size: 13px;">8 Modules + Final Boss Game (0,3,6,9) + Practice + Run</div>
            <div style="display: flex; justify-content: space-around; margin-top: 12px;"><div><b>XP:</b> {xp}</div><div><b>Date:</b> {date_str}</div><div><b>Grade:</b> A+ 🔥</div></div>
        </div>
        <div style="font-size: 11px; color: #64748B; margin-top: 8px;">ID: BP-{btech}-{xp}-{date_str.replace('-','')} | Verify at bhavpath.streamlit.app</div>
    </div>
    """

# --- PAGE 1: LOGIN - ONLY EMAIL + COLLEGE - NO PERCENTAGE HERE ---
if not st.session_state.logged:
    st.title("🚀 BhavPath - Login")
    st.markdown('<div class="white-card"><b>Welcome! Login with Email + College only - Percentage next page lo!</b><br>✅ Simple - No percentage here - Next page lo adugutham</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email", placeholder="bhav@gmail.com")
        college = st.text_input("College Name", placeholder="Rise College, Ongole")
        if st.button("Login & Continue →"):
            if email and college and "@" in email:
                st.session_state.user = {"email": email, "college": college, "btech": 81, "name": email.split("@")[0]}
                st.session_state.logged = True
                st.session_state.purpose_done = False
                st.balloons()
                st.rerun()
            else:
                st.error("Valid email and college needed fr")
    with col2:
        st.markdown('<div class="white-card"><b>🔥 Flow:</b><br>1. Login - Email + College only (This page)<br>2. Next page - Percentage + Purpose - BTech % ikkada adugutham!<br>3. Main App - Topics, Tutorial, Practice, Run, Game, Certificate<br>Only 3 steps - No confusion!</div>', unsafe_allow_html=True)

# --- PAGE 2: PURPOSE + PERCENTAGE - PERCENTAGE IKADA! ---
elif not st.session_state.purpose_done:
    st.title("📊 One More Step! - Your Stats")
    st.markdown(f'<div class="white-card">Yo <b>{st.session_state.user["name"]}</b>! Welcome to the squad 🚀<br>🏫 {st.session_state.user["college"]}<br>Let\'s lock in your stats - Percentage ikkada!</div>', unsafe_allow_html=True)
    
    # PERCENTAGE SLIDER IKADA - NEXT PAGE LO!
    btech = st.slider("What's your BTech flex? Drop your % - Percentage here!", 0, 100, st.session_state.user.get("btech", 81))
    st.markdown(f'<div class="blue-card"><b>Bet! Locked in: {btech}% 🔥</b><br>We\'re about to cook a custom prep just for you - No cap, this gonna be fire</div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("What you want? - Select one")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="white-card">🎯 <b>For Placement</b><br>Eligibility + Skill Gap for your %</div>', unsafe_allow_html=True)
        if st.button(f"Placement with {btech}% →"):
            st.session_state.user["btech"] = btech
            st.session_state.purpose_done = True
            st.balloons()
            st.rerun()
        st.markdown('<div class="white-card">📚 <b>Study Hub - 6 Topics</b><br>Direct open - Easy</div>', unsafe_allow_html=True)
        if st.button(f"Browse Topics with {btech}% →"):
            st.session_state.user["btech"] = btech
            st.session_state.purpose_done = True
            st.rerun()
    with c2:
        st.markdown('<div class="white-card">📄 <b>Resume Builder</b><br>Auto resume with your %</div>', unsafe_allow_html=True)
        if st.button(f"Resume with {btech}% →"):
            st.session_state.user["btech"] = btech
            st.session_state.purpose_done = True
            st.rerun()
        done = len([k for k,v in st.session_state.completed.items() if v])
        if done >= 3:
            st.markdown('<div class="blue-card"><b>🎮 FINAL BOSS - Game Zone</b><br>Modules done! End with banger 🔥</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="white-card"><b>Game unlocks after 3 modules<br>Current: {done}/3</b></div>', unsafe_allow_html=True)

# --- PAGE 3: MAIN APP - EVERYTHING ---
else:
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | {st.session_state.selected_topic}</b></div>', unsafe_allow_html=True)
    done = len([k for k,v in st.session_state.completed.items() if v])
    st.write(f"Progress: {done} modules | Game unlocks at 3 | Certificate after Final Boss win")
    st.progress(min(done/8, 1.0))
    
    col_logout, col_perc = st.columns([1,3])
    with col_logout:
        if st.button("← Back - Change %"):
            st.session_state.purpose_done = False
            st.rerun()
        if st.button("Logout"):
            st.session_state.logged = False
            st.session_state.purpose_done = False
            st.rerun()
    with col_perc:
        # Percentage change option here also
        new_btech = st.slider(f"Change BTech % if needed - Current {st.session_state.user['btech']}%", 0, 100, st.session_state.user["btech"], key="change_btech")
        if new_btech != st.session_state.user["btech"]:
            st.session_state.user["btech"] = new_btech
            st.success(f"Updated to {new_btech}%!")
            st.rerun()

    st.divider()
    col_topics, col_content, col_practice = st.columns([1, 2.2, 1])

    with col_topics:
        st.subheader("📚 Topics")
        for tname in TOPICS.keys():
            is_sel = st.session_state.selected_topic == tname
            if is_sel:
                st.markdown(f'<div class="blue-card"><b>📖 {tname} ✅</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="white-card"><b>{tname}</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
            if st.button(f"Open {tname} →", key=f"open_{tname}"):
                st.session_state.selected_topic = tname
                st.session_state.current_mod = 0
                st.rerun()
        st.divider()
        ad = ADS[0]
        st.markdown(f'<div class="ad-card"><b>📢 AD</b><br><b>{ad["title"]}</b><br>{ad["desc"]}<br><b>{ad["cta"]}</b></div>', unsafe_allow_html=True)

    with col_content:
        t = TOPICS[st.session_state.selected_topic]
        st.subheader(f"📖 {t['title']} - For {st.session_state.user['btech']}%")
        mod_names = [m["name"] for m in t["modules"]]
        selected_idx = st.selectbox(f"Module ({len(mod_names)} total):", range(len(mod_names)), format_func=lambda x: f"{x+1}. {mod_names[x]}", index=st.session_state.current_mod)
        st.session_state.current_mod = selected_idx
        mod = t["modules"][selected_idx]
        
        st.markdown(f'<div class="white-card"><b>Module {selected_idx+1}: {mod["name"]}</b><br><br>{mod["content"]}<br><br>For {st.session_state.user["btech"]}% profile - Helps in TCS NQT!</div>', unsafe_allow_html=True)
        st.code(mod["code"], language="python" if st.session_state.selected_topic in ["Python","Data Engineering"] else "cpp")
        
        col_prev, col_done, col_next = st.columns([1,1,1])
        with col_prev:
            if selected_idx > 0:
                if st.button("← Prev"): st.session_state.current_mod -=1; st.rerun()
        with col_done:
            key = f"{st.session_state.selected_topic}_{selected_idx}"
            if st.session_state.completed.get(key): st.success("✅ Done")
            else:
                if st.button(f"Mark Done +50 XP", key=f"done_{key}"):
                    st.session_state.completed[key]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
        with col_next:
            if selected_idx < len(mod_names)-1:
                if st.button("Next →"): st.session_state.current_mod+=1; st.rerun()
        
        st.divider()
        ad = ADS[1]
        st.markdown(f'<div class="ad-card" style="background: {ad["color"]} !important;"><b>📢 AD - For {st.session_state.user["btech"]}% profile</b><br><b>{ad["title"]}</b><br>{ad["desc"]}</div>', unsafe_allow_html=True)

        st.divider()
        st.subheader("🎮 FINAL BOSS - Game + Certificate")
        if done >= 3:
            st.markdown(f'<div class="blue-card"><b>🔥 UNLOCKED! {done} modules - Win game for Certificate!</b><br>Loop Legends - 0,3,6,9 coins</div>', unsafe_allow_html=True)
            step = st.slider("for(i=0; i<10; i+=?) - Final answer?", 1,5,3, key="game")
            if st.button("PLAY FINAL BOSS 🔥 - Win for Certificate!", key="play_game"):
                coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
                st.write(f"Path {path} | {coll}/4")
                if coll==4:
                    st.balloons(); st.success(f"SLAYED! +200 XP"); st.session_state.xp+=200; st.session_state.final_boss_won=True; st.session_state.cert_unlocked=True; st.snow()
                else:
                    st.error(f"Need i+=3 - Got {coll}/4")
            
            if st.session_state.cert_unlocked and st.session_state.final_boss_won:
                st.divider()
                st.subheader("🏆 Certificate Unlocked!")
                today = date.today().strftime("%d-%m-%Y")
                cert_html = generate_certificate(st.session_state.user["name"], st.session_state.user["college"], st.session_state.user["btech"], st.session_state.selected_topic, st.session_state.xp, today)
                st.markdown(cert_html, unsafe_allow_html=True)
                cert_text = f"BhavPath Certificate - {st.session_state.user['name']} - {st.session_state.user['college']} - {st.session_state.user['btech']}% - {st.session_state.selected_topic} - XP {st.session_state.xp} - Date {today} - ID BP-{st.session_state.user['btech']}-{st.session_state.xp}"
                st.download_button(label="📥 Download Certificate - For LinkedIn!", data=cert_text, file_name=f"BhavPath_Certificate_{st.session_state.selected_topic}_{st.session_state.user['name']}.txt", mime="text/plain")
        else:
            st.markdown(f'<div class="locked-card"><b>🔒 FINAL BOSS & Certificate Locked - Complete {3-done} more modules</b></div>', unsafe_allow_html=True)

    with col_practice:
        mod = TOPICS[st.session_state.selected_topic]["modules"][st.session_state.current_mod]
        st.subheader("🧠 Practice")
        st.markdown(f'<div class="practice-card"><b>Practice - {mod["name"]}</b></div>', unsafe_allow_html=True)
        st.write(f"**Q: {mod['q']}**")
        choice = st.radio("Choose:", mod["opts"], key=f"quiz_{st.session_state.selected_topic}_{st.session_state.current_mod}")
        if st.button("Check Answer", key=f"check_{st.session_state.current_mod}"):
            if choice == mod["ans"]:
                st.success(f"✅ Correct! {mod['ans']} - +20 XP"); st.session_state.xp+=20; st.balloons()
            else:
                st.error(f"❌ Wrong! Correct: {mod['ans']}")
        st.divider()
        st.subheader("▶️ Run Code")
        st.markdown(f'<div class="run-card"><b>Run - {mod["task"]}</b></div>', unsafe_allow_html=True)
        code_input = st.text_area("Code:", value=mod["code"], height=120, key=f"code_{st.session_state.current_mod}")
        if st.button("▶️ Run", key=f"run_{st.session_state.current_mod}"):
            st.success(f"Output: Hello BhavPath! Task {mod['task']} done! ✅")
