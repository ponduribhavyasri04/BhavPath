import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#AAA;'>What is Your Placement Story?</h3>", unsafe_allow_html=True)

# Inputs with grey placeholders
name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT","Mechanical","Civil"], index=None, placeholder="Ex: Data Science")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")

# NEW - Choose Skills
skills = st.multiselect(
    "Choose Your Skills",
    ["Python", "C", "C++", "Java", "Communication", "Aptitude", "DSA", "SQL", "Other"],
    placeholder="Select your skills - Ex: Python, C, Communication"
)

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    if name and skills:
        st.success(f"🔥 {name} ({branch}) - {college}")
        st.info(f"💡 Skills: {', '.join(skills)} - Your Placement DNA Generated!")
        # Skills basis ga roadmap kuda chepachu
        if "Python" in skills:
            st.write("✅ Python Developer Track Ready!")
        if "Communication" in skills:
            st.write("✅ HR Interview Ready!")
    else:
        st.warning("Please enter Name & Select Skills!")

st.markdown("---")
st.markdown("### 📚 BhavPath Materials - All PDFs")

all_pdfs = glob.glob("*.pdf") + glob.glob("*.PDF")
all_pdfs = sorted(list(set(all_pdfs)))
st.write(f"Total Found: {len(all_pdfs)} PDFs")

for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    st.markdown(f"**{i+1}. {fname}**")
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 Download {fname}", f, file_name=fname, key=f"skill_{i}", use_container_width=True)
