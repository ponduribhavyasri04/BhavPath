import os
import streamlit as st

# ... nee form code same ...
if st.session_state.get("show_skills", False):
    st.markdown("#### 📘 7 Skilled Materials")
    
    # Folder lo PDFs unte chupistundi, lekapote info isthundi
    pdf_folder = "materials"  # GitHub lo ee folder create chey
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder, exist_ok=True)
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")] if os.path.exists(pdf_folder) else []

    if len(pdf_files) == 0:
        st.warning("⚠️ Nuvvu inka PDFs upload cheledu Bhavya!")
        st.info("""
        **PDF ela add cheyali:**
        1. GitHub -> Add file -> Upload files
        2. `materials` ane folder lo 7 PDFs petu
        3. Reboot kottu - automatic ga vastayi
        """)
        # Demo ki fake list
        for m in ["Communication", "Resume", "Interview", "Aptitude", "GD", "Body Language", "Placement"]:
            with st.container(border=True):
                st.write(f"📄 {m}.pdf - (Upload pending)")
    else:
        for pdf in pdf_files:
            with st.container(border=True):
                c1,c2 = st.columns([3,1])
                with c1: st.write(f"📄 **{pdf}**")
                with c2: 
                    with open(os.path.join(pdf_folder, pdf), "rb") as f:
                        st.download_button("View", f, file_name=pdf, key=pdf, use_container_width=True)
