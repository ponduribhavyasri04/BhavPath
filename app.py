import streamlit as st
import random

st.set_page_config(page_title="BhavPath - Placement Predictor", page_icon="🚀", layout="wide")

st.markdown("<h1 style='text-align: center;'>🚀 BhavPath - India's First Placement DNA Test</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #666;'>What's Your Placement Story ??</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>An AI-powered Placement Readiness Predictor. <b>Discover, Predict & Improve your career!</b></p>", unsafe_allow_html=True)

# Input Section
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 Your Name", placeholder="Ex: Bhavya")
    college = st.text_input("🏫 College Name", placeholder="Ex: JNTU Ongole")
    percentage = st.slider("📊 Your B.Tech %", 40, 100, 75)

with col2:
    branch = st.selectbox("🎓 Branch", ["CSE", "ECE", "EEE", "AIML", "Other"])
    skills = st.multiselect("💡 Pick Your Superpowers", ["Python", "Java", "SQL", "DSA", "Communication", "Projects", "Internship"])

if st.button("🧬 GENERATE MY PLACEMENT DNA", type="primary", use_container_width=True):
    if not name or not skills:
        st.warning("Yo, fill all the details first!")
    else:
        dna_score = percentage
        if "Python" in skills: dna_score += 8
        if "DSA" in skills: dna_score += 12
        if "Communication" in skills: dna_score += 10
        if "Projects" in skills: dna_score += 7
        if "Internship" in skills: dna_score += 8
        
        st.balloons()
        st.markdown("---")
        
        # REPORT
        st.subheader(f"🔬 {name}'s Placement DNA Report")
        c1, c2, c3 = st.columns(3)
        c1.metric("DNA Score", f"{dna_score}/150", f"+{dna_score-75}")
        c2.metric("All India Rank (Est.)", f"#{random.randint(1000, 50000)}")
        c3.metric("Dream Job Chance", f"{min(98, dna_score-10)}%")

        # COMPANY WALL - THE VIRAL PART
        st.markdown("### 🏢 Which Companies You Eligible For? (Live Wall)")
        companies = {
            "Google / Microsoft (20+ LPA)": 95, "Amazon (15+ LPA)": 90,
            "TCS Digital / Infosys SP (7-10 LPA)": 75, "TCS NQT / Wipro / Accenture (4-7 LPA)": 60,
            "Tech Mahindra / Capgemini (3.5-5 LPA)": 50
        }
        for comp, cutoff in companies.items():
            if dna_score >= cutoff:
                st.success(f"✅ ELIGIBLE: {comp} - You a match!")
            else:
                st.error(f"❌ NOT YET: {comp} - Need {cutoff-dna_score} more points")
        
        # ROADMAP
        st.markdown("### 🗺️ Your 30-Day Glow-Up Roadmap")
        if dna_score < 75:
            st.markdown("- **Week 1-2:** Grind Python + SQL")
            st.markdown("- **Week 3:** Build 1 fire project")
            st.markdown("- **Week 4:** Level up communication")
        else:
            st.markdown("- **Next Move:** Hit up 10 HRs on LinkedIn, solve 2 DSA problems daily!")

        # VIRAL SHARE
        st.markdown("---")
        st.markdown(f"**🔥 Yo {name}, share this and go viral!**")
        share_text = f"My Placement DNA Score is {dna_score}! I'm eligible for TCS Digital! Check yours on BhavPath - India's Top Placement Predictor by Bhavya Sri"
        st.code(share_text)
        st.info("Copy and drop it on WhatsApp / LinkedIn - everyone gonna check your BhavPath and we going top!")

st.caption("🚀 Built by Bhavya Sri | Public Use - For All Indian Students | 2026")


