import streamlit as st
import os, csv
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="BhavPath Premium", page_icon="🚀", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
*{font-family:'Poppins',sans-serif}
.stApp{background:radial-gradient(ellipse at top left,#0f0c29 0%,#302b63 40%,#24243e 80%,#000 100%)!important;background-attachment:fixed!important}
.glass-premium{background:rgba(255,255,255,0.08)!important;backdrop-filter:blur(20px)!important;border:1px solid rgba(255,255,255,0.15)!important;border-radius:20px!important;padding:20px!important}
div[data-testid="stButton"]>button{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%)!important;color:white!important;border-radius:15px!important;font-weight:700!important;height:55px!important}
</style>
""", unsafe_allow_html=True)

USER_DATA_FILE = "/tmp/bhavpath_users.csv"

def save_user_data(n,e,c,p="",xp=0):
    fe = os.path.exists(USER_DATA_FILE)
    with open(USER_DATA_FILE,'a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if not fe:
            w.writerow(["Timestamp","Name","Email","College","Purpose","XP","Modules","Game"])
        w.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),n,e,c,p,xp,len(st.session_state.get('completed',[])),st.session_state.get('game_unlocked',False)])

def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return []
    with open(USER_DATA_FILE,'r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

# Session init
defaults = {
    'page':"welcome",'xp':0,'completed':[],'name':"",'email':"",'college':"",'purpose':"",
    'is_admin':False,'test_skill':None,'test_started':False,'game_unlocked':False,
    'open_theory':True,'open_interview':False,'open_placement':False,'open_code':False
}
for k,v in defaults.items():
    if k not in st.session_state:
        st.session_state[k]=v

TOPICS = {
    "C": ["Intro","Variables","Data Types","Operators","Loops","Arrays","Functions","Pointers","File Handling","Final Boss"],
    "C++": ["Intro","Variables","Loops","OOP Concepts","Classes","Inheritance","STL - Vectors","Final Boss"],
    "Python": ["Intro","Variables","Data Types","Loops","Functions","Lists","Tuples","Dictionary","File Handling","OOP - Classes","Final Boss"],
    "Java": ["Intro","Variables","Data Types","Operators","Loops","Arrays","Strings","OOP - Class","Collections - ArrayList","Collections - HashMap","Exception Handling","Multithreading","Final Boss"],
    "SQL": ["Intro","Basics - SELECT","WHERE Clause","Joins","Aggregate Functions","GROUP BY","Subqueries","Final Boss"],
    "DSA": ["Intro","Arrays","Strings","Linked List","Stack","Queue","Searching","Sorting","Trees","Graphs","Dynamic Programming","Final Boss"]
}

FULL_DB = {
    "Python": {
        "Lists": {
            "theory": """Python Lists Most Important for Placements
WHAT IS LIST Ordered collection mutable changeable allows duplicates heterogenous different types
Example 81 75 90 85 88 BTech scores
WHY IMPORTANT Data Engineering Store millions records Process ETL
Placement TCS NQT Infosys SP Amazon Data Engineer 100 percent ask Lists
OPERATIONS Access Index 0 First 81 Last 88 Every 3rd Index 0 3 6 9 Same as range 0 10 3 logic 0 3 6 9
Most Asked Methods append insert pop remove sort reverse len sum max min
List Comprehension one line filter elegant Pythonic TCS NQT asks eligible filter
REAL PLACEMENT TCS Easy Reverse average Infosys Medium Rotation Amazon Medium-Hard Second largest
Game Collect 0 3 6 9 green win Lists 20 percent Python interviews""",
            "code": """# Python Lists - Example Code - CHALA SPACE LO MIDDLE LO
btech_scores = [81, 75, 90, 85, 88, 92, 78, 85, 90, 88]
print(f"All Scores: {btech_scores}")
print(f"First: {btech_scores[0]}")
print(f"Last: {btech_scores[-1]}")
print(f"Every 3rd [0:10:3]: {btech_scores[0:10:3]}")
# Output [81,85,78,90] Index 0,3,6,9 Same as range(0,10,3)=0,3,6,9
average = sum(btech_scores)/len(btech_scores)
print(f"Average: {average:.2f}%")
eligible = [s for s in btech_scores if s>80]
print(f"Eligible >80%: {eligible}")
""",
            "interview": """Q1 What is list? Ans Ordered mutable allows duplicates heterogenous
Q2 First last every 3rd? Ans First arr[0] Last arr[-1] Every 3rd arr[0:10:3] Index 0,3,6,9 Same as range(0,10,3)=0,3,6,9
Q3 List vs Tuple? Ans List mutable Tuple immutable List slow Tuple fast
Q4 List comprehension? Ans One line filter [s for s in scores if s>80] Elegant""",
            "placement": """TCS Easy Reverse average max min 5 marks
Infosys Medium Rotation duplicates 10 marks
Amazon Medium-Hard Second largest without sorting Merge 10-15 LPA
Game Collect 0,3,6,9 win Lists 20 percent!"""
        },
        "Loops": {
            "theory": """Python Loops Most Important 0,3,6,9 Logic
WHAT IS LOOP Control structure repeats block Saves code Data Engineering lakhs records
TYPES FOR LOOP range stop range 10 => 0-9 range start stop 0 10 => 0-9 range start stop step 0 10 3 => 0 3 6 9
Logic start 0 stop 10 till 9 step 3 So 0 0+3=3 3+3=6 6+3=9 => 0,3,6,9 TCS NQT asks 0,3,6,9 Direct 2 marks
BhavPath Game Collect green coins 0,3,6,9 win Data Engineering Process every 3rd record Array Slicing arr[0:10:3]
REAL PLACEMENT TCS 10-15 marks Infosys 5 marks Amazon Must Game 0,3,6,9 LIST COMPREHENSION""",
            "code": """for i in range(0,10,3):
    print(i)
# Output
# 0
# 3
# 6
# 9
result = [i for i in range(0,10,3)]
print(result) # [0,3,6,9]
""",
            "interview": """Q1 Output range(0,10,3)? Ans 0,3,6,9 MOST ASKED
Q2 For vs While? Ans For known iterations While condition based
Q3 Break vs Continue vs Pass? Ans Break exits Continue skips Pass placeholder""",
            "placement": """TCS NQT Pattern printing 10-15 marks Output range(0,10,3) 0,3,6,9 direct 2 marks
Infosys Loop array find >80% eligible 5 marks
Amazon Process S3 files loops Must BhavPath Game Collect 0,3,6,9 win!"""
        },
        "Variables": {
            "theory": """Python Variables Theory Container name given to memory location No need type declaration Dynamic Typing name Bhavya Python knows string btech 81 Python knows int Makes Python easy fast RULES Start letter underscore No space special char Case sensitive Cannot be keyword Meaningful snake_case DATA TYPES int float str bool list tuple dict set TYPE CHECKING type isinstance Conversion int 81 Important Data Engineering REAL EXAMPLE TCS NQT Store 5 students BTech percent check eligible greater than 70 percent""",
            "code": """name='Bhavya'
btech=81
print(f"Name: {name}, B.Tech: {btech}%")
students=[81,75,60,90,55]
eligible=[s for s in students if s>70]
print(eligible) # [81,75,90]
""",
            "interview": """Q1 What is variable? Ans Container no type declaration dynamic typing
Q2 Rules naming? Ans Start letter underscore no space special char case sensitive""",
            "placement": """TCS NQT Store student BTech percent check eligibility greater than 70 percent Tests variables list condition 5 marks
Infosys Dynamic typing Difference Python vs C Theory 3 marks"""
        }
    },
    "C": {
        "Loops": {
            "theory": """C Loops Theory for i=0;i<10;i+=3 prints 0 3 6 9 Logic i=0 check 0<10 true print 0 i=3 print 3 i=6 print 6 i=9 print 9 i=12 false stop So 0,3,6,9 SAME as Python range(0,10,3)=0,3,6,9 Step logic TCS NQT asks star pattern PLACEMENT TCS NQT 3-4 questions loops pattern Infosys loop array Amazon process S3 files""",
            "code": """#include <stdio.h>
int main(){
 for(int i=0; i<10; i+=3) printf("%d ", i);
 return 0;
}
// Output: 0 3 6 9
""",
            "interview": """Q1 Output for(i=0;i<10;i+=3)? Ans 0 3 6 9
Q2 For vs While? Ans For known While condition""",
            "placement": """TCS NQT Pattern 10 marks Infosys Loop array BhavPath Game Collect 0,3,6,9!"""
        }
    },
    "DSA": {
        "Arrays": {
            "theory": """DSA Arrays Most Important for MAANG WHAT IS ARRAY Collection similar types contiguous memory Index 0 Python list as array Example 81 75 90 85 88 Foundation DSA Without arrays no DSA Arrays 30 percent DSA interviews WHY HEART OF PLACEMENTS Amazon Google 100 percent DSA interviews start arrays TCS Digital Infosys SP Wipro Elite DSA coding rounds Arrays must Package Good DSA 10 plus LPA Poor 3.5 LPA TYPES One Two Dynamic OPERATIONS Access O1 Search On INDEXING arr0 First 81 arr-1 Last 88 arr0:10:3 Every 3rd Index 0,3,6,9 Values 81,85,78,90 Step 3 REAL PLACEMENT TCS Easy Reverse average max min Infosys Medium Rotation duplicates second largest Amazon Medium-Hard Second largest without sorting Merge sorted Missing Kadane Flipkart ETL Process array Game Coins 0-9 Collect 0,3,6,9 green win Arrays 30 percent DSA""",
            "code": """btech_scores=[81,75,90,85,88,92,78,85,90,88]
print(f"First: {btech_scores[0]}") #81
print(f"Every 3rd [0:10:3]: {btech_scores[0:10:3]}")
# [81,85,78,90] Index 0,3,6,9
""",
            "interview": """Q1 What is array? Ans Collection contiguous memory index 0
Q2 Time complexity? Ans Access O1 Search On""",
            "placement": """TCS Easy Reverse average Infosys Medium Rotation Amazon Medium-Hard Second largest Merge Game 0,3,6,9!"""
        }
    }
}

def is_locked():
    if st.session_state.xp < 150:
        return True, f"Need 150 XP Have {st.session_state.xp}"
    if len(st.session_state.completed) < 3:
        return True, f"Complete 3 modules Have {len(st.session_state.completed)}"
    if not st.session_state.game_unlocked:
        return True, "Complete Test to unlock Game"
    return False, "Unlocked"

# WELCOME
if st.session_state.page == "welcome":
    st.markdown('<div style="background:linear-gradient(135deg,#667eea,#764ba2,#f093fb);padding:80px 20px;border-radius:30px;text-align:center;color:white"><div style="font-size:70px">🚀</div><div style="font-size:60px;font-weight:900">BhavPath</div><div style="font-size:28px;font-weight:600">Welcome to your placement story</div></div>', unsafe_allow_html=True)
    st.write("")
    _,mid,_ = st.columns([1,2,1])
    with mid:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.page="login"
            st.rerun()
        if st.button("🔐 Admin Login", use_container_width=True):
            st.session_state.page="admin_login"
            st.rerun()
    st.stop()

# ADMIN LOGIN
if st.session_state.page == "admin_login":
    _,col,_ = st.columns([1,2,1])
    with col:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        u = st.text_input("Admin Username")
        p = st.text_input("Admin Password", type="password")
        if st.button("Login as Admin →", use_container_width=True, type="primary"):
            if u=="admin" and p=="bhavpath123":
                st.session_state.is_admin=True
                st.session_state.page="admin_dashboard"
                st.rerun()
            else:
                st.error("Invalid")
        if st.button("Back"):
            st.session_state.page="welcome"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ADMIN DASHBOARD
if st.session_state.page == "admin_dashboard":
    users = load_user_data()
    st.markdown(f'<div style="background:linear-gradient(135deg,#f59e0b,#ef4444);padding:25px;border-radius:20px;text-align:center;color:white"><div style="font-size:32px;font-weight:900">🔐 Admin Dashboard - {len(users)} Visitors</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    if users:
        st.dataframe(users, use_container_width=True)
    else:
        st.info("No visitors yet")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Logout Admin"):
        st.session_state.is_admin=False
        st.session_state.page="welcome"
        st.rerun()
    st.stop()

# LOGIN
if st.session_state.page == "login":
    _,col,_ = st.columns([1,2,1])
    with col:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        n = st.text_input("Full Name", value=st.session_state.name)
        e = st.text_input("Email", value=st.session_state.email)
        cl = st.text_input("College", value=st.session_state.college)
        if st.button("Continue →", use_container_width=True, type="primary"):
            if n and e and cl:
                st.session_state.name=n
                st.session_state.email=e
                st.session_state.college=cl
                save_user_data(n,e,cl,"login",0)
                st.session_state.page="purpose"
                st.rerun()
            else:
                st.error("Fill all")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# PURPOSE
if st.session_state.page == "purpose":
    st.markdown(f'<div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:22px;border-radius:20px;text-align:center;color:white"><div style="font-size:30px;font-weight:800">🚀 BhavPath</div><div>Hi {st.session_state.name} | {st.session_state.college}</div></div>', unsafe_allow_html=True)
    il,lm = is_locked()
    c1,c2 = st.columns(2)
    with c1:
        if st.button("📊 Placement Percentage", use_container_width=True):
            st.session_state.purpose="placement"
            st.session_state.page="main"
            st.rerun()
    with c2:
        if st.button("📚 Skill Learning", use_container_width=True):
            st.session_state.purpose="skill"
            st.session_state.page="main"
            st.rerun()
    c3,c4 = st.columns(2)
    with c3:
        if st.button("📝 Test Zone", use_container_width=True):
            st.session_state.purpose="test"
            st.session_state.page="main"
            st.rerun()
    with c4:
        if il:
            st.markdown(f'<div style="background:rgba(239,68,68,0.15);border:2px solid #ef4444;border-radius:15px;padding:20px;text-align:center;height:75px"><div style="font-size:22px">🔒</div><div style="font-size:11px;color:#ef4444;font-weight:700">Certificate Locked</div></div>', unsafe_allow_html=True)
        else:
            if st.button("📜 Certificate Unlocked ✅", use_container_width=True):
                st.session_state.purpose="certificate"
                st.session_state.page="main"
                st.rerun()
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    with c1: st.metric("XP", f"{st.session_state.xp}/150")
    with c2: st.metric("Modules", f"{len(st.session_state.completed)}/3")
    with c3: st.metric("Game", "Yes" if st.session_state.game_unlocked else "No")
    st.progress(min(100,int(st.session_state.xp/150*33 + len(st.session_state.completed)/3*33 + (33 if st.session_state.game_unlocked else 0))))
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# SIDEBAR
st.sidebar.markdown('<div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:15px;border-radius:15px;color:white;text-align:center"><div style="font-size:22px;font-weight:800">🚀 BhavPath</div></div>', unsafe_allow_html=True)
st.sidebar.write(f"👤 {st.session_state.name}")
st.sidebar.metric("XP", st.session_state.xp)
if st.sidebar.button("Change Purpose"):
    st.session_state.page="purpose"
    st.rerun()
if st.sidebar.button("Logout"):
    st.session_state.page="welcome"
    st.rerun()

# SKILL - FINAL LAYOUT - RIGHT SIDE 4 BOXES + MIDDLE CHALA SPACE
if st.session_state.purpose == "skill":
    st.markdown('<div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:25px;border-radius:20px;text-align:center;color:white;margin-bottom:25px"><div style="font-size:32px;font-weight:900">📚 Skill Learning - Right Side 4 Boxes + Middle Chala Space</div></div>', unsafe_allow_html=True)
    left,middle,right = st.columns([0.8,3.5,1.2], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<p style="color:white;font-weight:800;font-size:13px;text-align:center">📚 SELECT SKILL</p>', unsafe_allow_html=True)
        selected_topic = st.radio("Skill", ["C","C++","Python","Java","SQL","DSA"], label_visibility="collapsed")
        st.divider()
        st.markdown(f'<p style="color:white;font-weight:700;font-size:12px;text-align:center">📖 Modules {len(TOPICS[selected_topic])}</p>', unsafe_allow_html=True)
        selected_module = st.radio("Modules", TOPICS[selected_topic], label_visibility="collapsed")
        st.divider()
        st.markdown(f'<div style="background:linear-gradient(135deg,#4ade80,#22c55e);padding:10px;border-radius:10px;text-align:center;color:white"><div style="font-size:12px;font-weight:800">{selected_topic} - {selected_module}</div><div style="font-size:18px;font-weight:900">{st.session_state.xp} XP</div></div>', unsafe_allow_html=True)
        key = f"{selected_topic}-{selected_module}"
        if key not in st.session_state.completed:
            if st.button("✅ +50 XP", use_container_width=True, type="primary"):
                st.session_state.completed.append(key)
                st.session_state.xp+=50
                save_user_data(st.session_state.name,st.session_state.email,st.session_state.college,f"skill-{selected_topic}",st.session_state.xp)
                st.balloons()
                st.rerun()
        else:
            st.success("✅ Done")
        st.markdown('</div>', unsafe_allow_html=True)
    with middle:
        st.markdown('<div class="glass-premium" style="padding:40px !important">', unsafe_allow_html=True)
        st.markdown(f'<div style="background:linear-gradient(135deg,rgba(102,126,234,0.25),rgba(59,130,246,0.25));padding:30px;border-radius:20px;border-left:7px solid #667eea;margin-bottom:35px"><div style="color:#667eea;font-size:12px;font-weight:800">MATERIAL HEADING - MIDDLE - CHALA SPACE LO</div><div style="color:white;font-size:36px;font-weight:900;margin-top:10px">{selected_topic} - {selected_module}</div></div>', unsafe_allow_html=True)
        data = FULL_DB.get(selected_topic,{}).get(selected_module,None)
        if not data:
            data = {
                "theory": f"{selected_module} in {selected_topic} Full Detailed Theory Important for placements TCS NQT 2-3 questions Infosys SP mandatory Amazon 10-15 LPA advanced Real World daily Example Code prints 0,3,6,9 using range(0,10,3) Step logic Used Game Collect 0,3,6,9 green coins win MUST for placements",
                "code": f"# {selected_topic} - {selected_module}\nfor i in range(0,10,3):\n    print(i)\n# Output 0 3 6 9",
                "interview": f"Q1 What is {selected_module}? Ans Core concept\nQ2 Why important? Ans TCS NQT 2-3 Qs",
                "placement": f"TCS NQT 2-3 Qs 5 marks Infosys SP mandatory Amazon 10-15 LPA"
            }
        st.markdown('<div style="background:linear-gradient(135deg,#8b5cf6,#667eea);padding:22px;border-radius:16px;text-align:center;color:white;margin-bottom:25px"><div style="font-size:20px;font-weight:800">💻 EXAMPLE CODE - Middle lo - Chala Space lo - Clear ga</div></div>', unsafe_allow_html=True)
        st.markdown('<div style="background:rgba(0,0,0,0.35);border:2px solid rgba(167,139,250,0.4);border-radius:18px;padding:35px;margin-bottom:15px;min-height:450px">', unsafe_allow_html=True)
        st.code(data["code"], language="python")
        st.success("✅ Output: 0,3,6,9 - range(0,10,3) - Middle lo chala space")
        st.markdown('</div>', unsafe_allow_html=True)
        st.write(""); st.divider(); st.write("")
        st.markdown('<div style="background:linear-gradient(135deg,#f59e0b,#ef4444);padding:22px;border-radius:16px;text-align:center;color:white;margin-bottom:25px"><div style="font-size:20px;font-weight:800">⌨️ PRACTICING SPACE - Kindha - Middle lo - Chala Space lo</div></div>', unsafe_allow_html=True)
        st.markdown('<div style="background:rgba(0,0,0,0.25);border:2px solid rgba(251,191,36,0.4);border-radius:18px;padding:35px;min-height:550px">', unsafe_allow_html=True)
        default_practice = f"# {selected_topic} - {selected_module} - Practice Here - CHALA SPACE LO\nfor i in range(0,10,3):\n    print(i)\n# Output 0,3,6,9\n# Task: avg, >70% filter, reverse arr[::-1], every 3rd arr[0:10:3]\n"
        pc = st.text_area("Practice", value=default_practice, height=450, label_visibility="collapsed", key=f"pm_{selected_topic}_{selected_module}")
        if st.button("▶️ Run Your Code", use_container_width=True, type="primary", key="run_mid"):
            try:
                import io,sys
                old=sys.stdout; sys.stdout=buf=io.StringIO()
                if selected_topic in ["C","C++","Java","SQL"]:
                    sys.stdout=old; st.info("Preview:"); st.code(pc)
                else:
                    exec(pc); sys.stdout=old; out=buf.getvalue() or "No output"
                    st.success("✅ Output:"); st.code(out); st.balloons()
            except Exception as e:
                sys.stdout=old; st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-premium" style="padding:18px !important">', unsafe_allow_html=True)
        st.markdown('<p style="color:white;font-weight:800;font-size:13px;text-align:center">📦 RIGHT SIDE - 4 BOXES</p>', unsafe_allow_html=True)
        data = FULL_DB.get(selected_topic,{}).get(selected_module,None)
        if not data:
            data = {"theory": f"{selected_module} Full Theory","code":"for i in range(0,10,3):\n    print(i)","interview":"Q1 What is module?","placement":"TCS NQT Qs"}
        if st.button("📖 Theory - Python Lists - Full Detailed - Click to Open", use_container_width=True, key="bt"):
            st.session_state.open_theory = not st.session_state.open_theory
        if st.session_state.open_theory:
            st.markdown(f'<div style="background:rgba(15,12,41,0.95);border:2px solid #667eea;padding:18px;border-radius:14px;margin-top:10px;margin-bottom:18px;max-height:300px;overflow-y:auto"><div style="color:#60a5fa;font-size:11px;font-weight:800">📖 THEORY - RIGHT SIDE</div><div style="color:white;font-size:12px;white-space:pre-wrap">{data["theory"]}</div></div>', unsafe_allow_html=True)
        st.write("")
        if st.button("💼 Interview Questions - Click to Open", use_container_width=True, key="bi"):
            st.session_state.open_interview = not st.session_state.open_interview
        if st.session_state.open_interview:
            st.markdown(f'<div style="background:rgba(251,191,36,0.12);border:2px solid #fbbf24;padding:18px;border-radius:14px;margin-bottom:18px;max-height:300px;overflow-y:auto"><div style="color:#fbbf24;font-size:11px;font-weight:800">💼 INTERVIEW - RIGHT SIDE</div><div style="color:white;font-size:12px;white-space:pre-wrap">{data["interview"]}</div></div>', unsafe_allow_html=True)
        st.write("")
        if st.button("🏢 Placement - Company Wise - Click to Open", use_container_width=True, key="bp"):
            st.session_state.open_placement = not st.session_state.open_placement
        if st.session_state.open_placement:
            st.markdown(f'<div style="background:rgba(74,222,128,0.12);border:2px solid #4ade80;padding:18px;border-radius:14px;margin-bottom:18px;max-height:300px;overflow-y:auto"><div style="color:#4ade80;font-size:11px;font-weight:800">🏢 PLACEMENT - RIGHT SIDE</div><div style="color:white;font-size:12px;white-space:pre-wrap">{data["placement"]}</div></div>', unsafe_allow_html=True)
        st.write("")
        if st.button("💻 Code Examples - Click to Open", use_container_width=True, key="bc"):
            st.session_state.open_code = not st.session_state.open_code
        if st.session_state.open_code:
            st.code(data["code"], language="python")
        st.markdown('</div>', unsafe_allow_html=True)

# PLACEMENT - COMMUNICATION + AUTO CHANGE
elif st.session_state.purpose == "placement":
    st.markdown('<div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:25px;border-radius:20px;text-align:center;color:white;margin-bottom:20px"><div style="font-size:32px;font-weight:900">📊 Placement - Smart Filter + Communication + Auto Change</div></div>', unsafe_allow_html=True)
    COMPANIES_DB=[
        {"name":"TCS Ninja","min_10th":60,"min_inter":60,"min_btech":60,"skills":["C","Communication"],"package":"3.5 LPA","color":"#4ade80","role":"Software Engineer","comm_required":"Basic"},
        {"name":"TCS Digital","min_10th":70,"min_inter":70,"min_btech":70,"skills":["Python","DSA","Communication"],"package":"7 LPA","color":"#667eea","role":"Digital - SDE","comm_required":"Good"},
        {"name":"TCS Prime","min_10th":75,"min_inter":75,"min_btech":75,"skills":["DSA","Java","Communication"],"package":"9-11 LPA","color":"#8b5cf6","role":"Prime Engineer","comm_required":"Excellent"},
        {"name":"Infosys SP","min_10th":65,"min_inter":65,"min_btech":65,"skills":["Python","Java","Communication"],"package":"5-9 LPA","color":"#fbbf24","role":"Systems Engineer","comm_required":"Good"},
        {"name":"Wipro Elite","min_10th":60,"min_inter":60,"min_btech":60,"skills":["Java","SQL","Communication"],"package":"3.5-6 LPA","color":"#a78bfa","role":"Project Engineer","comm_required":"Basic"},
        {"name":"Amazon Data Engineer","min_10th":75,"min_inter":70,"min_btech":70,"skills":["Python","SQL","DSA","Communication"],"package":"10-15 LPA","color":"#f472b6","role":"Data Engineer","comm_required":"Excellent"},
        {"name":"Flipkart SDE","min_10th":70,"min_inter":70,"min_btech":70,"skills":["DSA","Python","Communication"],"package":"12-20 LPA","color":"#60a5fa","role":"Software Developer","comm_required":"Good"},
        {"name":"Accenture","min_10th":65,"min_inter":65,"min_btech":65,"skills":["SQL","Java","Communication"],"package":"4.5-6.5 LPA","color":"#f97316","role":"ASE","comm_required":"Good"},
    ]
    left,right = st.columns([1,1.8], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        tenth=st.number_input("10th %",0,100,85)
        inter=st.number_input("Inter %",0,100,82)
        btech=st.number_input("B.Tech %",0,100,81)
        st.divider()
        skill_c=st.checkbox("C - Programming",value=True)
        skill_cpp=st.checkbox("C++",value=False)
        skill_python=st.checkbox("Python",value=True)
        skill_java=st.checkbox("Java",value=True)
        skill_sql=st.checkbox("SQL",value=True)
        skill_dsa=st.checkbox("DSA",value=False)
        st.divider()
        skill_comm=st.checkbox("Communication - English + HR",value=True)
        comm_level=st.selectbox("Communication Level",["Basic - Can Speak","Good - Fluent","Excellent - Public Speaking"],index=1)
        selected_skills=[]
        if skill_c: selected_skills.append("C")
        if skill_cpp: selected_skills.append("C++")
        if skill_python: selected_skills.append("Python")
        if skill_java: selected_skills.append("Java")
        if skill_sql: selected_skills.append("SQL")
        if skill_dsa: selected_skills.append("DSA")
        if skill_comm: selected_skills.append("Communication")
        st.markdown(f'<div style="background:rgba(102,126,234,0.2);padding:10px;border-radius:10px;text-align:center"><div style="color:#aaa;font-size:11px">Selected: {", ".join(selected_skills)}<br>B.Tech: {btech}% | Comm: {comm_level}</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        eligible=[]; not_eligible=[]
        for comp in COMPANIES_DB:
            perc_ok=(tenth>=comp["min_10th"] and inter>=comp["min_inter"] and btech>=comp["min_btech"])
            if selected_skills:
                ms=set(selected_skills)&set(comp["skills"])
                if "Communication" in comp["skills"] and "Communication" not in selected_skills:
                    skill_ok=False; reason="Need Communication"
                else:
                    skill_ok=len(ms)>=1; reason=f"Matched: {', '.join(ms)}" if ms else "No match"
            else:
                skill_ok=False; reason="Select skill"
            comm_ok=True
            if comp["comm_required"]=="Excellent" and comm_level=="Basic - Can Speak":
                comm_ok=False; reason="Need Good/Excellent Comm"
            if perc_ok and skill_ok and comm_ok:
                eligible.append((comp,reason))
            else:
                not_eligible.append((comp,reason))
        if eligible:
            st.success(f"✅ Eligible for {len(eligible)}/{len(COMPANIES_DB)} - Selecting Criteria Batti Change Ayinayi")
            for comp,reason in eligible:
                st.markdown(f"<div style='background:rgba(255,255,255,0.08);border-left:5px solid {comp['color']};border-radius:15px;padding:15px;margin-bottom:12px'><div style='color:white;font-weight:800'>{comp['name']} ✅</div><div style='color:{comp['color']};font-size:12px'>{comp['role']} | {comp['package']}</div><div style='color:#aaa;font-size:11px'>Skills: {', '.join(comp['skills'])} | {reason}</div></div>", unsafe_allow_html=True)
        else:
            st.error("❌ No match - Select Communication + Skills")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.purpose == "test":
    st.markdown('<h2 style="color:white">📝 Test Zone + Real Game</h2>', unsafe_allow_html=True)
    if not st.session_state.test_started and not st.session_state.game_unlocked:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("C Language", use_container_width=True): st.session_state.test_skill="C"
            if st.button("Python", use_container_width=True): st.session_state.test_skill="Python"
        with c2:
            if st.button("C++", use_container_width=True): st.session_state.test_skill="C++"
            if st.button("Java", use_container_width=True): st.session_state.test_skill="Java"
        with c3:
            if st.button("SQL", use_container_width=True): st.session_state.test_skill="SQL"
            if st.button("DSA", use_container_width=True): st.session_state.test_skill="DSA"
        if st.session_state.test_skill:
            if st.button(f"Start {st.session_state.test_skill} Test →", type="primary", use_container_width=True):
                st.session_state.test_started=True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    elif st.session_state.test_started and not st.session_state.game_unlocked:
        st.markdown('<div class="glass-premium">Q1. range(0,10,3)? 0,3,6,9 Most Asked</div>', unsafe_allow_html=True)
        ans = st.radio("Select", ["0,3,6,9","0,1,2"], index=None)
        if st.button("Submit & Unlock Game", type="primary", use_container_width=True):
            st.session_state.game_unlocked=True
            st.session_state.test_started=False
            st.session_state.xp+=50
            st.balloons()
            st.rerun()
    else:
        game_html = """<!DOCTYPE html><html><head><style>body{margin:0;background:#0f0c29;display:flex;justify-content:center;align-items:center;flex-direction:column}#gameCanvas{border:4px solid #667eea;border-radius:20px;background:#1a1a4e}#info{color:white;margin:10px;text-align:center;background:rgba(255,255,255,0.1);padding:12px 24px;border-radius:15px}</style></head><body><div id="info"><div>Score: <span id="score" style="color:#4ade80">0</span> | Target: <b style="color:#4ade80">0,3,6,9</b> | Lives: <span id="lives">3</span></div></div><canvas id="gameCanvas" width="600" height="400"></canvas><div id="message" style="color:#fbbf24;font-weight:bold;margin-top:10px"></div><script>const canvas=document.getElementById('gameCanvas');const ctx=canvas.getContext('2d');const scoreEl=document.getElementById('score');const livesEl=document.getElementById('lives');const messageEl=document.getElementById('message');let player={x:300,y:200,size:22,speed:6,color:'#667eea'};let keys={};let score=0;let lives=3;let collected=[];let targetSequence=[0,3,6,9];let coins=[];function spawnCoins(){coins=[];[0,3,6,9].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:true,size:20,color:'#4ade80',collected:false})});[1,2,4,5,7,8].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:false,size:17,color:'#ef4444',collected:false})});}function drawPlayer(){ctx.fillStyle=player.color;ctx.beginPath();ctx.arc(player.x,player.y,player.size,0,Math.PI*2);ctx.fill();}function drawCoins(){coins.forEach(coin=>{if(!coin.collected){ctx.fillStyle=coin.color;ctx.beginPath();ctx.arc(coin.x,coin.y,coin.size,0,Math.PI*2);ctx.fill();ctx.fillStyle='white';ctx.font='bold 14px Poppins';ctx.textAlign='center';ctx.fillText(coin.value,coin.x,coin.y+5);}});}function checkCollision(){coins.forEach(coin=>{if(!coin.collected){let dx=player.x-coin.x,dy=player.y-coin.y,dist=Math.sqrt(dx*dx+dy*dy);if(dist<player.size+coin.size){coin.collected=true;if(coin.isCorrect){if(collected.length<targetSequence.length&&coin.value===targetSequence[collected.length]){collected.push(coin.value);score+=25;messageEl.textContent=`Correct!`;messageEl.style.color='#4ade80';}else{lives--;}}else{lives--;}updateUI();if(JSON.stringify(collected)===JSON.stringify(targetSequence)){messageEl.textContent='WIN! +100 XP!';}if(lives<=0){messageEl.textContent='Game Over!';}}}});}function updateUI(){scoreEl.textContent=score;livesEl.textContent=lives;}function update(){if(keys['ArrowUp']||keys['w'])player.y-=player.speed;if(keys['ArrowDown']||keys['s'])player.y+=player.speed;if(keys['ArrowLeft']||keys['a'])player.x-=player.speed;if(keys['ArrowRight']||keys['d'])player.x+=player.speed;player.x=Math.max(player.size,Math.min(canvas.width-player.size,player.x));player.y=Math.max(player.size,Math.min(canvas.height-player.size,player.y));ctx.clearRect(0,0,canvas.width,canvas.height);drawCoins();drawPlayer();checkCollision();requestAnimationFrame(update);}window.addEventListener('keydown',e=>{keys[e.key]=true;});window.addEventListener('keyup',e=>{keys[e.key]=false;});spawnCoins();update();</script></body></html>"""
        components.html(game_html, height=580, width=650)
        if st.button("Claim Win +100 XP", use_container_width=True):
            st.session_state.xp+=100
            st.balloons()

elif st.session_state.purpose == "certificate":
    il,lm = is_locked()
    if il:
        st.markdown(f'<div style="background:linear-gradient(135deg,#ef4444,#dc2626);padding:30px;border-radius:20px;text-align:center;color:white"><div style="font-size:60px">🔒</div><div style="font-size:32px;font-weight:900">Certificate Locked</div><div>{lm}</div></div>', unsafe_allow_html=True)
        st.stop()
    st.balloons()
    st.markdown(f'<div style="background:white;border-radius:20px;padding:40px;text-align:center"><div style="font-size:50px">🏆</div><div style="font-size:36px;font-weight:900;color:#667eea">BHAVPATH PREMIUM</div><div style="font-size:28px;font-weight:800;margin-top:15px">{st.session_state.name}</div><div style="color:#555">{st.session_state.college}</div><div style="margin:20px">XP: {st.session_state.xp} | Modules: {len(st.session_state.completed)}</div><div style="background:#f0f4ff;padding:15px;border-radius:15px;color:green;font-weight:800">PLACEMENT READY</div></div>', unsafe_allow_html=True)

else:
    st.markdown('<div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:25px;border-radius:20px;text-align:center;color:white"><div style="font-size:32px;font-weight:900">💼 AI Interview - Robot Zoom</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    st.text_area("Your Answer", placeholder="Myself Bhavya from Rise College...", height=120)
    if st.button("📜 Submit Interview & Get Certificate", use_container_width=True, type="primary"):
        st.session_state.purpose="certificate"
        st.balloons()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
