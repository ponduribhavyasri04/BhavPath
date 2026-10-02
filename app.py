import streamlit as st

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.title("🚀 BhavPath")

name = st.text_input("Your Name", "Bhavya Ponduri")
college = st.text_input("College Name", "RISE KRISHNA SAI GANDHI GROUP OF INSTITUTIONS")
percent = st.slider("Your B.Tech %", 0, 100, 58)
branch = st.selectbox("Branch", ["CSE", "ECE", "EEE", "MECH", "AI & DS"])
powers = st.multiselect("Pick Your Superpowers", ["Python", "Communication", "SQL", "Java", "C", "C++", "DBMS"], default=["Python", "SQL"])

if st.button("GENERATE MY PLACEMENT DNA"):
    score = 75 + len(powers)*5
    if score > 95: score = 95
    st.success(f"{name} Your Score is {score}% - Eligible for TCS Digital!")
    st.balloons()
