import streamlit as st
import os

st.set_page_config(page_title="BhavPath", layout="centered")
st.title("🚀 BhavPath")
st.write("Your Placement Journey Starts Here!")

name = st.text_input("Full Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["Data Science","CSE","ECE","EEE","MECH"])
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Group Of Institutions")
phone = st.text_input("Phone Number", placeholder="Ex: 9876543210")

if st.button("Submit & Get Access", type="primary", use_container_width=True):
    if name and phone:
        st.success(f"Saved {name}! ✅")
        st.balloons()

st.divider()
with st.container(border=True):
    st.markdown("### 📚 Click here to view all your skilled materials")
    show = st.button("Skilled Material", use_container_width=True, type="primary")

if show:
    # Root lo & materials folder lo rendu chotla check chestundi
    all_pdfs = []
    for folder in [".", "materials"]:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f.lower().endswith(".pdf"):
                    all_pdfs.append(os.path.join(folder, f))
    
    if all_pdfs:
        st.success(f"✅ {len(all_pdfs)} PDFs found!")
        for path in all_pdfs:
            fname = os.path.basename(path)
            with st.container(border=True):
                c1,c2 = st.columns([3,1])
                c1.write(f"📄 {fname}")
                with open(path, "rb") as file:
                    c2.download_button("View", file, file_name=fname, key=f"btn_{path}", use_container_width=True)
    else:
        st.warning("PDFs kanipinchaledu - upload ayyayo ledo okasari check chey!")
