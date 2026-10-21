import streamlit as st

st.set_page_config(page_title="BhavPath", layout="wide", page_icon="🔥")

st.markdown("""
<style>
    .top-bar {
        background: #1d4ed8;
        color: white !important;
        padding: 14px 20px;
        border-radius: 10px;
        font-weight: 800;
        font-size: 18px;
    }
    .black-line { height: 4px; background: black; margin: 10px 0; }
    .hero-main {
        background: linear-gradient(135deg, #1d4ed8, #2563eb);
        color: white !important;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 15px;
    }
    .hero-main h1 { color: white !important; margin: 0; font-size: 40px; }
    .hero-main p { color: #dbeafe !important; margin: 5px 0 0 0; font-size: 16px; }
    div.stButton > button {
        background: #2563eb !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
    }
    .card-white {
        background: white;
        color: black !important;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-weight: 600;
    }
    .card-blue {
        background: #2563eb;
        color: white !important;
        padding: 15px;
        border-radius: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# 1. TOP BAR
st.markdown('<div class="top-bar">BhavPath | Rise | 81 percent | 820 XP | Python</div>', unsafe_allow_html=True)
st.markdown('<div class="black-line"></div>', unsafe_allow_html=True)

# 2. BHAVPATH HERO - STARTING PAGE LO BIG GA
st.markdown("""
<div class="hero-main">
    <h1>BhavPath</h1>
    <p>Rise • Learn Python • Build Your Future | 81% Completed | 820 XP</p>
</div>
""", unsafe_allow_html=True)

# 3. TOP BUTTONS - NO GAP
c1, c2 = st.columns(2, gap="small")
with c1:
    st.button("Back Change percent", use_container_width=True)
with c2:
    st.button("Back to All Topics List Malli", use_container_width=True)

# 4. MAIN - NO WHITE SPACE
left, right = st.columns([1, 2.5], gap="small")

with left:
    st.markdown('<div class="card-white">List Page varake -<br>Ikkada matrame Open buttons</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="card-blue">Python SELECTED<br><small>Easy plus Data Science</small></div>', unsafe_allow_html=True)
    st.button("Open Python", use_container_width=True, key="open_py")

with right:
    st.markdown('<p style="color:black; font-weight:700; margin:0 0 10px 0;">Python Topics - Click to Open Detail</p>', unsafe_allow_html=True)
    topics = ["1. Introduction", "2. Variables", "3. Operators", "4. Loops", "5. Identifiers"]
    for t in topics:
        if st.button(f"• {t}  →  Open Detail", key=t, use_container_width=True):
            st.success(f"{t} Opened!")
            st.code(f"# {t}\nprint('Welcome to {t} in BhavPath')", language="python")
