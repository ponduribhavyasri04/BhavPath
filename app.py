import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.title("🚀 BhavPath")
st.markdown("### Your Placement Journey Starts Here!")
st.markdown("---")

st.markdown("### 📝 Start Your Journey")
with st.form("lead_form", clear_on_submit=False):
    name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
    branch = st.selectbox("Branch", ["CSE", "Data Science", "ECE", "EEE", "MECH", "CIVIL", "Other"])
    college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
    percentage = st.text_input("Percentage / CGPA", placeholder="Ex: 85% or 8.5 CGPA")
    phone = st.text_input("Phone Number", placeholder="Ex: 9876543210")
    submit = st.form_submit_button("Submit & Get Access", use_container_width=True, type="primary")

if submit:
    if name and phone:
        file_exists = os.path.isfile("bhavpath_leads.csv")
        df_new = pd.DataFrame([{
            "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Name": name, "Branch": branch, "College": college,
            "Percentage": percentage, "Phone": phone
        }])
        df_new.to_csv("bhavpath_leads.csv", mode='a', header=not file_exists, index=False)
        st.success(f"{name} | Saved! ✅")
        st.balloons()
    else:
        st.error("Name & Phone required")

st.markdown("---")
st.markdown("### 📚 Your Learning Hub")
with st.container(border=True):
    st.markdown("#### 💻 Click here to view all your")
    st.markdown("#### skilled materials")
    if st.button("Skilled Material", use_container_width=True, type="primary"):
        st.session_state.show_skills = not st.session_state.get("show_skills", False)

if st.session_state.get("show_skills", False):
    st.markdown("#### 📘 7 Skilled Materials")
    for m in ["1. Communication", "2. Resume Building", "3. Interview Prep", "4. Aptitude", "5. GD Tips", "6. Body Language", "7. Placement Guide"]:
        with st.container(border=True):
            c1,c2 = st.columns([3,1])
            with c1: st.write(f"📄 **{m}**")
            with c2: st.button("View", key=f"view_{m}", use_container_width=True)

st.caption("Made with ❤️ by Bhavya")

if st.query_params.get("admin") == "bhavya":
    st.markdown("---")
    st.markdown("## 🔐 Bhavya's Private Dashboard")
    pwd = st.text_input("Password", type="password")
    if pwd == "bhavya":
        if os.path.isfile("bhavpath_leads.csv"):
            df = pd.read_csv("bhavpath_leads.csv")
            st.metric("Total Leads", len(df))
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Download CSV", df.to_csv(index=False), "leads.csv")
