import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #F8FAFC !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 14px; border: 1px solid #E2E8F0; }
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
.practice-card { background: #FFFBEB !important; border: 2px solid #F59E0B; border-radius: 10px; padding: 14px; }
.practice-card * { color: #000000 !important; font-weight: 800 !important; }
.example-card { background: #F0FDF4 !important; border: 2px solid #86EFAC; border-radius: 10px; padding: 14px; }
.example-card * { color: #000000 !important; font-weight: 700 !important; }
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
    st.session_state.logged=False
if 'user' not in st.session_state:
    st.session_state.user={"btech":81}
if 'xp' not in st.session_state:
    st.session_state.xp=820
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic="Python"
if 'completed' not in st.session_state:
    st.session_state.completed={}
if 'current_mod' not in st.session_state:
    st.session_state.current_mod=0
if 'cert_unlocked' not in st.session_state:
    st.session_state.cert_unlocked=False
if 'final_boss_won' not in st.session_state:
    st.session_state.final_boss_won=False
if 'purpose_done' not in st.session_state:
    st.session_state.purpose_done=False
if 'page_view' not in st.session_state:
    st.session_state.page_view="list"

def make_modules(base_name):
    return [
        {"name":"Introduction","content":f"{base_name} Easy syntax.","code":"print(\"Hello\")","q":"Who invented Python?","opts":["Guido van Rossum - Creator","Dennis Ritchie - C Creator"],"ans":"Guido van Rossum - Creator","task":"Print Hello","examples":[{"qs":"Ex 1: Print Bhav 81%","code":"name='Bhav'\nprint(name)","ans":"print()"}]},
        {"name":"Basic Input / Output","content":"input() for input, print() for output.","code":"name=input('Enter: ')\nprint(name)","q":"Which function for input?","opts":["input() - Python input","scanf() - C input"],"ans":"input() - Python input","task":"IO","examples":[{"qs":"Ex 1: Take BTech %","code":"btech=int(input())\nprint(btech)","ans":"input()"}]},
        {"name":"Identifiers","content":"Names for variables. my_var valid, 1var invalid","code":"my_var=81","q":"Valid identifier?","opts":["my_var is valid","1var is invalid"],"ans":"my_var is valid","task":"Identifier","examples":[{"qs":"Ex: Valid vs Invalid","code":"# Valid: my_var\n# Invalid: 1var","ans":"letter/_"}]},
        {"name":"Keywords","content":"Reserved words like if, else, for - 35 keywords","code":"import keyword\nprint(keyword.kwlist)","q":"Which is keyword?","opts":["for is keyword","bhav is not keyword"],"ans":"for is keyword","task":"Keywords","examples":[{"qs":"Ex: List keywords","code":"import keyword\nprint(keyword.kwlist)","ans":"35"}]},
        {"name":"Variables","content":"No type needed! btech=81","code":"btech=81","q":"How to declare variable?","opts":["btech=81 - Python style","int btech=81 - C style"],"ans":"btech=81 - Python style","task":"Variable","examples":[{"qs":"Ex: Swap","code":"a=81\nb=75\na,b=b,a","ans":"Swap"}]},
        {"name":"Data Types","content":"int, float, str, list mutable","code":"marks=[81,75,80]","q":"Mutable?","opts":["list is mutable","tuple is not mutable"],"ans":"list is mutable","task":"Data Types","examples":[{"qs":"Ex: Avg","code":"marks=[81,75,80]\nprint(sum(marks)/len(marks))","ans":"avg"}]},
        {"name":"Operators","content":"+ - * / %, Comparison","code":"a=81\nprint(a>=60)","q":"Comparison for 60%?","opts":[">= greater than equal","+ plus operator"],"ans":">= greater than equal","task":"Operators","examples":[{"qs":"Ex: Eligible","code":"btech=81\nprint(btech>=60)","ans":"True"}]},
        {"name":"Conditional Statements","content":"if btech>=60: eligible","code":"if 81>=60:\n    print('Eligible')","q":"Correct if condition?","opts":["if btech>=60: correct","for btech wrong"],"ans":"if btech>=60: correct","task":"Conditional","examples":[{"qs":"Ex: TCS NQT","code":"if 81>=60:\n    print('Eligible')","ans":"if"}]},
        {"name":"Loops","content":"for i in range(0,10,3): -> 0 3 6 9","code":"for i in range(0,10,3):\n    print(i, end=\" \")","q":"Output of range(0,10,3)?","opts":["0 3 6 9 coins","0 1 2 no coins"],"ans":"0 3 6 9 coins","task":"Loops","examples":[{"qs":"Ex 1: 0 3 6 9","code":"for i in range(0,10,3):\n    print(i)","ans":"0 3 6 9"},{"qs":"Ex 2: Sum 1-10","code":"total=0\nfor i in range(1,11):\n    total+=i\nprint(total)","ans":"55"}]},
        {"name":"Pandas","content":"Pandas mean()","code":"import pandas as pd","q":"Pandas mean?","opts":["df['btech'].mean() correct","mean(df) wrong"],"ans":"df['btech'].mean() correct","task":"Pandas","examples":[{"qs":"Ex: Mean","code":"import pandas as pd\ndf=pd.DataFrame({'btech':[81,75]})\nprint(df['btech'].mean())","ans":"mean"}]},
    ]

TOPICS={
    "Python":{"title":"Python - 10 Modules","desc":"Easy + Data Science","modules":make_modules("Python")},
    "C":{"title":"C - 10 Modules","desc":"Dennis Ritchie 1972","modules":make_modules("C")},
    "C++":{"title":"C++ - 10 Modules","desc":"Gaming Engines","modules":make_modules("C++")},
    "Java":{"title":"Java - 10 Modules","desc":"Android","modules":make_modules("Java")},
    "Data Engineering":{"title":"Data Engineering - 10 Modules","desc":"8-15 LPA","modules":make_modules("Data Engineering")},
    "Software Engineering":{"title":"Software Engineering - 10 Modules","desc":"SDLC, Agile","modules":make_modules("Software Engineering")},
}
ADS=[{"title":"TCS NQT 2025 - Apply Now!","desc":"60% eligibility? You have 81%!","cta":"Apply Now"}]

def generate_certificate(name,college,btech,topic,xp,date_str):
    return f"""<div class="cert-card"><div style="font-size: 22px; font-weight: 900; color: #0F2C61;">🏆 CERTIFICATE 🏆</div><div style="border: 2px solid #FFB300; border-radius: 12px; padding: 12px; background: white; margin-top:8px;"><div style="font-size: 18px; font-weight: 900; color: #2563EB;">{name}</div><div style="font-size: 11px; color: #000000;">from {college} with {btech}%</div><div style="font-size: 14px; font-weight: 800; color: #0F2C61; margin-top:6px;">{topic}</div><div style="display: flex; justify-content: space-around; margin-top:8px; font-size:10px;"><div><b>XP:</b> {xp}</div><div><b>Date:</b> {date_str}</div><div><b>Grade:</b> A+</div></div></div></div>"""

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
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</b></div>', unsafe_allow_html=True)
    done=len([k for k,v in st.session_state.completed.items() if v])
    st.progress(min(done/8,1.0))
    if st.button("Back - Change %"):
        st.session_state.purpose_done=False
        st.rerun()
    st.divider()
    if st.session_state.page_view=="list":
        col_topics,col_content=st.columns([1,3])
    else:
        col_topics,col_content,col_side=st.columns([0.7,1.5,1.8])
    with col_topics:
        st.subheader("📚 Topics")
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
            st.subheader(f"{t['title']}")
            st.markdown(f'<div class="bullet-card"><b>{t["title"]} - Modules List - Select cheyagane next page lo open:</b></div>', unsafe_allow_html=True)
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
            st.subheader(f"Next Page - {t['title']}")
            st.markdown(f'<div class="blue-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]}</b></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="white-card"><b>{mod["name"]}</b><br><br>{mod["content"]}</div>', unsafe_allow_html=True)
            st.code(mod["code"],language="python")
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
                    if st.button(f"Mark Done +50 XP",key=f"done_{key}"):
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
                if st.button("PLAY FINAL BOSS 🔥",key="play_game"):
                    coins=[0,3,6,9]
                    path=list(range(0,10,step))
                    coll=len([x for x in path if x in coins])
                    st.write(f"Path {path} | {coll}/4")
                    if coll==4:
                        st.balloons()
                        st.success(f"SLAYED! +200 XP - Certificate side lo!")
                        st.session_state.xp+=200
                        st.session_state.final_boss_won=True
                        st.session_state.cert_unlocked=True
                    else:
                        st.error(f"Need i+=3 - Got {coll}/4")
            else:
                st.markdown(f'<div class="locked-card"><b>🔒 Locked - Complete {3-done} more</b></div>', unsafe_allow_html=True)
    if st.session_state.page_view=="detail":
        with col_side:
            st.subheader("🏆 Certificate - Side ki")
            if st.session_state.cert_unlocked and st.session_state.final_boss_won:
                today=date.today().strftime("%d-%m-%Y")
                cert_html=generate_certificate(st.session_state.user["name"],st.session_state.user["college"],st.session_state.user["btech"],st.session_state.selected_topic,st.session_state.xp,today)
                st.markdown(cert_html,unsafe_allow_html=True)
                cert_text=f"BhavPath Certificate - {st.session_state.user['name']} - {st.session_state.user['college']} - {st.session_state.user['btech']}% - {st.session_state.selected_topic} - XP {st.session_state.xp} - Date {today}"
                st.download_button(label="📥 Download Certificate",data=cert_text,file_name=f"Certificate_{st.session_state.selected_topic}.txt",mime="text/plain",use_container_width=True)
            else:
                st.markdown('<div class="cert-side-card"><b>🏆 Certificate Side ki</b><br>Game win chey - Ikkada side lo certificate vastundi!<br><br>🔒 Locked - 3 modules + Final Boss</div>', unsafe_allow_html=True)
            st.divider()
            mod=TOPICS[st.session_state.selected_topic]["modules"][st.session_state.current_mod]
            st.subheader("🧠 Practice - Side - BLACK LETTERS")
            st.markdown(f'<div class="practice-card"><b>Practice - {mod["name"]}</b><br><br>Q: {mod["q"]}</div>', unsafe_allow_html=True)
            choice=st.radio("Select Answer - Black Clear:",mod["opts"],key=f"quiz_{st.session_state.selected_topic}_{st.session_state.current_mod}")
            if st.button("Check Answer",key=f"check_{st.session_state.current_mod}",use_container_width=True):
                if choice==mod["ans"]:
                    st.success(f"✅ Correct! {mod['ans']} - +20 XP")
                    st.session_state.xp+=20
                    st.balloons()
                else:
                    st.error(f"❌ Wrong! Correct: {mod['ans']}")
            st.divider()
            st.subheader("📝 Example Sums - BIG - Side")
            for idx,ex in enumerate(mod.get("examples",[])):
                st.markdown(f'<div class="example-card"><b>Example {idx+1}: {ex["qs"]}</b></div>', unsafe_allow_html=True)
                st.code(ex["code"],language="python")
                with st.expander(f"Show Answer - Example {idx+1}"):
                    st.success(f"Answer: {ex['ans']}")
            st.divider()
            st.subheader("▶️ Run Code - Side")
            code_input=st.text_area("Your Code:",value=mod["code"],height=200,key=f"code_{st.session_state.current_mod}")
            if st.button("▶️ Run Code",key=f"run_{st.session_state.current_mod}",use_container_width=True):
                st.success(f"Output: Task {mod['task']} done!")
