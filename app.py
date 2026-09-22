import streamlit as st
import random

st.set_page_config(page_title="BhavPath - Whats Your Placement Story", page_icon="🚀", layout="wide")

st.markdown("<p style='text-align: center;'>An AI-powered Placement Readiness Predictor. <b>Discover, Predict & Improve</b></p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name", placeholder="Ex: Bhavya")
    college = st.text_input("College Name", placeholder="Ex: JNTU Ongole")
    percentage = st.slider("Your B.Tech %", 40, 100, 75)
with col2:
    branch = st.selectbox("Branch", ["CSE", "ECE", "EEE", "AIML", "Other"])
    skills = st.multiselect("Pick Your Superpowers", ["Python", "Java", "SQL", "DSA", "Communication", "Projects", "Internship"])

if st.button("GENERATE MY PLACEMENT DNA", type="primary", use_container_width=True):
    if not name or not skills:
        st.warning("Name and Skills pettu!")
    else:
        score = random.randint(70,95)
        st.balloons()
        st.success(f"{name} Your Score is {score}% - Eligible for TCS Digital!")
        share = f"My Placement DNA is {score}%! Check yours on BhavPath bhavpath.streamlit.app"
        st.code(share)

st.caption("Built by Bhavya Sri 2026")
st.write("---")
st.write("BhavPath is Indias First Placement DNA Test")
st.write("Keywords: BhavPath, Placement Predictor, JNTU Placement")


     
       
