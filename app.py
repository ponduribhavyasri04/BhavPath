import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

# --- CSS FOR CARD LIKE YOUR PHOTO ---
st.markdown("""
<style>
div[data-testid="stContainer"] {
    border-radius: 15px !important;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 BhavPath")
st.subheader("Your Placement Journey Starts Here!")
st.markdown("---")

# --- LEAD FORM ---
st.markdown("### 📝 Start Your Journey")
with st.form("lead_form"):
    name = st.text_input("Full Name")
    branch = st.selectbox("Branch", ["CSE", "ECE", "EEE", "MECH", "CIVIL", "Other"])
    college = st.text_input("College Name")
    percentage = st.text_input("Percentage / CGPA")
    phone = st.text_input("Phone Number")
    submit = st.form_submit_button("Submit & Get Access", use_container_width=True, type="primary")

if submit:
    if name and phone:
        file_exists = os.path.isfile("bhavpath_leads.csv")
        new_data = pd.DataFrame([{
            "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Name": name, "Branch": branch, "College": college,
            "Percentage": percentage, "Phone": phone
        }])
        new_data.to_csv("bhavpath_leads.csv", mode='a', header=not file_exists, index=False)
        st.success(f"Bhav | Your Placement Story Started! Saved! ✅")
        st.balloons()
    else:
        st.error("Please fill Name & Phone")

st.markdown("---")

# ===== SKILLED MATERIAL CARD - EXACT LIKE YOUR COURSES PHOTO =====
st.markdown("### 📚 Your Learning")

with st.container(border=True):
    # Image + Text like your photo
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://cdn-icons-png.flaticon.com/512/2728/2728612.png", width=110)
    with col_text:
        st.markdown("")
        st.markdown("**Click here to view all your skilled materials**")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Blue Button like Courses
    if st.button("Skilled Material", use_container_width=True, type="primary"):
        st.session_state.show_skills = not st.session_state.get("show_skills", False)

# --- SHOW 7 PDFs AFTER CLICK ---
if st.session_state.get("show_skills"):
    st.markdown("#### 📘 7 Skilled Materials")
    
    pdf_list = [
        "1. Communication Skills",
        "2. Resume Building Mastery", 
        "3. Interview Preparation",
        "4. Aptitude & Reasoning",
        "5. Group Discussion Tips",
        "6. Body Language Guide",
        "7. Complete Placement Guide"
    ]
    
    for pdf_name in pdf_list:
        with st.container(border=True):
            col1, col2 = st.columns([3,1])
            with col1:
                st.write(f"📄 **{pdf_name}**")
            with col2:
                # Nee original PDF files unte avi link chey
                st.download_button("View", data=f"Content of {pdf_name}", file_name=f"{pdf_name}.pdf", key=pdf_name)

st.markdown("---")
st.caption("Made with ❤️ by Bhavya for Students")

# ===== SECRET ADMIN DASHBOARD - ONLY FOR YOU =====
query_params = st.query_params
if query_params.get("admin") == "bhavya":
    st.markdown("---")
    st.markdown("## 🔐 Bhavya's Private Dashboard - Only You Can See")
    pwd = st.text_input("Enter Secret Password", type="password")
    
    if pwd == "bhavya":  # Nee own password - marchukovachu
        st.success("Welcome Bhavya!")
        if os.path.isfile("bhavpath_leads.csv"):
            df = pd.read_csv("bhavpath_leads.csv")
            st.metric("Total Leads", len(df))
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Download All Leads CSV", df.to_csv(index=False), "bhavpath_leads.csv")
        else:
            st.info("No leads yet - 0")
    elif pwd != "":
        st.error("Wrong password")
