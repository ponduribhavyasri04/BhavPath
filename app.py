import streamlit as st
import os

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #0E0E0E; }
</style>
""", unsafe_allow_html=True)

# --- HEADING ---
st.markdown("<h1 style='text-align: center; color: #FF2D2D; font-weight: 900; margin-bottom: 0px;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #AAAAAA; margin-top: 0px; font-weight: 400;'>What's Your Placement Story?</h3>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- INPUTS ---
name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
college = st.text_input("College Name", placeholder="Ex: RISE Krishna Sai Gandhi Group Of Institutions")
branch = st.selectbox("Branch", ["CSE", "CSE - Data Science", "Data Science", "ECE", "EEE", "MECH", "CIVIL", "AI & ML", "IT", "AIML"], index=None, placeholder="Ex: Data Science")
percentage = st.slider("Your B.Tech %", 0, 100, 75)
superpowers = st.multiselect("Pick Your Superpowers", ["Python", "Java", "C", "SQL", "Aptitude", "Communication", "DSA", "DBMS", "OS", "CN"], placeholder="Ex: Python, Communication, SQL")

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    if not name:
        st.warning("Please enter your Name!")
    elif not branch:
        st.warning("Please select your Branch!")
    else:
        score = percentage
        if "Python" in superpowers: score += 5
        if "SQL" in superpowers: score += 5
        if "Communication" in superpowers: score += 5
        if score > 100: score = 95
        st.balloons()
        if score >= 90:
            st.success(f"🔥 {name} Your Score is {score}% - Eligible for TCS Digital!")
        elif score >= 75:
            st.success(f"✅ {name} Your Score is {score}% - Eligible for TCS Ninja & Wipro!")
        else:
            st.info(f"📚 {name} Your Score is {score}% - Keep Learning, You Will Get Placed!")

# --- PDF SECTION ADDED ---
st.markdown("---")
st.markdown("### 📚 Download Your BhavPath Materials")
st.markdown("Made by Bhavya for RISE Students")

pdf_files = {
    "Aptitude & Reasoning": "BhavPath A&S.pdf",
    "C Programming": "BhavPath C.pdf",
    "Data Structures": "BhavPath DE.pdf",
    "Python Mastery": "BhavPath Python.pdf",
    "Software Engineering": "BhavPath SE.pdf",
    "SQL Mastery": "BhavPath SQL.pdf",
    "Java Mastery": "BhavPath Java.pdf"
}

for title, filename in pdf_files.items():
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            st.download_button(f"📥 Download {title}", f, file_name=filename, use_container_width=True)
    else:
        st.caption(f"⚠️ {filename} - upload in GitHub root")

st.markdown("---")
st.caption("Built with ❤️ by Bhavya Ponduri | BhavPath")
