import streamlit as st

st.set_page_config(page_title="BhavPath - Career Guide", page_icon="🚀", layout="wide")

# --- HOME PAGE ---
st.title("🚀 BhavPath - Bhavya's Career Path")
st.subheader("For 3rd Year to 4th Year - 58% Batch - Data Scientist Dream")
st.markdown("---")

# Home Page Options
option = st.selectbox("👇 Select What You Need:", 
    ["-- Select --", 
     "📚 Previous Papers (Python, C, C++, Java, SQL, DBMS)",
     "💼 Interview Questions (TCS, Infosys, Wipro - 58% Eligible)",
     "🎯 Placement Eligibility Checker",
     "📖 Study Material (6 PDFs)",
     "📝 Resume Builder - 1 Year Experience",
     "🧠 Data Scientist Roadmap (3rd Year to 4th Year)",
     "🏆 APBOCWWB Best Course - AI Data Scientist"]
)

if option == "-- Select --":
    st.info("👆 Meedha options nundi okati select chey Bhavya!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Courses", "32 - AI Data Scientist", "THE BEST")
    with col2:
        st.metric("Your Batch", "58%", "Eligible")
    with col3:
        st.metric("Experience Plan", "6 Months → 1 Year", "Genuine")

elif "Previous Papers" in option:
    st.header("📚 Previous Papers")
    paper = st.radio("Select Subject:", ["Python", "C", "C++", "Java", "SQL", "DBMS"])
    st.success(f"{paper} Previous Papers - 5 Years - Download Ready - (Nee PDFs nundi)")

elif "Interview Questions" in option:
    st.header("💼 Interview Questions")
    company = st.selectbox("Company:", ["TCS", "Infosys", "Wipro", "Accenture"])
    st.write(f"**{company} - For 58% Batch:**")
    st.code("1. Python - List vs Tuple?\n2. SQL - JOIN types?\n3. DBMS - ACID properties?\n4. Java - OOPs concepts?\n5. C - Pointer?")

elif "Eligibility Checker" in option:
    st.header("🎯 Placement Eligibility Checker")
    per = st.slider("Your %:", 50, 100, 58)
    if per >= 60:
        st.success("Eligible for all - TCS, Infosys, Wipro!")
    else:
        st.warning(f"{per}% - Eligible for Wipro, Accenture, APBOCWWB Data Scientist Course 32 - 1 year plan tho 60% laaga resume build chey!")

elif "Study Material" in option:
    st.header("📖 Study Material - 6 PDFs")
    st.write("- Python Basic to Advance\n- C Programming\n- C++\n- SQL\n- DBMS\n- Java Full Stack\n")
    st.button("📥 Download All PDFs")

elif "Resume Builder" in option:
    st.header("📝 Resume Builder - 1 Year Genuine Experience")
    st.markdown("""
    **After 4th Year Resume:**
    - APBOCWWB AI Data Scientist - 6 Months (Govt Cert)
    - Internship + 3 Projects - 6 Months
    - **Total: 1 Year Real Experience - BGV Safe**
    """)

elif "Data Scientist Roadmap" in option:
    st.header("🧠 Data Scientist Roadmap")
    st.markdown("""
    **3rd Year (Now):** Python + SQL + APBOCWWB Course 32
    **4th Year 1st Sem:** 3 Projects + Internship
    **After 4th Year:** 1 Year Experience - Apply TCS/Infosys
    """)

elif "APBOCWWB" in option:
    st.header("🏆 THE BEST - Course 32 AI Data Scientist")
    st.success("Course ID 32 - 6 Months - Highest Placement - 5-8 LPA - THE BEST FOR YOU!")
    st.write("Help Line: 9649 808 808")
    st.write("Bhavya Ponduri - Certified")

st.markdown("---")
st.caption("Made with ❤️ by Bhavya Ponduri | BhavPath - 2026")
