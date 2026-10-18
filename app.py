import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - Clean No Monetization", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.stApp { background-color: #FFFFFF !important; }
h1,h2,h3,p,div,span,label { color: #0F172A !important; }
.white-card { background: #FFFFFF !important; border-radius: 12px; padding: 18px; border: 1px solid #E2E8F0; margin-bottom: 14px; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 12px; padding: 14px; }
.blue-card b { color: #FFFFFF !important; }
.help-card { background: #EFF6FF !important; border: 1px solid #BFDBFE; border-radius: 12px; padding: 14px; margin-bottom: 12px; }
.content-card { background: #F8FAFC !important; border-left: 4px solid #2563EB; border-radius: 8px; padding: 14px; margin-bottom: 12px; }
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

TOPICS = {
    "Python - 8 Modules": {
        "short": "Python", "title": "Python - 8 Modules", "about": "Easy, trending 2025",
        "modules": [
            {"name": "1. Intro", "what_is": "Python easy language by Guido 1991. No semicolon, only indentation.", "code": "print('Hello Python')\nname='Bhav'\nprint(f'{name} 81%')", "q": "Who invented Python?", "opts": ["Guido van Rossum", "Dennis Ritchie"], "ans": "Guido van Rossum"},
            {"name": "2. Variables", "what_is": "No type needed! btech=81, name='Bhav'. Dynamic!", "code": "btech=81\nname='Bhav'\nprint(f'{name} {btech}%')", "q": "Python var?", "opts": ["btech=81", "int btech=81"], "ans": "btech=81"},
            {"name": "3. Loops - Final Boss", "what_is": "for i in range(0,10,3): -> 0 3 6 9 coins! Final Boss logic!", "code": "for i in range(0,10,3):\n    print(i, end=' ') # 0 3 6 9", "q": "range(0,10,3)?", "opts": ["0 3 6 9", "0 1 2"], "ans": "0 3 6 9"},
        ]
    },
    "Data Engineering": {"short": "Data Eng", "title": "Data Engineering - 8-15 LPA", "about": "SQL, Python, ETL", "modules": [{"name": "1. SQL", "what_is": "SELECT, WHERE filter - 80% interviews ask SQL!", "code": "SELECT * FROM students WHERE btech>=60;", "q": "WHERE?", "opts": ["Filter", "Group"], "ans": "Filter"}]},
    "C Programming": {"short": "C", "title": "C Programming", "about": "Dennis Ritchie", "modules": [{"name": "1. Intro", "what_is": "C by Dennis Ritchie - Mother language", "code": "printf('Hello C');", "q": "Who invented C?", "opts": ["Dennis Ritchie", "Guido"], "ans": "Dennis Ritchie"}]},
}
TOPICS["C++"] = TOPICS["C Programming"]
TOPICS["Java"] = TOPICS["C Programming"]
TOPICS["Software Eng"] = TOPICS["Data Engineering"]

# HELPFUL LINKS - NO MONETIZATION TEXT - ONLY OFFICIAL SITES
LINKS = [
    {"title": "TCS NQT 2025", "desc": "60% eligibility? You have 81%! Official apply page - 8 LPA", "cta": "Apply on TCS Official →", "url": "https://nextstep.tcs.com/campus/"},
    {"title": "Data Engineering - Learn", "desc": "SQL + Python + Spark - Free resources to learn", "cta": "Learn on Official Docs →", "url": "https://docs.python.org/3/"},
    {"title": "Naukri Jobs", "desc": "Jobs for 81% BTech - Official job search", "cta": "Search Jobs →", "url": "https://www.naukri.com/"},
]

if not st.session_state.logged:
    st.title("🚀 BhavPath")
    c1, c2 = st.columns([1,1], gap="large")
    with c1:
        email = st.text_input("Email", placeholder="bhav@gmail.com")
        college = st.text_input("College", placeholder="Rise College, Ongole")
        btech = st.slider("BTech %", 0, 100, 81)
        if st.button("Start Learning →", use_container_width=True, type="primary"):
            if email and "@" in email:
                st.session_state.user = {"email": email, "college": college, "btech": btech, "name": email.split("@")[0]}
                st.session_state.logged = True
                st.rerun()
    with c2:
        st.markdown('<div class="white-card"><h3>Clean - No Monetization</h3><p>✅ No Rs 10 per click text</p><p>✅ Only helpful official links</p><p>✅ Professional for placement</p></div>', unsafe_allow_html=True)
    st.stop()

st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</b></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.8], gap="large")

with col_left:
    st.subheader("📚 Topics")
    for tname, tdata in TOPICS.items():
        if st.session_state.topic == tname:
            st.markdown(f'<div class="blue-card"><b>📖 {tdata["short"]} ✅</b></div>', unsafe_allow_html=True)
        else:
            if st.button(f"{tdata['short']}", key=f"btn_{tname}", use_container_width=True):
                st.session_state.topic = tname
                st.session_state.mod = 0
                st.rerun()
    
    st.divider()
    st.subheader("🔗 Helpful Links")
    st.caption("Official sites - Click to open")
    for link in LINKS:
        st.markdown(f'<div class="help-card"><b>{link["title"]}</b><br><span style="font-size:12px;">{link["desc"]}</span></div>', unsafe_allow_html=True)
        st.link_button(link["cta"], link["url"], use_container_width=True)
        st.write("")
    
    if st.button("Logout", use_container_width=True):
        st.session_state.logged = False
        st.rerun()

with col_right:
    t = TOPICS[st.session_state.topic]
    st.title(f"📘 {t['title']}")
    mod_names = [m["name"] for m in t["modules"]]
    sel = st.selectbox(f"Module ({len(mod_names)} total):", range(len(mod_names)), format_func=lambda x: mod_names[x], index=st.session_state.mod)
    st.session_state.mod = sel
    mod = t["modules"][sel]
    
    st.markdown(f'<div class="white-card"><h3>{mod["name"]}</h3><p>{mod["what_is"]}</p></div>', unsafe_allow_html=True)
    st.code(mod["code"], language="python")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if sel>0:
            if st.button("← Prev"): st.session_state.mod-=1; st.rerun()
    with col2:
        key = f"{st.session_state.topic}_{sel}"
        if st.session_state.done.get(key):
            st.success("✅ Done")
        else:
            if st.button("Mark Done +50 XP", type="primary"):
                st.session_state.done[key]=True
                st.session_state.xp+=50
                st.balloons()
                st.rerun()
    with col3:
        if sel < len(mod_names)-1:
            if st.button("Next →"): st.session_state.mod+=1; st.rerun()
    
    st.divider()
    st.write(f"**Q: {mod['q']}**")
    choice = st.radio("Choose:", mod["opts"], key=f"q_{sel}")
    if st.button("Check Answer"):
        if choice==mod["ans"]:
            st.success(f"✅ Correct! {mod['ans']}")
            st.balloons()
        else:
            st.error(f"Correct: {mod['ans']}")
