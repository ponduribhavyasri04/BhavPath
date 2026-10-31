import streamlit as st

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"

# --- BACKGROUND GRAPHICS ---
st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

# --- 1st PAGE: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("""
    <div style='text-align:center;position:relative;z-index:10;padding-top:20vh'>
        <h1 style='color:#c7f0ff;font-size:78px;font-weight:900;'>Welcome to BhavPath</h1>
        <div style='margin:35px auto;padding:28px 50px;border-radius:18px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);backdrop-filter:blur(20px);display:inline-block;'>
            <h2 style='font-size:34px;font-weight:800;margin:0;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>What is Your Placement Story..??</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    _,c2,_ = st.columns([1.3,1,1.3])
    with c2:
        st.write("")
        st.write("")
        if st.button("Start Your Journey →", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

# --- 2nd PAGE: LOGIN - NUVVU ANUKUNNADI IDHE ---
else:
    st.markdown("""
    <div style='text-align:center;position:relative;z-index:10;padding-top:8vh'>
        <h1 style='color:white;font-size:42px;font-weight:900;margin:0;'>Login to BhavPath</h1>
        <p style='color:#8b9cff;font-size:16px;margin-top:10px;'>Continue your placement story</p>
    </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1.2, 1, 1.2])
    with col:
        st.write("")
        st.write("")
        email = st.text_input("📧 Email ID", placeholder="yourname@gmail.com")
        college = st.text_input("🎓 College Name", placeholder="QIS College of Engineering")
        st.write("")
        st.write("")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if email and college:
                st.session_state.email = email
                st.balloons()
                st.success(f"Welcome {college}!")
            else:
                st.error("Email & College name enter chey rey!")
        
        st.write("")
        if st.button("← Back to Welcome"):
            st.session_state.page = "welcome"
            st.rerun()
