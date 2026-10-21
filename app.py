import streamlit as st

st.set_page_config(page_title="BhavPath", layout="wide", page_icon="✨")

# --- CSS FOR SAME BLUE-WHITE LOOK ---
st.markdown("""
<style>
    .top-bar {
        background: #1d4ed8;
        color: white !important;
        padding: 15px 20px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
    }
    .black-line { border: 2px solid black; margin: 15px 0; }
    div.stButton > button {
        background: #2563eb;
        color: white;
        border: none;
        padding: 12px;
        border-radius: 6px;
        font-weight: 500;
        width: 100%;
    }
    div.stButton > button:hover {
        background: #1d4ed8;
        color: white;
    }
    .info-card {
        background: white;
        color: black;
        padding: 15px;
        border: 1px solid #ccc;
        border-radius: 8px;
        font-weight: bold;
    }
    .python-header {
        background: #2563eb;
        color: white;
        padding: 15px;
        border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# --- TOP BAR ---
st.markdown('<div class="top-bar">BhavPath | Rise | 81 percent | 820 XP | Python</div>', unsafe_allow_html=True)
st.markdown('<div class="black-line"></div>', unsafe_allow_html=True)

# --- TOP BUTTONS ---
colA, colB = st.columns(2)
with colA:
    st.button("Back Change percent")
with colB:
    st.button("Back to All Topics List Malli")

st.write("")

# --- MAIN CONTENT ---
left, right = st.columns([1, 3])

with left:
    st.markdown('<div class="info-card">List Page varake -<br>Ikkada matrame<br>Open buttons</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="python-header">
        <b>Python SELECTED</b><br>
        <span style="color:#dbeafe; font-size:13px;">Easy plus Data Science</span>
    </div>
    """, unsafe_allow_html=True)
    st.button("Open Python", key="open_py")

with right:
    topics = ["1. Introduction", "2. Variables", "3. Operators", "4. Loops", "5. Identifiers"]
    for topic in topics:
        if st.button(f"• {topic}  →  Open Detail", key=topic):
            st.success(f"You opened {topic}")
            st.balloons()
