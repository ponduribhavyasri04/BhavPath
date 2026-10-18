  import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - Next Page + Example Sums", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #F8FAFC !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; font-size: 24px !important; }
h2,h3 { color: #0F2C61 !important; }
.white-card { background: #FFFFFF !important; border-radius: 10px; padding: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-bottom: 8px; border: 1px solid #E2E8F0; color: #000000 !important; }
.blue-card { background: #2563EB !important; border-radius: 10px; padding: 12px; color: #FFFFFF !important; }
.blue-card b, .blue-card div { color: #FFFFFF !important; }
.bullet-card { background: #FFFFFF !important; border-radius: 10px; padding: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; }
.ad-card { background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important; border-radius: 10px; padding: 12px; margin-bottom: 8px; color: #FFFFFF !important; }
.ad-card b, .ad-card div { color: #FFFFFF !important; }
.cert-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFE082 100%) !important; border: 3px solid #FFB300 !important; border-radius: 16px; padding: 20px; text-align: center; }
.practice-card { background: #FFFBEB !important; border: 1px solid #F59E0B; border-radius: 8px; padding: 10px; margin-bottom: 8px; color: #000000 !important; }
.example-card { background: #F0FDF4 !important; border: 1px solid #86EFAC; border-radius: 8px; padding: 10px; margin-bottom: 8px; color: #000000 !important; }
.example-card b { color: #166534 !important; }
.run-card { background: #1E293B !important; border-radius: 8px; padding: 10px; color: #FFFFFF !important; }
.locked-card { background: #E2E8F0 !important; border-radius: 8px; padding: 10px; color: #000000 !important; }
.stButton>button { background: #2563EB !important; color: #FFFFFF !important; border-radius: 8px; font-weight: bold !important; border: none !important; }
.stButton>button * { color: #FFFFFF !important; }
.stCodeBlock, .stCodeBlock * { background-color: #1E293B !important; color: #FFFFFF !important; }
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
if 'page_view' not in st.session_state: st.session_state.page_view = "list"

TOPICS = {
    "Python": {"title": "Python - 8 Modules", "desc": "Easy + Data Science", "modules": [
        {"name": "Introduction", "content": "Python by Guido 1991. Easy syntax. Pandas for Data Science.", "code": "print(\"Hello Python\")", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum", "task": "Print Hello Python",
         "examples": [{"qs": "Ex 1: Print your name Bhav with 81%", "code": "name='Bhav'\nbtech=81\nprint(f\"{name} {btech}%\")\n# Output: Bhav 81%", "ans": "Use f-string"}, {"qs": "Ex 2: Print Hello World", "code": "print(\"Hello World\")", "ans": "Simple print"}]},
        {"name": "Basic Input / Output", "content": "input() for input, print() for output.", "code": "name=input('Enter: ')\nprint(name)", "q": "Input function?", "opts": ["input()", "scanf"], "ans": "input()", "task": "Take input",
         "examples": [{"qs": "Ex 1: Take BTech % as input", "code": "btech=int(input(\"Enter BTech %: \"))\nprint(f\"Your %: {btech}\")", "ans": "int(input())"}, {"qs": "Ex 2: Add two numbers", "code": "a=int(input())\nb=int(input())\nprint(a+b)", "ans": "input + int"}]},
        {"name": "Identifiers", "content": "Names for variables, functions. Must start with letter/_ - Example: my_var, btech, _name valid; 1var invalid", "code": "my_var=81\nprint(my_var)", "q": "Valid identifier?", "opts": ["my_var", "1var"], "ans": "my_var", "task": "Identifier",
         "examples": [{"qs": "Ex 1: Valid vs Invalid", "code": "# Valid\nmy_btech=81\n_name='Bhav'\nbtech1=81\n# Invalid - 1btech=81 (starts with number)\nprint(my_btech)", "ans": "Letter/_ start only"}, {"qs": "Ex 2: Find invalid - _score, 2score, score2", "code": "_score=81 # valid\nscore2=81 # valid\n# 2score=81 # invalid", "ans": "2score invalid"}]},
        {"name": "Keywords", "content": "Reserved words like if, else, for, def, class. Cannot use as identifier. 35 keywords in Python.", "code": "import keyword\nprint(keyword.kwlist)", "q": "Keyword?", "opts": ["for", "bhav"], "ans": "for", "task": "List keywords",
         "examples": [{"qs": "Ex 1: List all keywords", "code": "import keyword\nprint(keyword.kwlist)\nprint(len(keyword.kwlist)) # 35", "ans": "35 keywords"}, {"qs": "Ex 2: Check if 'bhav' is keyword", "code": "import keyword\nprint(keyword.iskeyword('bhav')) # False\nprint(keyword.iskeyword('for')) # True", "ans": "iskeyword()"}]},
        {"name": "Variables", "content": "No type needed! btech=81, name='Bhav'. Dynamic typing.", "code": "btech=81\nname='Bhav'\nprint(f\"{name} {btech}%\")", "q": "Python var?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81", "task": "Declare btech=81",
         "examples": [{"qs": "Ex 1: Swap two numbers", "code": "a=81\nb=75\na,b=b,a\nprint(a,b) # 75 81", "ans": "a,b=b,a"}, {"qs": "Ex 2: Store college and %", "code": "college='Rise College'\nbtech=81\nprint(college, btech)", "ans": "Variable assignment"}]},
        {"name": "Data Types", "content": "int, float, str, list [81,75,80] mutable, dict {'name':'Bhav'}", "code": "marks=[81,75,80]\nprint(type(marks))", "q": "Mutable?", "opts": ["list", "tuple"], "ans": "list", "task": "Data Types",
         "examples": [{"qs": "Ex 1: List - Avg marks", "code": "marks=[81,75,80]\navg=sum(marks)/len(marks)\nprint(avg) # 78.66", "ans": "sum/len"}, {"qs": "Ex 2: Dict - Student info", "code": "student={'name':'Bhav','btech':81,'college':'Rise'}\nprint(student['name'])", "ans": "Dict key access"}]},
        {"name": "Operators", "content": "Arithmetic + - * / %, Comparison == !=, Logical and or", "code": "a=81\nb=60\nprint(a>=b)", "q": "Comparison?", "opts": [">=", "+"], "ans": ">=", "task": "Operators",
         "examples": [{"qs": "Ex 1: Check eligible 60%", "code": "btech=81\nprint(btech>=60) # True - Eligible\nprint(btech<60) # False", "ans": ">= comparison"}, {"qs": "Ex 2: Even or Odd", "code": "num=81\nprint(num%2==0) # False - Odd\nprint(num%2==1) # True", "ans": "% modulo"}]},
        {"name": "Conditional Statements", "content": "if btech>=60: eligible else not - TCS NQT 60%!", "code": "if 81>=60:\n    print('Eligible')", "q": "if condition?", "opts": ["if btech>=60:", "for btech"], "ans": "if btech>=60:", "task": "Conditional",
         "examples": [{"qs": "Ex 1: TCS NQT Eligibility", "code": "btech=81\nif btech>=60:\n    print(\"Eligible for TCS NQT - 8 LPA\")\nelse:\n    print(\"Not Eligible\")", "ans": "if-else"}, {"qs": "Ex 2: Grade", "code": "per=81\nif per>=80:\n    print(\"A grade\")\nelif per>=60:\n    print(\"B grade\")\nelse:\n    print(\"C grade\")", "ans": "if-elif-else"}]},
        {"name": "Loops", "content": "for i in range(0,10,3): print(i) -> 0 3 6 9 coins! Final Boss!", "code": "for i in range(0,10,3):\n    print(i, end=\" \") # 0 3 6 9", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run range 0-10 step 3",
         "examples": [{"qs": "Ex 1: Print 0 3 6 9 - Final Boss", "code": "for i in range(0,10,3):\n    print(i, end=\" \")\n# Output: 0 3 6 9 - Collect 4 coins!", "ans": "range(0,10,3)"}, {"qs": "Ex 2: Sum 1 to 10", "code": "total=0\nfor i in range(1,11):\n    total+=i\nprint(total) # 55", "ans": "Loop sum"}, {"qs": "Ex 3: Table of 81", "code": "for i in range(1,6):\n    print(f\"81 x {i} = {81*i}\")", "ans": "Loop table"}]},
        {"name": "Pandas", "content": "Pandas: df=pd.DataFrame, mean() - Must for DE!", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())", "q": "Pandas mean?", "opts": ["df['btech'].mean()", "mean(df)"], "ans": "df['btech'].mean()", "task": "Calculate mean",
         "examples": [{"qs": "Ex 1: Avg BTech % with Pandas", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75,80,85]})\nprint(df['btech'].mean()) # 80.25", "ans": "df.mean()"}, {"qs": "Ex 2: Filter >=60", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,45,60]})\neligible=df[df['btech']>=60]\nprint(eligible)", "ans": "df filter"}]},
    ]},
    "C": {"title": "C - Mother Language", "desc": "Dennis Ritchie 1972", "modules": [
        {"name": "Introduction", "content": "C by Dennis Ritchie. Fast.", "code": "printf(\"Hello C\");", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie", "task": "Print Hello C", "examples": [{"qs": "Ex: Hello C", "code": "printf(\"Hello C\");", "ans": "printf"}]},
        {"name": "Loops", "content": "for(i=0;i<10;i+=3) -> 0 3 6 9", "code": "for(int i=0;i<10;i+=3) printf(\"%d \", i);", "q": "i+=3?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9", "task": "Run loop", "examples": [{"qs": "Ex: 0 3 6 9", "code": "for(int i=0;i<10;i+=3) printf(\"%d \", i);", "ans": "i+=3"}]},
    ]},
    "Data Engineering": {"title": "Data Engineering - 8-15 LPA", "desc": "Build pipelines", "modules": [
        {"name": "SQL Basics", "content": "SELECT, WHERE filter, GROUP BY", "code": "SELECT * FROM students WHERE btech>=60;", "q": "WHERE for?", "opts": ["Filter", "Group"], "ans": "Filter", "task": "SELECT with WHERE", "examples": [{"qs": "Ex: Filter eligible", "code": "SELECT * FROM students WHERE btech>=60;", "ans": "WHERE filter"}]},
        {"name": "ETL", "content": "Extract pd.read_csv, Transform eligible, Load to warehouse", "code": "df['eligible']=df['btech']>=60", "q": "Transform?", "opts": ["Clean/filter", "Get data"], "ans": "Clean/filter", "task": "Add eligible column", "examples": [{"qs": "Ex: Add eligible", "code": "df['eligible']=df['btech']>=60", "ans": "Transform"}]},
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
        <div style="font-size: 28px; font-weight: 900; color: #0F2C61;">🏆 CERTIFICATE 🏆</div>
        <div style="border: 2px solid #FFB300; border-radius: 12px; padding: 16px; background: white;">
            <div style="font-size: 26px; font-weight: 900; color: #2563EB;">{name}</div>
            <div style="font-size: 14px;">from <b>{college}</b> with <b>{btech}% BTech</b></div>
            <div style="font-size: 18px; font-weight: 800; color: #0F2C61; margin-top: 8px;">{topic}</div>
            <div style="display: flex; justify-content: space-around; margin-top: 12px;"><div><b>XP:</b> {xp}</div><div><b>Date:</b> {date_str}</div><div><b>Grade:</b> A+</div></div>
        </div>
    </div>
    """

if not st.session_state.logged:
    st.title("🚀 BhavPath - Login")
    st.markdown('<div class="white-card"><b>Welcome! Login with Email + College only</b></div>', unsafe_allow_html=True)
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
    with col2:
        st.markdown('<div class="white-card"><b>🔥 Flow:</b><br>1. Login<br>2. Percentage + Purpose<br>3. Main App</div>', unsafe_allow_html=True)

elif not st.session_state.purpose_done:
    st.title("📊 One More Step! - Your Stats")
    st.markdown(f'<div class="white-card">Yo <b>{st.session_state.user["name"]}</b>! Welcome 🚀<br>🏫 {st.session_state.user["college"]}</div>', unsafe_allow_html=True)
    btech = st.slider("What's your BTech flex?", 0, 100, st.session_state.user.get("btech", 81))
    st.markdown(f'<div class="blue-card"><b>Bet! Locked in: {btech}% 🔥</b></div>', unsafe_allow_html=True)
    st.divider()
    if st.button(f"Browse Topics with {btech}% →"):
        st.session_state.user["btech"] = btech
        st.session_state.purpose_done = True
        st.rerun()

else:
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | {st.session_state.selected_topic}</b></div>', unsafe_allow_html=True)
    done = len([k for k,v in st.session_state.completed.items() if v])
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
        new_btech = st.slider(f"Change BTech % - Current {st.session_state.user['btech']}%", 0, 100, st.session_state.user["btech"], key="change_btech")
        if new_btech != st.session_state.user["btech"]:
            st.session_state.user["btech"] = new_btech
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
                st.session_state.page_view = "list"
                st.rerun()
        st.divider()
        ad = ADS[0]
        st.markdown(f'<div class="ad-card"><b>📢 AD</b><br><b>{ad["title"]}</b><br>{ad["desc"]}<br><b>{ad["cta"]}</b></div>', unsafe_allow_html=True)

    with col_content:
        t = TOPICS[st.session_state.selected_topic]

        if st.session_state.page_view == "list":
            st.subheader(f"📖 {t['title']} - For {st.session_state.user['btech']}%")
            st.markdown(f'<div class="bullet-card"><b>📋 {t["title"]} - Modules List - Select cheyagane next page lo open:</b></div>', unsafe_allow_html=True)
            for i, mod in enumerate(t["modules"]):
                is_done = st.session_state.completed.get(f"{st.session_state.selected_topic}_{i}")
                tick = "✅" if is_done else "•"
                if st.button(f"{tick} {i+1}. {mod['name']} → Open in Next Page", key=f"nextpage_{st.session_state.selected_topic}_{i}", use_container_width=True):
                    st.session_state.current_mod = i
                    st.session_state.page_view = "detail"
                    st.rerun()
        else:
            mod = t["modules"][st.session_state.current_mod]
            if st.button(f"← Back to {t['title']} List", key="back_to_list", use_container_width=True):
                st.session_state.page_view = "list"
                st.rerun()
            st.divider()
            st.subheader(f"📖 Next Page - {t['title']}")
            st.markdown(f'<div class="blue-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]} - Full Page Open ✅</b></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="white-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]}</b><br><br>{mod["content"]}<br><br>For {st.session_state.user["btech"]}% profile - Helps in TCS NQT!</div>', unsafe_allow_html=True)
            st.code(mod["code"], language="python")
            col_prev, col_done, col_next = st.columns([1,1,1])
            with col_prev:
                if st.session_state.current_mod > 0:
                    if st.button("← Prev Module"):
                        st.session_state.current_mod -=1
                        st.rerun()
                if st.button("← Back to List"):
                    st.session_state.page_view = "list"
                    st.rerun()
            with col_done:
                key = f"{st.session_state.selected_topic}_{st.session_state.current_mod}"
                if st.session_state.completed.get(key): st.success("✅ Done")
                else:
                    if st.button(f"Mark Done +50 XP", key=f"done_{key}"):
                        st.session_state.completed[key]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
            with col_next:
                if st.session_state.current_mod < len(t["modules"])-1:
                    if st.button("Next Module →"):
                        st.session_state.current_mod+=1
                        st.rerun()
            st.divider()
            st.subheader("🎮 FINAL BOSS - Game + Certificate")
            if done >= 3:
                st.markdown(f'<div class="blue-card"><b>🔥 UNLOCKED! {done} modules</b></div>', unsafe_allow_html=True)
                step = st.slider("for(i=0; i<10; i+=?)", 1,5,3, key="game")
                if st.button("PLAY FINAL BOSS 🔥", key="play_game"):
                    coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
                    st.write(f"Path {path} | {coll}/4")
                    if coll==4:
                        st.balloons(); st.success(f"SLAYED! +200 XP"); st.session_state.xp+=200; st.session_state.final_boss_won=True; st.session_state.cert_unlocked=True
                    else:
                        st.error(f"Need i+=3 - Got {coll}/4")
                if st.session_state.cert_unlocked and st.session_state.final_boss_won:
                    today = date.today().strftime("%d-%m-%Y")
                    cert_html = generate_certificate(st.session_state.user["name"], st.session_state.user["college"], st.session_state.user["btech"], st.session_state.selected_topic, st.session_state.xp, today)
                    st.markdown(cert_html, unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="locked-card"><b>🔒 Locked - Complete {3-done} more</b></div>', unsafe_allow_html=True)

    with col_practice:
        if st.session_state.page_view == "detail":
            mod = TOPICS[st.session_state.selected_topic]["modules"][st.session_state.current_mod]
            st.subheader("🧠 Practice - Next Page")
            st.markdown(f'<div class="practice-card"><b>Practice - {mod["name"]} - Next Page lo</b></div>', unsafe_allow_html=True)
            st.write(f"**Q: {mod['q']}**")
            choice = st.radio("Choose:", mod["opts"], key=f"quiz_{st.session_state.selected_topic}_{st.session_state.current_mod}")
            if st.button("Check Answer", key=f"check_{st.session_state.current_mod}"):
                if choice == mod["ans"]:
                    st.success(f"✅ Correct! +20 XP"); st.session_state.xp+=20; st.balloons()
                else:
                    st.error(f"❌ Wrong! Correct: {mod['ans']}")

            st.divider()
            # ===== EXAMPLE SUMS - PRACTICE KI - NEXT PAGE LO =====
            st.subheader("📝 Example Sums - Practice")
            for idx, ex in enumerate(mod.get("examples", [])):
                st.markdown(f'<div class="example-card"><b>Example {idx+1}: {ex["qs"]}</b></div>', unsafe_allow_html=True)
                st.code(ex["code"], language="python")
                with st.expander(f"Show Answer - Example {idx+1}"):
                    st.success(f"Answer: {ex['ans']}")
            # ===== EXAMPLE SUMS END =====

            st.divider()
            st.subheader("▶️ Run Code")
            st.markdown(f'<div class="run-card"><b>Run - {mod["task"]}</b></div>', unsafe_allow_html=True)
            code_input = st.text_area("Code:", value=mod["code"], height=120, key=f"code_{st.session_state.current_mod}")
            if st.button("▶️ Run", key=f"run_{st.session_state.current_mod}"):
                st.success(f"Output: Hello BhavPath! Task {mod['task']} done! ✅")
        else:
            st.subheader("👈 Select Module")
            st.markdown('<div class="white-card"><b>List lo nundi ye module select chesthe adhi next page lo open avutundi - Full content + Example Sums + Practice + Run + Game antha next page lo!</b></div>', unsafe_allow_html=True)
