import streamlit as st

st.set_page_config(page_title="BhavPath Advanced", layout="wide", page_icon="🚀")

st.markdown("""
<style>
    .stApp { background: #0a0e1a; }
    .top-bar { background: linear-gradient(90deg, #1e3a8a, #0ea5e9); color: white !important; padding: 16px 22px; border-radius: 14px; font-weight: 900; letter-spacing: 1px; display:flex; justify-content:space-between; }
    .hero-adv { background: radial-gradient(circle at top left, #1d4ed8, #020617); border: 1px solid #1e293b; padding: 28px; border-radius: 20px; color: white !important; }
    .hero-adv h1 { color: white !important; font-size: 48px; margin: 0; background: linear-gradient(90deg, white, #7dd3fc); -webkit-background-clip: text; -webkit-text-fill-color: white; }
    .glass { background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 18px; color: white !important; }
    .skill-orbit { background: #111827; border: 1px solid #1f2937; padding: 12px; border-radius: 12px; text-align: center; color: white !important; cursor: pointer; transition: 0.2s; }
    .skill-orbit:hover { border-color: #38bdf8; transform: scale(1.03); }
    .active-skill { background: linear-gradient(135deg, #2563eb, #0ea5e9) !important; border: none !important; }
    .match-ring { width: 90px; height: 90px; border-radius: 50%; background: conic-gradient(#22c55e 85%, #1f2937 0); display: flex; align-items: center; justify-content: center; margin: auto; }
    .match-inner { width: 70px; height: 70px; background: #0f172a; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; }
    div.stButton > button { background: linear-gradient(90deg, #2563eb, #0ea5e9) !important; color: white !important; border: none !important; border-radius: 10px !important; font-weight: 800 !important; height: 46px; }
    .content-dark { background: #111827; border: 1px solid #1f2937; padding: 20px; border-radius: 14px; color: #e5e7eb !important; }
    p, li, h2, h3, h4 { color: #e5e7eb !important; }
</style>
""", unsafe_allow_html=True)

# DATA - Advanced
DATA = {
    "Python": {
        "story": "**Python - BhavPath Story Mode**\n\nImagine Python is like **Telugu** - simple, easy to talk. 1991 lo Guido van Rossum create chesadu.\n\n**Real Power:**\n- Instagram, YouTube backend Python lone.\n- AI/ML antha Python tho ne start.\n\n**BhavPath Visual:** Python -> Data -> AI -> Job",
        "crack": "**TCS NQT lo Python ela adugutaru?**\n- List lo duplicates remove cheyyi? `[1,1,2] -> [1,2]`\n- Decorator ante enti? - Real interview lo adigaru.",
        "code": 'def bhavpath_magic(s):\n    return s[::-1].upper()\n\nprint(bhavpath_magic("bhavpath"))\n# Output: HTAPHVAHB'
    },
    "C": {
        "story": "**C - The Foundation - Story Mode**\n\n1972 lo Dennis Ritchie Bell Labs lo create chesadu - UNIX kosam.\n\n**Nee screenshot info kante advanced:**\nC ante oka building foundation. Foundation strong aithe 100 floors kattachu.\n- Java, PHP, JS anni C nundi vachayi - **Mother of Languages**\n- Pointers ante - intlo address - direct memory magic.\n\n**Visual:**\n01 Unreal Engine - Game speed\n02 Epic Games - Rendering\n03 Physics - Real movement",
        "crack": "**Infosys lo C ela?**\n- Dangling pointer ante? - Interview lo trap question.\n- malloc vs calloc - memory allocation story.",
        "code": '#include <stdio.h>\nint main(){\n int *p;\n int a = 75; // Your percentage\n p = &a;\n printf("Your %d%% is stored at %p - Pointer Magic!", a, p);\n return 0;\n}'
    },
    "Java": {
        "story": "**Java - Job Machine**\nWORA - Write Once Run Anywhere. JVM valla.\nAccenture, Cognizant motham Java lone - 4-6 LPA.",
        "crack": "**Accenture Pattern:**\nOOPs 4 pillars - real project lo ela use chesav?",
        "code": 'class BhavPath {\n public static void main(String[] a){\n  System.out.println("BhavPath Rise: 81% -> 100%");\n }\n}'
    }
}

COMPANIES = [
    {"name": "TCS NQT", "min": 60, "pkg": "7 LPA", "color": "#22c55e"},
    {"name": "Infosys SP", "min": 65, "pkg": "9 LPA", "color": "#a855f7"},
    {"name": "Wipro", "min": 60, "pkg": "3.5 LPA", "color": "#f59e0b"},
]

if "page" not in st.session_state: st.session_state.page = "login"
if "skill" not in st.session_state: st.session_state.skill = "C"
if "mode" not in st.session_state: st.session_state.mode = "Learn"

# 1. LOGIN - Advanced Glass
if st.session_state.page == "login":
    st.markdown('<div class="top-bar"><span>BHAVPATH • ADVANCED</span><span>Rise 81% | 820 XP</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-adv" style="margin-top:15px;"><h1>BhavPath</h1><p style="color:#7dd3fc; font-size:18px;">Not a Tutorial Site. Its Your Placement Orbit.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass" style="max-width:400px; margin:30px auto;">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:white; text-align:center;">Enter Orbit</h3>', unsafe_allow_html=True)
    mail = st.text_input("Mail", placeholder="student@gmail.com")
    college = st.text_input("College", placeholder="Ongole College")
    if st.button("Launch →", use_container_width=True):
        if "@" in mail: st.session_state.mail=mail; st.session_state.college=college; st.session_state.page="profile"; st.rerun()
        else: st.error("Valid mail")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 2. PROFILE - Percent + Skill Orbit
if st.session_state.page == "profile":
    st.markdown(f'<div class="top-bar"><span>BHAVPATH | {st.session_state.college}</span><span>{st.session_state.mail}</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-adv" style="margin-top:12px;"><h1>Build Your Orbit</h1><p style="color:#94a3b8;">Percentage + Skills batti Company Match Score chupistha - GFG lo ledu</p></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1,1])
    with c1:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        percent = st.slider("Your Power %", 40, 100, 75)
        skills = st.multiselect("Select Your Orbits", list(DATA.keys()), default=["C","Python"])
        if st.button("Calculate Match →", use_container_width=True):
            st.session_state.percent=percent; st.session_state.skills=skills; st.session_state.page="companies"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass"><h4 style="color:white;">How BhavPath is Advanced?</h4><p style="color:#94a3b8; font-size:14px;">• No Tutorial/Quiz tabs like GFG<br>• Story Mode Learning<br>• Live Code Orbit<br>• Company Match Ring - Unique<br>• Dark Glass UI - Premium Feel</p></div>', unsafe_allow_html=True)
    st.stop()

# 3. COMPANIES - Match Ring
if st.session_state.page == "companies":
    p = st.session_state.percent
    st.markdown(f'<div class="top-bar"><span>BHAVPATH • {p}% POWER</span><span>{", ".join(st.session_state.skills)}</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="display:flex; gap:12px; margin-top:15px;">', unsafe_allow_html=True)
    cols = st.columns(len(COMPANIES))
    for i, comp in enumerate(COMPANIES):
        match = 85 if p >= comp["min"] else 40
        with cols[i]:
            st.markdown(f"""
            <div class="glass" style="text-align:center;">
                <div class="match-ring" style="background: conic-gradient({comp['color']} {match}%, #1f2937 0);"><div class="match-inner">{match}%</div></div>
                <h4 style="margin:12px 0 4px 0;">{comp['name']}</h4>
                <p style="color:#94a3b8; font-size:12px; margin:0;">Need {comp['min']}% • {comp['pkg']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Enter {comp['name']} Orbit", key=comp["name"], use_container_width=True):
                st.session_state.company=comp; st.session_state.page="advanced_detail"; st.session_state.skill=st.session_state.skills[0]; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 4. ADVANCED DETAIL - NOT GFG AT ALL
if st.session_state.page == "advanced_detail":
    comp = st.session_state.company
    st.markdown(f'<div class="top-bar"><span>BHAVPATH X {comp["name"]} • ORBIT ACTIVE</span><span>{st.session_state.percent}% MATCH</span></div>', unsafe_allow_html=True)
    
    # Skill Orbit Selector - Horizontal Pill
    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#94a3b8; margin:0 0 10px 0;">Select Skill Orbit - Python aithe Python Story, C aithe C Story - Full Original:</p>', unsafe_allow_html=True)
    scols = st.columns(len(st.session_state.skills))
    for i, s in enumerate(st.session_state.skills):
        active = "active-skill" if st.session_state.skill==s else ""
        with scols[i]:
            if st.button(s, key=f"orbit_{s}", use_container_width=True):
                st.session_state.skill=s; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    curr = st.session_state.skill
    d = DATA[curr]

    # Mode Switch - BhavPath Original Names
    m1, m2, m3 = st.columns(3)
    with m1:
        if st.button("📖 Learn Story", use_container_width=True, type="primary" if st.session_state.mode=="Learn" else "secondary"): st.session_state.mode="Learn"; st.rerun()
    with m2:
        if st.button("💻 Code Lab", use_container_width=True, type="primary" if st.session_state.mode=="Code" else "secondary"): st.session_state.mode="Code"; st.rerun()
    with m3:
        if st.button("🎯 Crack Interview", use_container_width=True, type="primary" if st.session_state.mode=="Crack" else "secondary"): st.session_state.mode="Crack"; st.rerun()

    # Content - 2 columns
    left, right = st.columns([1.3, 1])
    with left:
        st.markdown('<div class="content-dark">', unsafe_allow_html=True)
        if st.session_state.mode == "Learn":
            st.markdown(d["story"])
        elif st.session_state.mode == "Crack":
            st.markdown(d["crack"])
            st.info(f"BhavPath AI: {curr} lo {comp['name']} kosam idi important - {st.session_state.percent}% unna neeku easy!")
        else:
            st.markdown(f"### {curr} Live Lab - {comp['name']} Pattern")
            st.code(d["code"], language="python")
            if st.button("Run Orbit Code ▶️"): st.balloons(); st.success(f"Executed! +20 XP | Rise 81% -> 85%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with right:
        st.markdown(f"""
        <div class="glass">
            <h4 style="color:white; margin-top:0;">{comp['name']} Mission</h4>
            <p style="color:#94a3b8; font-size:13px;">Package: {comp['pkg']}<br>Need: {comp['min']}%+<br>Your Power: {st.session_state.percent}%</p>
            <div class="match-ring" style="background: conic-gradient({comp['color']} 85%, #1f2937 0);"><div class="match-inner">READY</div></div>
            <p style="color:#7dd3fc; font-size:12px; text-align:center; margin-top:12px;">BhavPath Rise Level: 2 → 3<br>820 XP + 50 XP on complete</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="glass" style="margin-top:12px;"><p style="color:#94a3b8; font-size:13px;">🤖 AI Doubt: Adugu - Telugu lo aina</p></div>', unsafe_allow_html=True)
        doubt = st.text_input("Doubt?", placeholder="Ex: Pointer ante enti?")
        if doubt: st.info(f"AI: {doubt} - Simple ga {curr} lo...")

    if st.button("← Back to Orbits"): st.session_state.page="companies"; st.rerun()
