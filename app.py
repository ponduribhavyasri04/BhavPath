import streamlit as st
import pandas as pd

try:
    from sklearn.ensemble import RandomForestClassifier
    import numpy as np
    SK = True
except:
    SK = False

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
    st.session_state.college = 'QIS College'
    st.session_state.skill = 'C'
    st.session_state.topic = 'Intro'
    st.session_state.pdata = None

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
.detail-box{position:relative;z-index:10;max-height:85vh;overflow-y:auto;padding:25px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.diag{background:linear-gradient(135deg,#0d1a3a,#1a0a2a);border:2px solid #0d4aff;border-radius:15px;padding:15px;margin:10px 0;color:white;text-align:center}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

@st.cache_resource
def get_model():
    if not SK:
        return None
    np.random.seed(42)
    n=300
    tenth=np.random.randint(60,99,n)
    inter=np.random.randint(60,98,n)
    btech=np.random.randint(55,95,n)
    sc=np.random.randint(1,7,n)
    placed=((tenth+inter+btech)/3+sc*5>75).astype(int)
    X=pd.DataFrame({'tenth':tenth,'inter':inter,'btech':btech,'skills':sc})
    y=placed
    m=RandomForestClassifier(n_estimators=100,random_state=42)
    m.fit(X,y)
    return m

model=get_model()

def diag_html(s,t):
    return f"<div class='diag'><h4 style='color:#fef08a;'>{s} - {t} - Memory Layout</h4><div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:10px;'><div style='border:2px solid #0d4aff;border-radius:10px;padding:10px 18px;background:#0d4aff33;'>1000: Val1</div><div style='border:2px solid #ff006a;border-radius:10px;padding:10px 18px;background:#ff006a33;'>1004: Val2</div><div style='border:2px solid #fef08a;border-radius:10px;padding:10px 18px;background:#fef08a33;'>1008: Val3</div><div style='border:2px solid #00f5ff;border-radius:10px;padding:10px 18px;background:#00f5ff33;'>1012: Val4</div></div><div style='margin-top:10px;color:#ff006a;'>ptr contiguous</div></div>"

# WELCOME
if st.session_state.page == 'welcome':
    st.markdown("<div class='center' style='padding-top:22vh'><h1 style='color:#c7f0ff;font-size:70px;font-weight:900;'>Welcome to BhavPath</h1><div class='glass' style='display:inline-block;margin-top:20px;padding:28px 50px;'><h2 style='margin:0;font-size:32px;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>What is Your Placement Story..??</h2></div></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.4,1,1.4])
    with c:
        st.write("")
        st.write("")
        if st.button('Next', use_container_width=True):
            st.session_state.page='login'
            st.rerun()

elif st.session_state.page == 'login':
    st.markdown("<div class='center'><h1 style='color:white;'>Login to BhavPath</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1.2,1,1.2])
    with col:
        st.write("")
        email=st.text_input('Email')
        college=st.text_input('College Name')
        if st.button('Continue', use_container_width=True, type='primary'):
            if email and college:
                st.session_state.college=college
                st.session_state.page='purpose'
                st.rerun()
        if st.button('Back', use_container_width=True):
            st.session_state.page='welcome'
            st.rerun()

elif st.session_state.page == 'purpose':
    st.markdown("<div class='center'><h1 style='color:white;'>What is the purpose?</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.5,1])
    with col:
        st.write("")
        c1,c2=st.columns(2)
        with c1:
            if st.button('Placement Prediction', use_container_width=True):
                st.session_state.page='p_welcome'
                st.rerun()
            st.write("")
            if st.button('Test Zone', use_container_width=True):
                st.session_state.page='coming'
                st.rerun()
        with c2:
            if st.button('Technical Skills', use_container_width=True):
                st.session_state.page='t_welcome'
                st.rerun()
            st.write("")
            if st.button('Interview + Code', use_container_width=True):
                st.session_state.page='i_welcome'
                st.rerun()

elif st.session_state.page == 'p_welcome':
    st.markdown(f"<div class='center'><h1 style='color:white;'>Welcome to Placement Prediction</h1><p style='color:#a78bfa;'>{st.session_state.college}</p></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write("")
        if st.button('Next - Enter Details', use_container_width=True, type='primary'):
            st.session_state.page='p_form'
            st.rerun()
        if st.button('Back', use_container_width=True):
            st.session_state.page='purpose'
            st.rerun()

elif st.session_state.page == 'p_form':
    st.markdown("<div class='center'><h1 style='color:white;'>Enter Your Details</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.3,1])
    with col:
        name=st.text_input('Name')
        tenth=st.number_input('10th %',0.0,100.0,85.0)
        inter=st.number_input('Inter %',0.0,100.0,80.0)
        btech=st.number_input('B.Tech %',0.0,100.0,75.0)
        skills=st.text_input('Skills', placeholder='Python, Java, SQL')
        if st.button('Predict', use_container_width=True, type='primary'):
            st.session_state.pdata=(name,tenth,inter,btech,skills)
            st.session_state.page='p_result'
            st.rerun()
        if st.button('Back', use_container_width=True):
            st.session_state.page='p_welcome'
            st.rerun()

elif st.session_state.page == 'p_result':
    name,tenth,inter,btech,skills=st.session_state.pdata
    cnt=len([s for s in skills.split(',') if s.strip()]) if skills else 1
    if SK and model is not None:
        X_new=pd.DataFrame({'tenth':[tenth],'inter':[inter],'btech':[btech],'skills':[cnt]})
        prob=float(model.predict_proba(X_new)[0][1]*100)
        pred=int(model.predict(X_new)[0])
    else:
        avg_tmp=(tenth+inter+btech)/3
        prob=avg_tmp+cnt*3
        if prob>100:
            prob=92
        pred=1 if prob>70 else 0
    avg=(tenth+inter+btech)/3
    st.markdown(f"<div class='center'><h1 style='color:white;'>Result for {name} - {prob:.1f}% Chance</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        colr='#00ff88' if pred==1 else '#ff006a'
        status='HIGH CHANCE - PLACED' if pred==1 else 'NEED IMPROVEMENT'
        st.markdown(f"<div class='glass'><h3 style='color:{colr};'>{status}</h3><p style='color:white;'>10th {tenth}% | Inter {inter}% | BTech {btech}% | Skills {cnt} | Avg {avg:.1f}%</p></div>", unsafe_allow_html=True)
        st.write("")
        if prob>=80:
            comps=[['Google/Amazon','Eligible'],['TCS Digital','Eligible'],['Infosys SP','Eligible']]
        elif prob>=60:
            comps=[['TCS Digital','Eligible'],['Infosys','Eligible'],['Wipro','Eligible']]
        else:
            comps=[['Wipro','Try'],['TCS NQT','Practice Needed']]
        df=pd.DataFrame(comps, columns=['Company','Status'])
        st.dataframe(df, use_container_width=True)
        st.bar_chart(pd.DataFrame({'Score':[tenth,inter,btech]}, index=['10th','Inter','BTech']))
        st.progress(int(prob))
        st.write("")
        b1,b2=st.columns(2)
        with b1:
            if st.button('Back', use_container_width=True):
                st.session_state.page='p_form'
                st.rerun()
        with b2:
            if st.button('Home', use_container_width=True):
                st.session_state.page='purpose'
                st.rerun()

elif st.session_state.page == 't_welcome':
    st.markdown("<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:50px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA</p></div></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write("")
        st.write("")
        if st.button('Explore Skills', use_container_width=True, type='primary'):
            st.session_state.page='t_skills'
            st.rerun()
        if st.button('Back', use_container_width=True):
            st.session_state.page='purpose'
            st.rerun()

elif st.session_state.page == 't_skills':
    st.markdown("<div class='center'><h1 style='color:white;'>Select Your Skill</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        r1_c1,r1_c2,r1_c3=st.columns(3)
        with r1_c1:
            if st.button('C', use_container_width=True):
                st.session_state.skill='C'
                st.session_state.topic='Intro'
                st.session_state.page='skill_detail'
                st.rerun()
        with r1_c2:
            if st.button('C++', use_container_width=True):
                st.session_state.skill='C++'
                st.session_state.topic='Basics'
                st.session_state.page='skill_detail'
                st.rerun()
        with r1_c3:
            if st.button('Java', use_container_width=True):
                st.session_state.skill='Java'
                st.session_state.topic='Basics'
                st.session_state.page='skill_detail'
                st.rerun()
        st.write("")
        r2_c1,r2_c2,r2_c3=st.columns(3)
        with r2_c1:
            if st.button('Python', use_container_width=True):
                st.session_state.skill='Python'
                st.session_state.topic='Basics'
                st.session_state.page='skill_detail'
                st.rerun()
        with r2_c2:
            if st.button('SQL', use_container_width=True):
                st.session_state.skill='SQL'
                st.session_state.topic='SELECT'
                st.session_state.page='skill_detail'
                st.rerun()
        with r2_c3:
            if st.button('DSA', use_container_width=True):
                st.session_state.skill='DSA'
                st.session_state.topic='Arrays'
                st.session_state.page='skill_detail'
                st.rerun()
        st.write("")
        st.write("")
        if st.button('Back', use_container_width=True):
            st.session_state.page='t_welcome'
            st.rerun()

elif st.session_state.page == 'skill_detail':
    skill=st.session_state.skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Detailed</h1></div>", unsafe_allow_html=True)
    topics_map={'C':['Intro','Data Types','Loops','Functions','Pointers','Arrays','Structures','File Handling'],'C++':['Basics','OOP','STL','Pointers','Inheritance','Polymorphism','Templates','Projects'],'Java':['Basics','OOP','Collections','Exception','Multithreading','JDBC','Spring','Projects'],'Python':['Basics','Loops','Functions','OOP','Libraries','File Handling','Django','Projects'],'SQL':['SELECT','JOINS','GROUP BY','Subqueries','Indexing','Normalization','Procedures','Projects'],'DSA':['Arrays','Linked List','Stack & Queue','Trees','Graphs','Sorting','DP','Greedy']}
    tlist=topics_map.get(skill, topics_map['C'])
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        col1,col2=st.columns([1,2.5])
        with col1:
            st.markdown(f"<div class='glass'><h3 style='color:white;margin:0;'>{skill} Topics</h3></div>", unsafe_allow_html=True)
            st.write("")
            for i,t in enumerate(tlist,1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True):
                    st.session_state.topic=t
                    st.rerun()
            st.write("")
            if st.button('Back', use_container_width=True):
                st.session_state.page='t_skills'
                st.rerun()
        with col2:
            st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#fef08a;margin-top:0;'>{st.session_state.topic} in {skill}</h2>", unsafe_allow_html=True)
            st.markdown(diag_html(skill, st.session_state.topic), unsafe_allow_html=True)
            st.write("")
            st.markdown(f"<div style='color:white;'>Detailed tutorial for {st.session_state.topic} in {skill}. TCS, Infosys, Amazon asks this.</div>", unsafe_allow_html=True)
            st.markdown("---", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:#00ff88;'>Try {skill} Code</h3>", unsafe_allow_html=True)
            default_code=f"print('Hello {skill} - {st.session_state.topic}')\narr=[1,2,3]\nprint(arr)"
            code_input=st.text_area('Code Editor', value=default_code, height=120, key=f"code_{skill}_{st.session_state.topic}")
            if st.button('Run Code', key=f"run_{skill}_{st.session_state.topic}"):
                try:
                    import sys
                    from io import StringIO
                    old_stdout=sys.stdout
                    sys.stdout=mystdout=StringIO()
                    exec(code_input, {})
                    sys.stdout=old_stdout
                    output=mystdout.getvalue()
                    st.success(f"Output:\n{output}")
                except Exception as e:
                    st.error(f"Error: {e}")
            st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 'i_welcome':
    st.markdown("<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:50px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>Crack TCS, Infosys, Amazon, Google</p></div></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write("")
        st.write("")
        if st.button('Start Interview Prep', use_container_width=True, type='primary'):
            st.session_state.page='iv_skills'
            st.rerun()
        if st.button('Back', use_container_width=True):
            st.session_state.page='purpose'
            st.rerun()

elif st.session_state.page == 'iv_skills':
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        c1,c2,c3=st.columns(3)
        with c1:
            if st.button('C Interview', use_container_width=True):
                st.session_state.skill='C'
                st.session_state.page='iv_detail'
                st.rerun()
        with c2:
            if st.button('C++ Interview', use_container_width=True):
                st.session_state.skill='C++'
                st.session_state.page='iv_detail'
                st.rerun()
        with c3:
            if st.button('Java Interview', use_container_width=True):
                st.session_state.skill='Java'
                st.session_state.page='iv_detail'
                st.rerun()
        st.write("")
        c4,c5,c6=st.columns(3)
        with c4:
            if st.button('Python Interview', use_container_width=True):
                st.session_state.skill='Python'
                st.session_state.page='iv_detail'
                st.rerun()
        with c5:
            if st.button('SQL Interview', use_container_width=True):
                st.session_state.skill='SQL'
                st.session_state.page='iv_detail'
                st.rerun()
        with c6:
            if st.button('DSA Interview', use_container_width=True):
                st.session_state.skill='DSA'
                st.session_state.page='iv_detail'
                st.rerun()
        st.write("")
        st.write("")
        if st.button('Back', use_container_width=True):
            st.session_state.page='i_welcome'
            st.rerun()

elif st.session_state.page == 'iv_detail':
    skill=st.session_state.skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview - With Pics</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
        st.markdown(diag_html(skill, 'Interview'), unsafe_allow_html=True)
        st.markdown(f"<h2 style='color:#fef08a;'>{skill} Interview - 15 Qs</h2><p style='color:white;'>Q1-Q15 detailed</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
        if st.button('Back to Skills'):
            st.session_state.page='iv_skills'
            st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon</h1></div>", unsafe_allow_html=True)
    if st.button('Back'):
        st.session_state.page='purpose'
        st.rerun()
