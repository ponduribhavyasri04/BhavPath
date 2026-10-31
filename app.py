import streamlit as st
import pandas as pd
import io

# Safe imports - no crash
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    MATPLOT = True
except:
    MATPLOT = False

try:
    from sklearn.ensemble import RandomForestClassifier
    import numpy as np
    SKLEARN = True
except:
    SKLEARN = False

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = "QIS College"
    st.session_state.selected_skill = "C"
    st.session_state.topic = "Intro"
    st.session_state.pdata = None

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
.detail-box{position:relative;z-index:10;max-height:85vh;overflow-y:auto;padding:25px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.diagram-box{background:linear-gradient(135deg,#0d1a3a,#1a0a2a);border:2px solid #0d4aff;border-radius:15px;padding:15px;margin:10px 0;color:white;text-align:center}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_model():
    if not SKLEARN:
        return None
    np.random.seed(42)
    n = 300
    tenth = np.random.randint(60, 99, n)
    inter = np.random.randint(60, 98, n)
    btech = np.random.randint(55, 95, n)
    skill_cnt = np.random.randint(1, 7, n)
    placed = ((tenth+inter+btech)/3 + skill_cnt*5 > 75).astype(int)
    X = pd.DataFrame({"tenth": tenth, "inter": inter, "btech": btech, "skills": skill_cnt})
    y = placed
    m = RandomForestClassifier(n_estimators=100, random_state=42)
    m.fit(X, y)
    return m

model = get_model()

def get_diagram_html(skill, topic):
    html = f"""
    <div class="diagram-box">
        <h4 style="color:#fef08a;">{skill} - {topic} - Memory Layout</h4>
        <div style="display:flex;justify-content:center;gap:12px;margin-top:12px;flex-wrap:wrap;">
            <div style="border:2px solid #0d4aff;border-radius:10px;padding:12px 20px;background:#0d4aff33;"><div style="font-size:10px;color:#a78bfa;">1000</div><div style="font-weight:bold;">Val1</div></div>
            <div style="border:2px solid #ff006a;border-radius:10px;padding:12px 20px;background:#ff006a33;"><div style="font-size:10px;color:#a78bfa;">1004</div><div style="font-weight:bold;">Val2</div></div>
            <div style="border:2px solid #fef08a;border-radius:10px;padding:12px 20px;background:#fef08a33;"><div style="font-size:10px;color:#a78bfa;">1008</div><div style="font-weight:bold;">Val3</div></div>
            <div style="border:2px solid #00f5ff;border-radius:10px;padding:12px 20px;background:#00f5ff33;"><div style="font-size:10px;color:#a78bfa;">1012</div><div style="font-weight:bold;">Val4</div></div>
        </div>
        <div style="margin-top:10px;color:#ff006a;">pointer (ptr) - Contiguous Memory</div>
    </div>
    """
    return html

def get_content(skill, topic):
    return f"""
### {topic} in {skill} - Complete Tutorial

1. INTRODUCTION: {topic} is core concept in {skill}. Without this cannot crack TCS, Infosys, Amazon.

2. TYPES: Basic, Intermediate, Advanced O(n log n)

3. REAL EXAMPLE: Banking software uses {topic} for 1 lakh records. Without {topic} 1 hour, with {topic} 1 second.

4. CODE: Level1 var=10, Level2 if>5, Level3 for loop, Level4 Placement solve_{topic.lower()}, Level5 FAANG optimized

5. MISTAKES: Not init, = vs ==, memory leak, off-by-one

6. PLACEMENT: TCS 2-3 Qs, Infosys coding, Amazon DSA.

7. SUMMARY: Practice 1 hr theory + 2 hr coding.
"""

# ===== PAGES =====
if st.session_state.page == "welcome":
    st.markdown("<div class='center' style='padding-top:22vh'><h1 style='color:#c7f0ff;font-size:70px;font-weight:900;'>Welcome to BhavPath</h1><div class='glass' style='display:inline-block;margin-top:20px;padding:28px 50px;'><h2 style='margin:0;font-size:32px;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>What is Your Placement Story..??</h2></div></div>", unsafe_allow_html=True)
    _, c, _ = st.columns([1.4, 1, 1.4])
    with c:
        st.write("")
        st.write("")
        if st.button("Next", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

elif st.session_state.page == "login":
    st.markdown("<div class='center'><h1 style='color:white;'>Login to BhavPath</h1></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([1.2, 1, 1.2])
    with col:
        st.write("")
        email = st.text_input("Email")
        college = st.text_input("College Name")
        if st.button("Continue", use_container_width=True, type="primary"):
            if email and college:
                st.session_state.college = college
                st.session_state.page = "purpose"
                st.rerun()
        if st.button("Back"):
            st.session_state.page = "welcome"
            st.rerun()

elif st.session_state.page == "purpose":
    st.markdown("<div class='center'><h1 style='color:white;'>What is the purpose?</h1></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Placement Prediction", use_container_width=True):
                st.session_state.page = "placement_welcome"
                st.rerun()
            st.write("")
            if st.button("Test Zone", use_container_width=True):
                st.session_state.page = "coming_soon"
                st.rerun()
        with c2:
            if st.button("Technical Skills", use_container_width=True):
                st.session_state.page = "tech_welcome"
                st.rerun()
            st.write("")
            if st.button("Interview + Code", use_container_width=True):
                st.session_state.page = "interview_welcome"
                st.rerun()

elif st.session_state.page == "placement_welcome":
    st.markdown(f"<div class='center'><h1 style='color:white;'>Welcome to Placement Prediction</h1><p style='color:#a78bfa;'>{st.session_state.college}</p></div>", unsafe_allow_html=True)
    _, c, _ = st.columns([1.3, 1, 1.3])
    with c:
        st.write("")
        if st.button("Next - Enter Details", use_container_width=True, type="primary"):
            st.session_state.page = "placement_form"
            st.rerun()
        if st.button("Back"):
            st.session_state.page = "purpose"
            st.rerun()

elif st.session_state.page == "placement_form":
    st.markdown("<div class='center'><h1 style='color:white;'>Enter Your Details</h1></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.3, 1])
    with col:
        name = st.text_input("1. Name")
        tenth = st.number_input("2. 10th %", 0.0, 100.0, 85.0)
        inter = st.number_input("3. Inter %", 0.0, 100.0, 80.0)
        btech = st.number_input("4. B.Tech %", 0.0, 100.0, 75.0)
        skills = st.text_input("5. Skills", placeholder="Python, Java, SQL")
        if st.button("Predict", use_container_width=True, type="primary"):
            st.session_state.pdata = (name, tenth, inter, btech, skills)
            st.session_state.page = "placement_result"
            st.rerun()
        if st.button("Back"):
            st.session_state.page = "placement_welcome"
            st.rerun()

elif st.session_state.page == "placement_result":
    name, tenth, inter, btech, skills = st.session_state.pdata
    skill_cnt = len([s for s in skills.split(",") if s.strip()]) if skills else 1
    if SKLEARN and model is not None:
        X_new = pd.DataFrame({"tenth": [tenth], "inter": [inter], "btech": [btech], "skills": [skill_cnt]})
        prob = float(model.predict_proba(X_new)[0][1] * 100)
        pred = int(model.predict(X_new)[0])
    else:
        avg_tmp = (tenth + inter + btech) / 3
        prob = avg_tmp + skill_cnt * 3
        if prob > 100:
            prob = 92
        pred = 1 if prob > 70 else 0
    avg = (tenth + inter + btech) / 3
    st.markdown(f"<div class='center'><h1 style='color:white;'>Result for {name} - {prob:.1f}% Chance</h1></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([0.5, 2, 0.5])
    with col:
        color = "#00ff88" if pred == 1 else "#ff006a"
        status = "HIGH CHANCE - PLACED" if pred == 1 else "NEED IMPROVEMENT"
        st.markdown(f"<div class='glass'><h3 style='color:{color};'>{status}</h3><p style='color:white;'>Your Score: 10th {tenth}% | Inter {inter}% | BTech {btech}% | Skills {skill_cnt} | Avg {avg:.1f}%</p></div>", unsafe_allow_html=True)
        st.write("")
        if prob >= 80:
            comps = [["Google/Amazon", "Eligible"], ["TCS Digital", "Eligible"], ["Infosys SP", "Eligible"], ["Wipro Elite", "Eligible"]]
        elif prob >= 60:
            comps = [["TCS Digital", "Eligible"], ["Infosys", "Eligible"], ["Wipro", "Eligible"], ["Capgemini", "Eligible"]]
        else:
            comps = [["Wipro", "Try"], ["TCS NQT", "Practice Needed"], ["Improve Skills", "Need DSA"]]
        df = pd.DataFrame(comps, columns=["Company", "Status"])
        st.dataframe(df, use_container_width=True)
        st.bar_chart(pd.DataFrame({"Score": [tenth, inter, btech]}, index=["10th", "Inter", "BTech"]))
        st.progress(int(prob))
        st.write("")
        b1, b2 = st.columns(2)
        with b1:
            if st.button("Back", use_container_width=True):
                st.session_state.page = "placement_form"
                st.rerun()
        with b2:
            if st.button("Home", use_container_width=True):
                st.session_state.page = "purpose"
                st.rerun()

elif st.session_state.page == "tech_welcome":
    st.markdown("<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:50px;font-weight:900;'>BhavPath Technical Skills</h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - Pic Diagrams + Code Runner</p></div></div>", unsafe_allow_html=True)
    _, c, _ = st.columns([1.3, 1, 1.3])
    with c:
        st.write("")
        st.write("")
        if st.button("Explore Skills", use_container_width=True, type="primary"):
            st.session_state.page = "tech_skills"
            st.rerun()
        if st.button("Back"):
            st.session_state.page = "purpose"
            st.rerun()

elif st.session_state.page == "tech_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Your Skill</h1><p style='color:#a78bfa;'>48 Topics - Pic Diagrams + Run Code</p></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([0.3, 2, 0.3])
    with col:
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C", use_container_width=True):
                st.session_state.selected_skill = "C"
                st.session_state.topic = "Intro"
                st.session_state.page = "skill_detail"
                st.rerun()
        with r1_c2:
            if st.button("C++", use_container_width=True):
                st.session_state.selected_skill = "C++"
                st.session_state.topic = "Basics"
                st.session_state.page = "skill_detail"
                st.rerun()
        with r1_c3:
            if st.button("Java", use_container_width=True):
                st.session_state.selected_skill = "Java"
                st.session_state.topic = "Basics"
                st.session_state.page = "skill_detail"
                st.rerun()
        st.write("")
        r2_c1, r2_c2, r2_c3 = st.columns(3)
        with r2_c1:
            if st.button("Python", use_container_width=True):
                st.session_state.selected_skill = "Python"
                st.session_state.topic = "Basics"
                st.session_state.page = "skill_detail"
                st.rerun()
        with r2_c2:
            if st.button("SQL", use_container_width=True):
                st.session_state.selected_skill = "SQL"
                st.session_state.topic = "SELECT"
                st.session_state.page = "skill_detail"
                st.rerun()
        with r2_c3:
            if st.button("DSA", use_container_width=True):
                st.session_state.selected_skill = "DSA"
                st.session_state.topic = "Arrays"
                st.session_state.page = "skill_detail"
                st.rerun()
        st.write("")
        st.write("")
        if st.button("Back", use_container_width=True):
            st.session_state.page = "tech_welcome"
            st.rerun()

elif st.session_state.page == "skill_detail":
    skill = st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Detailed</h1></div>", unsafe_allow_html=True)
    all_topics = {
        "C": ["Intro", "Data Types", "Loops", "Functions", "Pointers", "Arrays", "Structures", "File Handling"],
        "C++": ["Basics", "OOP", "STL", "Pointers", "Inheritance", "Polymorphism", "Templates", "Projects"],
        "Java": ["Basics", "OOP", "Collections", "Exception", "Multithreading", "JDBC", "Spring", "Projects"],
        "Python": ["Basics", "Loops", "Functions", "OOP", "Libraries", "File Handling", "Django", "Projects"],
        "SQL": ["SELECT", "JOINS", "GROUP BY", "Subqueries", "Indexing", "Normalization", "Procedures", "Projects"],
        "DSA": ["Arrays", "Linked List", "Stack & Queue", "Trees", "Graphs", "Sorting", "DP", "Greedy"]
    }
    topics_list = all_topics.get(skill, all_topics["C"])
    _, c, _ = st.columns([0.1, 3, 0.1])
    with c:
        col1, col2 = st.columns([1, 2.5])
        with col1:
            st.markdown(f"<div class='glass'><h3 style='color:white;margin:0;'>{skill} Topics</h3></div>", unsafe_allow_html=True)
            st.write("")
            for i, t in enumerate(topics_list, 1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True, type="primary" if st.session_state.topic == t else "secondary"):
                    st.session_state.topic = t
                    st.rerun()
            st.write("")
            if st.button("Back"):
                st.session_state.page = "tech_skills"
                st.rerun()
        with col2:
            st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#fef08a;margin-top:0;'>{st.session_state.topic} in {skill}</h2>", unsafe_allow_html=True)
            st.markdown(get_diagram_html(skill, st.session_state.topic), unsafe_allow_html=True)
            st.write("")
            content = get_content(skill, st.session_state.topic)
            st.markdown(f"<div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div>", unsafe_allow_html=True)
            st.markdown("---", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:#00ff88;'>Try {skill} Code - Run Online</h3>", unsafe_allow_html=True)
            default_code = f"print('Hello {skill} - {st.session_state.topic}')\narr=[1,2,3]\nprint(arr)"
            code_input = st.text_area("Code Editor", value=default_code, height=120, key=f"code_{skill}_{st.session_state.topic}")
            if st.button("Run Code", key=f"run_{skill}_{st.session_state.topic}"):
                try:
                    import sys
                    from io import StringIO
                    old_stdout = sys.stdout
                    sys.stdout = mystdout = StringIO()
                    exec(code_input, {})
                    sys.stdout = old_stdout
                    output = mystdout.getvalue()
                    st.success(f"Output:\n{output}")
                except Exception as e:
                    st.error(f"Error: {e}")
            st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "interview_welcome":
    st.markdown("<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:50px;font-weight:900;'>BhavPath Interview Zone</h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>Crack TCS, Infosys, Amazon, Google</p></div></div>", unsafe_allow_html=True)
    _, c, _ = st.columns([1.3, 1, 1.3])
    with c:
        st.write("")
        st.write("")
        if st.button("Start Interview Prep", use_container_width=True, type="primary"):
            st.session_state.page = "interview_skills"
            st.rerun()
        if st.button("Back"):
            st.session_state.page = "purpose"
            st.rerun()

elif st.session_state.page == "interview_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([0.3, 2, 0.3])
    with col:
        st.write("")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("C Interview", use_container_width=True):
                st.session_state.selected_skill = "C"
                st.session_state.page = "interview_detail"
                st.rerun()
        with c2:
            if st.button("C++ Interview", use_container_width=True):
                st.session_state.selected_skill = "C++"
                st.session_state.page = "interview_detail"
                st.rerun()
        with c3:
            if st.button("Java Interview", use_container_width=True):
                st.session_state.selected_skill = "Java"
                st.session_state.page = "interview_detail"
                st.rerun()
        st.write("")
        c4, c5, c6 = st.columns(3)
        with c4:
            if st.button("Python Interview", use_container_width=True):
                st.session_state.selected_skill = "Python"
                st.session_state.page = "interview_detail"
                st.rerun()
        with c5:
            if st.button("SQL Interview", use_container_width=True):
                st.session_state.selected_skill = "SQL"
                st.session_state.page = "interview_detail"
                st.rerun()
        with c6:
            if st.button("DSA Interview", use_container_width=True):
                st.session_state.selected_skill = "DSA"
                st.session_state.page = "interview_detail"
                st.rerun()
        st.write("")
        st.write("")
        if st.button("Back"):
            st.session_state.page = "interview_welcome"
            st.rerun()

elif st.session_state.page == "interview_detail":
    skill = st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview</h1></div>", unsafe_allow_html=True)
    _, c, _ = st.columns([0.1, 3, 0.1])
    with c:
        st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
        st.markdown(get_diagram_html(skill, "Interview"), unsafe_allow_html=True)
        st.markdown(f"<h2 style='color:#fef08a;'>{skill} Interview - 15 Qs</h2><p style='color:white;'>Q1-Q15 detailed with diagrams, code, tips for TCS, Amazon</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("Back to Interview Skills"):
            st.session_state.page = "interview_skills"
            st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon</h1></div>", unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.page = "purpose"
        st.rerun()
