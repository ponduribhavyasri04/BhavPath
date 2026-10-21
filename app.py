import streamlit as st

st.set_page_config(page_title="BhavPath - Topic Wise", layout="wide", page_icon="🚀")

st.markdown("""
<style>
    .stApp { background: #0a0e1a; }
    .top-bar { background: linear-gradient(90deg, #1e3a8a, #0ea5e9); color: white !important; padding: 16px 22px; border-radius: 14px; font-weight: 900; display:flex; justify-content:space-between; }
    .glass { background: rgba(255,255,255,0.06); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 16px; color: white !important; }
    .content-dark { background: #111827; border: 1px solid #1f2937; padding: 20px; border-radius: 14px; color: #e5e7eb !important; }
    .topic-item { background: rgba(255,255,255,0.05); border-left: 3px solid #0ea5e9; padding: 10px 12px; margin-bottom: 8px; border-radius: 8px; font-size: 13px; color: #e5e7eb; cursor: pointer; }
    .topic-item:hover { background: rgba(56,189,248,0.15); border-left-color: #22c55e; }
    div.stButton > button { background: linear-gradient(90deg, #2563eb, #0ea5e9) !important; color: white !important; border: none !important; border-radius: 10px !important; font-weight: 800 !important; height: 46px; }
    .gfg-box { background: white; color: black !important; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .gfg-box h2, .gfg-box h3, .gfg-box p, .gfg-box li { color: black !important; }
    .gfg-box pre { background: #f8fafc; padding: 12px; border-radius: 8px; border: 1px solid #e2e8f0; }
</style>
""", unsafe_allow_html=True)

# ===== TOPIC-WISE DETAILED CONTENT - GEEKSFORGEEKS STYLE =====
TOPIC_DETAILS = {
    "C": {
        "10. File Handling": {
            "title": "C File Handling - GeeksforGeeks Style",
            "content": """
**File Handling in C - Last Updated 26 Aug 2026**

File handling is used to store data permanently.

**Why File Handling?**
- Data loss avoid cheyyadaniki
- Real projects lo must

**Functions:**
- fopen() - open file
- fclose() - close
- fprintf() - write
- fscanf() - read

**Example:**
            """,
            "code": '#include <stdio.h>\nint main(){\n FILE *fp = fopen("bhavpath.txt", "w");\n fprintf(fp, "BhavPath 82%% Power");\n fclose(fp);\n printf("File Written!");\n return 0;\n}',
            "interview": "**Q:** fopen modes? -> r, w, a, r+, w+, a+"
        },
        "11. Dynamic Memory - malloc, calloc": {
            "title": "Dynamic Memory Allocation in C - malloc, calloc, free",
            "content": """
**Dynamic Memory - Last Updated**

C lo memory runtime lo allocate cheyyadam.

**malloc():**
- Single block: malloc(100)
- Garbage value untundi

**calloc():**
- Multiple blocks: calloc(5, sizeof(int))
- Zero tho fill chestundi

**free():**
- Memory free cheyyali - lekapothe memory leak

**TCS NQT Pattern:** malloc use chesi array create cheyyamantaru.
            """,
            "code": '#include <stdio.h>\n#include <stdlib.h>\nint main(){\n int *p = (int*)malloc(5 * sizeof(int));\n for(int i=0;i<5;i++) p[i]=i+1;\n for(int i=0;i<5;i++) printf("%d ", p[i]);\n free(p);\n return 0;\n}',
            "interview": "**Q:** malloc vs calloc? **Q:** What is memory leak? **Q:** Why free() needed?"
        },
        "12. TCS NQT Coding Patterns": {
            "title": "TCS NQT Coding Patterns in C - BhavPath Original",
            "content": """
**TCS NQT lo adige C Patterns**

1. **Reverse String**
2. **Factorial, Prime Check**
3. **Array Duplicates Remove**
4. **File Handling + malloc combine**

**BhavPath Tip:** 82% power unna neeku TCS NQT easy - daily 2 patterns practice cheyyi.

**Pattern List:**
- Reverse, Palindrome
- Factorial, Fibonacci
- File Handling
            """,
            "code": '#include <stdio.h>\n// TCS Pattern: Reverse + Factorial\nint main(){\n char s[]="BhavPath";\n for(int i=5;i>=0;i--) printf("%c", s[i]);\n return 0;\n}',
            "interview": "**TCS Coding Round:** 1 coding Q - File handling or malloc based vastundi - 30 mins"
        }
    },
    "Python": {
        "12. TCS/Infosys Patterns - Reverse, Duplicates": {
            "title": "Python TCS/Infosys Patterns",
            "content": "Python lo TCS patterns - Reverse, Duplicates remove, etc.",
            "code": 's="BhavPath"\nprint(s[::-1])\nprint(list(set([1,1,2])))',
            "interview": "Q: How to remove duplicates? -> set()"
        }
    }
}

FULL_TOPICS = {
    "C": ["01. C Basics - History & Setup", "02. Data Types, Variables", "03. Input/Output - printf, scanf", "04. Operators", "05. If-Else, Loops", "06. Functions", "07. Arrays & Strings", "08. Pointers - TCS Important", "09. Structures & Unions", "10. File Handling", "11. Dynamic Memory - malloc, calloc", "12. TCS NQT Coding Patterns"],
    "Python": ["01. Python Basics", "02. Data Types - list, tuple, dict", "03. Loops", "04. Functions", "05. OOPs", "06. File Handling", "07. Libraries", "08. Exception", "09. Decorators", "10. Django", "11. AI/ML Intro", "12. TCS/Infosys Patterns - Reverse, Duplicates"],
    "C++": ["01. C++ Basics", "02. Data Types", "03. Loops", "04. Class, Object", "05. Inheritance", "06. Encapsulation", "07. STL - vector, map - MUST", "08. Pointers", "09. Exception", "10. File", "11. CP Tricks", "12. Wipro Patterns"],
    "Java": ["01. Java Basics JVM", "02. Data Types", "03. Loops", "04. Class Object", "05. Inheritance", "06. Abstraction", "07. String", "08. Collections", "09. Exception", "10. Multithreading", "11. Spring", "12. Accenture Patterns"],
    "SQL": ["01. SQL Basics", "02. SELECT", "03. INSERT", "04. Constraints", "05. Keys", "06. JOINs - MUST", "07. GROUP BY", "08. Aggregate", "09. Subqueries", "10. Indexes", "11. Views", "12. TCS SQL Qs"],
    "DSA": ["01. What is DSA?", "02. Complexity", "03. Arrays", "04. Linked List", "05. Stack Queue", "06. Sorting", "07. Searching", "08. Strings", "09. Recursion", "10. Trees", "11. Graphs", "12. DP Basics"]
}

COMPANIES = [
    {"name":"TCS NQT", "min":60, "pkg":"7 LPA", "color":"#22c55e"},
    {"name":"Infosys SP", "min":65, "pkg":"9 LPA", "color":"#a855f7"},
    {"name":"Wipro", "min":60, "pkg":"3.5 LPA", "color":"#f59e0b"},
]

if "page" not in st.session_state: st.session_state.page="login"
if "skill" not in st.session_state: st.session_state.skill="C"
if "mode" not in st.session_state: st.session_state.mode="Learn"
if "selected_topic" not in st.session_state: st.session_state.selected_topic=None

# 1. LOGIN
if st.session_state.page=="login":
    st.markdown('<div class="top-bar"><span>BHAVPATH • ADVANCED</span><span>820 XP</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass" style="max-width:420px; margin:30px auto; text-align:center;"><h3>Login</h3>', unsafe_allow_html=True)
    mail = st.text_input("Mail")
    college = st.text_input("College")
    if st.button("Launch →", use_container_width=True):
        st.session_state.mail=mail; st.session_state.college=college; st.session_state.page="profile"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 2. PROFILE
if st.session_state.page=="profile":
    st.markdown(f'<div class="top-bar"><span>BHAVPATH | {st.session_state.college}</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass" style="max-width:700px; margin:20px auto;">', unsafe_allow_html=True)
    percent = st.slider("Your Power %", 40, 100, 82)
    skills = st.multiselect("Select Skills", list(FULL_TOPICS.keys()), default=["C","Python"])
    if st.button("Show Companies →", use_container_width=True):
        st.session_state.percent=percent; st.session_state.skills=skills; st.session_state.page="companies"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. COMPANIES
if st.session_state.page=="companies":
    p = st.session_state.percent
    st.markdown(f'<div class="top-bar"><span>BHAVPATH • {p}% POWER</span><span>{", ".join(st.session_state.skills)}</span></div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, comp in enumerate(COMPANIES):
        if p >= comp["min"]:
            with cols[i%3]:
                st.markdown(f'<div class="glass" style="text-align:center;"><h4>{comp["name"]}</h4><p>{comp["pkg"]}</p></div>', unsafe_allow_html=True)
                if st.button(f"Enter {comp['name']}", key=comp["name"], use_container_width=True):
                    st.session_state.company=comp; st.session_state.page="detail"; st.session_state.skill=st.session_state.skills[0]; st.session_state.selected_topic=None; st.rerun()
    st.stop()

# 4. SKILL PAGE WITH TOPIC CLICK -> TOPIC PAGE
if st.session_state.page=="detail":
    comp = st.session_state.company
    st.markdown(f'<div class="top-bar"><span>BHAVPATH X {comp["name"]} • ORBIT ACTIVE</span><span>{st.session_state.percent}% MATCH</span></div>', unsafe_allow_html=True)

    # Skill select
    scols = st.columns(len(st.session_state.skills))
    for i, s in enumerate(st.session_state.skills):
        if scols[i].button(s, key=f"sk_{s}", type="primary" if st.session_state.skill==s else "secondary", use_container_width=True):
            st.session_state.skill=s; st.session_state.selected_topic=None; st.session_state.mode="Learn"; st.rerun()

    curr = st.session_state.skill

    # IF TOPIC SELECTED -> SHOW GEEKSFORGEEKS STYLE TOPIC PAGE
    if st.session_state.selected_topic:
        topic = st.session_state.selected_topic
        detail = TOPIC_DETAILS.get(curr, {}).get(topic, None)
        # If no specific detail, create generic
        if not detail:
            detail = {
                "title": f"{topic} - {curr} - BhavPath",
                "content": f"**{topic}**\n\nFull tutorial for {curr} - {topic}. This is like GeeksforGeeks page but BhavPath original.\n\n- What is {topic}?\n- Why important for {comp['name']}?\n- How to use?\n\n**BhavPath Tip:** {curr} lo {topic} TCS NQT lo 100% adugutaru.",
                "code": f'// {curr} - {topic}\n// Practice code for {topic}\nprintf("{curr} {topic} - 82%% Power");',
                "interview": f"Q: What is {topic}? Q: Explain {topic} in {curr}?"
            }
        
        st.markdown(f'<div class="gfg-box"><h2>{detail["title"]}</h2><p style="color:gray; font-size:12px;">Last Updated: 26 Aug 2026 | {curr} | {comp["name"]} | BhavPath Original</p><hr>', unsafe_allow_html=True)
        st.markdown(f'<div class="gfg-box">{detail["content"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="gfg-box">', unsafe_allow_html=True)
        st.markdown("**Example Code:**")
        st.code(detail["code"])
        st.markdown("**Interview Qs:**")
        st.markdown(detail["interview"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("← Back to Topic List"): 
            st.session_state.selected_topic=None
            st.rerun()
        st.stop()

    # NORMAL - TOPIC LIST
    m1, m2, m3 = st.columns(3)
    with m1:
        if st.button("📖 Learn Story", use_container_width=True, type="primary" if st.session_state.mode=="Learn" else "secondary"): st.session_state.mode="Learn"; st.rerun()
    with m2:
        if st.button("💻 Code Lab", use_container_width=True, type="primary" if st.session_state.mode=="Code" else "secondary"): st.session_state.mode="Code"; st.rerun()
    with m3:
        if st.button("🎯 Interview", use_container_width=True, type="primary" if st.session_state.mode=="Crack" else "secondary"): st.session_state.mode="Crack"; st.rerun()

    left, right = st.columns([1.6, 1])
    with left:
        st.markdown('<div class="content-dark">', unsafe_allow_html=True)
        if st.session_state.mode=="Learn":
            st.markdown(f"### {curr} - Click any Topic to Open Full Page (like GFG)")
            topics = FULL_TOPICS[curr]
            for topic in topics:
                if st.button(topic, key=f"topic_{topic}", use_container_width=True):
                    st.session_state.selected_topic=topic
                    st.rerun()
            st.markdown("---")
            st.markdown(f"**C - The Foundation - Story Mode**\n\n1972 - Dennis Ritchie - Bell Labs.\n\nWhy Mother? Java, PHP, JS, C++ anni C nundi vachayi.")
        elif st.session_state.mode=="Code":
            st.markdown(f"### {curr} - Practice Code")
            st.code(f'// {curr} Practice\nprintf("BhavPath {curr} - 82% Power");')
        else:
            st.markdown(f"### {curr} - Interview Qs for {comp['name']}")
            st.markdown("TCS Qs: pointer? malloc vs calloc?")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown(f'<div class="glass"><h4>{comp["name"]} Mission</h4><p>Package: {comp["pkg"]} | You: {st.session_state.percent}%</p><p style="color:#7dd3fc;">Skill: {curr}<br>Click topic to open like GeeksforGeeks</p></div>', unsafe_allow_html=True)

    if st.button("← Back to Companies"): st.session_state.page="companies"; st.rerun()
