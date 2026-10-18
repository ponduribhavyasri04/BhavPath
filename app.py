import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - No Side Box When Locked", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #F8FAFC !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 14px; border: 1px solid #E2E8F0; }
.white-card b, .white-card div { color: #000000 !important; font-weight: 600 !important; }
.blue-card { background: #2563EB !important; border-radius: 12px; padding: 14px; }
.blue-card * { color: #FFFFFF !important; font-weight: 700 !important; }
.bullet-card { background: #FFFFFF !important; border-radius: 12px; padding: 18px; border: 1px solid #E2E8F0; }
.bullet-card b, .bullet-card div { color: #000000 !important; }
.info-card { background: #EFF6FF !important; border-left: 5px solid #2563EB !important; border-radius: 10px; padding: 14px; margin-bottom: 12px; }
.info-card b, .info-card div { color: #000000 !important; }
.ad-card { background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important; border-radius: 12px; padding: 12px; }
.ad-card * { color: #FFFFFF !important; }
.cert-card { background: linear-gradient(135deg, #FFF8E1 0%, #FFE082 100%) !important; border: 3px solid #FFB300 !important; border-radius: 16px; padding: 20px; text-align: center; }
.practice-card { background: #FFFBEB !important; border: 2px solid #F59E0B; border-radius: 10px; padding: 14px; margin-bottom: 10px; }
.practice-card b, .practice-card div { color: #000000 !important; font-weight: 800 !important; }
.example-card { background: #F0FDF4 !important; border: 2px solid #86EFAC; border-radius: 10px; padding: 14px; margin-bottom: 12px; }
.example-card * { color: #000000 !important; }
.locked-card { background: #E2E8F0 !important; border-radius: 8px; padding: 10px; }
.locked-card * { color: #000000 !important; }
.stButton>button { background: #2563EB !important; border-radius: 8px; font-weight: bold !important; border: none !important; }
.stButton>button * { color: #FFFFFF !important; }
div[data-testid="stRadio"] { background: #FFFFFF !important; border-radius: 10px; padding: 10px; border: 1px solid #E2E8F0; }
div[data-testid="stRadio"] label p { color: #000000 !important; font-weight: 700 !important; font-size: 16px !important; }
div[data-testid="stRadio"] div[role="radiogroup"] label { background: #F8FAFC !important; border: 1px solid #CBD5E1 !important; border-radius: 8px; padding: 8px 12px !important; width: 100%; }
label[data-testid="stWidgetLabel"] p { color: #000000 !important; font-weight: 900 !important; font-size: 18px !important; }
div[data-testid="stCodeBlock"] { background-color: #1E293B !important; border-radius: 10px !important; }
div[data-testid="stCodeBlock"] * { color: #E2E8F0 !important; }
div[data-testid="stTextArea"] textarea { background-color: #1E293B !important; color: #FFFFFF !important; font-size: 14px !important; border: 2px solid #334155 !important; }
div[data-testid="stTextArea"] label p { color: #000000 !important; font-weight: 800 !important; }
div[data-testid="stTextArea"] { background: #FFFFFF !important; padding: 10px; border-radius: 10px; border: 1px solid #E2E8F0; }
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state:
    st.session_state.logged=False
    st.session_state.user={"btech":81}
    st.session_state.xp=820
    st.session_state.selected_topic="Python"
    st.session_state.completed={}
    st.session_state.current_mod=0
    st.session_state.cert_unlocked=False
    st.session_state.final_boss_won=False
    st.session_state.purpose_done=False
    st.session_state.page_view="list"

def make_modules(base_name):
    return [
        {"name":"Introduction","about":f"{base_name} ante enti? Easy language, beginners ki best.","content":f"{base_name} easy syntax with print()","code":"print(\"Hello Bhav\")\nprint(\"Welcome to BhavPath\")","q":"Who invented Python?","opts":["Guido van Rossum - Creator","Dennis Ritchie - C Creator"],"ans":"Guido van Rossum - Creator","task":"Print Hello","examples":[{"qs":"Print Bhav 81%","code":"name='Bhav'\nprint(name)","ans":"print()"}]},
        {"name":"Basic Input / Output","about":"Input/Output - input() tho data, print() tho output. BTech % ki int(input()).","content":"input() for input, print() for output","code":"name=input('Enter name: ')\nprint(f\"Hello {name}\")","q":"Which function for input?","opts":["input() - Python","scanf() - C"],"ans":"input() - Python","task":"Take input","examples":[{"qs":"Take BTech","code":"btech=int(input())\nprint(btech)","ans":"input()"}]},
        {"name":"Identifiers","about":"Identifiers - Variable names. letter/_ start, number kaadu. my_var valid, 1var invalid.","content":"my_var valid, 1var invalid","code":"my_btech=81\n_name='Bhav'\nprint(my_btech)","q":"Valid identifier?","opts":["my_var - Valid","1var - Invalid"],"ans":"my_var - Valid","task":"Identifier","examples":[{"qs":"Valid vs Invalid","code":"_score=81 # valid","ans":"letter/_"}]},
        {"name":"Keywords","about":"Keywords - Reserved words, for if else def class - 35 keywords.","content":"35 keywords - for, if, else","code":"import keyword\nprint(keyword.kwlist)","q":"Which is keyword?","opts":["for is keyword","bhav is not keyword"],"ans":"for is keyword","task":"Keywords","examples":[{"qs":"List keywords","code":"import keyword\nprint(keyword.kwlist)","ans":"35"}]},
        {"name":"Variables","about":"Variables - Data store container. Python lo type vaddu, btech=81 direct. Swap a,b=b,a.","content":"No type needed btech=81","code":"btech=81\nname='Bhav'\nprint(f\"{name} {btech}%\")\na=81\nb=75\na,b=b,a\nprint(a,b)","q":"How to declare variable?","opts":["btech=81 - Python style","int btech=81 - C style"],"ans":"btech=81 - Python style","task":"Declare btech","examples":[{"qs":"Swap","code":"a=81\nb=75\na,b=b,a","ans":"Swap"}]},
        {"name":"Data Types","about":"Data Types - int 81, float 81.5, str 'Bhav', list [81,75,80] mutable, dict key-value.","content":"int, float, str, list mutable, dict","code":"marks=[81,75,80,85]\nprint(sum(marks)/len(marks))","q":"Mutable?","opts":["list is mutable","tuple is immutable"],"ans":"list is mutable","task":"Avg marks","examples":[{"qs":"Avg","code":"marks=[81,75,80]\nprint(sum(marks)/len(marks))","ans":"avg"}]},
        {"name":"Operators","about":"Operators - Arithmetic + - * / %, Comparison >= ==, Logical and or.","content":"Arithmetic + - * / %, Comparison >=","code":"btech=81\nprint(btech>=60)","q":"Comparison for 60%?","opts":[">= greater equal","+ plus"],"ans":">= greater equal","task":"Check >=60","examples":[{"qs":"Eligible","code":"btech=81\nprint(btech>=60)","ans":"True"}]},
        {"name":"Conditional Statements","about":"Conditional - if btech>=60 eligible else not. elif grades A+ B C.","content":"if elif else","code":"btech=81\nif btech>=80:\n    print('A+ - 81%')\nelif btech>=60:\n    print('Eligible')","q":"Correct if?","opts":["if btech>=60: correct","for btech wrong"],"ans":"if btech>=60: correct","task":"TCS eligibility","examples":[{"qs":"TCS NQT","code":"if 81>=60:\n    print('Eligible')","ans":"if"}]},
        {"name":"Loops","about":"Loops - Repeat work. range(0,10,3) ante 0 3 6 9 coins Final Boss! Sum 1-10=55.","content":"for i in range(0,10,3): 0 3 6 9","code":"for i in range(0,10,3):\n    print(i)\ntotal=0\nfor i in range(1,11):\n    total+=i\nprint(total)","q":"Output range(0,10,3)?","opts":["0 3 6 9 coins","0 1 2 no coins"],"ans":"0 3 6 9 coins","task":"Collect coins","examples":[{"qs":"0 3 6 9","code":"for i in range(0,10,3):\n    print(i)","ans":"0 3 6 9"}]},
        {"name":"Pandas","about":"Pandas - Data analysis, DataFrame table, mean filter >=60.","content":"Pandas DataFrame mean","code":"import pandas as pd\ndf=pd.DataFrame({'btech':[81,75,80,85]})\nprint(df['btech'].mean())","q":"Pandas mean?","opts":["df['btech'].mean() correct","mean(df) wrong"],"ans":"df['btech'].mean() correct","task":"Avg Pandas","examples":[{"qs":"Avg","code":"import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())","ans":"mean"}]},
    ]

def make_sql_modules():
    return [
        {"name":"Introduction to SQL","about":"SQL - Structured Query Language, database ki, TCS must.","content":"SQL for database","code":"CREATE DATABASE bhavpath_db;\nUSE bhavpath_db;","q":"SQL stands for?","opts":["Structured Query Language","Simple Query Language"],"ans":"Structured Query Language","task":"Create DB","examples":[{"qs":"Create DB","code":"CREATE DATABASE rise;","ans":"CREATE"}]},
        {"name":"SELECT Statement","about":"SELECT - Data chudataniki, * all columns.","content":"SELECT * FROM students","code":"SELECT * FROM students;\nSELECT name, btech FROM students;","q":"Select all?","opts":["SELECT * FROM students","SELECT ALL FROM students"],"ans":"SELECT * FROM students","task":"SELECT all","examples":[{"qs":"Select Bhav","code":"SELECT * FROM students WHERE name='Bhav';","ans":"WHERE"}]},
        {"name":"WHERE Clause","about":"WHERE - Filter ki, btech>=60 eligible.","content":"WHERE filtering","code":"SELECT * FROM students WHERE btech>=60;","q":"Filter 60%?","opts":["WHERE btech>=60","FILTER btech>=60"],"ans":"WHERE btech>=60","task":"Filter >=60","examples":[{"qs":"81% filter","code":"SELECT * FROM students WHERE btech=81;","ans":"WHERE"}]},
        {"name":"INSERT Statement","about":"INSERT - Kotta data add ki.","content":"INSERT INTO VALUES","code":"INSERT INTO students (name, btech) VALUES ('Bhav', 81);","q":"Insert?","opts":["INSERT INTO VALUES","ADD INTO"],"ans":"INSERT INTO VALUES","task":"Insert Bhav","examples":[{"qs":"Insert Bhav","code":"INSERT INTO students VALUES ('Bhav',81);","ans":"INSERT"}]},
        {"name":"UPDATE Statement","about":"UPDATE - Unna data marchadaniki.","content":"UPDATE SET WHERE","code":"UPDATE students SET btech=85 WHERE name='Bhav';","q":"Update?","opts":["UPDATE SET","MODIFY SET"],"ans":"UPDATE SET","task":"Update","examples":[{"qs":"Update Bhav","code":"UPDATE students SET btech=85 WHERE name='Bhav';","ans":"UPDATE"}]},
        {"name":"DELETE Statement","about":"DELETE - Data delete ki, WHERE lekunda all delete.","content":"DELETE WHERE","code":"DELETE FROM students WHERE btech<60;","q":"Delete low?","opts":["DELETE WHERE btech<60","REMOVE WHERE"],"ans":"DELETE WHERE btech<60","task":"Delete <60","examples":[{"qs":"Delete low","code":"DELETE FROM students WHERE btech<60;","ans":"DELETE"}]},
        {"name":"JOINs","about":"JOINs - Rendu tables kalapadaniki.","content":"JOIN INNER JOIN","code":"SELECT * FROM students INNER JOIN placements ON id;","q":"Join?","opts":["INNER JOIN common","JOIN TABLES wrong"],"ans":"INNER JOIN common","task":"Join","examples":[{"qs":"Inner join","code":"SELECT * FROM students INNER JOIN placements ON id;","ans":"INNER JOIN"}]},
        {"name":"GROUP BY","about":"GROUP BY - Group chesi COUNT AVG.","content":"GROUP BY college","code":"SELECT college, COUNT(*) FROM students GROUP BY college;","q":"Group by?","opts":["GROUP BY college","GROUP college"],"ans":"GROUP BY college","task":"Avg per college","examples":[{"qs":"Count","code":"SELECT college, COUNT(*) FROM students GROUP BY college;","ans":"GROUP BY"}]},
        {"name":"ORDER BY","about":"ORDER BY - Sort ki, DESC high to low topper first.","content":"ORDER BY DESC","code":"SELECT * FROM students ORDER BY btech DESC;","q":"Order high to low?","opts":["ORDER BY DESC high to low","ORDER BY ASC low to high"],"ans":"ORDER BY DESC high to low","task":"Topper first","examples":[{"qs":"Top 3","code":"SELECT * FROM students ORDER BY btech DESC LIMIT 3;","ans":"DESC"}]},
        {"name":"Aggregate Functions","about":"Aggregate - COUNT AVG MAX MIN SUM.","content":"COUNT AVG MAX MIN","code":"SELECT COUNT(*) FROM students;\nSELECT AVG(btech) FROM students;","q":"Avg?","opts":["AVG(btech)","AVERAGE(btech)"],"ans":"AVG(btech)","task":"Avg calc","examples":[{"qs":"Avg","code":"SELECT AVG(btech) FROM students;","ans":"AVG"}]},
    ]

TOPICS={
    "Python":{"title":"Python - 10 Modules","desc":"Easy + Data Science","modules":make_modules("Python")},
    "C":{"title":"C - 10 Modules","desc":"Dennis Ritchie 1972 - Mother","modules":make_modules("C")},
    "C++":{"title":"C++ - 10 Modules","desc":"Bjarne Stroustrup - Gaming","modules":make_modules("C++")},
    "Java":{"title":"Java - 10 Modules","desc":"James Gosling - Android","modules":make_modules("Java")},
    "SQL":{"title":"SQL - 10 Modules","desc":"Database - TCS must - 8 LPA","modules":make_sql_modules()},
}
ADS=[{"title":"TCS NQT 2025 - Apply Now!","desc":"60% eligibility? You have 81%! 8 LPA!","cta":"Apply Now"}]

def generate_certificate(name,college,btech,topic,xp,date_str):
    return f"""<div class="cert-card"><div style="font-size: 22px; font-weight: 900; color: #0F2C61;">CERTIFICATE</div><div style="font-size: 12px; color: #000000; font-weight: 700;">BhavPath Verified</div><div style="border: 2px solid #FFB300; border-radius: 12px; padding: 12px; background: white; margin-top:8px;"><div style="font-size: 18px; font-weight: 900; color: #2563EB;">{name}</div><div style="font-size: 11px; color: #000000;">from {college} with {btech}%</div><div style="font-size: 14px; font-weight: 800; color: #0F2C61; margin-top:6px;">{topic}</div><div style="display: flex; justify-content: space-around; margin-top:8px; font-size:10px; color: #000000;"><div><b>XP:</b> {xp}</div><div><b>Date:</b> {date_str}</div><div><b>Grade:</b> A+</div></div></div></div>"""

if not st.session_state.logged:
    st.title("BhavPath - Login")
    st.markdown('<div class="white-card">Welcome! Login</div>', unsafe_allow_html=True)
    email=st.text_input("Email",placeholder="bhav@gmail.com")
    college=st.text_input("College Name",placeholder="Rise College, Ongole")
    if st.button("Login & Continue"):
        if email and college and "@" in email:
            st.session_state.user={"email":email,"college":college,"btech":81,"name":email.split("@")[0]}
            st.session_state.logged=True
            st.session_state.purpose_done=False
            st.balloons()
            st.rerun()
elif not st.session_state.purpose_done:
    st.title("One More Step!")
    btech=st.slider("BTech %?",0,100,81)
    if st.button(f"Browse Topics with {btech}%"):
        st.session_state.user["btech"]=btech
        st.session_state.purpose_done=True
        st.rerun()
else:
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | {st.session_state.selected_topic}</b></div>', unsafe_allow_html=True)
    done=len([k for k,v in st.session_state.completed.items() if v])
    st.progress(min(done/8,1.0))
    if st.button("Back - Change %"):
        st.session_state.purpose_done=False
        st.rerun()
    st.divider()
    if st.session_state.page_view=="list":
        col_topics,col_content=st.columns([1,3])
    else:
        # CERTIFICATE SIDE KI KADA - HIDE WHEN LOCKED
        if st.session_state.cert_unlocked and st.session_state.final_boss_won:
            col_topics,col_content,col_side=st.columns([0.5,2.4,0.8])
        else:
            col_topics,col_content=st.columns([0.7,3.0])
    with col_topics:
        st.subheader("Topics")
        for tname in TOPICS.keys():
            is_sel=st.session_state.selected_topic==tname
            if is_sel:
                st.markdown(f'<div class="blue-card"><b>{tname} SELECTED</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="white-card"><b>{tname}</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
            if st.button(f"Open {tname}",key=f"open_{tname}"):
                st.session_state.selected_topic=tname
                st.session_state.current_mod=0
                st.session_state.page_view="list"
                st.rerun()
        ad=ADS[0]
        st.markdown(f'<div class="ad-card"><b>{ad["title"]}</b><br>{ad["desc"]}</div>', unsafe_allow_html=True)
    with col_content:
        t=TOPICS[st.session_state.selected_topic]
        if st.session_state.page_view=="list":
            st.subheader(f"{t['title']} - {len(t['modules'])} Modules")
            st.markdown(f'<div class="bullet-card"><b>{t["title"]} - Modules List - Topic select chesukunna taruwata middle lo content, code space, practice vastundi!</b><br>Python, C, C++, Java, SQL only - DE/SE deleted!</div>', unsafe_allow_html=True)
            for i,mod in enumerate(t["modules"]):
                is_done=st.session_state.completed.get(f"{st.session_state.selected_topic}_{i}")
                tick="✅" if is_done else "•"
                if st.button(f"{tick} {i+1}. {mod['name']} -> Open",key=f"nextpage_{st.session_state.selected_topic}_{i}",use_container_width=True):
                    st.session_state.current_mod=i
                    st.session_state.page_view="detail"
                    st.rerun()
        else:
            mod=t["modules"][st.session_state.current_mod]
            if st.button(f"← Back to {t['title']} List",key="back_to_list",use_container_width=True):
                st.session_state.page_view="list"
                st.rerun()
            st.divider()
            st.subheader(f"{t['title']} - Module {st.session_state.current_mod+1}")
            st.markdown(f'<div class="blue-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]}</b></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><b>📘 About {mod["name"]} - Content Information:</b><br><br>{mod["about"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="white-card"><b>📚 Summary:</b> {mod["content"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bullet-card"><b>💻 Code for {mod["name"]} - Code Space:</b></div>', unsafe_allow_html=True)
            st.code(mod["code"],language="python" if "SQL" not in t['title'] else "sql")
            st.divider()
            st.subheader("▶️ Code Space - Your Code - Middle Spacious")
            st.markdown(f'<div class="white-card"><b>Your Code Space - {mod["task"]} - Spacious:</b><br>Topic select chesukunna taruwata code space ikkada vastundi - Big area!</div>', unsafe_allow_html=True)
            code_input=st.text_area("Your Code - Big Area:",value=mod["code"],height=250,key=f"code_mid_{st.session_state.current_mod}")
            if st.button("▶️ Run Code - Middle",key=f"run_mid_{st.session_state.current_mod}",use_container_width=True):
                st.success(f"✅ Output: {mod['task']} done!")
                st.code(code_input,language="python" if "SQL" not in t['title'] else "sql")
            st.divider()
            st.subheader("🧠 Practice Space - Middle - Black Clear")
            st.markdown(f'<div class="practice-card"><b>Practice - {mod["name"]} - Middle</b><br><br>Q: {mod["q"]}</div>', unsafe_allow_html=True)
            choice=st.radio("Select Answer - Black Clear:",mod["opts"],key=f"quiz_mid_{st.session_state.selected_topic}_{st.session_state.current_mod}")
            if st.button("Check Answer - Middle",key=f"check_mid_{st.session_state.current_mod}",use_container_width=True):
                if choice==mod["ans"]:
                    st.success(f"✅ Correct! {mod['ans']} - +20 XP")
                    st.session_state.xp+=20
                    st.balloons()
                else:
                    st.error(f"❌ Wrong! Correct: {mod['ans']}")
            st.divider()
            st.subheader("📝 Example Sums - Middle")
            for idx,ex in enumerate(mod.get("examples",[])):
                st.markdown(f'<div class="example-card"><b>Example {idx+1}: {ex["qs"]}</b></div>', unsafe_allow_html=True)
                st.code(ex["code"],language="python" if "SQL" not in t['title'] else "sql")
                with st.expander(f"Show Answer - Example {idx+1}"):
                    st.success(f"Answer: {ex['ans']}")
            col_prev,col_done,col_next=st.columns([1,1,1])
            with col_prev:
                if st.session_state.current_mod>0:
                    if st.button("← Prev"):
                        st.session_state.current_mod-=1
                        st.rerun()
            with col_done:
                key=f"{st.session_state.selected_topic}_{st.session_state.current_mod}"
                if st.session_state.completed.get(key):
                    st.success("✅ Done")
                else:
                    if st.button(f"Mark Done +50 XP",key=f"done_mid_{key}"):
                        st.session_state.completed[key]=True
                        st.session_state.xp+=50
                        st.balloons()
                        st.rerun()
            with col_next:
                if st.session_state.current_mod<len(t["modules"])-1:
                    if st.button("Next →"):
                        st.session_state.current_mod+=1
                        st.rerun()
            st.divider()
            st.subheader("🎮 FINAL BOSS")
            if done>=3:
                st.markdown(f'<div class="blue-card"><b>🔥 UNLOCKED! {done} modules</b></div>', unsafe_allow_html=True)
                step=st.slider("for(i=0; i<10; i+=?)",1,5,3,key="game")
                if st.button("PLAY FINAL BOSS 🔥",key="play_game_mid"):
                    coins=[0,3,6,9]
                    path=list(range(0,10,step))
                    coll=len([x for x in path if x in coins])
                    st.write(f"Path {path} | {coll}/4")
                    if coll==4:
                        st.balloons()
                        st.success(f"SLAYED! +200 XP - Certificate side lo vachindhi!")
                        st.session_state.xp+=200
                        st.session_state.final_boss_won=True
                        st.session_state.cert_unlocked=True
                        st.rerun()
                    else:
                        st.error(f"Need i+=3 - Got {coll}/4")
            else:
                st.markdown(f'<div class="locked-card"><b>🔒 Locked - Complete {3-done} more</b></div>', unsafe_allow_html=True)
    if st.session_state.page_view=="detail":
        if st.session_state.cert_unlocked and st.session_state.final_boss_won:
            with col_side:
                today=date.today().strftime("%d-%m-%Y")
                cert_html=generate_certificate(st.session_state.user["name"],st.session_state.user["college"],st.session_state.user["btech"],st.session_state.selected_topic,st.session_state.xp,today)
                st.markdown(cert_html,unsafe_allow_html=True)
                cert_text=f"BhavPath Certificate - {st.session_state.user['name']} - {st.session_state.user['college']} - {st.session_state.user['btech']}% - {st.session_state.selected_topic} - XP {st.session_state.xp} - Date {today}"
                st.download_button(label="📥 Download Certificate",data=cert_text,file_name=f"Certificate_{st.session_state.selected_topic}.txt",mime="text/plain",use_container_width=True)             
