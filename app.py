import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="centered")
st.title("🚀 BhavPath")
st.write("Your Placement Journey Starts Here!")
# FORM
name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["Data Science","CSE","ECE","EEE","MECH","CIVIL"])
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
phone = st.text_input("Phone Number", placeholder="Ex: 9876543210")

if st.button("Submit & Get Access", type="primary", use_container_width=True):
    if name and phone:
        st.success(f"Saved {name}! ✅")
        st.balloons()
    else:
        st.error("Name & Phone pettu!")

st.divider()

# SKILLED MATERIAL - NO ERROR VERSION
with st.container(border=True):
    st.markdown("### 📚 Click here to view all your skilled materials")
    show = st.button("Skilled Material", use_container_width=True, type="primary")

if show:
    try:
        folder = "materials"
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
            st.info("📁 'materials' folder create ayindi! Ippudu GitHub lo akkada PDFs upload chey Bhavya!")
        else:
            files = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]
            if files:
                st.success(f"✅ {len(files)} PDFs found!")
                for f in files:
                    with st.container(border=True):
                        col1, col2 = st.columns([3,1])
                        col1.write(f"📄 {f}")
                        try:
                            with open(os.path.join(folder, f), "rb") as pdf:
                                col2.download_button("View", pdf, file_name=f, key=f"btn_{f}", use_container_width=True)
                        except:
                            col2.write("Error")
            else:
                st.warning("📄 Folder undi kani PDFs levu! GitHub lo upload chey:")
                st.code("materials/Communication.pdf\nmaterials/Resume.pdf\nmaterials/Interview.pdf")
    except Exception as e:
        st.error("Kotha folder create chestunna... refresh chey!")
        st.info("GitHub lo 'materials' ane folder lo 7 PDFs upload chey Bhavya!")

st.caption("Made with ❤️ by Bhavya")
