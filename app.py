import streamlit as st

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

# --- HEADER ---
st.title("🚀 BhavPath")
st.markdown("**Bhavya Ponduri | 3rd Year BTech | Data Scientist Journey | 58% Batch**")
st.markdown("---")

# --- HOME PAGE OPTIONS ---
menu = st.selectbox("🏠 Home - Select Option:", [
    "Home",
    "📚 Previous Papers",
    "💼 Interview Questions", 
    "📖 Study Material - Python, C, C++, Java, SQL, DBMS",
    "🎯 Placement Eligibility - 58%",
    "🧠 Data Scientist Roadmap - 3rd to 4th Year",
    "🏆 APBOCWWB Course 32 - THE BEST"
])

# --- HOME ---
if menu == "Home":
    st.success("Welcome to BhavPath - Your Career Guide")
    st.info("APBOCWWB Course 32 - AI Data Scientist - 6 Months = 1 Year Experience Plan")
    st.metric("Current", "3rd Year BTech", "Learning Phase")
    st.metric("After 4th Year", "1 Year Experience", "Genuine - BGV Safe")

# --- PREVIOUS PAPERS ---
elif "Previous Papers" in menu:
    st.header("📚 Previous Papers")
    subject = st.radio("Subject:", ["Python", "C", "C++", "Java", "SQL", "DBMS"])
    st.write(f"**{subject} - 5 Years Previous Papers Ready**")
    st.download_button("Download PDF", "PDF Content", file_name=f"{subject}.pdf")

# --- INTERVIEW QUESTIONS ---
elif "Interview Questions" in menu:
    st.header("💼 Interview Questions for 58% Batch")
    st.code("""
    TCS / Infosys / Wipro - 58% Eligible:
    1. Python - What is Data Science?
    2. SQL - Difference between WHERE and HAVING?
    3. DBMS - What is Normalization?
    4. Java - OOPs Concepts
    5. C - Pointers & Arrays
    """)

# --- STUDY MATERIAL ---
elif "Study Material" in menu:
    st.header("📖 Study Material - 6 PDFs")
    st.write("✅ Python - Basic to Advance\n✅ C Programming\n✅ C++\n✅ SQL\n✅ DBMS\n✅ Java Full Stack")

# --- ELIGIBILITY ---
elif "Placement" in menu:
    st.header("🎯 58% Eligibility Checker")
    st.warning("58% - Wipro, Accenture, APBOCWWB Course 32 - Eligible!")
    st.success("After 1 Year Plan (3rd to 4th Year) - You will be 1 Year Experienced - Eligible for All!")

# --- ROADMAP ---
elif "Roadmap" in menu:
    st.header("🧠 3rd Year to 4th Year - 1 Year Experience Roadmap")
    st.markdown("""
    **Now (3rd Year):** Learn - APBOCWWB Course 32
    **Next 6 Months:** 3 Projects + Internship
    **After 4th Year:** Resume lo 1 Year Experience - Genuine
    """)

# --- APBOCWWB ---
elif "APBOCWWB" in menu:
    st.header("🏆 THE BEST - Course 32 AI Data Scientist")
    st.success("Course ID 32 - 6 Months - Govt Certified - Industry Ready - 5-8 LPA")
    st.write("Help Line: 9649 808 808")

st.markdown("---")
st.caption("Made by Bhavya Ponduri | bhavpath.streamlit.app | 2026")
