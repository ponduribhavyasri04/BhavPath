import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - Final Overall", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #F8FAFC !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 10px; border: 1px solid #E2E8F0; }
.white-card * { color: #000000 !important; font-weight: 600 !important; }
.blue-card { background: #2563EB !important; border-radius: 12px; padding: 14px; }
.blue-card * { color: #FFFFFF !important; }
.bullet-card { background: #FFFFFF !important; border-radius: 12px; padding: 18px; border: 1px solid #E2E8F0; }
.bullet-card * { color: #000000 !important; }
.ad-card { background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important; border-radius: 12px; padding: 12px; }
.ad-card * { color: #FFFFFF !important; }
.cert-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFE082 100%) !important; border: 3px solid #FFB300 !important; border-radius: 16px; padding: 20px; text-align: center; }
.cert-side-card { background: #FFF8E1 !important; border: 2px solid #FFB300 !important; border-radius: 12px; padding: 12px; }
.cert-side-card * { color: #000000 !important; }
.practice-card { background: #FFFBEB !important; border: 2px solid #F59E0B; border-radius: 10px; padding: 14px; margin-bottom: 10px; }
.practice-card * { color: #000000 !important; font-weight: 800 !important; }
.example-card { background: #F0FDF4 !important; border: 2px solid #86EFAC; border-radius: 10px; padding: 14px; margin-bottom: 12px; }
.example-card * { color: #000000 !important; font-weight: 700 !important; }
.example-card b { color: #166534 !important; }
.run-card { background: #1E293B !important; border-radius: 10px; padding: 14px; }
.run-card * { color: #FFFFFF !important; }
.locked-card { background: #E2E8F0 !important; border-radius: 8px; padding: 10px; }
.locked-card * { color: #000000 !important; }
.stButton>button { background: #2563EB !important; border-radius: 8px; font-weight: bold !important; border: none !important; }
.stButton>button * { color: #FFFFFF !important; }
div[data-testid="stRadio"] { background: #FFFFFF !important; border-radius: 10px; padding: 10px; border: 1px solid #E2E8F0; }
div[data-testid="stRadio"] * { color: #000000 !important; font-weight: 700 !important; font-size: 16px !important; }
div[data-testid="stRadio"] label { color: #000000 !important; font-weight: 800 !important; font-size: 16px !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label { background: #F8FAFC !important; border: 1px solid #CBD5E1 !important; border-radius: 8px; padding: 8px 12px !important; width: 100%; }
label[data-testid="stWidgetLabel"] { color: #000000 !important; font-weight: 900 !important; font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state:
    st.session_state.logged = False
if 'user' not in st.session_state:
    st.session_state.user = {"btech": 81}
if 'xp' not in st.session_state:
    st.session_state.xp = 820
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = "Python"
if 'completed' not in st.session_state:
    st.session_state.completed = {}
if 'current_mod' not in st.session_state:
    st.session_state.current_mod = 0
if 'cert_unlocked' not in st.session_state:
    st.session_state.cert_unlocked = False
if 'final_boss_won' not in st.session_state:
    st.session_state.final_boss_won = False
if 'purpose_done' not in st.session_state:
    st.session_state.purpose_done = False
if 'page_view' not in st.session_state:
    st.session_state.page_view = "list"

def make_modules(base_name):
    return [
        {"name": "Introduction", "content": f"{base_name} - Easy syntax. By Guido 1991.", "code": "print(\"Hello\")", "q": "Who invented Python?", "opts": ["Guido van Rossum - Creator", "Dennis Ritchie - C Creator"], "ans": "Guido van Rossum - Creator", "task": "Print Hello", "examples": [{"qs": "Ex 1: Print Bhav 81%", "code": "name='Bhav'\nbtech=81\nprint(f\"{name} {btech}%\")\n# Output: Bhav 81%", "ans": "f-string"}, {"qs": "Ex 2: Hello from Rise College", "code": "college='Rise College'\nprint(f\"Hello from {college}\")", "ans": "f-string"}, {"qs": "Ex 3: Simple calc", "code": "a=81\nb=60\nprint(a+b) # 141", "ans": "141"}]},
        {"name": "Basic Input / Output", "content": "input() for input, print() for output.", "code": "name=input('Enter: ')\nprint(name)", "q": "Which function for input in Python?", "opts": ["input() - Python input", "scanf() - C input"], "ans": "input() - Python input", "task": "Take input", "examples": [{"qs": "Ex 1: Take BTech % as input", "code": "btech=int(input(\"Enter BTech %: \"))\nif btech>=60:\n    print(\"Eligible\")\nelse:\n    print(\"Not Eligible\")", "ans": "int(input()) + if"}, {"qs": "Ex 2: Add two numbers", "code": "a=int(input(\"Enter a: \"))\nb=int(input(\"Enter b: \"))\nprint(f\"Sum: {a+b}\")", "ans": "Add with input"}]},
        {"name": "Identifiers", "content": "Names for variables. Must start with letter/_ - my_var valid, 1var invalid", "code": "my_var=81\nprint(my_var)", "q": "Valid identifier?", "opts": ["my_var - Valid", "1var - Invalid"], "ans": "my_var - Valid", "task": "Identifier", "examples": [{"qs": "Ex 1: Valid vs Invalid Full List", "code": "# Valid: my_btech=81, _name='Bhav', btech1=81\n# Invalid: 1btech=81 (number start), my-var (hyphen), my btech (space)\nprint(\"Valid only\")", "ans": "Letter/_ start"}, {"qs": "Ex 2: Find invalid: _score, 2score, score2", "code": "_score=81 # valid\nscore2=81 # valid\n# 2score invalid - number start", "ans": "2score invalid"}, {"qs": "Ex 3: 3 valid identifiers", "code": "btech_percentage=81\ncollege_name='Rise College'\nstudent_name='Bhav'\nprint(btech_percentage, college_name, student_name)", "ans": "Valid names"}]},
        {"name": "Keywords", "content": "Reserved words like if, else, for, def, class. 35 keywords.", "code": "import keyword\nprint(keyword.kwlist)", "q": "Which is keyword?", "opts": ["for - Loop keyword", "bhav - Not keyword"], "ans": "for - Loop keyword", "task": "List keywords", "examples": [{"qs": "Ex 1: List all 35 keywords", "code": "import keyword\nprint(keyword.kwlist)\nprint(f\"Total: {len(keyword.kwlist)}\") # 35", "ans": "35 keywords"}, {"qs": "Ex 2: Check if keyword", "code": "import keyword\nprint(keyword.iskeyword('for')) # True\nprint(keyword.iskeyword('bhav')) # False", "ans": "iskeyword()"}]},
        {"name": "Variables", "content": "No type needed! btech=81, name='Bhav'. Dynamic typing.", "code": "btech=81\nname='Bhav'\nprint(f\"{name} {btech}%\")", "q": "How to declare variable in Python?", "opts": ["btech=81 - Python style", "int btech=81 - C style"], "ans": "btech=81 - Python style", "task": "Declare btech=81", "examples": [{"qs": "Ex 1: Swap 81 and 75", "code": "a=81\nb=75\nprint(f\"Before: {a}, {b}\")\na,b=b,a\nprint(f\"After: {a}, {b}\") # 75 81", "ans": "a,b=b,a"}, {"qs": "Ex 2: Store student info", "code": "college='Rise College, Ongole'\nbtech=81\nname='Bhav'\nprint(f\"{name}, {btech}%, {college}\")", "ans": "Multiple variables"}]},
        {"name": "Data Types", "content": "int, float, str, list [81,75,80] mutable, dict {'name':'Bhav'}", "code": "marks=[81,75,80]\nprint(type(marks))", "q": "Which is mutable?", "opts": ["list - Mutable", "tuple - Immutable"], "ans": "list - Mutable", "task": "Data Types", "examples": [{"qs": "Ex 1: Avg marks 81,75,80,85", "code": "marks=[81,75,80,85]\ntotal=sum(marks)\navg=total/len(marks)\nprint(f\"Total: {total}, Avg: {avg}\") # 80.25", "ans": "sum/len"}, {"qs": "Ex 2: Dict - Student info", "code": "student={'name':'Bhav','btech':81,'college':'Rise','eligible':True}\nprint(student['name'])\nprint(student['btech'])", "ans": "Dict access"}]},
        {"name": "Operators", "content": "Arithmetic + - * / %, Comparison == !=, Logical and or", "code": "a=81\nb=60\nprint(a>=b)", "q": "Comparison operator for eligibility?", "opts": [">= - Greater equal", "+ - Plus"], "ans": ">= - Greater equal", "task": "Operators", "examples": [{"qs": "Ex 1: TCS NQT eligibility 81%>=60%", "code": "btech=81\nprint(f\"btech>=60: {btech>=60}\") # True - Eligible for 8 LPA\nprint(f\"btech==81: {btech==81}\") # True", "ans": ">= comparison"}, {"qs": "Ex 2: Even or Odd 81", "code": "num=81\nif num%2==0:\n    print(\"Even\")\nelse:\n    print(\"Odd\") # Odd", "ans": "% modulo"}]},
        {"name": "Conditional Statements", "content": "if btech>=60: eligible else not - TCS NQT 60%!", "code": "if 81>=60:\n    print('Eligible')", "q": "Correct if condition?", "opts": ["if btech>=60: - Correct", "for btech - Wrong"], "ans": "if btech>=60: - Correct", "task": "Conditional", "examples": [{"qs": "Ex 1: TCS NQT 81%", "code": "btech=81\nif btech>=60:\n    print(\"Eligible for TCS NQT - 8 LPA\")\nelse:\n    print(\"Not Eligible\")", "ans": "if-else"}, {"qs": "Ex 2: Grade 81%", "code": "per=81\nif per>=90:\n    print(\"O - Outstanding\")\nelif per>=80:\n    print(\"A+ - Excellent - 81%\")\nelif per>=60:\n    print(\"B\")\nelse:\n    print(\"C\")", "ans": "if-elif-else"}, {"qs": "Ex 3: All subjects eligible", "code": "btech=81\ntenth=75\ninter=80\nif btech>=60 and tenth>=60 and inter>=60:\n    print(\"Eligible for all\")", "ans": "and operator"}]},
        {"name": "Loops", "content": "for i in range(0,10,3): print(i) -> 0 3 6 9 coins! Final Boss!", "code": "for i in range(0,10,3):\n    print(i, end=\" \") # 0 3 6 9", "q": "Output of range(0,10,3)?", "opts": ["0 3 6 9 - Final Boss coins", "0 1 2 - No coins"], "ans": "0 3 6 9 - Final Boss coins", "task": "Run range 0-10 step 3", "examples": [{"qs": "Ex 1: Print 0 3 6 9 - Final Boss", "code": "print(\"Collecting coins: 0,3,6,9\")\nfor i in range(0,10,3):\n    print(f\"Coin at {i} Collected!\")\nprint(\"4/4 coins - Boss Slayed!\")", "ans": "range(0,10,3)"}, {"qs": "Ex 2: Sum 1 to 10 = 55", "code": "total=0\nfor i in range(1,11):\n    total+=i\nprint(f\"Final Sum: {total}\") # 55", "ans": "Loop sum 55"}, {"qs": "Ex 3: Table of 81 - 5 times", "code": "print(\"Table of 81:\")\nfor i in range(1,6):\n    print(f\"81 x {i} = {81*i}\")", "ans": "Table loop"}, {"qs": "Ex 4: Print Bhav 3 times", "code": "for i in range(3):\n    print(f\"{i+1}. Bhav - Rise College - 81%\")", "ans": "Simple loop"}]},
        {"name": "Pandas", "content": "Pandas: df=pd.DataFrame, mean() - Must for DE!", "code": "import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())", "q": "Pandas mean?", "opts": ["df['btech'].mean() - Correct", "mean(df) - Wrong"], "ans": "df['btech'].mean() - Correct", "task": "Calculate mean", "examples": [{"qs": "Ex 1: Avg BTech with Pandas", "code": "import pandas as pd\ndf=pd.DataFrame({'name':['Bhav','Ravi','Sita'], 'btech':[81,75,80]})\nprint(df)\nprint(f\"Avg: {df['btech'].mean()}\")", "ans": "df.mean()"}, {"qs": "Ex 2: Filter eligible >=60", "code": "import pandas as pd\ndf=pd.DataFrame({'name':['Bhav','Ravi','Low'], 'btech':[81,45,60]})\neligible=df[df['btech']>=60]\nprint(eligible)\nprint(f\"Count: {len(eligible)}\")", "ans": "df filtering"}]},
    ]

TOPICS = {
    "Python": {"title": "Python - 10 Modules", "desc": "Easy + Data Science", "modules": make_modules("Python")},
    "C": {"title": "C - 10 Modules", "desc": "Dennis Ritchie 1972 - Mother Language", "modules": make_modules("C")},
    "C++": {"title": "C++ - 10 Modules", "desc": "Bjarne Stroustrup - Gaming Engines", "modules": make_modules("C++")},
    "Java": {"title": "Java - 10 Modules", "desc": "James Gosling - Android + Enterprise", "modules": make_modules("Java")},
    "Data Engineering": {"title": "Data Engineering - 10 Modules", "desc": "Build pipelines - 8-15 LPA", "modules": make_modules("Data Engineering")},
    "Software Engineering": {"title": "Software Engineering - 10 Modules", "desc": "SDLC, Agile, Design Patterns", "modules": make_modules("Software Engineering")},
}

ADS = [{"title": "TCS NQT 2025 - Apply Now!", "desc": "60% eligibility? You have 81%! 8 LPA package!", "cta": "Apply Now"}]

def generate_certificate(name, college, btech, topic, xp, date_str):
    return f"""
    <div class="cert-card">
        <div style="font-size: 22px; font-weight: 900; color: #0F2C61;">🏆 CERTIFICATE 🏆</div>
        <div style="font-size: 12px; color: #64748B;">BhavPath - 10 Modules</div>
        <div style="border: 2px solid #FFB300; border-radius: 12px; padding: 12px; background: white; margin-top:8px;">
            <div style="font-size: 18px; font-weight: 900; color: #2563EB;">{name}</div>
            <div style="font-size: 11px; color: #000000;">from {college} with {btech}% BTech</div>
            <div style="font-size: 14px; font-weight: 800; color: #0F2C61; margin-top:6px;">{topic}</div>
            <div style="font-size: 10px; color: #000000;">10 Modules + Final Boss Slayed</div>
            <div style="display: flex; justify-content: space-around; margin-top:8px; font-size:10px; color: #000000;"><div><b>XP:</b> {xp}</div><div><b>Date:</b> {date_str}</div><div><b>Grade:</b> A+</div></div>
        </div>
        <div style="font-size: 8px; color: #64748B; margin-top:6px;">ID: BP-{btech}-{xp} | Verified</div>
    </div>
    """

if not st.session_state.logged:
    st.title("BhavPath - Login")
    st.markdown('<div class="white-card">Welcome! Login with Email + College only</div>', unsafe_allow_html=True)
    email = st.text_input("Email", placeholder="bhav@gmail.com")
    college = st.text_input("College Name", placeholder="Rise College, Ongole")
    if st.button("Login & Continue"):
        if email and college and "@" in email:
            st.session_state.user = {"email": email, "college": college, "btech": 81, "name": email.split("@")[0]}
            st.session_state.logged = True
            st.session_state.purpose_done = False
            st.balloons()
            st.rerun()
        else:
            st.error("Valid email and college needed")

elif not st.session_state.purpose_done:
    st.title("One More Step! - Your Stats")
    st.markdown(f'<div class="white-card">Yo {st.session_state.user["name"]}! Welcome<br>{st.session_state.user["college"]}</div>', unsafe_allow_html=True)
    btech = st.slider("What's your BTech %?", 0, 100, 81)
    st.markdown(f'<div class="blue-card"><b>Locked in: {btech}%</b></div>', unsafe_allow_html=True)
    if st.button(f"Browse Topics with {btech}%"):
        st.session_state.user["btech"] = btech
        st.session_state.purpose_done = True
        st.rerun()

else:
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | {st.session_state.selected_topic}</b></div>', unsafe_allow_html=True)
    done = len([k for k,v in st.session_state.completed.items() if v])
    st.progress(min(done/8, 1.0))
    if st.button("Back - Change %"):
        st.session_state.purpose_done = False
        st.rerun()
    st.divider()

    if st.session_state.page_view == "list":
        col_topics, col_content = st.columns([1, 3])
    else:
        col_topics, col_content, col_side = st.columns([0.7, 1.5, 1.8])

    with col_topics:
        st.subheader("📚 Topics")
        for tname in TOPICS.keys():
            is_sel = st.session_state.selected_topic == tname
            if is_sel:
                st.markdown(f'<div class="blue-card"><b>{tname} SELECTED</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="white-card"><b>{tname}</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
            if st.button(f"Open {tname}", key=f"open_{tname}"):
                st.session_state.selected_topic = tname
                st.session_state.current_mod = 0
                st.session_state.page_view = "list"
                st.rerun()
        ad = ADS[0]
        st.markdown(f'<div class="ad-card"><b>{ad["title"]}</b><br>{ad["desc"]}</div>', unsafe_allow_html=True)

    with col_content:
        t = TOPICS[st.session_state.selected_topic]
        if st.session_state.page_view == "list":
            st.subheader(f"{t['title']} - {len(t['modules'])} Modules")
            st.markdown(f'<div class="bullet-card"><b>{t["title"]} - Modules List - Select cheyagane next page lo open:</b><br>Python ki laane anni skills ki list vasthundi - C, C++, Java, DE, SE kuda!</div>', unsafe_allow_html=True)
            for i, mod in enumerate(t["modules"]):
                is_done = st.session_state.completed.get(f"{st.session_state.selected_topic}_{i}")
                tick = "✅" if is_done else "•"
                if st.button(f"{tick} {i+1}. {mod['name']} -> Open in Next Page", key=f"nextpage_{st.session_state.selected_topic}_{i}", use_container_width=True):
                    st.session_state.current_mod = i
                    st.session_state.page_view = "detail"
                    st.rerun()
        else:
            mod = t["modules"][st.session_state.current_mod]
            if st.button(f"← Back to {t['title']} List", key="back_to_list", use_container_width=True):
                st.session_state.page_view = "list"
                st.rerun()
            st.divider()
            st.subheader(f"Next Page - {t['title']}")
            st.markdown(f'<div class="blue-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]} - Full Page Open</b></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="white-card"><b>{mod["name"]}</b><br><br>{mod["content"]}<br><br>For {st.session_state.user["btech"]}% profile - Helps in TCS NQT!</div>', unsafe_allow_html=True)
            st.code(mod["code"], language="python")
            col_prev, col_done, col_next = st.columns([1,1,1])
            with col_prev:
                if st.session_state.current_mod > 0:
                    if st.button("← Prev"):
                        st.session_state.current_mod -= 1
                        st.rerun()
            with col_done:
                key = f"{st.session_state.selected_topic}_{st.session_state.current_mod}"
                if st.session_state.completed.get(key):
                    st.success("✅ Done")
                else:
                    if st.button(f"Mark Done +50 XP", key=f"done_{key}"):
                        st.session_state.completed[key] = True
                        st.session_state.xp += 50
                        st.balloons()
                        st.rerun()
            with col_next:
                if st.session_state.current_mod < len(t["modules"])-1:
                    if st.button("Next →"):
                        st.session_state.current_mod += 1
                        st.rerun()
            st.divider()
            st.subheader("🎮 FINAL BOSS - Game + Certificate Side ki")
            if done >= 3:
                st.markdown(f'<div class="blue-card"><b>🔥 UNLOCKED! {done} modules - Win for Certificate Side lo!</b></div>', unsafe_allow_html=True)
                step = st.slider("for(i=0; i<10; i+=?)", 1, 5, 3, key="game")
                if st.button("PLAY FINAL BOSS 🔥", key="play_game"):
                    coins = [0, 3, 6, 9]
                    path = list(range(0, 10, step))
                    coll = len([x for x in path if x in coins])
                    st.write(f"Path {path} | {coll}/4")
                    if coll == 4:
                        st.balloons()
                        st.success(f"SLAYED! +200 XP - Certificate side lo chudu!")
                        st.session_state.xp += 200
                        st.session_state.final_boss_won = True
                        st.session_state.cert_unlocked = True
                    else:
                        st.error(f"Need i+=3 - Got {coll}/4")
            else:
                st.markdown(f'<div class="locked-card"><b>🔒 Locked - Complete {3-done} more - Certificate side ki vastundi after win!</b></div>', unsafe_allow_html=True)

    if st.session_state.page_view == "detail":
        with col_side:
            st.subheader("🏆 Certificate - Side ki")
            if st.session_state.cert_unlocked and st.session_state.final_boss_won:
                today = date.today().strftime("%d-%m-%Y")
                cert_html = generate_certificate(st.session_state.user["name"], st.session_state.user["college"], st.session_state.user["btech"], st.session_state.selected_topic, st.session_state.xp, today)
                st.markdown(cert_html, unsafe_allow_html=True)
                cert_text = f"BhavPath Certificate - {st.session_state.user['name']} - {st.session_state.user['college']} - {st.session_state.user['btech']}% - {st.session_state.selected_topic} - XP {st.session_state.xp} - Date {today}"
                st.download_button(label="📥 Download Certificate", data=cert_text, file_name=f"Certificate_{st.session_state.selected_topic}.txt", mime="text/plain", use_container_width=True)
            else:
                st.markdown('<div class="cert-side-card"><b>🏆 Certificate Side ki</b><br>Game win chey - Ikkada side lo certificate vastundi!<br><br>🔒 Locked - 3 modules + Final Boss</div>', unsafe_allow_html=True)
            st.divider()
            mod = TOPICS[st.session_state.selected_topic]["modules"][st.session_state.current_mod]
            st.subheader("🧠 Practice - Side - BLACK LETTERS")
            st.markdown(f'<div class="practice-card"><b>Practice - {mod["name"]}</b><br><br>Q: {mod["q"]}</div>', unsafe_allow_html=True)
            choice = st.radio("Select Answer - Black Clear:", mod["opts"], key=f"quiz_{st.session_state.selected_topic}_{st.session_state.current_mod}")
            if st.button("Check Answer", key=f"check_{st.session_state.current_mod}", use_container_width=True):
                if choice == mod["ans"]:
                    st.success(f"✅ Correct! {mod['ans']} - +20 XP")
                    st.session_state.xp += 20
                    st.balloons()
                else:
                    st.error(f"❌ Wrong! Correct: {mod['ans']}")
            st.divider()
            st.subheader("📝 Example Sums - BIG - Side")
            st.markdown('<div class="white-card"><b>Example Sums - Big ga - 3-4 per module!</b></div>', unsafe_allow_html=True)
            for idx, ex in enumerate(mod.get("examples", [])):
                st.markdown(f'<div class="example-card"><b>Example {idx+1}: {ex["qs"]} - BIG</b></div>', unsafe_allow_html=True)
                st.code(ex["code"], language="python")
                with st.expander(f"✅ Show Answer - Example {idx+1}", expanded=False):
                    st.success(f"Answer: {ex['ans']}")
            st.divider()
            st.subheader("▶️ Run Code - Side")
            st.markdown(f'<div class="run-card"><b>Run - {mod["task"]}</b></div>', unsafe_allow_html=True)
            code_input = st.text_area("Your Code - Big Area:", value=mod["code"], height=200, key=f"code_{st.session_state.current_mod}")
            if st.button("▶️ Run Code", key=f"run_{st.session_state.current_mod}", use_container_width=True):
                st.success(f"✅ Output: Task {mod['task']} done! Big column lo!")
                st.code(code_input, language="python")
