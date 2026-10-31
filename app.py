import streamlit as st

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp { background: #000000; }
.g1{position:fixed;width:600px;height:600px;background:#6a00ff;filter:blur(120px);border-radius:50%;top:-150px;left:-150px;opacity:.8}
.g2{position:fixed;width:700px;height:700px;background:#ff006a;filter:blur(120px);border-radius:50%;bottom:-200px;right:-150px;opacity:.7}
.main{position:relative;z-index:10;text-align:center;padding-top:10vh}
.title{font-size:90px;font-weight:900;background:linear-gradient(90deg,#fff,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent; line-height:1.1}
.qbox{margin-top:35px;padding:28px 55px;border-radius:22px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);backdrop-filter:blur(20px);box-shadow:0 0 60px #ff006a66;display:inline-block}
.qbox h2{font-size:42px;background:linear-gradient(90deg,#fde047,#ff006a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;margin:0}
</style>
<div class="g1"></div>
<div class="g2"></div>
<div class="main">
<div class="title">Welcome to BhavPath</div>
<div class="qbox"><h2>What is Your Placement Story..??</h2></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1.5,1])
with col2:
    st.button("Start Your Journey →", use_container_width=True)
