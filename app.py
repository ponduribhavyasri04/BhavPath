import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="BhavPath", layout="centered")
st.title("🚀 BhavPath")
st.caption("Your Placement Journey Starts Here!")

# FORM WITH GREY EXAMPLE
name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["Data Science","CSE","ECE","EEE","MECH","CIVIL"])
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
percentage = st.text_input("Percentage", placeholder="Ex: 85% or 8.5 CGPA")
phone = st.text_input("Phone Number", placeholder="Ex: 9876543210")

if st.button("Submit & Get Access", type="primary", use_container_width=True):
    if name and phone:
        is_new = not os.path.isfile("leads.csv")
        pd.DataFrame([{
            "Date": datetime.now().strftime("%d-%m-%Y"),
            "Name": name, "Branch": branch,
            "College": college, "Per": percentage, "Phone": phone
        }]).to_csv("leads.csv", mode='a', header=is_new, index=False)
        st.success(f"Saved {name}! ✅")
        st.balloons()
    else:
        st.error("Name & Phone pettu Bhavya!")

st.divider()

# SKILLED MATERIAL
with st.container(border=True):
    st.markdown("### 📚 Click here to view all your skilled materials")
    if st.button("Skilled Material", use_container_width=True, type="primary"):
        st.session_state.show = not st.session_state.get("show", False)

if st.session_state.get("show"):
    folder = "materials"
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.endswith(".pdf"):
                with st.container(border=True):
                    c1,c2 = st.columns([3,1])
                    c1.write(f"📄 {f}")
                    with open(os.path.join(folder, f), "rb") as file:
                        c2.download_button("View", file, file_name=f, key=f, use_container_width=True)
    else:
        st.info("7 PDFs kosam GitHub lo 'materials' folder create chesi upload chey!")

# ADMIN - bhavpath.streamlit.app/?admin=bhavya
if st.query_params.get("admin") == "bhavya":
    pwd = st.text_input("Admin Password", type="password")
    if pwd == "bhavya" and os.path.isfile("leads.csv"):
        df = pd.read_csv("leads.csv")
        st.dataframe(df, use_container_width=True)
        st.download_button("Download CSV", df.to_csv(index=False), "leads.csv")
