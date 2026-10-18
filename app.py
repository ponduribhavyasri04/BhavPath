import streamlit as st

# --- CONFIG & BLUE THEME ---
st.set_page_config(page_title="BhavPath BLUE - Final", layout="centered", page_icon="💙")
st.markdown("""
<style>
.stApp{background:#F0F6FF;} h1,h2,h3{color:#1E3A8A;}
.stButton>button{background:#2563EB; color:white; border-radius:12px; font-weight:bold; border:none; width:100%;}
.stButton>button:hover{background:#1D4ED8;}
.white-card{background:white; border-radius:14px; padding:14px; box-shadow:0 4px 12px rgba(37,99,235,0.1); margin-bottom:10px; border-left:5px solid #2563EB;}
.blue-card{background:linear-gradient(135deg, #3B82F6, #1E40AF); color:white; border-radius:16px; padding:18px;}
</style>
""", unsafe_allow_html=True)

# --- SESSION ---
if 'page' not in st.session_state: st.session_state.page="login"
if 'xp' not in st.session_state: st.session_state.xp=820
if 'user' not in st.session_state: st.session_state.user={}
if 'topics' not in st.session_state: st.session_state.topics={"Variables & Data Types":100, "Control Structures":60, "OOP Concepts":30, "Pointers & Memory":0}

# --- 1. LOGIN (CodeTantra Style) ---
def login():
    st.title("🚀 BhavPath Login")
    st.caption("CodeTantra Style")
    name=st.text_input("Full Name", "Bhav")
    branch=st.text_input("Branch", "Data Science")
    btech=st.number_input("BTech %", 0,100,70)
    pwd=st.text_input("Password", type="password", value="1234")
    if st.button("Login 🔐"):
        st.session_state.user={"name":name,"branch":branch,"btech":btech}
        st.session_state.page="purpose"
        st.rerun()

# --- 2. PURPOSE (Your Idea) ---
def purpose():
    st.header(f"Welcome {st.session_state.user['name']} 👋")
    st.write(f"BTech {st.session_state.user['btech']}% | {st.session_state.xp} XP")
    st.subheader("Why are you here?")
    c1,c2=st.columns(2)
    with c1:
        st.markdown('<div class="white-card">🎯 <b>For Placement</b><br>Q&A, Eligibility</div>',unsafe_allow_html=True)
        if st.button("Placement",key="pl"): st.session_state.purpose="placement"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">🎮 <b>Gaming Zone</b><br>Play & Learn C++</div>',unsafe_allow_html=True)
        if st.button("Gaming Zone",key="gm"): st.session_state.purpose="gaming"; st.session_state.page="main"; st.rerun()
    with c2:
        st.markdown('<div class="white-card">📚 <b>Study Materials</b><br>GFG Blue Style</div>',unsafe_allow_html=True)
        if st.button("Materials",key="mt"): st.session_state.purpose="materials"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">💼 <b>Others</b><br>Resume</div>',unsafe_allow_html=True)
        if st.button("Others",key="ot"): st.session_state.purpose="others"; st.session_state.page="main"; st.rerun()

# --- 3. MAIN DASHBOARD ---
def main():
    st.markdown(f'<div style="background:#2563EB; color:white; padding:10px 15px; border-radius:12px;"><b>BhavPath</b> | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</div><br>',unsafe_allow_html=True)
    if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

    # PLACEMENT
    if st.session_state.purpose=="placement":
        b=st.session_state.user['btech']
        st.subheader("🎯 Placement")
        if b>=60: st.success(f"🏆 Eligible for TCS NQT (Need 60%, You {b}%)")
        else: st.error(f"Not Eligible (Need 60%, You {b}%)")
        st.info(f"Q: Tell me about yourself?\n\nAns: I am {st.session_state.user['name']} from {st.session_state.user['branch']} with {b}%. Built BhavPath to personalize prep. My edge is converting {b}% profile into tailored answers.")

    # MATERIALS - BLUE GFG
    elif st.session_state.purpose=="materials":
        st.title("C++ Programming Language")
        st.caption(f"Last Updated: 12 Oct 2024 • Recommended for {st.session_state.user['btech']}% profile")
        st.markdown("**Features:** ✅ Object-Oriented ✅ Memory Management ✅ STL ✅ High Performance")
        st.markdown('<div class="blue-card"><b>🎮 Gaming Engines</b><br>Unreal Engine • Godot • Custom Engines<br><i>Tap to explore - Interactive</i></div>',unsafe_allow_html=True)
        st.subheader("Basics")
        for t,p in st.session_state.topics.items():
            st.markdown(f'<div class="white-card"><b>{t}</b> - {p}% <br><progress value="{p}" max="100" style="width:100%"></progress></div>',unsafe_allow_html=True)
            if st.button(f"Mark Done +10 XP - {t}", key=t):
                st.session_state.topics[t]=min(100,p+20); st.session_state.xp+=10; st.balloons(); st.rerun()
        c1,c2,c3=st.columns(3)
        with c1:
            if st.button("Try IDE"): st.code('cout << "Hello BhavPath";')
        with c2:
            if st.button("Ask AI"): st.info("AI: For 70% profile, focus on OOP + Projects to justify percentage in interview.")
        with c3:
            if st.button("Mark Done +10 XP"): st.session_state.xp+=10; st.rerun()

    # GAMING - WORKING GAMES
    elif st.session_state.purpose=="gaming":
        st.title("🎮 Learn C++ with Games")
        st.caption("Work ayye games - Play chey, XP sampadinchu!")
        
        # GAME 1 - 100% WORKING
        st.divider()
        st.markdown('<div class="white-card"><b>1. Loop Legends - Runner</b><br>For loop tho coins collect chey</div>',unsafe_allow_html=True)
        step = st.slider("for(i=0; i<10; i+=?)", 1, 5, 3, key="g1_s")
        if st.button("🏃 PLAY Loop Legends - RUN!", key="g1_b"):
            coins=[0,3,6,9]
            path=list(range(0,10,step))
            collected=len([x for x in path if x in coins])
            runner=""
            for i in range(10):
                if i in path and i in coins: runner+="🪙🏃 "
                elif i in path: runner+="➖🏃 "
                else: runner+="➖ "
            st.write(runner)
            st.write(f"Path: {path} | Coins Collected: {collected}/4")
            if collected==4 and step==3:
                st.balloons(); st.success("PERFECT! +50 XP"); st.session_state.xp+=50
            else:
                st.error("Fail! Hint: coins 0,3,6,9 lo unnai - i+=3 try chey")

        # GAME 2 - 100% WORKING
        st.divider()
        st.markdown('<div class="white-card"><b>2. Variable Vault - Treasure</b><br>Data type correct ga pettu</div>',unsafe_allow_html=True)
        box=st.selectbox("Box lo enti?", ["Gold Count (100)", "Name (Bhav)", "Is Win? (True/False)"], key="g2_s")
        dtype=st.radio("Type?", ["int","string","bool"], horizontal=True, key="g2_t")
        if st.button("🔓 PLAY Variable Vault - OPEN!", key="g2_b"):
            corr={"Gold Count (100)":"int","Name (Bhav)":"string","Is Win? (True/False)":"bool"}
            if dtype==corr[box]:
                st.success(f"Vault Opened! {box} -> {dtype} Correct! +50 XP"); st.session_state.xp+=50; st.balloons()
            else:
                st.error(f"Locked! {box} ki {corr[box]} kavali")

        # GAME 3 - 100% WORKING
        st.divider()
        st.markdown('<div class="white-card"><b>3. Pointer Panic - Maze</b><br>Pointer ni correct address ki pampu</div>',unsafe_allow_html=True)
        st.code("int a = 10;\nint *p;\n// p = ?")
        ans=st.text_input("p = ?", placeholder="&a", key="g3_i")
        if st.button("🧩 PLAY Pointer Panic - SOLVE!", key="g3_b"):
            if ans.strip()=="&a":
                st.success("Maze Cleared! Pointer Correct! +50 XP"); st.session_state.xp+=50; st.balloons()
            else:
                st.error("Wrong! Address kavali - &a rayali")

        st.divider()
        st.metric("Your Total XP", f"{st.session_state.xp} XP", f"Level {st.session_state.xp//200}")

    else:
        st.info("Resume Builder Coming Soon!")

# ROUTER
if st.session_state.page=="login": login()
elif st.session_state.page=="purpose": purpose()
else: main()
