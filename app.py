# --- SESSION ---
if 'page' not in st.session_state: st.session_state.page="login"
if 'xp' not in st.session_state: st.session_state.xp=820
if 'streak' not in st.session_state: st.session_state.streak=3
if 'user' not in st.session_state: st.session_state.user={}

def login():
    st.title("🚀 BhavPath - Login")
    st.markdown('<div class="white-card"><b>Login - Email & College Name Only</b></div>', unsafe_allow_html=True)
    
    email = st.text_input("📧 Email", placeholder="bhav@gmail.com")
    clg_name = st.text_input("🏫 College Name", placeholder="QIS College, Ongole")
    
    if st.button("Login 🔐 - Continue"):
        if email and clg_name and "@" in email:
            st.session_state.user = {"email": email, "clg": clg_name, "name": email.split("@")[0]}
            st.session_state.page = "btech"  # NEXT PAGE - BTECH ASK
            st.rerun()
        else:
            st.error("Valid Email & College Name pettali!")

def btech_page():
    st.title("📊 One More Step!")
    st.markdown(f'<div class="white-card"><b>Welcome {st.session_state.user["name"]}!</b><br>🏫 {st.session_state.user["clg"]}<br>Personalized prep kosam BTech % cheppu</div>', unsafe_allow_html=True)
    
    btech = st.slider("BTech Percentage Entha?", 0, 100, 70)
    st.markdown(f'<div class="blue-card"><b>Selected: {btech}%</b><br>Idi batti neeku tailored interview Q&A, eligibility, skill gap analysis istham!</div>', unsafe_allow_html=True)
    
    if st.button(f"Continue with {btech}% →"):
        st.session_state.user["btech"] = btech
        st.session_state.page = "purpose"
        st.balloons()
        st.rerun()

def purpose():
    st.header(f"Welcome {st.session_state.user['name']}! 👋")
    st.markdown(f'<div class="white-card">📧 {st.session_state.user["email"]}<br>🏫 {st.session_state.user["clg"]}<br>BTech: <b>{st.session_state.user["btech"]}%</b> | XP: <b>{st.session_state.xp}</b></div>', unsafe_allow_html=True)
    
    st.subheader("Why are you here today?")
    c1,c2=st.columns(2)
    with c1:
        st.markdown('<div class="white-card">🎯 <b>For Placement</b><br>Eligibility + Q&A for your %</div>', unsafe_allow_html=True)
        if st.button("Placement →", key="pl"): st.session_state.purpose="placement"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">🎮 <b>Gaming Zone</b><br>3 Working Games</div>', unsafe_allow_html=True)
        if st.button("Gaming Zone →", key="gm"): st.session_state.purpose="gaming"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">🏆 <b>Leaderboard</b><br>College Ranking</div>', unsafe_allow_html=True)
        if st.button("Leaderboard →", key="lb"): st.session_state.purpose="leaderboard"; st.session_state.page="main"; st.rerun()
    with c2:
        st.markdown('<div class="white-card">📚 <b>Materials - GFG Full</b><br>Theory + Interview Qs + Examples</div>', unsafe_allow_html=True)
        if st.button("Materials →", key="mt"): st.session_state.purpose="materials"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">🤖 <b>AI Doubt Solver</b><br>Ask Doubts</div>', unsafe_allow_html=True)
        if st.button("AI Solver →", key="ai"): st.session_state.purpose="ai"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">📄 <b>Resume + Certificate</b><br>Auto Generate</div>', unsafe_allow_html=True)
        if st.button("Resume →", key="rs"): st.session_state.purpose="resume"; st.session_state.page="main"; st.rerun()

# --- ROUTER UPDATE ---
if st.session_state.page=="login": login()
elif st.session_state.page=="btech": btech_page()
elif st.session_state.page=="purpose": purpose()
else: main()  # main() function neeku mundu ichina full features code ye
