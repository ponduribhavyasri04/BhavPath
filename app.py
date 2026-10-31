import streamlit as st
st.set_page_config(page_title="Login - BhavPath", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.card{position:relative;z-index:10;width:500px;margin:10vh auto;padding:40px;border-radius:24px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(25px);box-shadow:0 0 80px #3b82f688}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

st.markdown('<div style="position:relative;z-index:10;text-align:center;margin-top:8vh"><h1 style="color:white;font-size:38px;font-weight:900;">Login to BhavPath</h1><p style="color:#a78bfa;">Continue your placement story</p></div>', unsafe_allow_html=True)

_,col,_ = st.columns([1,1.1,1])
with col:
    st.markdown("<br>")
    email = st.text_input("📧 Email ID", placeholder="yourname@gmail.com")
    college = st.text_input("🎓 College Name", placeholder="QIS College of Engineering")
    st.markdown("<br>")
    if st.button("Continue →", use_container_width=True, type="primary"):
        if email and college:
            st.session_state.email = email
            st.session_state.college = college
            st.success("Login Success!")
            st.balloons()
        else:
            st.error("Email & College name compulsory rey!")
