import streamlit as st

st.set_page_config(page_title="BhavPath", layout="wide")

st.markdown("""
<style>
.top-bar { background: #1d4ed8; color: white; padding: 15px 20px; border-radius: 8px; font-weight: bold; }
.blue-btn { background: #2563eb; color: white; padding: 14px; border-radius: 8px; text-align: center; margin: 5px 0; font-weight: 500; }
.white-card { background: white; color: black; padding: 15px; border: 1px solid #ddd; border-radius: 8px; font-weight: bold; }
</style>
<div class="top-bar">BhavPath | Rise | 81 percent | 820 XP | Python</div>
<hr style="border: 3px solid black; margin: 15px 0;">
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.button("Back Change percent", use_container_width=True)
with col2:
    st.button("Back to All Topics List Malli", use_container_width=True)

left, right = st.columns([1, 3])

with left:
    st.markdown('<div class="white-card">List Page varake -<br>Ikkada matrame<br>Open buttons</div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#2563eb; color:white; padding:15px; border-radius:8px 8px 0 0; margin-top:15px;"><b>Python SELECTED</b><br><small>Easy plus Data Science</small></div>', unsafe_allow_html=True)
    st.button("Open Python", use_container_width=True)

with right:
    topics = ["1. Introduction", "2. Variables", "3. Operators", "4. Loops", "5. Identifiers"]
    for t in topics:
        if st.button(f"• {t}  →  Open Detail", key=t, use_container_width=True):
            st.success(f"{t} opened!")

