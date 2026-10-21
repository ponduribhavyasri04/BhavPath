import streamlit as st

st.set_page_config(page_title="BhavPath - Super Cool Orbit", layout="wide", page_icon="🚀")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&display=swap');
.stApp { background: radial-gradient(1200px at 10% 10%, #1e1b4b 0%, #0f172a 40%, #020617 100%); overflow-x: hidden; }
.top-bar { background: linear-gradient(90deg, #6366f1, #06b6d4, #22c55e); padding: 14px 22px; border-radius: 16px; font-family: 'Space Grotesk'; font-weight: 800; display:flex; justify-content:space-between; color: white; box-shadow: 0 0 30px rgba(99,102,241,0.6); animation: glow 3s infinite; }
@keyframes glow { 0% { box-shadow: 0 0 20px rgba(99,102,241,0.4);} 50% { box-shadow: 0 0 40px rgba(6,182,214,0.7);} 100% { box-shadow: 0 0 20px rgba(99,102,241,0.4);} }
.glass { background: rgba(255,255,255,0.08); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.15); border-radius: 20px; padding: 16px; color: white; box-shadow: 0 8px 40px rgba(0,0,0,0.5); transition: 0.4s; }
.glass:hover { transform: translateY(-4px) scale(1.01); box-shadow: 0 16px 50px rgba(99,102,241,0.4); }
.gfg-card { background: linear-gradient(145deg, #ffffff, #f1f5f9); border-radius: 16px; padding: 14px; color: #0f172a; border: 1px solid #e2e8f0; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
.gfg-topic-active { background: linear-gradient(90deg, #6366f1, #06b6d4) !important; color: white !important; }
.code-neon { background: #020617; border: 1px solid #334155; border-left: 4px solid #22c55e; border-radius: 12px; padding: 14px; color: #7dd3fc; font-family: monospace; box-shadow: inset 0 0 20px rgba(34,197,94,0.1); }
.ad-card { background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06b6d4 100%); border-radius: 16px; padding: 16px; color: white; text-align: center; animation: float 4s ease-in-out infinite; position: relative; overflow: hidden; }
.ad-card::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent); transform: rotate(45deg); animation: shine 3s infinite; }
@keyframes float { 0%,100% { transform: translateY(0px);} 50% { transform: translateY(-8px);} }
@keyframes shine { 0% { transform: translateX(-100%) rotate(45deg);} 100% { transform: translateX(100%) rotate(45deg);} }
.xp-badge { background: linear-gradient(90deg, #22c55e, #16a34a); padding: 6px 14px; border-radius: 20px; font-weight: 900; color: white; box-shadow: 0 0 15px rgba(34,197,94,0.6); }
.boss-card { background: linear-gradient(135deg, #1e293b, #0f172a); border: 2px dashed #22c55e; border-radius: 16px; padding: 16px; color: #e2e7eb; }
div.stButton > button { background: linear-gradient(90deg, #6366f1, #06b6d4) !important; color: white !important; border: none !important; border-radius: 12px !important; font-weight: 800 !important; height: 44px; box-shadow: 0 0 20px rgba(99,102,241,0.5); }
</style>
""", unsafe_allow_html=True)

# ===== SUPER COOL DATA =====
GFG_FULL = {
    "Python": [
        {"id": "01", "title": "Introduction - What is Python?", "icon": "🐍", "what": "Python by Guido van Rossum 1991. Super easy syntax like English. Instagram, YouTube, Netflix backend is Python. For 81% profile - Helps in TCS NQT! Best for Data Science.", "why": "Why Python? Easy to learn, huge jobs, AI/ML future, 9 LPA packages", "code1": 'print("Hello Python")\nprint("BhavPath 81% Power - Super Cool")', "code2": '# Real Use: Take BTech %\nbtech = int(input("Enter BTech %: "))\nif btech >= 81:\n print("Eligible for TCS NQT - 7 LPA!")', "quiz": ("Who invented Python?", ["Guido van Rossum", "Dennis Ritchie"], "Guido van Rossum"), "practice": 's="BhavPath"\nprint(s[::-1]) # Reverse - TCS Pattern', "ad": "🔥 PYTHON MASTERY - 50% OFF! For 81% Students - Crack TCS NQT in 30 Days!"},
        {"id": "02", "title": "Variables & Data Types", "icon": "📦", "what": "Variables store data. list=mutable [1,2,3], tuple=immutable (1,2,3), dict=key-value {\"percent\":81}", "why": "Data types important for DSA and interviews", "code1": 'x=81\nname="BhavPath"\nmy_list=[81,82,85]\nprint(f"{name} - {x}%")', "code2": '# Example: Add two numbers\na=int(input())\nb=int(input())\nprint(f"Sum: {a+b}")', "quiz": ("list mutable?", ["Yes", "No"], "Yes"), "practice": 'nums=[1,1,2,3,2]\nprint(list(set(nums))) # Remove duplicates', "ad": "💎 DATA SCIENCE WITH PYTHON - 81% Students Special Offer!"},
        {"id": "06", "title": "File Handling", "icon": "📁", "what": "File handling - store data permanently. open(), read(), write(), close() - Real projects use this daily. TCS asks this!", "why": "Permanent storage - Without this data lost on close", "code1": 'f=open("bhavpath.txt","w")\nf.write("BhavPath 81% Power")\nf.close()\nprint("File Written - Cool!")', "code2": '# Read file\nf=open("bhavpath.txt","r")\nprint(f.read())', "quiz": ("File handling for permanent storage?", ["Yes", "No"], "Yes"), "practice": '# Write your % to file\nf=open("percent.txt","w")\nf.write("81")\nf.close()', "ad": "🚀 FILE HANDLING MASTERCLASS - Free for 81% Profile!"},
        {"id": "08", "title": "TCS NQT Patterns - FINAL BOSS", "icon": "👑", "what": "TCS NQT Patterns - Reverse string, Remove duplicates, Factorial, Prime - 81% profile final level - 7 LPA ready!", "why": "TCS NQT has 1 coding Q - 30 mins - This clears it", "code1": 's="BhavPath"\nprint(s[::-1]) # Reverse\nlst=[1,1,2,3,2]\nprint(list(set(lst))) # Duplicates', "code2": '# Factorial - TCS Q\ndef fact(n): return 1 if n==0 else n*fact(n-1)\nprint(fact(5))', "quiz": ("DSA needed for TCS?", ["Yes", "No"], "Yes"), "practice": '# FINAL MOCK\ns="TCS NQT 81%"\nprint("".join(reversed(s)))', "ad": "🏆 TCS NQT CRACKER - 81% Students Get 7 LPA - Join Now!"},
    ],
    "C": [
        {"id": "01", "title": "Introduction - Dennis Ritchie 1972", "icon": "🔵", "what": "C by Dennis Ritchie 1972 at Bell Labs for UNIX. Mother of all languages - C++, Java, Python borrowed from C", "why": "C strong = Any language easy - TCS NQT must", "code1": '#include <stdio.h>\nint main(){\n printf("Hello C - BhavPath 81%% Super Cool");\n return 0;\n}', "code2": 'int percent=81;\nprintf("Your %%: %d - Eligible", percent);', "quiz": ("Who invented C?", ["Dennis Ritchie", "Guido"], "Dennis Ritchie"), "practice": 'printf("82%% Power");', "ad": "⚡ C MASTERY - Foundation of All Languages!"},
        {"id": "06", "title": "Pointers - HIGH PRIORITY", "icon": "🎯", "what": "Pointers store address. &a=address, *p=value at address. TCS NQT 100% asks this - Most important topic!", "why": "Without pointers no TCS interview clear", "code1": '#include <stdio.h>\nint main(){\n int a=81;\n int *p=&a;\n printf("a=%d, *p=%d, addr=%p", a, *p, p);\n}', "code2": 'void swap(int *x, int *y){int t=*x; *x=*y; *y=t;}', "quiz": ("Pointer stores address?", ["Yes", "No"], "Yes"), "practice": 'int percent=81;\nprintf("Addr: %p", &percent);', "ad": "🎯 POINTERS UNLOCKED - TCS NQT Secret Weapon!"},
    ],
    "C++": [{"id": f"0{i+1}", "title": f"C++ Topic {i+1}", "icon": "💜", "what": "C++ content", "why": "Why C++", "code1": 'cout<<"C++ Super Cool";', "code2": 'vector<int> v={1,2,3};', "quiz": ("C++ has OOPs?", ["Yes","No"], "Yes"), "practice": '// Practice C++', "ad": "💜 C++ POWER - Game Dev & CP!"} for i in range(4)],
    "Java": [{"id": f"0{i+1}", "title": f"Java Topic {i+1}", "icon": "☕", "what": "Java content", "why": "Why Java", "code1": 'System.out.println("Java Cool");', "code2": 'System.out.println("81%");', "quiz": ("Java platform independent?", ["Yes","No"], "Yes"), "practice": '// Practice Java', "ad": "☕ JAVA ENTERPRISE - 9 LPA Jobs!"} for i in range(4)],
}

if "skill" not in st.session_state: st.session_state.skill="Python"
if "idx" not in st.session_state: st.session_state.idx=0
if "xp" not in st.session_state: st.session_state.xp=820
if "done" not in st.session_state: st.session_state.done=[]

# Top bar
st.markdown(f'<div class="top-bar"><span>🚀 BHAVPATH • SUPER COOL ORBIT • {st.session_state.skill.upper()} • 81% POWER</span><span class="xp-badge">{st.session_state.xp} XP • LVL 3</span></div>', unsafe_allow_html=True)

# Ad Banner Top
st.markdown(f"""
<div class="ad-card" style="margin-top:12px;">
    <h3 style="margin:0;">🌟 {GFG_FULL[st.session_state.skill][st.session_state.idx]["ad"]} 🌟</h3>
    <p style="margin:4px 0 0 0; font-size:12px;">For 81% Profile Students Only - Limited Time - 50% OFF - Graphics Enabled</p>
</div>
""", unsafe_allow_html=True)

left, mid, right = st.columns([1.1, 2.2, 1.1])

# LEFT - SUPER COOL TOPICS - GFG STYLE WITH GRAPHICS
with left:
    st.markdown('<div class="glass"><h3 style="margin:0;">📚 Topics - GFG Super Cool</h3><p style="font-size:11px; color:#94a3b8; margin:4px 0 12px 0;">Click to open full GFG article with graphics</p>', unsafe_allow_html=True)
    for skill_name in GFG_FULL.keys():
        is_sk = st.session_state.skill==skill_name
        if st.button(f"{'🚀' if is_sk else '💫'} {skill_name} - {len(GFG_FULL[skill_name])} Modules", key=f"sk_{skill_name}", use_container_width=True, type="primary" if is_sk else "secondary"):
            st.session_state.skill=skill_name
            st.session_state.idx=0
            st.rerun()
        if is_sk:
            for i, mod in enumerate(GFG_FULL[skill_name]):
                active = st.session_state.idx==i
                tick = "✅" if f"{skill_name}_{i}" in st.session_state.done else mod["icon"]
                label = f"{tick} {mod['id']}. {mod['title'][:30]}"
                if st.button(label, key=f"mod_{skill_name}_{i}", use_container_width=True, type="primary" if active else "secondary"):
                    st.session_state.idx=i
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Mini Ad
    st.markdown("""
    <div class="ad-card" style="margin-top:12px; padding:12px;">
        <b>🎮 FINAL BOSS GAME</b><br>
        <span style="font-size:11px;">Play + Get Certificate + 200 XP</span><br>
        <span style="font-size:10px; background: white; color: #6366f1; padding: 4px 8px; border-radius: 12px; font-weight:800;">FREE FOR 81%</span>
    </div>
    """, unsafe_allow_html=True)

# MIDDLE - FULL GFG PAGE WITH GRAPHICS
with mid:
    mod = GFG_FULL[st.session_state.skill][st.session_state.idx]
    st.markdown(f"""
    <div class="gfg-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h2 style="margin:0; color:#0f172a;">{mod['icon']} {mod['title']} | GFG Style | BhavPath Super Cool</h2>
            <span class="xp-badge">81% SPECIAL</span>
        </div>
        <p style="color: gray; font-size:11px; margin:6px 0 0 0;">Last Updated: 26 Aug 2026 | {st.session_state.skill} | TCS NQT | Graphics Enabled | Super Cool UI</p>
        <hr style="margin:12px 0;">
        <h3 style="color:#6366f1;">📖 What is {mod['title']}?</h3>
        <p style="color:#334155; line-height:1.6;">{mod['what']}</p>
        <h3 style="color:#06b6d4;">🎯 Why Important for 81% Profile?</h3>
        <p style="color:#334155;">{mod['why']}</p>
        <div style="background: linear-gradient(90deg, #dbeafe, #e0e7ff); padding:10px; border-radius:10px; border-left:4px solid #6366f1;">
            <b style="color:#1e40af;">💡 BhavPath Tip for 81%:</b><br>
            <span style="color:#334155; font-size:13px;">This topic asked in TCS NQT 2024, 2025 - Must for 7 LPA - Practice daily!</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    st.markdown(f'<h3 style="margin:0;">💻 Example 1 - Basic - {mod["title"]}</h3>', unsafe_allow_html=True)
    st.markdown(f'<div class="code-neon">{mod["code1"]}</div>', unsafe_allow_html=True)
    st.code(mod["code1"], language="python" if st.session_state.skill=="Python" else "c")
    
    st.markdown(f'<h3 style="margin:16px 0 0 0;">📝 Example 2 - Real Use (For 81% Profile - TCS NQT)</h3>', unsafe_allow_html=True)
    st.code(mod["code2"], language="python" if st.session_state.skill=="Python" else "c")
    
    # Ad in middle
    st.markdown(f"""
    <div class="ad-card" style="margin-top:14px;">
        <b>🔥 {mod["ad"]}</b><br>
        <span style="font-size:11px;">Click Below to Unlock Full Course with Graphics + Certificate</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Navigation + XP
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("← Prev", use_container_width=True, disabled=st.session_state.idx==0):
            st.session_state.idx-=1; st.rerun()
    with c2:
        if st.button(f"✅ Mark Done +50 XP", use_container_width=True, type="primary"):
            key = f"{st.session_state.skill}_{st.session_state.idx}"
            if key not in st.session_state.done:
                st.session_state.done.append(key)
                st.session_state.xp+=50
                st.balloons()
                st.success(f"+50 XP! {mod['title']} Completed - Super Cool!")
            else:
                st.info("Already done!")
    with c3:
        if st.button("Next →", use_container_width=True, disabled=st.session_state.idx==len(GFG_FULL[st.session_state.skill])-1):
            st.session_state.idx+=1; st.rerun()

# RIGHT - PRACTICE + RUN CODE + GRAPHICS ADS
with right:
    st.markdown('<div class="glass"><h3 style="margin:0;">🎯 Practice - Super Cool</h3>', unsafe_allow_html=True)
    st.markdown(f'<div class="gfg-card" style="margin-top:10px;"><b>Q: {mod["quiz"][0]}</b><br><span style="font-size:11px; color:gray;">For 81% - TCS NQT Style</span></div>', unsafe_allow_html=True)
    choice = st.radio("Choose:", mod["quiz"][1], key=f"q_{st.session_state.idx}")
    if st.button("Check Answer", use_container_width=True, key=f"chk_{st.session_state.idx}"):
        if choice==mod["quiz"][2]:
            st.success(f"✅ Correct! {choice} +20 XP")
            st.session_state.xp+=20
            st.balloons()
        else:
            st.error(f"❌ Wrong! Correct: {mod['quiz'][2]}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass" style="margin-top:12px;"><h3>▶️ Run Code - Live Graphics</h3>', unsafe_allow_html=True)
    st.markdown(f'<div class="gfg-card" style="background: linear-gradient(90deg, #f0fdf4, #dcfce7);"><b>💡 Practice Code - {mod["title"]}</b><br><span style="font-size:11px;">TCS Pattern - Edit & Run - Graphics Enabled</span></div>', unsafe_allow_html=True)
    st.code(mod["practice"], language="python" if st.session_state.skill=="Python" else "c")
    edit = st.text_area("Edit & Run Your Code:", value=mod["practice"], height=90, key=f"edit_{st.session_state.idx}")
    if st.button(f"▶️ Run {mod['title']} - Super Cool Output", use_container_width=True, type="primary"):
        st.markdown(f'<div class="code-neon">Running...<br>{edit}<br><br>Output: BhavPath 81% Power - Executed! Super Cool! +10 XP</div>', unsafe_allow_html=True)
        st.session_state.xp+=10
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="ad-card" style="margin-top:12px;">
        <h4 style="margin:0;">📢 AD - Data Engineering Course</h4>
        <p style="font-size:11px; margin:6px 0;">50% OFF for 81% Profile Students - With Super Cool Graphics!</p>
        <div style="background: white; color: #6366f1; padding: 6px; border-radius: 8px; font-weight: 800; font-size:12px;">GET OFFER - 2 Days Left!</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Final Boss
    done_cnt = len([k for k in st.session_state.done if k.startswith(st.session_state.skill)])
    st.markdown(f'<div class="boss-card" style="margin-top:12px;"><h3 style="margin:0; color:#22c55e;">🎮 FINAL BOSS - Game + Certificate</h3><p style="font-size:12px; margin:6px 0;">Progress: {done_cnt}/{len(GFG_FULL[st.session_state.skill])} Modules</p></div>', unsafe_allow_html=True)
    if done_cnt >= 2:
        st.success(f"🏆 UNLOCKED! {st.session_state.skill} Final Boss Ready!")
        if st.button("🎮 Play Game + Get Certificate +200 XP", use_container_width=True, type="primary"):
            st.balloons()
            st.success(f"Certificate Unlocked! Super Cool Graphics Certificate for {st.session_state.skill}!")
            st.session_state.xp+=200
    else:
        st.info(f"🔒 Locked - Complete {2-done_cnt} more to unlock")

st.markdown("""
<div class="ad-card" style="margin-top:20px;">
    <h2 style="margin:0;">🚀 BHAVPATH SUPER COOL ORBIT - FOR 81% STUDENTS - NO PERCENTAGE PACKAGE 🚀</h2>
    <p style="margin:6px 0 0 0;">Python | C | C++ | Java | SQL | DSA | Data Engineering | All with Graphics + Ads + Games + Certificates | 81% → 85% → 90% Rise!</p>
</div>
""", unsafe_allow_html=True)
