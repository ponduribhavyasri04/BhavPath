import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#AAA;'>What is Your Placement Story?</h3>", unsafe_allow_html=True)

# 1. Issac Paul place lo - Bhavya Ponduri grey lo
name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")

# 2. Branches lo Data Science add chesi - Ex: grey lo
branch = st.selectbox(
    "Branch", 
    ["CSE", "Data Science", "ECE", "EEE", "IT", "Mechanical", "Civil"], 
    index=None, 
    placeholder="Ex: Data Science"
)

# 3. College - Rise Krishna Sai grey lo
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    if name:
        st.success(f"🔥 {name} from {branch} - {college} - Ready for Placement!")
    else:
        st.warning("Please enter your name!")

st.markdown("---")

# 4. PDFs - Including ADS
st.markdown("### 📚 BhavPath Materials - All PDFs")

all_pdfs = glob.glob("*.pdf") + glob.glob("*.PDF")
all_pdfs = sorted(list(set(all_pdfs)))

st.write(f"Total Found: {len(all_pdfs)} PDFs")

for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    st.markdown(f"**{i+1}. {fname}**")
    with open(pdf_path, "rb") as f:
        st.download_button(
            label=f"📥 Download {fname}", 
            data=f, 
            file_name=fname, 
            key=f"final_{i}", 
            use_container_width=True
        )
