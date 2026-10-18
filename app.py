import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath BLUE - Final", layout="centered", page_icon="💙")

# --- THEME - BLACK LETTERS CLEAR (Your old video issue fixed) ---
st.markdown("""
<style>
.stApp { background-color: #EAF2FF !important; }
h1,h2,h3,p,div,span,label { color: #000000 !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; }
.white-card { background: #FFFFFF !important; color: #000000 !important; border-radius: 14px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); margin-bottom: 12px; border: 2px solid #2563EB; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 16px; padding: 18px; }
.blue-card b { color: #FFFFFF !important; }
.stButton>button { background: #2563EB !important; color: #FFFFFF !important; border-radius: 12px; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

# --- SESSION INIT - IDI LINE 2 LO ERROR FIX ---
if 'page' not in st.session_state: st.session_state.page = "login"
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'streak' not in st.session_state: st.session_state.streak = 3
if 'user' not in st.session_state: st.session_state.user = {}
if 'purpose' not in st.session_state: st.session_state.purpose = None
if 'topics' not in st.session_state: st.session_state.topics = {"Variables":100, "Control":60, "OOP":30, "Pointers":0}

# --- 1. LOGIN - EMAIL + CLG ONLY (Nuvvu adiginattu) ---
def login():
    st.title("🚀 BhavPath - Login")
    st.markdown('<div class="white-card"><b>Login - Email & College Name Only</b></div>', unsafe_allow_html=True)
    email = st.text_input("📧 Email", placeholder="bhav@gmail.com")
    clg_name = st.text_input("🏫 College Name", placeholder="QIS College, Ongole")
    if st.button("Login 🔐 - Continue"):
        if email and clg_name and "@" in email:
            st.session_state.user = {"email": email, "clg": clg_name, "name": email.split("@")[0]}
            st.session_state.page = "btech"
            st.rerun()
        else:
            st.error("Valid Email & College Name pettali!")

# --- 2. BTECH ASK - TARVATA (Nuvvu adiginattu) ---
def btech_page():
    st.title("📊 One More Step!")
    st.markdown(f'<div class="white-card"><b>Welcome {st.session_state.user["name"]}!</b><br>🏫 {st.session_state.user["clg"]}<br>Personalized prep kosam BTech % cheppu</div>', unsafe_allow_html=True)
    btech = st.slider("BTech Percentage Entha?", 0, 100, 70)
    st.markdown(f'<div class="blue-card"><b>Selected: {btech}%</b><br>Idi batti neeku tailored interview Q&A istham!</div>', unsafe_allow_html=True)
    if st.button(f"Continue with {btech}% →"):
        st.session_state.user["btech"] = btech
        st.session_state.page = "purpose"
        st.balloons()
        st.rerun()

# --- 3. PURPOSE ---
def purpose():
    st.header(f"Welcome {st.session_state.user['name']}! 👋")
    st.markdown(f'<div class="white-card">📧 {st.session_state.user["email"]}<br>🏫 {st.session_state.user["clg"]}<br>BTech: <b>{st.session_state.user["btech"]}%</b> | XP: <b>{st.session_state.xp}</b></div>', unsafe_allow_html=True)
    st.subheader("Why are you here today?")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="white-card">🎯 <b>For Placement</b><br>Eligibility + Q&A</div>', unsafe_allow_html=True)
        if st.button("Placement →", key="pl"): st.session_state.purpose="placement"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">🎮 <b>Gaming Zone</b><br>3 Working Games</div>', unsafe_allow_html=True)
        if st.button("Gaming Zone →", key="gm"): st.session_state.purpose="gaming"; st.session_state.page="main"; st.rerun()
    with c2:
        st.markdown('<div class="white-card">📚 <b>Materials - GFG Full</b><br>Theory + Interview Qs</div>', unsafe_allow_html=True)
        if st.button("Materials →", key="mt"): st.session_state.purpose="materials"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">📄 <b>Resume + Certificate</b><br>Auto Generate</div>', unsafe_allow_html=True)
        if st.button("Resume →", key="rs"): st.session_state.purpose="resume"; st.session_state.page="main"; st.rerun()

# --- 4. MAIN ---
def main():
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["name"]} | {st.session_state.user["clg"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</b></div><br>', unsafe_allow_html=True)
    if st.button("← Back to Purpose"): st.session_state.page="purpose"; st.rerun()

    if st.session_state.purpose=="placement":
        b=st.session_state.user['btech']
        st.subheader("Placement Dashboard")
        if b>=60: st.success(f"✅ Eligible for TCS NQT - Need 60%, You {b}%")
        else: st.error(f"❌ Not Eligible - Need 60%, You {b}%")
        with st.expander("Q: Tell me about yourself? (For 70%)"):
            st.write(f"I am {st.session_state.user['name']} from {st.session_state.user['clg']} with {b}% in BTech. Built BhavPath app that personalizes prep based on percentage.")

    elif st.session_state.purpose=="materials":
        st.title("C++ Programming Language - GFG Style")
        st.caption(f"Last Updated: 25 Aug 2025 | Recommended for {st.session_state.user['btech']}% profile")
        st.markdown('<div class="white-card"><b>What is C++?</b><br>C++ by Bjarne Stroustrup. Extension of C with OOP. Used for Gaming Engines.</div>', unsafe_allow_html=True)
        st.markdown('<div class="blue-card"><b>🎮 Gaming Engines:</b><br>Unreal Engine (Fortnite), Godot (Free) - All use C++ for speed</div>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["📖 Tutorial", "💼 Interview Qs"])
        with tab1:
            with st.expander("Variables & Data Types - Full Info"):
                st.write("int a=10 (4 bytes), string name='Bhav', bool flag=true - Container to store data. For 70%: Why data types? To save memory.")
                st.code('int a=10;\nstring branch="Data Science";')
            with st.expander("Control Statements - For Loop"):
                st.write("if(btech>=60) eligible. for(i=0;i<10;i+=3) coins at 0,3,6,9 - Loop Legends game logic")
                st.code('for(int i=0; i<10; i+=3){ cout<<i; }')
        with tab2:
            with st.expander("What is OOP?"):
                st.write("Class, Object, Inheritance, Polymorphism - Code reuse")
            with st.expander("Tell me about yourself? (70% Data Science)"):
                st.write(f"I am {st.session_state.user['name']} from {st.session_state.user['clg']} with {b}% - Built BhavPath...")

    elif st.session_state.purpose=="gaming":
        st.title("🎮 Gaming Zone - Working Games")
        st.markdown('<div class="white-card"><b>1. Loop Legends</b><br>Coins at 0,3,6,9 - Need i+=3</div>', unsafe_allow_html=True)
        step=st.slider("for(i=0; i<10; i+=?)", 1,5,3)
        if st.button("PLAY Loop Legends"):
            coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
            st.write(f"Path {path} | Collected {coll}/4")
            if coll==4: st.balloons(); st.success(f"+50 XP - Total {st.session_state.xp+50}"); st.session_state.xp+=50
            else: st.error(f"Only {coll}/4 - Hint i+=3")
        st.divider()
        st.markdown('<div class="white-card"><b>2. Variable Vault</b></div>', unsafe_allow_html=True)
        box=st.selectbox("Box?", ["Gold Count (100)","Name (Bhav)","Is Win? True"])
        dtype=st.radio("Type?", ["int","string","bool"], horizontal=True)
        if st.button("PLAY Variable Vault"):
            corr={"Gold Count (100)":"int","Name (Bhav)":"string","Is Win? True":"bool"}
            if dtype==corr[box]: st.balloons(); st.success("+50 XP"); st.session_state.xp+=50
            else: st.error(f"Need {corr[box]}")

    elif st.session_state.purpose=="resume":
        st.title("📄 Resume")
        st.markdown(f'<div class="white-card"><b>Name:</b> {st.session_state.user["name"]}<br><b>College:</b> {st.session_state.user["clg"]}<br><b>BTech:</b> {st.session_state.user["btech"]}%<br><b>Skills:</b> C++ Basics, Gaming Logic<br><b>Project:</b> BhavPath - Game-Based Learning<br><b>XP:</b> {st.session_state.xp}</div>', unsafe_allow_html=True)

# --- ROUTER ---
if st.session_state.page=="login": login()
elif st.session_state.page=="btech": btech_page()
elif st.session_state.page=="purpose": purpose()
else: main()
