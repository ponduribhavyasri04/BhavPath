import streamlit as st
import os, glob

st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="centered")
st.markdown("<h1 style='text-align:center;color:#FF2D2D;'>BhavPath</h1>", unsafe_allow_html=True)

st.markdown("### 📚 BhavPath Materials - All PDFs")

pdfs = glob.glob("*.pdf")
st.write(f"Total PDFs Found: {len(pdfs)}")

for i in range(len(pdfs)):
    file_path = pdfs[i]
    file_name = os.path.basename(file_path)
    st.markdown(f"**{i+1}. {file_name}**")
    with open(file_path, "rb") as f:
        st.download_button(
            label=f"📥 Download {file_name}",
            data=f,
            file_name=file_name,
            key=f"pdf_{i}",
            use_container_width=True
        )
