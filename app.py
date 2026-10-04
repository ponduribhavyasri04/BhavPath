import streamlit as st
import glob
import os
import base64

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#AAA;'>What is Your Placement Story?</h3>", unsafe_allow_html=True)

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE"], index=None)

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    st.success(f"🔥 {name} Ready for Placement!")

st.markdown("---")
st.markdown("### 📚 Materials - Drag & Read")

pdf_files = glob.glob("*.pdf")

for pdf_path in pdf_files:
    file_name = os.path.basename(pdf_path)
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
        b64 = base64.b64encode(pdf_bytes).decode()
    
    st.markdown(f"**{file_name}**")
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 Download {file_name}", f, file_name=file_name, use_container_width=True)
    
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="500" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.markdown("---")
