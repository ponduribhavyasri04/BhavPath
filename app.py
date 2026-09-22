import streamlit as st

# Page Config
st.set_page_config(page_title="BhavPath - Career Guidance", page_icon="🚀", layout="wide")

# Header
st.title("🚀 BhavPath")
st.subheader("Nee Bhavishyathu - Nee Dhaari | Your Future, Your Path")
st.write("---")

# Sidebar
st.sidebar.title("Bhavya's Guidance")
menu = st.sidebar.selectbox("Choose", ["Home", "Career Paths", "Skills", "About Bhavya"])

if menu == "Home":
    st.header("Welcome to BhavPath 💙")
    st.write("Students ki best career guidance isthunna platform!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Engineering**\n\nJEE, EAMCET guidance")
    with col2:
        st.success("**Medicine**\n\nNEET guidance")
    with col3:
        st.warning("**Govt Jobs**\n\nUPSC, SSC guidance")
    
    st.write("---")
    st.subheader("Why BhavPath?")
    st.write("✅ 100% Free guidance\n✅ Telugu + English lo\n✅ Real success stories")

elif menu == "Career Paths":
    st.header("Career Paths 🛤️")
    career = st.selectbox("Select your interest", ["Engineering", "Doctor", "Government Job", "Business"])
    if career:
        st.success(f"Great choice Bhavya! {career} kosam full roadmap isthanu!")
        st.write("1. 10th tarvata em cheyali\n2. Inter lo em teesukovali\n3. Entrance exams enti\n4. Best colleges")

elif menu == "Skills":
    st.header("Top Skills for 2026 🔥")
    st.write("- **AI & Coding**\n- **Communication**\n- **Digital Marketing**\n- **Public Speaking**")

else:
    st.header("About Bhavya 👩‍🎓")
    st.write("Hi! Nenu Bhavya Sri - Students ki help cheyali ani ee BhavPath create chesa!")
    st.write("Mission: 10,000 students ki free guidance!")

st.sidebar.write("---")
st.sidebar.write("Made with 💙 by Bhavya")
