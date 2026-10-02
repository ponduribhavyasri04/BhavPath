import streamlit as st

st.set_page_config(page_title="BhavPath Placement Predictor", page_icon="🚀", layout="centered")

st.title("BhavPath Placement Predictor")
st.subheader("What's your Placement Story ..?")

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
college = st.text_input("College Name", placeholder="Ex: RISE Krishna Sai Gandhi Group Of Institutions")
percent = st.slider("Your B.Tech %", 0, 100, 58)
branch = st.selectbox("Branch", ["CSE", "ECE", "EEE", "MECH", "AI & DS"])
powers = st.multiselect("Pick Your Superpowers", ["Python", "Communication", "SQL", "Java", "C", "DBMS"], placeholder="Choose your skills")

if st.button("GENERATE MY PLACEMENT DNA"):
    if name == "":
        name = "Bhavya Ponduri"
    score = 75 + len(powers) * 5
    if score > 95:
        score = 95
    st.success(f"{name} Your Score is {score}% - Eligible for TCS Digital!")
    st.balloons()
