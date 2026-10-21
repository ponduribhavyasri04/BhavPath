import streamlit as st

st.set_page_config(page_title="BhavPath", layout="wide", page_icon="🔥")

# --- FIXED CSS - NO WHITE ON WHITE ---
st.markdown("""
<style>
    .main { background: #f0f2f5; }
    .top-bar {
        background: #1d4ed8;
        color: white !important;
        padding: 16px 20px;
        border-radius: 10px;
        font-weight: 800;
        font-size: 18px;
        letter-spacing: 0.5px;
    }
    .black-line { height: 5px; background: black; margin: 12px 0; border-radius: 2px; }
    div.stButton > button {
        background: #2563eb !important;
        color: white !important;
        border: none !important;
        padding: 14px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    .info-card {
        background: white;
        color: black !important;
        padding: 16px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }
    .topic-card {
        background: #2563eb;
        color: white;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-weight: 500;
    }
    .hero {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "list"
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None

# TOP BAR - ALWAYS VISIBLE
st.markdown('<div class="top-bar">BhavPath | Rise | 81 percent | 820 XP | Python</div>', unsafe_allow_html=True)
st.markdown('<div class="black-line"></div>', unsafe_allow_html=True)

# TOP BUTTONS
c1, c2 = st.columns(2)
with c1:
    if st.button("Back Change percent"):
        st.session_state.page = "list"
with c2:
    if st.button("Back to All Topics List Malli"):
        st.session_state.page = "list"

# LIST PAGE
if st.session_state.page == "list":
    left, right = st.columns([1, 2.5])

    with left:
        st.markdown('<div class="hero"><h3 style="margin:0; color:#1d4ed8;">BhavPath 🚀</h3><p style="margin:5px 0 0 0; color:black;">Learn Python with XP & Rise</p><p style="margin:10px 0 0 0;">Progress: <b>81%</b> | XP: <b>820</b></p></div>', unsafe_allow_html=True)
        st.markdown('<div class="info-card">List Page varake -<br>Ikkada matrame<br>Open buttons</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div style="background:#2563eb; color:white; padding:15px; border-radius:10px;"><b>Python SELECTED</b><br><span style="color:#dbeafe;">Easy plus Data Science</span></div>', unsafe_allow_html=True)
        if st.button("Open Python", key="open_py_main"):
            st.session_state.page = "list"

    with right:
        st.markdown('<h4 style="color:black;">Python Topics</h4>', unsafe_allow_html=True)
        topics = {
            "1. Introduction": "Python ante enti, ela start cheyyali, BhavPath lo first step.",
            "2. Variables": "Variables ante boxes lantivi, data store cheyyadaniki.",
            "3. Operators": "+ - * / logic, calculations cheyyadaniki.",
            "4. Loops": "For, While loops - same pani repeat cheyyadaniki.",
            "5. Identifiers": "Names ivvadam - variable, function names rules."
        }
        for title, desc in topics.items():
            if st.button(f"• {title}  →  Open Detail", key=title):
                st.session_state.selected_topic = title
                st.session_state.page = "detail"
                st.rerun()

# DETAIL PAGE
else:
    topic = st.session_state.selected_topic
    st.markdown(f'<div class="hero"><h2 style="color:#1d4ed8; margin:0;">{topic}</h2><p style="color:black;">Detailed explanation in Telugu + English</p></div>', unsafe_allow_html=True)
    
    if st.button("← Back to List"):
        st.session_state.page = "list"
        st.rerun()

    st.info(f"Here you can add full content for {topic} - examples, code, practice.")
    st.code(f"# Example for {topic}\nprint('BhavPath - {topic}')", language="python")
