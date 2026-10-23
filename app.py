import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import os, csv

st.set_page_config(page_title="BhavPath Premium", page_icon="🚀", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: radial-gradient(ellipse at top left, #0f0c29 0%, #302b63 40%, #24243e 80%, #000000 100%) !important; background-attachment: fixed !important; }
.welcome-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important; padding: 80px 20px !important; border-radius: 30px !important; text-align: center !important; color: white !important; box-shadow: 0 20px 60px rgba(102,126,234,0.6) !important; }
.login-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; padding: 22px !important; border-radius: 20px !important; text-align: center !important; color: white !important; }
.glass-premium { background: rgba(255,255,255,0.08) !important; backdrop-filter: blur(20px) !important; border: 1px solid rgba(255,255,255,0.15) !important; border-radius: 20px !important; padding: 20px !important; }
div[data-testid="stButton"] > button { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; color: white !important; border-radius: 15px !important; font-weight: 700 !important; height: 75px !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, rgba(15,12,41,0.98) 0%, rgba(48,43,99,0.98) 100%) !important; }
</style>
""", unsafe_allow_html=True)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "bhavpath123"
ADMIN_EMAIL = "admin@bhavpath.com"
USER_DATA_FILE = "/tmp/bhavpath_users.csv"

def save_user_data(name, email, college, purpose="", xp=0):
    file_exists = os.path.exists(USER_DATA_FILE)
    with open(USER_DATA_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Name", "Email", "College", "Purpose", "XP", "Modules", "Game"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, email, college, purpose, xp, len(st.session_state.get('completed', [])), st.session_state.get('game_unlocked', False)])

def load_user_data():
    if not os.path.exists(USER_DATA_FILE): return []
    with open(USER_DATA_FILE, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'completed' not in st.session_state: st.session_state.completed = []
if 'name' not in st.session_state: st.session_state.name = ""
if 'email' not in st.session_state: st.session_state.email = ""
if 'college' not in st.session_state: st.session_state.college = ""
if 'purpose' not in st.session_state: st.session_state.purpose = ""
if 'is_admin' not in st.session_state: st.session_state.is_admin = False
if 'test_skill' not in st.session_state: st.session_state.test_skill = None
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'test_answers' not in st.session_state: st.session_state.test_answers = {}
if 'game_unlocked' not in st.session_state: st.session_state.game_unlocked = False
if 'game_score' not in st.session_state: st.session_state.game_score = 0
if 'cert_skill' not in st.session_state: st.session_state.cert_skill = None
if 'cert_stage' not in st.session_state: st.session_state.cert_stage = "select"
if 'cert_answers' not in st.session_state: st.session_state.cert_answers = {}
if 'cert_score' not in st.session_state: st.session_state.cert_score = 0
if 'open_theory' not in st.session_state: st.session_state.open_theory = True
if 'open_interview' not in st.session_state: st.session_state.open_interview = False
if 'open_placement' not in st.session_state: st.session_state.open_placement = False
if 'open_code' not in st.session_state: st.session_state.open_code = False

TOPICS = {
    "C": ["Intro", "Variables", "Loops", "Arrays", "Final Boss"],
    "C++": ["Intro", "STL", "Final Boss"],
    "Python": ["Variables", "Loops", "Lists", "Final Boss"],
    "Java": ["Intro", "Variables", "Final Boss"],
    "SQL": ["Basics", "Joins", "Final Boss"],
    "DSA": ["Arrays", "Final Boss"]
}

FULL_DB = {
    "C": {
        "Intro": {"theory": "C Programming Mother of All Languages: C general-purpose procedural middle-level language Dennis Ritchie 1972 Bell Labs Mother of all languages because most modern languages derived from C Fast efficient close to hardware WHY IMPORTANT Speed Compiled fast direct memory access pointers Foundation If you know C learn C++ Java Python easily 80% syntax similar System Programming OS Windows Linux macOS written in C Embedded IoT use C Placements TCS NQT Wipro Elite Infosys 60% companies ask C FEATURES Procedural Middle-Level Portable Rich Library Pointers powerful STRUCTURE #include <stdio.h> Header int main() Main { } Braces printf() Print return 0 Success REAL WORLD OS Development Linux kernel Embedded AC Washing Machine Game Development Database MySQL Oracle in C", "code": '#include <stdio.h>\nint main() {\n    printf("BhavPath C\\n");\n    int btech=81;\n    printf("B.Tech: %d", btech);\n    return 0;\n}', "interview": "Q1 Who developed C? Ans Dennis Ritchie 1972\nQ2 Why mother? Ans Most languages derived\nQ3 Pointer? Ans Stores address\nQ4 C vs Python? Ans C compiled fast manual memory", "placement": "TCS NQT 2 coding C Array reverse String palindrome Wipro Pointers structures Package C 3.5-5 LPA base must"},
        "Loops": {"theory": "C Loops Complete Theory Most Important WHAT IS LOOP Control structure repeats block multiple times Instead printf 10 times loop writes once repeats 10 times Saves code Data Engineering loops process lakhs records Without loops no Data Engineer job TYPES FOR LOOP for(i=0;i<10;i+=3) Output 0 3 6 9 Logic i=0 check 0<10 true print 0 i=3 print 3 i=6 print 6 i=9 print 9 i=12 false stop So 0,3,6,9 SAME as Python range(0,10,3)=0,3,6,9 Step logic WHILE LOOP while(condition){code} Output same 0 3 6 9 DO-WHILE Executes at least once LOOP CONTROL break Exit immediately continue Skip NESTED LOOPS Loop inside loop for pattern printing TCS NQT asks star pattern PLACEMENT TCS NQT 3-4 questions loops pattern printing Infosys loop through array find eligible Amazon process S3 files loops BhavPath Game uses range(0,10,3)=0,3,6,9 logic", "code": '#include <stdio.h>\nint main(){\n    for(int i=0; i<10; i+=3) printf("%d ", i);\n    // Output: 0 3 6 9\n    return 0;\n}', "interview": "Q1 Output for(i=0;i<10;i+=3)? Ans 0 3 6 9\nQ2 For vs While? Ans For known While condition\nQ3 Do-While vs While? Ans Do-While at least once", "placement": "TCS NQT Pattern printing loops 10 marks Print 0 3 6 9 Infosys Loop array average BhavPath Game Collect 0,3,6,9!"},
    },
    "Python": {
        "Variables": {"theory": "Python Variables Complete Theory WHAT IS VARIABLE Container name given to memory location storing data value Unlike C Python variable does NOT need type declaration Python automatically detects type Dynamic Typing Example name='Bhavya' Python knows string btech=81 Python knows int No need int btech=81 like C Makes Python easy fast WHY SPECIAL DYNAMIC TYPING In C int btech=81 You must say int In Python btech=81 No need Python interpreter decides type at RUNTIME not compile time Dynamic vs Static C Advantage Fast coding less code For Data Engineering saves time TYPES Local Inside function Global Outside Instance Inside class self.btech=81 Class Variable Shared college='Rise College' RULES Start letter or underscore Cannot start number 1btech invalid btech1 valid _btech valid Can contain letters numbers underscore No space special char student btech invalid student_btech valid Case sensitive btech BTECH Btech different Cannot be keyword if for while def class import invalid Meaningful snake_case student_btech_percent not x y Constants CAPS PI=3.14 DATA TYPES int float str bool list tuple dict set TYPE CHECKING type() isinstance() Conversion int('81') Important Data Engineering REAL EXAMPLE TCS NQT Store 5 students B.Tech % check eligible >70% Tests variables list condition", "code": "name='Bhavya'\nbtech=81\nprint(f\"Name: {name}, B.Tech: {btech}%\")\n\nstudents=[81,75,60,90,55]\neligible=[s for s in students if s>70]\nprint(eligible) # [81,75,90]", "interview": "Q1 What is variable? Ans Container no type declaration dynamic typing\nQ2 Rules naming? Ans Start letter/_ no space special char case sensitive\nQ3 Dynamic vs static? Ans Dynamic runtime Static compile time", "placement": "TCS NQT Store student B.Tech % check eligibility >70% Tests variables list condition 5 marks Infosys What is dynamic typing Difference Python vs C Theory 3 marks Amazon Store millions records variables!"},
        "Loops": {"theory": "Python Loops Complete Theory Most Important 0,3,6,9 Logic WHAT IS LOOP Control structure repeats block multiple times Saves code Data Engineering lakhs records Without loops no Data Engineer job 40% programming TYPES FOR LOOP Known iterations for variable in sequence: code Sequence can be range() list string tuple dict Most Important range() Function Heart range(stop) range(10) => 0-9 range(start,stop) 0,10 => 0-9 range(start,stop,step) 0,10,3 => 0,3,6,9 Logic start=0 stop=10 till 9 step=3 0, 0+3=3, 3+3=6, 6+3=9 => 0,3,6,9 TCS NQT asks Output range(0,10,3)? Ans 0,3,6,9 Direct 2 marks BhavPath Real Game Collect green coins order 0,3,6,9 win Red bombs 1,2,4,5,7,8 avoid Data Engineering Process every 3rd record sampling Array Slicing arr[0:10:3] every 3rd element WHILE LOOP Condition based NESTED LOOPS Star pattern REAL PLACEMENT TCS NQT 10-15 marks Infosys 5 marks Amazon Must Game 0,3,6,9 LIST COMPREHENSION [i for i in range(0,10,3)]=[0,3,6,9] one line Pythonic", "code": "for i in range(0,10,3):\n    print(i)\n# Output:\n# 0\n# 3\n# 6\n# 9\n\nresult=[i for i in range(0,10,3)]\nprint(result) # [0,3,6,9]", "interview": "Q1 Output range(0,10,3)? Ans 0,3,6,9 Start 0 stop 10 till 9 step 3 MOST ASKED\nQ2 For vs While? Ans For known iterations While condition based\nQ3 Break vs Continue vs Pass? Ans Break exits Continue skips Pass placeholder", "placement": "TCS NQT Pattern printing star number pyramid 10-15 marks Output range(0,10,3) 0,3,6,9 direct 2 marks Infosys Loop array find >80% eligible 5 marks Amazon Process S3 files lakhs records loops Must BhavPath Game Collect 0,3,6,9 green coins win!"},
    },
    "DSA": {
        "Arrays": {"theory": "DSA Arrays Complete Theory Most Important for MAANG WHAT IS ARRAY Collection similar data types stored contiguous continuous adjacent memory locations Index starts 0 In Python list used as array Example [81,75,90,85,88] 5 integers continuous memory Array foundation DSA Without arrays no DSA no MAANG job Arrays 30% DSA interviews WHY HEART OF PLACEMENTS Amazon Google Flipkart Microsoft 100% DSA interviews start arrays TCS Digital Infosys SP Wipro Elite DSA coding rounds Arrays must Package Good DSA 10+ LPA Poor DSA 3.5 LPA TYPES One Dimensional Two Dimensional Matrix Dynamic Array Python list grows automatically Associative Array Dict OPERATIONS Access O(1) Fast Search O(n) Linear Insert Delete O(n) Shift Traversal O(n) Sorting O(n log n) INDEXING SLICING arr[0] First 81 arr[-1] Last 88 arr[0:10:3] Every 3rd Index 0,3,6,9 Values 81,85,78,90 Step 3 REAL PLACEMENT TCS Easy Reverse average max min Infosys Medium Rotation duplicates second largest Amazon Medium-Hard Second largest without sorting Merge sorted Missing Kadane Flipkart ETL Process array BhavPath Game Coins 0-9 Collect 0,3,6,9 green win Arrays 30% DSA", "code": "btech_scores=[81,75,90,85,88,92,78,85,90,88]\nprint(f\"First: {btech_scores[0]}\") #81\nprint(f\"Every 3rd [0:10:3]: {btech_scores[0:10:3]}\")\n# [81,85,78,90] Index 0,3,6,9", "interview": "Q1 What is array? Ans Collection similar types contiguous memory index 0\nQ2 Time complexity Access Search Insert Delete? Ans Access O(1) Search O(n) Insert Delete O(n)\nQ3 First last every 3rd? Ans First arr[0] Last arr[-1] Every 3rd arr[0:10:3] Index 0,3,6,9", "placement": "TCS Easy Reverse average max min 2 Qs 5 marks Infosys Medium Rotation duplicates second largest 3 Qs 10 marks Amazon Medium-Hard 10-15 LPA Second largest without sorting Merge sorted Missing Kadane Game 0,3,6,9 win Arrays 30% DSA!"},
    }
}

def is_certificate_locked():
    if st.session_state.xp < 150: return True, f"Need 150 XP - You have {st.session_state.xp}"
    if len(st.session_state.completed) < 3: return True, f"Complete 3 modules - You did {len(st.session_state.completed)}"
    if not st.session_state.game_unlocked: return True, "Complete 1 Test to unlock Game"
    return False, "Unlocked"

# WELCOME PAGE
if st.session_state.page == "welcome":
    st.markdown("""<div class="welcome-box"><div style="font-size:70px">🚀</div><div style="font-size:60px; font-weight:900">BhavPath</div><div style="font-size:28px; margin-top:10px; font-weight:600">Welcome to your placement story</div><div style="font-size:16px; margin-top:10px; opacity:0.9">Learn. Grind. Game. Get Placed.</div></div>""", unsafe_allow_html=True)
    st.markdown("<br>")
    st.markdown("""<div class="glass-premium" style="text-align: center; padding: 25px;"><div style="font-size:20px; font-weight:600; color:white; font-style: italic;">"Your placement story is not about being perfect, it's about being persistent. Every line of code you write today is a step closer to your dream offer."</div><div style="font-size:12px; color:#aaa; margin-top:10px">BHAVPATH PREMIUM</div></div>""", unsafe_allow_html=True)
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.page = "login"; st.rerun()
        if st.button("🔐 Admin Login", use_container_width=True):
            st.session_state.page = "admin_login"; st.rerun()
    st.stop()

# ADMIN LOGIN
if st.session_state.page == "admin_login":
    st.markdown('<div class="login-header"><div style="font-size:35px; font-weight:800">🔐 Admin Access</div><div>BhavPath Admin Panel</div></div>', unsafe_allow_html=True)
    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        username = st.text_input("Admin Username")
        password = st.text_input("Admin Password", type="password")
        st.info(f"Default: {ADMIN_USERNAME} / {ADMIN_PASSWORD}")
        if st.button("Login as Admin →", use_container_width=True, type="primary"):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.is_admin = True; st.session_state.page = "admin_dashboard"; st.rerun()
            else: st.error("Invalid credentials")
        if st.button("Back to Welcome"): st.session_state.page = "welcome"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ADMIN DASHBOARD
if st.session_state.page == "admin_dashboard":
    if not st.session_state.is_admin: st.error("Admin access required"); st.stop()
    st.markdown('<div style="background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); padding: 25px; border-radius: 20px; text-align: center; color: white;"><div style="font-size:32px; font-weight:900">🔐 Admin Dashboard</div><div>How many members opened your site</div></div>', unsafe_allow_html=True)
    users = load_user_data()
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Visitors", len(users))
    with c2: st.metric("Unique Emails", len(set([u['Email'] for u in users])) if users else 0)
    with c3: st.metric("Colleges", len(set([u['College'] for u in users])) if users else 0)
    with c4: 
        avg_xp = sum([int(u['XP']) if u['XP'].isdigit() else 0 for u in users]) / len(users) if users else 0
        st.metric("Avg XP", f"{avg_xp:.0f}")
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    st.markdown("#### 📊 All Visitors")
    if users: 
        st.dataframe(users, use_container_width=True)
        st.download_button("📥 Download CSV", data=open(USER_DATA_FILE, 'r').read() if os.path.exists(USER_DATA_FILE) else "No data", file_name="bhavpath_users.csv", mime="text/csv", use_container_width=True)
        if st.button("🗑️ Clear Data"): 
            if os.path.exists(USER_DATA_FILE): os.remove(USER_DATA_FILE)
            st.rerun()
    else: st.info("No visitors yet. Share your link!")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Logout Admin", use_container_width=True):
        st.session_state.is_admin = False; st.session_state.page = "welcome"; st.rerun()
    st.stop()

# LOGIN PAGE
if st.session_state.page == "login":
    st.markdown('<div class="login-header"><div style="font-size:35px; font-weight:800">🚀 BhavPath</div><div>Premium</div></div>', unsafe_allow_html=True)
    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:white; text-align:center;">🔐 Student Login</h3>', unsafe_allow_html=True)
        name = st.text_input("Full Name", value=st.session_state.name, placeholder="Bhavya")
        email = st.text_input("Email", value=st.session_state.email, placeholder="bhavya@gmail.com")
        college = st.text_input("College", value=st.session_state.college, placeholder="Rise College, Ongole")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if name and email and college:
                if email == ADMIN_EMAIL:
                    st.session_state.is_admin = True; st.session_state.page = "admin_dashboard"; st.rerun()
                st.session_state.name = name; st.session_state.email = email; st.session_state.college = college
                save_user_data(name, email, college, "login", 0)
                st.session_state.page = "purpose"; st.rerun()
            else: st.error("Fill all fields")
        if st.button("Back to Welcome"): st.session_state.page = "welcome"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# PURPOSE PAGE
if st.session_state.page == "purpose":
    st.markdown(f'<div class="login-header"><div style="font-size:30px; font-weight:800">🚀 BhavPath</div><div>Hi {st.session_state.name} 👋 | {st.session_state.college}</div></div>', unsafe_allow_html=True)
    is_locked, lock_msg = is_certificate_locked()
    st.markdown('<h4 style="color:white; text-align:center;">Why did you come to this link? Select Purpose:</h4>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("📊 Placement Percentage", use_container_width=True):
            st.session_state.purpose = "placement"; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, "placement", st.session_state.xp); st.session_state.page = "main"; st.rerun()
    with col2:
        if st.button("📚 Skill Learning", use_container_width=True):
            st.session_state.purpose = "skill"; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, "skill", st.session_state.xp); st.session_state.page = "main"; st.rerun()
    col3, col4 = st.columns(2, gap="large")
    with col3:
        if st.button("📝 Test Zone", use_container_width=True):
            st.session_state.purpose = "test"; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, "test", st.session_state.xp); st.session_state.page = "main"; st.rerun()
    with col4:
        if is_locked:
            st.markdown(f'<div style="background: rgba(239,68,68,0.15); border: 2px solid #ef4444; border-radius: 15px; padding: 20px; text-align: center; height: 75px; display: flex; align-items: center; justify-content: center; flex-direction: column;"><div style="font-size:22px">🔒</div><div style="font-size:11px; color:#ef4444; font-weight:700">Certificate Locked</div></div>', unsafe_allow_html=True)
            st.caption(f"🔒 {lock_msg}")
        else:
            if st.button("📜 Certificate Zone - Unlocked ✅", use_container_width=True):
                st.session_state.purpose = "certificate"; st.session_state.page = "main"; st.rerun()
    _, mid, _ = st.columns([1,1,1])
    with mid:
        if st.button("💼 Interview - Robot Zoom", use_container_width=True):
            st.session_state.purpose = "interview"; st.session_state.page = "main"; st.rerun()
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"; st.rerun()
    st.markdown("<br>")
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("XP", f"{st.session_state.xp}/150")
    with c2: st.metric("Modules", f"{len(st.session_state.completed)}/3")
    with c3: st.metric("Game", "Yes" if st.session_state.game_unlocked else "No")
    progress = min(100, int(st.session_state.xp/150*33 + len(st.session_state.completed)/3*33 + (33 if st.session_state.game_unlocked else 0)))
    st.progress(progress)
    st.write(f"Progress: {progress}%")
    if is_locked: st.error(f"🔒 {lock_msg}")
    else: st.success("🎉 Certificate Unlocked!"); st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

st.sidebar.markdown(f'<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 15px; border-radius: 15px; color: white; text-align: center;"><div style="font-size:22px; font-weight:800">🚀 BhavPath</div></div>', unsafe_allow_html=True)
st.sidebar.write(f"👤 {st.session_state.name} | 🎓 {st.session_state.college}")
st.sidebar.metric("XP", st.session_state.xp)
st.sidebar.metric("Modules", len(st.session_state.completed))
if st.sidebar.button("Change Purpose"): st.session_state.page = "purpose"; st.rerun()
if st.sidebar.button("Logout"): st.session_state.page = "welcome"; st.rerun()
if st.sidebar.button("🔐 Admin"): st.session_state.page = "admin_dashboard"; st.session_state.is_admin = True; st.rerun()

# SKILL LEARNING WITH 3 BOXES RIGHT SIDE + GEEKS STYLE PRACTICE (NO NAME)
if st.session_state.purpose == "skill":
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">📚 Skill Learning - 3 Box System</div></div>', unsafe_allow_html=True)
    left, middle, right = st.columns([1,2.5,1.2], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        selected_topic = st.radio("Select Skill - 6 Skills", ["C", "C++", "Python", "Java", "SQL", "DSA"], label_visibility="collapsed")
        st.markdown("<br>")
        selected_module = st.radio(f"Modules in {selected_topic}", TOPICS[selected_topic], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    with middle:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown(f'<div style="background: rgba(102,126,234,0.15); padding: 15px; border-radius: 12px; border-left: 4px solid #667eea; margin-bottom: 15px;"><div style="color:#667eea; font-size:11px; font-weight:700">MATERIAL HEADING</div><div style="color:white; font-size:24px; font-weight:800">{selected_topic} - {selected_module}</div></div>', unsafe_allow_html=True)
        data = FULL_DB.get(selected_topic, {}).get(selected_module, None)
        if not data:
            data = {"theory": f"{selected_module} in {selected_topic} Full Detailed Theory: {selected_module} is core fundamental concept in {selected_topic} Used to store process manage data Without {selected_module} cannot write program Building block Important for placements TCS NQT 2-3 questions Infosys SP mandatory Amazon 10-15 LPA advanced Real World Data Engineering Backend Frontend Data Science daily Example Code prints 0,3,6,9 using range(0,10,3) Step logic This is {selected_module} logic Used BhavPath Game Collect 0,3,6,9 green coins win! {selected_module} MUST for placements Master {selected_module} = Master {selected_topic} = Get Placed!", "code": f"# {selected_topic} - {selected_module}\nfor i in range(0,10,3):\n    print(i)\n# Output: 0,3,6,9", "interview": f"Q1 What is {selected_module}? Ans Core fundamental concept in {selected_topic}\nQ2 Why important? Ans TCS NQT 2-3 Qs Infosys SP mandatory Amazon advanced\nQ3 Example? Ans Code prints 0,3,6,9 using range(0,10,3) Most asked!", "placement": f"TCS NQT 2-3 questions on {selected_module} in {selected_topic} Infosys SP mandatory 5 marks Amazon Data Engineer 10-15 LPA Advanced {selected_module} Package Without {selected_module} 3.5 LPA With 7-15 LPA!"}
        if st.button(f"📖 Theory - {selected_topic} {selected_module} - Full Detailed - Click to Open", use_container_width=True, key="btn_theory"):
            st.session_state.open_theory = not st.session_state.open_theory
        if st.session_state.open_theory:
            st.markdown(f'<div style="background: rgba(15,12,41,0.9); border: 1px solid rgba(102,126,234,0.4); border-radius: 12px; padding: 20px; margin-bottom: 15px; max-height: 400px; overflow-y: auto;"><div style="color:#60a5fa; font-size:12px; font-weight:700; margin-bottom:10px;">📖 THEORY - FULL DETAILED</div><div style="color:white; font-size:14px; line-height:1.7; white-space: pre-wrap;">{data["theory"]}</div></div>', unsafe_allow_html=True)
        if st.button(f"💼 Interview Questions - Click to Open", use_container_width=True, key="btn_interview"):
            st.session_state.open_interview = not st.session_state.open_interview
        if st.session_state.open_interview:
            st.markdown(f'<div style="background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.4); border-radius: 12px; padding: 20px; margin-bottom: 15px;"><div style="color:#fbbf24; font-size:12px; font-weight:700; margin-bottom:10px;">💼 INTERVIEW QUESTIONS</div><div style="color:white; font-size:14px; line-height:1.8; white-space: pre-wrap;">{data["interview"]}</div></div>', unsafe_allow_html=True)
        if st.button(f"🏢 Placement - Company Wise - Click to Open", use_container_width=True, key="btn_placement"):
            st.session_state.open_placement = not st.session_state.open_placement
        if st.session_state.open_placement:
            st.markdown(f'<div style="background: rgba(74,222,128,0.1); border: 1px solid rgba(74,222,128,0.4); border-radius: 12px; padding: 20px; margin-bottom: 15px;"><div style="color:#4ade80; font-size:12px; font-weight:700; margin-bottom:10px;">🏢 PLACEMENT INFO</div><div style="color:white; font-size:14px; line-height:1.8; white-space: pre-wrap;">{data["placement"]}</div></div>', unsafe_allow_html=True)
        if st.button(f"💻 Code Examples - Click to Open", use_container_width=True, key="btn_code"):
            st.session_state.open_code = not st.session_state.open_code
        if st.session_state.open_code:
            st.code(data["code"], language="python")
            st.success("✅ Output: 0,3,6,9 - range(0,10,3) logic!")
        st.divider()
        key = f"{selected_topic}-{selected_module}"
        if key not in st.session_state.completed:
            if st.button(f"✅ Mark {selected_module} Completed +50 XP", type="primary", use_container_width=True):
                st.session_state.completed.append(key); st.session_state.xp+=50; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, f"skill-{selected_topic}", st.session_state.xp); st.balloons()
        else: st.success("✅ Completed")
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        PRACTICE_DB = {
            "C": {"Intro": '#include <stdio.h>\nint main() {\n    printf("Hello World\\n");\n    return 0;\n}\n// Task: Print college name', "Variables": '#include <stdio.h>\nint main() {\n    int btech=81;\n    printf("B.Tech: %d%%\\n", btech);\n    return 0;\n}\n// Task: Create 10th, Inter, B.Tech vars', "Loops": '#include <stdio.h>\nint main() {\n    for(int i=0; i<10; i+=3) printf("%d ", i);\n    // Output: 0 3 6 9\n    return 0;\n}\n// Task: Print even 0-10', "Arrays": '#include <stdio.h>\nint main() {\n    int arr[]={81,75,90,85,88};\n    int sum=0;\n    for(int i=0;i<5;i++) sum+=arr[i];\n    printf("Avg: %.2f", sum/5.0);\n    return 0;\n}\n// Task: Find max'},
            "Python": {"Variables": 'name="Bhavya"\ncollege="Rise College"\nbtech=81\nprint(f"Name: {name}, B.Tech: {btech}%")\n# Task: Check eligibility >70\nstudents=[81,75,60,90,55]\neligible=[s for s in students if s>70]\nprint(eligible)', "Loops": 'print("range(0,10,3):")\nfor i in range(0,10,3):\n    print(i)\n# [0,3,6,9]\nresult=[i for i in range(0,10,3)]\nprint(result)\n# Task: Print 0-20 step 4', "Lists": 'btech_scores=[81,75,90,85,88,92]\nprint(f"First: {btech_scores[0]}")\nprint(f"Last: {btech_scores[-1]}")\nprint(f"Every 3rd: {btech_scores[0:6:3]}")\navg=sum(btech_scores)/len(btech_scores)\nprint(f"Avg: {avg:.2f}")\neligible=[s for s in btech_scores if s>80]\nprint(f"Eligible >80%: {eligible}")'},
            "Java": {"Intro": 'public class Main{\n    public static void main(String[] args){\n        System.out.println("BhavPath Java");\n    }\n}\n// Task: Print B.Tech 81%', "Variables": 'public class Main{\n    public static void main(String[] args){\n        String name="Bhavya";\n        int btech=81;\n        System.out.println(name+" "+btech+"%");\n    }\n}'},
            "SQL": {"Basics": '-- Avg B.Tech\nSELECT AVG(btech) FROM students;\n-- >70% eligible\nSELECT name,btech FROM students WHERE btech>70 ORDER BY btech DESC;\n-- Task: Find max', "Joins": 'SELECT s.name,p.company FROM students s INNER JOIN placements p ON s.id=p.student_id WHERE s.btech>70;'},
            "DSA": {"Arrays": '# DSA Arrays\narr=[81,75,90,85,88,92]\nmax_val=max(arr)\nprint(f"Max: {max_val}")\nreversed_arr=arr[::-1]\nprint(f"Reversed: {reversed_arr}")\narr2=[10,20,30,40,50,60,70,80,90,100]\nprint(f"Every 3rd: {arr2[0:10:3]}")\n# [10,40,70,100]\n# Task: Find second largest'},
            "C++": {"Intro": '#include <bits/stdc++.h>\nusing namespace std;\nint main(){cout<<"BhavPath C++"; return 0;}', "STL": '#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n    vector<int> arr={0,3,6,9};\n    arr.push_back(12);\n    for(int x:arr) cout<<x<<" ";\n    return 0;\n}\n// Output: 0 3 6 9 12'}
        }
        default_code = f"# {selected_topic} - {selected_module} Practice\nfor i in range(0,10,3):\n    print(i)\n# Output: 0,3,6,9"
        practice_code_default = PRACTICE_DB.get(selected_topic, {}).get(selected_module, default_code)
        st.markdown(f'<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 18px; border-radius: 15px; color: white; text-align: center; margin-bottom: 12px;"><div style="font-size:28px">📊</div><div style="font-size:12px; opacity:0.8;">CURRENT MODULE</div><div style="font-size:16px; font-weight:800;">{selected_topic} - {selected_module}</div></div>', unsafe_allow_html=True)
        is_completed = f"{selected_topic}-{selected_module}" in st.session_state.completed
        st.markdown(f'<div style="background: {"linear-gradient(135deg, #4ade80 0%, #22c55e 100%)" if is_completed else "linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)"}; padding: 18px; border-radius: 15px; color: white; text-align: center; margin-bottom: 12px;"><div style="font-size:28px">{"✅" if is_completed else "⏳"}</div><div style="font-size:15px; font-weight:800;">{"Completed" if is_completed else "Not Completed"}</div><div style="font-size:22px; font-weight:900; margin-top:8px;">{st.session_state.xp} XP</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-premium" style="padding: 18px !important;"><div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;"><div style="font-size:22px">💻</div><div style="color:white; font-weight:800; font-size:15px;">Practice Editor - {selected_topic}</div></div><div style="background: rgba(102,126,234,0.2); padding: 8px; border-radius: 8px; margin-bottom:12px;"><div style="color:#aaa; font-size:11px;">📝 Task: Practice {selected_module} in {selected_topic} | Run below</div></div>', unsafe_allow_html=True)
        practice_code = st.text_area("Practice Code", value=practice_code_default, height=220, label_visibility="collapsed", key=f"practice_{selected_topic}_{selected_module}")
        if st.button("▶️ Run Code", use_container_width=True, type="primary", key="run_practice_new"):
            try:
                import io, sys
                old_stdout = sys.stdout; sys.stdout = buffer = io.StringIO()
                if selected_topic in ["C", "C++", "Java", "SQL"]:
                    sys.stdout = old_stdout
                    st.info(f"📋 {selected_topic} Code Preview:")
                    st.code(practice_code, language=selected_topic.lower() if selected_topic!="C++" else "cpp")
                    st.success("💡 Use local compiler for C/C++/Java | For SQL use MySQL")
                    st.markdown(f'<div style="background: rgba(74,222,128,0.1); padding: 12px; border-radius: 10px;"><div style="color:#4ade80; font-size:12px; font-weight:700;">Expected Output Logic:</div><div style="color:white; font-size:11px;">range(0,10,3)=0,3,6,9 logic similar in {selected_topic}</div></div>', unsafe_allow_html=True)
                else:
                    exec(practice_code); sys.stdout = old_stdout
                    output = buffer.getvalue() or "No output - Add print()"
                    st.success("✅ Output:"); st.code(output, language="text")
            except Exception as e:
                sys.stdout = old_stdout; st.error(f"❌ Error: {e}")
        st.markdown('<div style="background: rgba(102,126,234,0.15); padding: 10px; border-radius: 10px; margin-top:12px; border:1px dashed rgba(102,126,234,0.3);"><div style="color:#aaa; font-size:11px;">🎯 Practice: Print 0,3,6,9 | Avg array | Eligibility >70% | Reverse | Used TCS NQT Infosys Amazon</div></div></div>', unsafe_allow_html=True)

elif st.session_state.purpose == "placement":
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">📊 Placement Percentage - Advanced</div><div style="font-size:14px; opacity:0.9">10th + Inter + B.Tech + Skills</div></div>', unsafe_allow_html=True)
    COMPANIES_DB = [
        {"name": "TCS Ninja", "min_10th": 60, "min_inter": 60, "min_btech": 60, "skills": ["C"], "package": "3.5 LPA", "color": "#4ade80"},
        {"name": "TCS Digital", "min_10th": 70, "min_inter": 70, "min_btech": 70, "skills": ["C", "Python", "DSA"], "package": "7 LPA", "color": "#667eea"},
        {"name": "Infosys SP", "min_10th": 65, "min_inter": 65, "min_btech": 65, "skills": ["Python", "Java", "SQL"], "package": "5-9 LPA", "color": "#fbbf24"},
        {"name": "Wipro Elite", "min_10th": 60, "min_inter": 60, "min_btech": 60, "skills": ["Java", "C++"], "package": "3.5-6 LPA", "color": "#a78bfa"},
        {"name": "Amazon Data Engineer", "min_10th": 75, "min_inter": 70, "min_btech": 70, "skills": ["Python", "SQL", "DSA"], "package": "10-15 LPA", "color": "#f472b6"},
        {"name": "Flipkart SDE", "min_10th": 70, "min_inter": 70, "min_btech": 70, "skills": ["DSA", "Python", "Java"], "package": "12-20 LPA", "color": "#60a5fa"},
    ]
    left, right = st.columns([1, 1.8], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        tenth = st.number_input("10th %", 0, 100, 85)
        inter = st.number_input("Inter %", 0, 100, 82)
        btech = st.number_input("B.Tech %", 0, 100, 81)
        st.divider()
        skill_c = st.checkbox("C", value=True); skill_cpp = st.checkbox("C++", value=False); skill_python = st.checkbox("Python", value=True)
        skill_java = st.checkbox("Java", value=False); skill_sql = st.checkbox("SQL", value=True); skill_dsa = st.checkbox("DSA", value=False)
        selected_skills = []
        if skill_c: selected_skills.append("C")
        if skill_cpp: selected_skills.append("C++")
        if skill_python: selected_skills.append("Python")
        if skill_java: selected_skills.append("Java")
        if skill_sql: selected_skills.append("SQL")
        if skill_dsa: selected_skills.append("DSA")
        check_btn = st.button("🔍 Check Companies", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        if check_btn:
            st.session_state.xp += 10; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, "placement", st.session_state.xp)
            eligible = []
            for comp in COMPANIES_DB:
                perc_ok = (tenth >= comp["min_10th"] and inter >= comp["min_inter"] and btech >= comp["min_btech"])
                skill_match = len(set(selected_skills) & set(comp["skills"])) > 0 if selected_skills else True
                if perc_ok and skill_match: eligible.append(comp)
            if eligible:
                st.success(f"✅ Eligible for {len(eligible)} companies!")
                for comp in eligible:
                    st.markdown(f"<div style='background: rgba(255,255,255,0.08); border-left: 5px solid {comp['color']}; border-radius: 15px; padding: 15px; margin-bottom: 10px;'><div style='color:white; font-weight:800'>{comp['name']} ✅</div><div style='color:#aaa; font-size:12px'>Package: {comp['package']} | Skills: {', '.join(comp['skills'])}</div></div>", unsafe_allow_html=True)
            else: st.error("❌ No companies matched!")
        else: st.info("Enter details and click Check")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.purpose == "test":
    st.markdown('<h2 style="color:white">📝 Test Zone + Real Game</h2>', unsafe_allow_html=True)
    TEST_BANK = {"C": [{"q": "for(i=0;i<10;i+=3) output?", "o": ["0 3 6 9", "0 1 2"], "a": "0 3 6 9"}], "Python": [{"q": "range(0,10,3)?", "o": ["0,3,6,9", "0,1,2"], "a": "0,3,6,9"}], "DSA": [{"q": "LIFO?", "o": ["Stack", "Queue"], "a": "Stack"}]}
    if not st.session_state.test_started and not st.session_state.game_unlocked:
        c1,c2,c3 = st.columns(3, gap="large")
        with c1:
            if st.button("C Language", use_container_width=True): st.session_state.test_skill="C"
            if st.button("Python", use_container_width=True): st.session_state.test_skill="Python"
        with c2:
            if st.button("C++", use_container_width=True): st.session_state.test_skill="C++"
            if st.button("DSA", use_container_width=True): st.session_state.test_skill="DSA"
        with c3:
            if st.button("SQL", use_container_width=True): st.session_state.test_skill="SQL"
            if st.button("Java", use_container_width=True): st.session_state.test_skill="Java"
        if st.session_state.test_skill:
            if st.button(f"Start {st.session_state.test_skill} Test →", type="primary", use_container_width=True):
                st.session_state.test_started=True; st.rerun()
    elif st.session_state.test_started and not st.session_state.game_unlocked:
        skill = st.session_state.test_skill; questions = TEST_BANK.get(skill, TEST_BANK["Python"])
        for i,q in enumerate(questions):
            st.markdown(f'<div class="glass-premium"><b>Q{i+1}. {q["q"]}</b></div>', unsafe_allow_html=True)
            ans = st.radio("Select", q['o'], key=f"tq_{i}", index=None)
            if ans: st.session_state.test_answers[i]=ans
        if st.button("Submit & Unlock Game", type="primary", use_container_width=True):
            st.session_state.game_unlocked=True; st.session_state.test_started=False; st.session_state.xp+=50; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, "test", st.session_state.xp); st.balloons(); st.rerun()
    else:
        game_html = """<!DOCTYPE html><html><head><style>body{margin:0;background:#0f0c29;display:flex;justify-content:center;align-items:center;flex-direction:column}#gameCanvas{border:4px solid #667eea;border-radius:20px;background:#1a1a4e}#info{color:white;margin:10px;text-align:center;background:rgba(255,255,255,0.1);padding:12px 24px;border-radius:15px}</style></head><body><div id="info"><div>Score: <span id="score" style="color:#4ade80">0</span> | Target: <b style="color:#4ade80">0,3,6,9</b> | Lives: <span id="lives">3</span></div></div><canvas id="gameCanvas" width="600" height="400"></canvas><div id="message" style="color:#fbbf24; font-weight:bold; margin-top:10px"></div><script>const canvas=document.getElementById('gameCanvas');const ctx=canvas.getContext('2d');const scoreEl=document.getElementById('score');const livesEl=document.getElementById('lives');const messageEl=document.getElementById('message');let player={x:300,y:200,size:22,speed:6,color:'#667eea'};let keys={};let score=0;let lives=3;let collected=[];let targetSequence=[0,3,6,9];let coins=[];function spawnCoins(){coins=[];[0,3,6,9].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:true,size:20,color:'#4ade80',collected:false})});[1,2,4,5,7,8].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:false,size:17,color:'#ef4444',collected:false})});}function drawPlayer(){ctx.fillStyle=player.color;ctx.beginPath();ctx.arc(player.x,player.y,player.size,0,Math.PI*2);ctx.fill();}function drawCoins(){coins.forEach(coin=>{if(!coin.collected){ctx.fillStyle=coin.color;ctx.beginPath();ctx.arc(coin.x,coin.y,coin.size,0,Math.PI*2);ctx.fill();ctx.fillStyle='white';ctx.font='bold 14px Poppins';ctx.textAlign='center';ctx.fillText(coin.value,coin.x,coin.y+5);}});}function checkCollision(){coins.forEach(coin=>{if(!coin.collected){let dx=player.x-coin.x,dy=player.y-coin.y,dist=Math.sqrt(dx*dx+dy*dy);if(dist<player.size+coin.size){coin.collected=true;if(coin.isCorrect){if(collected.length<targetSequence.length&&coin.value===targetSequence[collected.length]){collected.push(coin.value);score+=25;messageEl.textContent=`Correct!`;messageEl.style.color='#4ade80';}else{lives--;}}else{lives--;}updateUI();if(JSON.stringify(collected)===JSON.stringify(targetSequence)){messageEl.textContent='WIN! +100 XP!';}if(lives<=0){messageEl.textContent='Game Over!';}}}});}function updateUI(){scoreEl.textContent=score;livesEl.textContent=lives;}function update(){if(keys['ArrowUp']||keys['w'])player.y-=player.speed;if(keys['ArrowDown']||keys['s'])player.y+=player.speed;if(keys['ArrowLeft']||keys['a'])player.x-=player.speed;if(keys['ArrowRight']||keys['d'])player.x+=player.speed;player.x=Math.max(player.size,Math.min(canvas.width-player.size,player.x));player.y=Math.max(player.size,Math.min(canvas.height-player.size,player.y));ctx.clearRect(0,0,canvas.width,canvas.height);drawCoins();drawPlayer();checkCollision();requestAnimationFrame(update);}window.addEventListener('keydown',e=>{keys[e.key]=true;});window.addEventListener('keyup',e=>{keys[e.key]=false;});spawnCoins();update();</script></body></html>"""
        components.html(game_html, height=580, width=650)
        if st.button("Claim Win +100 XP", use_container_width=True): st.session_state.xp+=100; save_user_data(st.session_state.name, st.session_state.email, st.session_state.college, "game", st.session_state.xp); st.balloons()

elif st.session_state.purpose == "certificate":
    is_locked, lock_msg = is_certificate_locked()
    if is_locked:
        st.markdown(f"""<div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); padding: 30px; border-radius: 20px; text-align: center; color: white;"><div style="font-size:60px">🔒</div><div style="font-size:32px; font-weight:900">Certificate Locked</div><div>{lock_msg}</div></div>""", unsafe_allow_html=True)
        st.markdown('<div class="glass-premium" style="text-align:center; padding:40px;">', unsafe_allow_html=True)
        st.markdown("### Requirements: 150 XP + 3 Modules + Game Unlocked")
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Your XP", st.session_state.xp)
        with c2: st.metric("Modules", len(st.session_state.completed))
        with c3: st.metric("Game", "Unlocked" if st.session_state.game_unlocked else "Locked")
        if st.button("📚 Go to Skill Learning", use_container_width=True, type="primary"): st.session_state.purpose = "skill"; st.rerun()
        if st.button("📝 Go to Test Zone", use_container_width=True): st.session_state.purpose = "test"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.stop()
    st.markdown('<div style="background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%); padding: 25px; border-radius: 20px; text-align: center; color: white;"><div style="font-size:32px; font-weight:900">📜 Certificate Unlocked ✅</div></div>', unsafe_allow_html=True)
    st.balloons()
    st.markdown(f'<div style="background:white; border-radius:20px; padding:40px; text-align:center"><div style="font-size:50px">🏆</div><div style="font-size:36px; font-weight:900; color:#667eea">BHAVPATH PREMIUM</div><div style="letter-spacing:3px; color:#666">CERTIFICATE OF EXCELLENCE</div><div style="font-size:28px; font-weight:800; margin-top:15px">{st.session_state.name}</div><div style="color:#555">{st.session_state.college} | {st.session_state.email}</div><div style="margin:20px">XP: {st.session_state.xp} | Modules: {len(st.session_state.completed)}</div><div style="background:#f0f4ff; padding:15px; border-radius:15px; color:green; font-weight:800">PLACEMENT READY - UNLOCKED AFTER HARD WORK</div></div>', unsafe_allow_html=True)

else:
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white;"><div style="font-size:32px; font-weight:900">💼 AI Interview - Robot Zoom</div></div>', unsafe_allow_html=True)
    robot_html = """<!DOCTYPE html><html><head><style>body{background:#0f0c29; color:white; font-family:Poppins; text-align:center; padding:20px;} .robot{width:110px;height:110px;background:linear-gradient(135deg,#667eea,#764ba2);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:60px;margin:20px auto;}</style></head><body><div class="robot">🤖</div><div>BhavPath AI Robot - Senior Interviewer</div><div style="margin-top:20px; background: rgba(102,126,234,0.2); padding:15px; border-radius:10px;">Q1. Tell me about yourself and explain range(0,10,3)=0,3,6,9 logic?</div></body></html>"""
    components.html(robot_html, height=400)
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    interview_skills = st.selectbox("Select Interview Type", ["Python Developer", "Java Developer", "SQL Data Engineer"])
    current_q = st.text_area("Your Answer", placeholder="Myself Bhavya from Rise College...", height=120)
    if current_q and len(current_q) > 20:
        if st.button("📜 Submit Interview & Get Certificate", use_container_width=True, type="primary"):
            st.session_state.cert_skill = interview_skills; st.session_state.cert_score = 88; st.session_state.cert_stage = "result"; st.session_state.purpose = "certificate"; st.balloons(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
