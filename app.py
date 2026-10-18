import streamlit as st
from datetime import date
import base64

st.set_page_config(page_title="BhavPath - Certificate + Ads", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #F8FAFC !important; }
h1,h2,h3,p,div,span,label,li { color: #000000 !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; font-size: 24px !important; }
.white-card { background: #FFFFFF !important; border-radius: 10px; padding: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-bottom: 8px; border: 1px solid #E2E8F0; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 10px; padding: 12px; }
.blue-card b { color: #FFFFFF !important; }
.ad-card { background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important; color: #FFFFFF !important; border-radius: 10px; padding: 12px; margin-bottom: 8px; border: 2px dashed #FFD700; }
.ad-card b, .ad-card div, .ad-card p { color: #FFFFFF !important; }
.cert-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFE082 100%) !important; border: 3px solid #FFB300 !important; border-radius: 16px; padding: 20px; text-align: center; margin-bottom: 10px; }
.practice-card { background: #FFFBEB !important; border: 1px solid #F59E0B; border-radius: 8px; padding: 10px; margin-bottom: 8px; }
.run-card { background: #1E293B !important; color: #FFFFFF !important; border-radius: 8px; padding: 10px; }
.run-card b { color: #FFFFFF !important; }
.locked-card { background: #E2E8F0 !important; border-radius: 8px; padding: 10px; }
.stButton>button { background: #2563EB !important; color: #FFFFFF !important; border-radius: 8px; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state: st.session_state.logged = False
if 'user' not in st.session_state: st.session_state.user = {}
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'selected_topic' not in st.session_state: st.session_state.selected_topic = "Python"
if 'completed' not in st.session_state: st.session_state.completed = {}
if 'current_mod' not in st.session_state: st.session_state.current_mod = 0
if 'cert_unlocked' not in st.session_state: st.session_state.cert_unlocked = False
if 'final_boss_won' not in st.session_state: st.session_state.final_boss_won = False

TOPICS = {
    "Python": {
        "title": "Python - 8 Modules - Data Science",
        "desc": "Easy + Powerful - Trending",
        "modules": [
            {"name": "Intro", "content": "Python by Guido 1991. Easy syntax, no semicolon. Pandas for Data Science.", "code": "print(\"Hello Python\")", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum", "task": "Print Hello Python"},
            {"name": "Variables", "content": "No type needed! btech=81, name='Bhav'. Dynamic!", "code": "btech=81\nname='Bhav'\nprint(f\"{name} {btech}%\")", "q": "Python var?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81", "task": "Declare btech=81"},
            {"name": "List & Dict", "content": "list [81,75,80] mutable, dict {'name':'Bhav'} key-value. For Data Science!", "code": "marks=[81,75,80]\nprint(sum(marks)/len(marks))", "q": "Mutable?", "opts": ["list", "tuple"], "ans": "list", "task": "Create list and avg"},
            {"name": "Control", "content": "if btech>=60: print(\"Eligible\") - Only indentation!", "code": "if btech>=60:\n    print(\"Eligible\")", "q": "Python if?", "opts": ["if btech>=60:", "if(btech>=60)"], "ans": "if btech>=60:", "task": "Check eligibility"},
            {"name": "Loops - Final Boss", "content": "for i in range(0,10,3): print(i) -> 0 3 6 9 coins! Final Boss logic!", "code": "for i in range(0,10,3):\n    print(i, end=\" \") # 0 3 6 9", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run range 0-10 step 3"},
            {"name": "Functions & Pandas", "content": "def add(a,b): return a+b. Pandas: pd.read_csv, mean() - Must for DE!", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())", "q": "Pandas mean?", "opts": ["df['btech'].mean()", "mean(df)"], "ans": "df['btech'].mean()", "task": "Calculate mean"},
        ]
    },
    "C": {"title": "C - 5 Modules", "desc": "Mother of all languages", "modules": [
        {"name": "Intro", "content": "C by Dennis Ritchie 1972. Fast.", "code": "printf(\"Hello C\");", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie", "task": "Print Hello C"},
        {"name": "Variables", "content": "int btech=81 (4 bytes)", "code": "int btech=81;", "q": "Size int?", "opts": ["4 bytes", "2 bytes"], "ans": "4 bytes", "task": "Declare btech"},
        {"name": "Loops Final Boss", "content": "for(i=0;i<10;i+=3) -> 0 3 6 9", "code": "for(int i=0;i<10;i+=3) printf(\"%d \", i);", "q": "i+=3?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run loop"},
        {"name": "Pointers", "content": "Stores address. int *p=&a;", "code": "int *p=&a;", "q": "Pointer stores?", "opts": ["Address", "Value"], "ans": "Address", "task": "Create pointer"},
        {"name": "Structures", "content": "struct Student{ int id; char name[20]; };", "code": "struct Student s1;", "q": "struct for?", "opts": ["Structure", "Function"], "ans": "Structure", "task": "Create struct"},
    ]},
    "C++": {"title": "C++ - Gaming Engines", "desc": "C with Classes", "modules": [
        {"name": "Intro", "content": "C++ by Bjarne 1983. OOP + Gaming.", "code": "cout<<\"Hello C++\";", "q": "Who invented C++?", "opts": ["Bjarne", "Dennis"], "ans": "Bjarne", "task": "Print Hello C++"},
        {"name": "Variables", "content": "int btech=81, string college='Rise'", "code": "string college=\"Rise\";", "q": "string needs?", "opts": ["#include <string>", "No need"], "ans": "#include <string>", "task": "Declare string"},
        {"name": "Loops Final Boss", "content": "for(i=0;i<10;i+=3) -> 0 3 6 9", "code": "for(int i=0;i<10;i+=3) cout<<i<<\" \";", "q": "i+=3?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run loop"},
        {"name": "OOP", "content": "class Student{ public: string name; };", "code": "class Student{};", "q": "Object?", "opts": ["Student s1", "class Student"], "ans": "Student s1", "task": "Create class"},
        {"name": "STL", "content": "vector<int> coins={0,3,6,9};", "code": "vector<int> coins={0,3,6,9};", "q": "vector like?", "opts": ["ArrayList", "Map"], "ans": "ArrayList", "task": "Create vector"},
    ]},
    "Data Engineering": {"title": "Data Engineering - 8-15 LPA", "desc": "Build pipelines", "modules": [
        {"name": "Intro DE", "content": "DE builds pipelines. Tools: SQL, Python, ETL.", "code": "SELECT 'Hello DE';", "q": "DE builds?", "opts": ["Pipelines", "Models"], "ans": "Pipelines", "task": "Print Hello DE"},
        {"name": "SQL Basics", "content": "SELECT, WHERE filter, GROUP BY group", "code": "SELECT * FROM students WHERE btech>=60;", "q": "WHERE for?", "opts": ["Filter", "Group"], "ans": "Filter", "task": "SELECT with WHERE"},
        {"name": "ETL Extract", "content": "Extract from CSV: pd.read_csv", "code": "df=pd.read_csv('students.csv')", "q": "Extract?", "opts": ["Get data", "Store data"], "ans": "Get data", "task": "Extract CSV"},
        {"name": "ETL Transform", "content": "Transform: df['eligible']=df['btech']>=60", "code": "df['eligible']=df['btech']>=60", "q": "Transform?", "opts": ["Clean/filter", "Get data"], "ans": "Clean/filter", "task": "Add eligible column"},
        {"name": "Spark & Cloud", "content": "Spark 100x faster than Hadoop. AWS S3 storage.", "code": "df.groupBy('college').avg('btech')", "q": "Spark vs Hadoop?", "opts": ["Spark faster", "Hadoop faster"], "ans": "Spark faster", "task": "Explain Spark"},
    ]},
}
TOPICS["Java"] = TOPICS["C"]
TOPICS["Java"]["title"] = "Java - Android + Enterprise"
TOPICS["Java"]["desc"] = "WORA - Write Once Run Anywhere"
TOPICS["Software Engineering"] = TOPICS["Data Engineering"]
TOPICS["Software Engineering"]["title"] = "Software Engineering - SDLC, Agile"
TOPICS["Software Engineering"]["desc"] = "Build like BhavPath"

# --- ADS DATA - MONETIZATION ---
ADS = [
    {"title": "🔥 TCS NQT 2025 - Apply Now!", "desc": "60% eligibility? You have 81%! Apply for TCS NQT - 8 LPA package - Last date 30 Aug!", "cta": "Apply Now →", "color": "#FF6B6B"},
    {"title": "📚 Data Engineering Course - 50% OFF!", "desc": "Learn SQL + Python + Spark + AWS - 8-15 LPA role - For 81% profile - Coupon: BHAV50", "cta": "Enroll Now - 50% OFF →", "color": "#4ECDC4"},
    {"title": "💼 Resume Builder Pro - Free!", "desc": "Auto resume from BhavPath - ATS friendly - Used by Rise College toppers!", "cta": "Build Resume →", "color": "#45B7D1"},
]

def generate_certificate(name, college, btech, topic, xp, date_str):
    cert_html = f"""
    <div class="cert-card">
        <div style="font-size: 32px; font-weight: 900; color: #0F2C61; margin-bottom: 8px;">🏆 CERTIFICATE OF COMPLETION 🏆</div>
        <div style="font-size: 14px; color: #64748B; margin-bottom: 16px;">BhavPath - Gamified Learning Platform</div>
        <div style="border: 2px solid #FFB300; border-radius: 12px; padding: 16px; background: white; margin-bottom: 12px;">
            <div style="font-size: 18px; margin-bottom: 8px;">This is to certify that</div>
            <div style="font-size: 28px; font-weight: 900; color: #2563EB; margin-bottom: 8px;">{name}</div>
            <div style="font-size: 14px; margin-bottom: 8px;">from <b>{college}</b> with <b>{btech}% BTech</b></div>
            <div style="font-size: 16px; margin-bottom: 8px;">has successfully completed</div>
            <div style="font-size: 20px; font-weight: 800; color: #0F2C61; margin-bottom: 8px;">{topic} - Complete Tutorial</div>
            <div style="font-size: 14px; margin-bottom: 12px;">8 Modules + Final Boss Game (0,3,6,9) + Practice + Run Code</div>
            <div style="display: flex; justify-content: space-around; margin-top: 12px;">
                <div><b>XP Earned:</b> {xp}</div>
                <div><b>Date:</b> {date_str}</div>
                <div><b>Grade:</b> A+ 🔥</div>
            </div>
        </div>
        <div style="font-size: 12px; color: #64748B;">Certificate ID: BP-{btech}-{xp}-{date_str.replace('-','')} | Verify at bhavpath.streamlit.app/verify</div>
        <div style="font-size: 12px; color: #64748B; margin-top: 8px;">Issued by BhavPath | Founder: Bhav | Rise College, Ongole | 81% BTech</div>
    </div>
    """
    return cert_html

if not st.session_state.logged:
    st.title("🚀 BhavPath - Login - Certificate + Ads Ready")
    st.markdown('<div class="white-card"><b>2 Pages Only - No confusion - Certificate + Ads included - Monetization ready!</b></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email", placeholder="bhav@gmail.com")
        college = st.text_input("College Name", placeholder="Rise College, Ongole")
        btech = st.slider("BTech %", 0, 100, 81)
        st.markdown(f'<div class="blue-card"><b>Bet! {btech}% locked 🔥</b><br>Custom prep + Certificate + Ads</div>', unsafe_allow_html=True)
        if st.button("Login & Start → 🔥"):
            if email and college and "@" in email:
                st.session_state.user = {"email": email, "college": college, "btech": btech, "name": email.split("@")[0]}
                st.session_state.logged = True
                st.balloons()
                st.rerun()
            else:
                st.error("Valid email needed fr")
    with col2:
        st.markdown('<div class="ad-card"><b>📢 AD: Why BhavPath?</b><br>✅ Certificate on completion<br>✅ Ads = Monetization - 8-15k per month possible!<br>✅ Direct topic open, 8 modules, practice, run, game at bottom</div>', unsafe_allow_html=True)
        st.markdown('<div class="white-card"><b>🔥 Inside:</b><br>📚 Topics direct open<br>📖 8 Modules easy<br>🧠 Practice + Run side<br>🎮 Game bottom<br>🏆 Certificate<br>📢 Ads</div>', unsafe_allow_html=True)
else:
    # Header with XP
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | {st.session_state.selected_topic}</b></div>', unsafe_allow_html=True)
    done = len([k for k,v in st.session_state.completed.items() if v])
    st.write(f"Progress: {done} modules | Game unlocks at 3 | Certificate unlocks after Final Boss win")
    st.progress(min(done/8, 1.0))
    if done < 3:
        st.warning(f"🔒 Final Boss & Certificate Locked - Complete {3-done} more modules")
    elif not st.session_state.final_boss_won:
        st.success("🔥 Final Boss Unlocked! Scroll down - Win game to get Certificate!")
    else:
        st.success("🏆 Certificate Unlocked! Scroll down - Download your certificate!")
    
    if st.button("Logout"):
        st.session_state.logged = False
        st.session_state.cert_unlocked = False
        st.session_state.final_boss_won = False
        st.rerun()

    st.divider()
    
    # 3 COLUMNS + ADS
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
        # AD 1 - Left side ad
        ad = ADS[0]
        st.markdown(f'<div class="ad-card" style="background: {ad["color"]} !important;"><b>📢 AD</b><br><b>{ad["title"]}</b><br>{ad["desc"]}<br><br><b>{ad["cta"]}</b></div>', unsafe_allow_html=True)
        if st.button("Click AD - TCS NQT", key="ad1"):
            st.success("Ad clicked! Redirecting to TCS NQT apply page (simulated) - Monetization: ₹10 per click!")

    with col_content:
        t = TOPICS[st.session_state.selected_topic]
        st.subheader(f"📖 {t['title']}")
        mod_names = [m["name"] for m in t["modules"]]
        selected_idx = st.selectbox(f"Module ({len(mod_names)} total):", range(len(mod_names)), format_func=lambda x: f"{x+1}. {mod_names[x]}", index=st.session_state.current_mod)
        st.session_state.current_mod = selected_idx
        mod = t["modules"][selected_idx]
        
        st.markdown(f'<div class="white-card"><b>Module {selected_idx+1}: {mod["name"]}</b><br><br>{mod["content"]}</div>', unsafe_allow_html=True)
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
        
        # AD 2 - Middle ad - Between content and game
        st.divider()
        ad = ADS[1]
        st.markdown(f'<div class="ad-card" style="background: {ad["color"]} !important;"><b>📢 AD - Recommended for {st.session_state.user["btech"]}% profile</b><br><b>{ad["title"]}</b><br>{ad["desc"]}<br><b>{ad["cta"]}</b></div>', unsafe_allow_html=True)
        if st.button("Click AD - DE Course", key="ad2"):
            st.success("Ad clicked! Coupon BHAV50 applied - Monetization: ₹50 per enrollment!")

        st.divider()
        # GAME + CERTIFICATE - SAME PAGE BOTTOM
        st.subheader("🎮 FINAL BOSS - Game Zone + Certificate")
        if done >= 3:
            st.markdown(f'<div class="blue-card"><b>🔥 UNLOCKED! {done} modules done - Win game to unlock Certificate!</b><br>Loop Legends - 0,3,6,9 coins - From {mod["name"]}</div>', unsafe_allow_html=True)
            step = st.slider("for(i=0; i<10; i+=?) - Final answer? - 0,3,6,9 coins", 1,5,3, key="game")
            if st.button("PLAY FINAL BOSS 🔥 - Win for Certificate!", key="play_game"):
                coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
                st.write(f"Path {path} | {coll}/4")
                if coll==4:
                    st.balloons(); st.success(f"SLAYED FINAL BOSS! 🔥 +200 XP"); st.session_state.xp+=200; st.session_state.final_boss_won=True; st.session_state.cert_unlocked=True; st.snow()
                else:
                    st.error(f"Need i+=3 - Got {coll}/4")
            
            # CERTIFICATE - UNLOCKS AFTER FINAL BOSS WIN
            if st.session_state.cert_unlocked and st.session_state.final_boss_won:
                st.divider()
                st.subheader("🏆 Certificate - Unlocked! Download Now!")
                today = date.today().strftime("%d-%m-%Y")
                cert_html = generate_certificate(st.session_state.user["name"], st.session_state.user["college"], st.session_state.user["btech"], st.session_state.selected_topic, st.session_state.xp, today)
                st.markdown(cert_html, unsafe_allow_html=True)
                
                # Download as text file (simulate PDF)
                cert_text = f"""
BhavPath - Certificate of Completion

This is to certify that {st.session_state.user["name"]} from {st.session_state.user["college"]} with {st.session_state.user["btech"]}% BTech
has successfully completed {st.session_state.selected_topic} - Complete Tutorial
8 Modules + Final Boss Game (0,3,6,9) + Practice + Run Code

XP Earned: {st.session_state.xp}
Date: {today}
Grade: A+

Certificate ID: BP-{st.session_state.user["btech"]}-{st.session_state.xp}-{today.replace('-','')}
Verify at bhavpath.streamlit.app/verify
Issued by BhavPath | Founder: Bhav | Rise College, Ongole
"""
                st.download_button(
                    label="📥 Download Certificate (TXT) - For LinkedIn!",
                    data=cert_text,
                    file_name=f"BhavPath_Certificate_{st.session_state.selected_topic}_{st.session_state.user['name']}.txt",
                    mime="text/plain",
                )
                st.success("🏆 Certificate downloaded! Share on LinkedIn - Tag BhavPath - Viral avthundi!")
                st.markdown('<div class="white-card"><b>💡 How to use certificate?</b><br>1. Download TXT<br>2. Take screenshot of certificate card above<br>3. Post on LinkedIn: "I completed Python - 8 Modules + Final Boss game - BhavPath - Certificate - #BhavPath #Python #DataEngineering"<br>4. Tag Rise College, friends<br>5. Get 100+ likes - Placement ki help!</div>', unsafe_allow_html=True)
                
                # AD 3 - After certificate - High value ad
                ad = ADS[2]
                st.markdown(f'<div class="ad-card" style="background: {ad["color"]} !important;"><b>📢 AD - Celebrate your win!</b><br><b>{ad["title"]}</b><br>{ad["desc"]}<br><b>{ad["cta"]}</b></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="locked-card"><b>🔒 FINAL BOSS & Certificate Locked - Complete {3-done} more modules - Game + Certificate at bottom same page!</b></div>', unsafe_allow_html=True)

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
        
        st.divider()
        # AD 4 - Right side ad - Small
        ad = ADS[0]
        st.markdown(f'<div class="ad-card" style="background: #FF8C00 !important; font-size: 12px;"><b>📢 AD</b><br>{ad["title"][:20]}...<br>{ad["cta"]}</div>', unsafe_allow_html=True)
        
        st.divider()
        st.markdown('<div class="white-card"><b>📚 Modules</b></div>', unsafe_allow_html=True)
        for i, mname in enumerate(mod_names):
            key = f"{st.session_state.selected_topic}_{i}"
            done_mark = "✅" if st.session_state.completed.get(key) else "⬜"
            st.write(f"{done_mark} {i+1}. {mname}")

        # Certificate preview if unlocked
        if st.session_state.cert_unlocked:
            st.divider()
            st.markdown('<div class="cert-card"><b>🏆 Certificate Ready!</b><br>Scroll middle bottom to download!</div>', unsafe_allow_html=True)
