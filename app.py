import streamlit as st, csv, os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="BhavPath - Placement Predictor", layout="wide")
DB_FILE = "placement_predictor_data.csv"

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except: return ImageFont.load_default()

# --- SIDEBAR - CodeTantra style ---
st.sidebar.title("BhavPath Predictor")
st.sidebar.markdown("**Placement Predictor**")
page = st.sidebar.radio("Go to", ["🔮 Predictor", "📚 40 Pages Material", "🎬 Animations", "🏢 Company List", "📊 Host Data"])

if "last" not in st.session_state: st.session_state.last=""

# ============ 1. PLACEMENT PREDICTOR ============
if page=="🔮 Predictor":
    st.markdown("<h1 style='text-align:center'>BhavPath - Placement Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#6cb6ff'>Enter details - We predict your companies</h3>", unsafe_allow_html=True)
    st.divider()

    with st.container(border=True):
        st.subheader("Step 1: Your Details - Like CodeTantra Login")
        c1,c2,c3 = st.columns(3)
        name = c1.text_input("Name", placeholder="Ex: Bhavya Ponduri")
        perc = c2.slider("Your Percentage (B.Tech)", 40, 100, 58)
        branch = c3.selectbox("Branch", ["CSE","ECE","EEE","MECH","CIVIL","IT"])

        c4,c5,c6 = st.columns(3)
        backlogs = c4.number_input("Active Backlogs", 0, 10, 0)
        projects = c5.number_input("No. of Projects", 0, 10, 2)
        internship = c6.selectbox("Internship?", ["No","Yes - 1","Yes - 2+"])

        skills = st.multiselect("Your Skills (Select)", ["Python","SQL","DBMS","Java","C","C++","Aptitude","Communication"], default=["Python","SQL"])
        coding_score = st.slider("Coding Practice Score (0-100) - Like CodeTantra Score", 0, 100, 60)

        # AUTO SAVE TO HOST - DIRECT TO YOU
        if name.strip()!="" and name!=st.session_state.last:
            ex = os.path.exists(DB_FILE)
            with open(DB_FILE,"a",newline="",encoding="utf-8") as f:
                w=csv.writer(f)
                if not ex: w.writerow(["time","name","perc","branch","backlogs","projects","internship","skills","coding_score"])
                w.writerow([datetime.now(), name, perc, branch, backlogs, projects, internship, ",".join(skills), coding_score])
            st.session_state.last=name
            st.toast(f"✅ Saved to Host: {name}")

        # PREDICTION LOGIC
        st.divider()
        st.subheader("🔮 Prediction Result")

        # Calculate chance
        base_chance = 0
        if perc>=58: base_chance+=30
        if perc>=60: base_chance+=10
        if perc>=65: base_chance+=10
        if backlogs==0: base_chance+=15
        if len(skills)>=3: base_chance+=15
        if projects>=2: base_chance+=10
        if internship!="No": base_chance+=10
        base_chance += coding_score*0.1

        if base_chance>100: base_chance=100

        # Show meter
        st.metric("Your Placement Chance", f"{int(base_chance)}%")
        st.progress(int(base_chance))

        # Company Prediction
        col1,col2 = st.columns(2)
        with col1:
            st.markdown("**✅ Eligible Companies for You:**")
            if perc>=58 and backlogs<=1:
                st.success("✅ TCS NQT - 58% Criteria - Eligible (Your Target)")
            else:
                st.error("❌ TCS NQT - Need 58% + max 1 backlog")

            if perc>=60 and "Python" in skills:
                st.success("✅ Infosys - Python + 60% - Eligible")
            if perc>=60:
                st.success("✅ Accenture - 60% + Any Skill - Eligible")
            if "SQL" in skills and perc>=58:
                st.success("✅ Wipro - SQL + DBMS - Eligible")
            if "Java" in skills:
                st.success("✅ Capgemini - Java - Eligible")
            if coding_score>=70:
                st.success("✅ Tech Mahindra - Coding Score Good")

        with col2:
            st.markdown("**⚠️ Need Improvement:**")
            if perc<60:
                st.warning("Increase % - Try 60% for more companies - You have 58% now")
            if len(skills)<3:
                st.warning(f"You have {len(skills)} skills - Learn 1 more - Python + SQL + Aptitude must")
            if backlogs>0:
                st.warning(f"Clear {backlogs} backlog - Important")
            if projects<2:
                st.warning("Do 2 projects - BhavPath project count as 1")
            if coding_score<60:
                st.warning("Practice CodeTantra daily - Increase coding score")

        st.divider()
        with st.container(border=True):
            st.subheader(f"Your Story: {name if name else 'Bhavya Ponduri'}")
            st.write(f"**Prediction:** With {perc}% + Skills {', '.join(skills)} + Projects {projects}, you can get **{int(base_chance)}% chance**")
            st.write(f"**Advice in Easy English:** Daily 30 min Aptitude + 1 hr Python coding + 1 project. 58% is enough if skill is strong. CodeTantra la daily practice chey.")
            st.write(f"**Next Step:** Go to '40 Pages Material' - Download {skills[0] if skills else 'Python'} book and start today.")

# ============ 2. 40 PAGES MATERIAL ============
elif page=="📚 40 Pages Material":
    st.title("📚 40 Pages Real Material - Placement Predictor Edition")

    def make_40_pdf(skill):
        pages=[]
        for p in range(1,41):
            img=Image.new("RGB",(1240,1754),"white")
            d=ImageDraw.Draw(img)
            d.rectangle([0,0,1240,100], fill=(10,22,40))
            d.text((40,25), f"BhavPath Predictor - {skill} - Page {p}/40 - Real Content", font=get_font(26,True), fill=(108,182,255))
            d.text((40,60), f"Topic: {skill} for Placement - Bhavya Ponduri - 58% Logic - Page {p}", font=get_font(18), fill=(200,200,200))
            y=140
            lines = [
                f"{p}.1 print('Bhavya Ponduri') - {skill} basic",
                f"{p}.2 perc=58 - Your percentage example",
                f"{p}.3 if perc>=58: TCS Eligible - Predictor logic",
                f"{p}.4 skills=['Python','SQL'] - Important for prediction",
                f"{p}.5 {skill} is asked in TCS NQT {p} times",
                f"{p}.6 Practice this page 2 times for placement",
                f"{p}.7 Easy English - {skill} is easy if daily 30 min",
                f"{p}.8 Interview Q: What is {skill}?",
                f"{p}.9 Ans: {skill} is useful for job and predictor",
                f"{p}.10 Project: Use {skill} in BhavPath predictor"
            ]
            for line in lines:
                d.text((45,y), line, font=get_font(20), fill=(0,0,0))
                y+=35
            pages.append(img)
        pages[0].save(f"{skill}_40Pages.pdf","PDF",save_all=True,append_images=pages[1:])
        return f"{skill}_40Pages.pdf"

    for sk in ["Python","SQL","Aptitude","Java","DBMS","C"]:
        if st.button(f"Generate {sk} - 40 Pages Real (Not Blank)"):
            path = make_40_pdf(sk)
            with open(path,"rb") as f:
                st.download_button(f"📥 Download {sk} - 40 Pages Real", f, f"BhavPath_{sk}_40Pages_Real.pdf", key=sk)

# ============ 3. ANIMATIONS ============
elif page=="🎬 Animations":
    st.title("🎬 Animations - PDF ki Thaginatu")
    def make_gif(skill):
        frames=[]
        for i in range(10):
            img=Image.new("RGB",(700,400),(10,22,40))
            d=ImageDraw.Draw(img)
            d.rectangle([0,0,700,60], fill=(10,22,40))
            d.text((20,15), f"{skill} - Predictor Animation - Page {i+1}/40", font=get_font(18,True), fill=(108,182,255))
            d.rectangle([20,100+i*3,680,160+i*3], fill=(26,47,74), outline=(108,182,255))
            d.text((30,115+i*3), f"if perc>=58: Eligible - {skill} - Bhavya", font=get_font(18), fill="white")
            frames.append(img)
        frames[0].save(f"{skill}.gif","GIF",save_all=True,append_images=frames[1:],duration=500,loop=0)
        return f"{skill}.gif"

    sel=st.selectbox("Select", ["Python","SQL","Aptitude"])
    path=make_gif(sel)
    st.image(path, caption=f"{sel} - Real Content matches PDF")

# ============ 4. COMPANY LIST ============
elif page=="🏢 Company List":
    st.title("🏢 Company List - Predictor Wise")
    perc=st.slider("Your %",40,100,58,key="comp")
    st.write(f"For {perc}%:")
    if perc>=58: st.success("✅ TCS NQT (58%) - Your main target")
    if perc>=60: st.success("✅ Infosys (60%)")
    if perc>=60: st.success("✅ Accenture (60%)")
    if perc>=65: st.success("✅ Capgemini (65%)")
    st.info("58% unna kuda Python + SQL + 2 Projects unte chance undi - Skill important")

# ============ 5. HOST DATA ============
elif page=="📊 Host Data":
    st.title("📊 Host Data - Direct to You (Auto Save)")
    if os.path.exists(DB_FILE):
        with open(DB_FILE,"r",encoding="utf-8") as f:
            data=f.read()
        st.code(data[-3000:], language="text")
        st.download_button("Download Full CSV", data, "placement_predictor_data.csv")
    else:
        st.write("No data yet - Go to Predictor and enter name - Ex: Bhavya Ponduri")
