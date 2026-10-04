import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")

st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;color:#AAA;'>What is Your Placement Story?</h3>", unsafe_allow_html=True)

name = st.text_input("Your Name", placeholder="Ex: Bhavya Ponduri")
branch = st.selectbox("Branch", ["CSE","Data Science","ECE","EEE","IT","Mechanical"], index=None, placeholder="Ex: Data Science")
college = st.text_input("College Name", placeholder="Ex: Rise Krishna Sai Gandhi Group Of Institutions")

# NEW - B.Tech Percentage
btech_per = st.text_input("B.Tech Percentage / CGPA", placeholder="Ex: 78% or 8.2 CGPA")

skills = st.multiselect("Choose Your Skills", ["Python","C","C++","Java","Communication","Aptitude","DSA","SQL","Other"], placeholder="Select skills - Ex: Python, C")

if st.button("GENERATE MY PLACEMENT DNA", use_container_width=True, type="primary"):
    st.balloons()
    if name and btech_per and skills:
        st.success(f"🔥 {name} | {branch} | {btech_per} | {college}")
        st.info(f"Skills: {', '.join(skills)}")
        
        # Extract % for logic
        try:
            per_val = float(''.join(filter(lambda x: x.isdigit() or x=='.', btech_per))[:4])
            if per_val <= 10: # CGPA to %
                per_val = per_val * 9.5
        except:
            per_val = 70

        st.markdown("### 🎯 Eligible Companies For You")
        
        if per_val >= 60:
            st.markdown("**60%+ Companies:**")
            st.write("✅ TCS Ninja | Infosys | Wipro | Tech Mahindra | Capgemini")
        if per_val >= 70:
            st.markdown("**70%+ Companies:**")
            st.write("✅ Accenture | Cognizant | HCL | IBM | Deloitte")
        if per_val >= 75:
            st.markdown("**75%+ Premium Companies:**")
            st.write("🔥 Amazon | Microsoft | Google | TCS Digital | Product Based")

        if "Python" in skills or "Java" in skills:
            st.markdown("**💻 Based on Skills:** Python/Java -> Full Stack, Data Science Roles")
        if "Communication" in skills:
            st.markdown("**🗣️ Communication Strong -> HR, Client Facing Roles Eligible**")

    else:
        st.warning("Please fill Name, B.Tech % and Skills!")

st.markdown("---")
st.markdown("### 📚 BhavPath Materials - All PDFs")
all_pdfs = sorted(list(set(glob.glob("*.pdf") + glob.glob("*.PDF"))))
st.write(f"Total Found: {len(all_pdfs)} PDFs")
for i, pdf_path in enumerate(all_pdfs):
    fname = os.path.basename(pdf_path)
    st.markdown(f"**{i+1}. {fname}**")
    with open(pdf_path, "rb") as f:
        st.download_button(f"📥 Download {fname}", f, file_name=fname, key=f"comp_{i}", use_container_width=True)
 
