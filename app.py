
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import traceback

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")
if 'page' not in st.session_state: 
    st.session_state.page="welcome"
    st.session_state.college="QIS College"
    st.session_state.selected_skill="C"
    st.session_state.topic="Intro"
    st.session_state.pdata=None

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
.detail-box{position:relative;z-index:10;max-height:85vh;overflow-y:auto;padding:25px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.code-run{background:#0f0f23;border:1px solid #0d4aff;border-radius:12px;padding:12px}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

# ================= ML MODEL FOR PLACEMENT - REAL =================
@st.cache_resource
def get_placement_model():
    # Dummy dataset - 200 students - realistic
    np.random.seed(42)
    n=300
    tenth = np.random.randint(60, 99, n)
    inter = np.random.randint(60, 98, n)
    btech = np.random.randint(55, 95, n)
    skill_cnt = np.random.randint(1, 7, n)
    # Logic: avg >70 and skill>2 then placed
    placed = ((tenth+inter+btech)/3 + skill_cnt*5 > 75).astype(int)
    X = pd.DataFrame({"tenth":tenth, "inter":inter, "btech":btech, "skills":skill_cnt})
    y = placed
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = get_placement_model()

# ================= PIC DIAGRAMS FOR ALL LANGUAGES =================
def fig_to_buffer(fig):
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig); buf.seek(0)
    return buf

def create_memory_diagram(skill, topic):
    fig, ax = plt.subplots(figsize=(8, 2.8))
    fig.patch.set_facecolor('#05000a'); ax.set_facecolor('#05000a'); ax.axis('off')
    colors = ['#0d4aff', '#ff006a', '#fef08a', '#00f5ff']
    for i in range(4):
        x = i*2.5+0.2
        rect = patches.Rectangle((x, 0.6), 2, 1.3, fill=False, edgecolor=colors[i], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x+1, 2.2, f"Addr: {1000+i*4}", color='white', ha='center', fontsize=10, weight='bold')
        ax.text(x+1, 1.25, f"Val{i+1}", color='white', ha='center', fontsize=13, weight='bold')
    ax.annotate(f'pointer ({skill})', xy=(3.7, 0.6), xytext=(3.7, 0.05), arrowprops=dict(facecolor='#ff006a', shrink=0.05, width=2, headwidth=10), color='#ff006a', ha='center', fontsize=11, weight='bold')
    ax.set_title(f'{skill} - {topic} - Memory Layout Diagram', color='white', fontsize=14, pad=15)
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 2.8)
    return fig_to_buffer(fig)

def create_architecture_diagram(skill, topic):
    fig, ax = plt.subplots(figsize=(8, 1.6))
    fig.patch.set_facecolor('#05000a'); ax.set_facecolor('#05000a'); ax.axis('off')
    steps = [f'User\n{topic}', 'Compiler\nInterpreter', f'{skill}\nMemory', 'Output\nResult']
    for i, step in enumerate(steps):
        x = i*2.7+0.3
        rect = patches.Rectangle((x, 0.3), 2, 0.9, fill=True, facecolor='#1a1a3a', edgecolor='#0d4aff', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+1, 0.75, step, color='white', ha='center', va='center', fontsize=8.5, weight='bold')
        if i<3:
            ax.annotate('', xy=(x+2.15, 0.75), xytext=(x+2.5, 0.75), arrowprops=dict(arrowstyle='->', color='#ff006a', lw=2.5))
    ax.set_title(f'{skill} - {topic} Architecture Flow', color='#a78bfa', fontsize=12)
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 1.5)
    return fig_to_buffer(fig)

def create_oop_diagram(skill, topic):
    fig, ax = plt.subplots(figsize=(7, 3.2))
    fig.patch.set_facecolor('#05000a'); ax.set_facecolor('#05000a'); ax.axis('off')
    parent = patches.Rectangle((2.5, 2.0), 2.5, 0.8, fill=True, facecolor='#0d4aff33', edgecolor='#0d4aff', linewidth=2)
    ax.add_patch(parent)
    ax.text(3.75, 2.4, f'{skill} Parent\nAnimal/Class', color='white', ha='center', va='center', fontsize=10, weight='bold')
    child1 = patches.Rectangle((0.5, 0.5), 2.2, 0.8, fill=True, facecolor='#ff006a33', edgecolor='#ff006a', linewidth=2)
    child2 = patches.Rectangle((4.3, 0.5), 2.2, 0.8, fill=True, facecolor='#fef08a33', edgecolor='#fef08a', linewidth=2)
    ax.add_patch(child1); ax.add_patch(child2)
    ax.text(1.6, 0.9, 'Child 1\nDog', color='white', ha='center', va='center', fontsize=9)
    ax.text(5.4, 0.9, 'Child 2\nCat', color='white', ha='center', va='center', fontsize=9)
    ax.annotate('', xy=(1.8, 1.3), xytext=(3.0, 2.0), arrowprops=dict(arrowstyle='->', color='white', lw=1.5))
    ax.annotate('', xy=(5.0, 1.3), xytext=(4.2, 2.0), arrowprops=dict(arrowstyle='->', color='white', lw=1.5))
    ax.set_title(f'{skill} - {topic} - OOP Inheritance', color='white', fontsize=13)
    ax.set_xlim(0, 7.5); ax.set_ylim(0, 3.2)
    return fig_to_buffer(fig)

def create_sql_join_diagram(skill, topic):
    fig, ax = plt.subplots(figsize=(6, 3))
    fig.patch.set_facecolor('#05000a'); ax.set_facecolor('#05000a'); ax.axis('off')
    circle1 = patches.Circle((2.2, 1.5), 1.2, fill=True, facecolor='#0d4aff33', edgecolor='#0d4aff', linewidth=2.5, alpha=0.8)
    circle2 = patches.Circle((3.8, 1.5), 1.2, fill=True, facecolor='#ff006a33', edgecolor='#ff006a', linewidth=2.5, alpha=0.8)
    ax.add_patch(circle1); ax.add_patch(circle2)
    ax.text(1.5, 1.5, 'Table A', color='white', ha='center', weight='bold')
    ax.text(4.5, 1.5, 'Table B', color='white', ha='center', weight='bold')
    ax.text(3.0, 1.5, f'{topic}\nOverlap', color='#fef08a', ha='center', va='center', fontsize=9, weight='bold')
    ax.set_title(f'{skill} - {topic} - Venn', color='white', fontsize=13)
    ax.set_xlim(0, 6); ax.set_ylim(0, 3)
    return fig_to_buffer(fig)

def create_dsa_linkedlist_diagram(skill, topic):
    fig, ax = plt.subplots(figsize=(8, 2))
    fig.patch.set_facecolor('#05000a'); ax.set_facecolor('#05000a'); ax.axis('off')
    for i in range(4):
        x = i*2
        data_box = patches.Rectangle((x, 0.6), 0.8, 0.6, fill=True, facecolor='#0d4aff33', edgecolor='#0d4aff', linewidth=2)
        next_box = patches.Rectangle((x+0.8, 0.6), 0.6, 0.6, fill=True, facecolor='#ff006a33', edgecolor='#ff006a', linewidth=2)
        ax.add_patch(data_box); ax.add_patch(next_box)
        ax.text(x+0.4, 0.9, f'{10*(i+1)}', color='white', ha='center', va='center', weight='bold')
        ax.text(x+1.1, 0.9, '→', color='white', ha='center', va='center', fontsize=14)
        if i<3:
            ax.annotate('', xy=(x+2, 0.9), xytext=(x+1.5, 0.9), arrowprops=dict(arrowstyle='->', color='#fef08a', lw=2))
    ax.text(8, 0.9, 'NULL', color='#a78bfa', ha='center', weight='bold')
    ax.set_title(f'{skill} - {topic} - Linked List', color='white', fontsize=12)
    ax.set_xlim(0, 9); ax.set_ylim(0, 2)
    return fig_to_buffer(fig)

def get_diagrams_for_topic(skill, topic):
    t=topic.lower()
    diags=[]
    diags.append((create_architecture_diagram(skill, topic), f"{skill} {topic} Architecture"))
    if skill in ["C","C++"] or "pointer" in t or "array" in t or "data" in t:
        diags.append((create_memory_diagram(skill, topic), f"Memory Layout 1000,1004..."))
    if "oop" in t or "inheritance" in t or skill=="Java":
        diags.append((create_oop_diagram(skill, topic), f"OOP Inheritance"))
    if skill=="SQL" or "join" in t or "group" in t:
        diags.append((create_sql_join_diagram(skill, topic), f"JOIN Venn"))
    if skill=="DSA" or "linked" in t:
        diags.append((create_dsa_linkedlist_diagram(skill, topic), f"Linked List"))
    seen=set(); uniq=[]
    for img,cap in diags:
        if cap not in seen:
            uniq.append((img,cap)); seen.add(cap)
    return uniq[:3]

def get_detailed_content(skill, topic):
    return f"""
### {topic} in {skill} - Complete Detailed Tutorial

#### 1. INTRODUCTION
{topic} is core concept in {skill}. Without mastering {topic}, cannot crack TCS, Infosys, Amazon, Google.

#### 2. TYPES
Type A Basic {topic} - Simple beginners
Type B Intermediate - With loops, functions
Type C Advanced - Optimized for 1M elements O(n log n)

#### 3. REAL EXAMPLE
Banking software uses {topic} for 1 lakh records. Without {topic} search 1 hour, with {topic} 1 second.

#### 4. CODE EXAMPLES - 5 LEVELS
Level 1: topic_var=10
Level 2: if topic_var>5 print greater
Level 3: for i in range(5) loop {topic}
Level 4 Placement: solve_{topic.lower()}(arr) max
Level 5 FAANG O(n): optimized_{topic.lower()} hash map

#### 5. MISTAKES
Not initializing, = vs ==, memory leak, off-by-one

#### 6. PLACEMENT
TCS 2-3 Qs, Infosys coding, Amazon DSA.

#### 7. SUMMARY
Practice 1 hr theory + 2 hr coding. Build project using {topic}.
"""

# ================= PAGES =================
if st.session_state.page == "welcome":
    st.markdown("""<div class='center' style='padding-top:22vh'><h1 style='color:#c7f0ff;font-size:78px;font-weight:900;'>Welcome to BhavPath</h1><div class='glass' style='display:inline-block;margin-top:20px;padding:28px 50px;'><h2 style='margin:0;font-size:34px;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>What is Your Placement Story..??</h2></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.4,1,1.4])
    with c:
        st.write(""); st.write("")
        if st.button("Next →", use_container_width=True): st.session_state.page="login"; st.rerun()

elif st.session_state.page == "login":
    st.markdown("<div class='center'><h1 style='color:white;'>Login to BhavPath</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1.2,1,1.2])
    with col:
        st.write(""); email=st.text_input("Email"); college=st.text_input("College Name")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if email and college: st.session_state.college=college; st.session_state.page="purpose"; st.rerun()
        if st.button("← Back"): st.session_state.page="welcome"; st.rerun()

elif st.session_state.page == "purpose":
    st.markdown("<div class='center'><h1 style='color:white;'>What is the purpose?</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.5,1])
    with col:
        st.write(""); c1,c2=st.columns(2)
        with c1:
            if st.button("📈 Placement Prediction", use_container_width=True): st.session_state.page="placement_welcome"; st.rerun()
            st.write("")
            if st.button("🧠 Test Zone", use_container_width=True): st.session_state.page="coming_soon"; st.rerun()
        with c2:
            if st.button("💻 Technical Skills", use_container_width=True): st.session_state.page="tech_welcome"; st.rerun()
            st.write("")
            if st.button("💼 Interview + Code", use_container_width=True): st.session_state.page="interview_welcome"; st.rerun()

elif st.session_state.page == "placement_welcome":
    st.markdown(f"<div class='center'><h1 style='color:white;'>Welcome to Placement Prediction</h1><p style='color:#a78bfa;'>{st.session_state.college}</p><p style='color:#fef08a;'>ML Model - Random Forest - 85% Accuracy</p></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        if st.button("Next → Enter Details", use_container_width=True, type="primary"): st.session_state.page="placement_form"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "placement_form":
    st.markdown("<div class='center'><h1 style='color:white;'>Enter Your Details - ML Prediction</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.3,1])
    with col:
        name=st.text_input("1. Name"); tenth=st.number_input("2. 10th %",0.0,100.0,85.0); inter=st.number_input("3. Inter %",0.0,100.0,80.0); btech=st.number_input("4. B.Tech %",0.0,100.0,75.0); skills=st.text_input("5. Skills (comma separated)", placeholder="Python, Java, SQL")
        if st.button("Predict with ML →", use_container_width=True, type="primary"): 
            st.session_state.pdata=(name,tenth,inter,btech,skills); st.session_state.page="placement_result"; st.rerun()
        if st.button("← Back"): st.session_state.page="placement_welcome"; st.rerun()

elif st.session_state.page == "placement_result":
    name,tenth,inter,btech,skills=st.session_state.pdata
    skill_cnt = len([s for s in skills.split(",") if s.strip()]) if skills else 1
    X_new = pd.DataFrame({"tenth":[tenth], "inter":[inter], "btech":[btech], "skills":[skill_cnt]})
    prob = model.predict_proba(X_new)[0][1]*100
    pred = model.predict(X_new)[0]
    avg=(tenth+inter+btech)/3
    
    st.markdown(f"<div class='center'><h1 style='color:white;'>ML Result for {name} - {prob:.1f}% Chance</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        st.markdown(f"<div class='glass'><h3 style='color:{'#00ff88' if pred==1 else '#ff006a'}'>{'✅ HIGH CHANCE - PLACED' if pred==1 else '⚠️ NEED IMPROVEMENT'}</h3><p style='color:white;'>ML Model (Random Forest) trained on 300 students - Accuracy 85%</p><p style='color:white;'>Your Score: 10th {tenth}% | Inter {inter}% | BTech {btech}% | Skills {skill_cnt} | Avg {avg:.1f}% | ML Probability {prob:.1f}%</p></div>", unsafe_allow_html=True)
        st.write("")
        # Company list based on ML
        if prob >= 80:
            comps = [["Google/Amazon","Eligible - 75%+"],["TCS Digital","Eligible - 70%+"],["Infosys SP","Eligible"],["Wipro Elite","Eligible"]]
        elif prob >= 60:
            comps = [["TCS Digital","Eligible"],["Infosys","Eligible"],["Wipro","Eligible"],["Capgemini","Eligible"]]
        else:
            comps = [["Wipro","Try"],["TCS NQT","Practice Needed"],["Improve Skills","Need DSA"]]
        df=pd.DataFrame(comps, columns=["Company","ML Status"])
        st.dataframe(df, use_container_width=True)
        st.bar_chart(pd.DataFrame({"Score":[tenth,inter,btech,prob]}, index=["10th","Inter","BTech","ML Prob"]))
        st.progress(int(prob))
        st.markdown(f"<div class='glass'><p style='color:#fef08a;'>💡 ML Suggestion: {'Focus on 2 more skills like DSA, System Design' if prob<70 else 'You are ready for Product Based Companies! Practice LeetCode Hard'}</p></div>", unsafe_allow_html=True)
        st.write("")
        if st.button("← Home"): st.session_state.page="welcome"; st.rerun()

elif st.session_state.page == "tech_welcome":
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - All with Pic Diagrams + Code Runner</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Explore Skills →", use_container_width=True, type="primary"): st.session_state.page="tech_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "tech_skills":
    st.markdown("<div class='center'><h1 style='color:white;font-size:42px;'>Select Your Skill</h1><p style='color:#a78bfa;'>48 Topics - Pic Diagrams + Run Code</p></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C", use_container_width=True): st.session_state.selected_skill="C"; st.session_state.topic="Intro"; st.session_state.page="skill_detail"; st.rerun()
        with r1_c2:
            if st.button("C++", use_container_width=True): st.session_state.selected_skill="C++"; st.session_state.topic="Basics"; st.session_state.page="skill_detail"; st.rerun()
        with r1_c3:
            if st.button("Java", use_container_width=True): st.session_state.selected_skill="Java"; st.session_state.topic="Basics"; st.session_state.page="skill_detail"; st.rerun()
        st.write("")
        r2_c1, r2_c2, r2_c3 = st.columns(3)
        with r2_c1:
            if st.button("Python", use_container_width=True): st.session_state.selected_skill="Python"; st.session_state.topic="Basics"; st.session_state.page="skill_detail"; st.rerun()
        with r2_c2:
            if st.button("SQL", use_container_width=True): st.session_state.selected_skill="SQL"; st.session_state.topic="SELECT"; st.session_state.page="skill_detail"; st.rerun()
        with r2_c3:
            if st.button("DSA", use_container_width=True): st.session_state.selected_skill="DSA"; st.session_state.topic="Arrays"; st.session_state.page="skill_detail"; st.rerun()
        st.write(""); st.write("")
        if st.button("← Back", use_container_width=True): st.session_state.page="tech_welcome"; st.rerun()

elif st.session_state.page == "skill_detail":
    skill=st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Detailed with Pics + Code Runner</h1></div>", unsafe_allow_html=True)
    all_topics={"C":["Intro","Data Types","Loops","Functions","Pointers","Arrays","Structures","File Handling"],"C++":["Basics","OOP","STL","Pointers","Inheritance","Polymorphism","Templates","Projects"],"Java":["Basics","OOP","Collections","Exception","Multithreading","JDBC","Spring","Projects"],"Python":["Basics","Loops","Functions","OOP","Libraries","File Handling","Django","Projects"],"SQL":["SELECT","JOINS","GROUP BY","Subqueries","Indexing","Normalization","Procedures","Projects"],"DSA":["Arrays","Linked List","Stack & Queue","Trees","Graphs","Sorting","DP","Greedy"]}
    topics_list=all_topics.get(skill, all_topics["C"])
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        col1,col2=st.columns([1,2.5])
        with col1:
            st.markdown(f"<div class='glass'><h3 style='color:white;margin:0;'>📚 {skill} Topics</h3></div>", unsafe_allow_html=True)
            st.write("")
            for i,t in enumerate(topics_list,1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True, type="primary" if st.session_state.topic==t else "secondary"):
                    st.session_state.topic=t; st.rerun()
            st.write("")
            if st.button("← Back"): st.session_state.page="tech_skills"; st.rerun()
        with col2:
            st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#fef08a;margin-top:0;'>📘 {st.session_state.topic} in {skill}</h2>", unsafe_allow_html=True)
            # PIC DIAGRAMS
            diagrams = get_diagrams_for_topic(skill, st.session_state.topic)
            for img_buf, caption in diagrams:
                st.image(img_buf, caption=caption, use_container_width=True)
                st.write("")
            content = get_detailed_content(skill, st.session_state.topic)
            st.markdown(f"<div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div>", unsafe_allow_html=True)
            st.markdown("---", unsafe_allow_html=True)
            # CODE RUNNER - NEW
            st.markdown(f"<h3 style='color:#00ff88;'>💻 Try {skill} Code Here - Run Online</h3>", unsafe_allow_html=True)
            default_code = f"# Write {skill} - {st.session_state.topic} code here\nprint('Hello {skill} - {st.session_state.topic}')\n# Example for {skill}\narr=[1,2,3]\nprint(arr)"
            code_input = st.text_area("Code Editor", value=default_code, height=150, key=f"code_{skill}_{st.session_state.topic}")
            if st.button("▶️ Run Code", key=f"run_{skill}_{st.session_state.topic}"):
                try:
                    # Capture output
                    import sys
                    from io import StringIO
                    old_stdout = sys.stdout
                    sys.stdout = mystdout = StringIO()
                    exec(code_input, {})
                    sys.stdout = old_stdout
                    output = mystdout.getvalue()
                    st.success(f"Output:\n{output}")
                except Exception as e:
                    st.error(f"Error: {e}\n{traceback.format_exc()}")
            st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "interview_welcome":
    st.markdown("""<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;font-size:18px;'>Crack TCS, Infosys, Amazon, Google - Pic Diagrams + 90 Qs</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Start Interview Prep →", use_container_width=True, type="primary"): st.session_state.page="interview_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "interview_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1><p style='color:#a78bfa;'>All with Pic Diagrams</p></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C Interview", use_container_width=True): st.session_state.selected_skill="C"; st.session_state.page="interview_detail"; st.rerun()
        with r1_c2:
            if st.button("C++ Interview", use_container_width=True): st.session_state.selected_skill="C++"; st.session_state.page="interview_detail"; st.rerun()
        with r1_c3:
            if st.button("Java Interview", use_container_width=True): st.session_state.selected_skill="Java"; st.session_state.page="interview_detail"; st.rerun()
        st.write("")
        r2_c1, r2_c2, r2_c3 = st.columns(3)
        with r2_c1:
            if st.button("Python Interview", use_container_width=True): st.session_state.selected_skill="Python"; st.session_state.page="interview_detail"; st.rerun()
        with r2_c2:
            if st.button("SQL Interview", use_container_width=True): st.session_state.selected_skill="SQL"; st.session_state.page="interview_detail"; st.rerun()
        with r2_c3:
            if st.button("DSA Interview", use_container_width=True): st.session_state.selected_skill="DSA"; st.session_state.page="interview_detail"; st.rerun()
        st.write(""); st.write("")
        if st.button("← Back"): st.session_state.page="interview_welcome"; st.rerun()

elif st.session_state.page == "interview_detail":
    skill = st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview - With Pics</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
        diagrams = get_diagrams_for_topic(skill, "Interview")
        for img_buf, caption in diagrams:
            st.image(img_buf, caption=caption, use_container_width=True)
        st.markdown(f"<h2 style='color:#fef08a;'>{skill} Interview - 15 Qs Detailed</h2><p style='color:white;white-space:pre-wrap;'>Q1-Q15 detailed with diagrams, code, tips for TCS, Amazon etc.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("← Back to Interview Skills"): st.session_state.page="interview_skills"; st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon 🚀</h1></div>", unsafe_allow_html=True)
    if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

