import streamlit as st

st.set_page_config(page_title="BhavPath Advanced Final", layout="wide", page_icon="🚀")

st.markdown("""
<style>
    .stApp { background: #0a0e1a; }
    .top-bar { background: linear-gradient(90deg, #1e3a8a, #0ea5e9); color: white !important; padding: 16px 22px; border-radius: 14px; font-weight: 900; display:flex; justify-content:space-between; }
    .glass { background: rgba(255,255,255,0.06); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 16px; color: white !important; }
    .content-dark { background: #111827; border: 1px solid #1f2937; padding: 20px; border-radius: 14px; color: #e5e7eb !important; }
    .topic-item { background: rgba(255,255,255,0.05); border-left: 3px solid #0ea5e9; padding: 9px 12px; margin-bottom: 7px; border-radius: 6px; font-size: 13px; color: #e5e7eb; }
    div.stButton > button { background: linear-gradient(90deg, #2563eb, #0ea5e9) !important; color: white !important; border: none !important; border-radius: 10px !important; font-weight: 800 !important; height: 46px; }
    p, li, h3, h4, h2 { color: #e5e7eb !important; }
</style>
""", unsafe_allow_html=True)

# ===== FULL DATABASE - 6 SKILLS + TOPIC LIST =====
FULL_DATA = {
    "C": {
        "topics": ["01. C Basics - History & Setup (1972 Dennis Ritchie)", "02. Data Types, Variables", "03. Input/Output - printf, scanf", "04. Operators", "05. If-Else, Loops - for, while", "06. Functions", "07. Arrays & Strings", "08. Pointers - Important for TCS", "09. Structures & Unions", "10. File Handling", "11. Dynamic Memory - malloc, calloc", "12. TCS NQT Coding Patterns"],
        "story": "**C - The Foundation - Story Mode**\n\n1972 - Dennis Ritchie - Bell Labs - UNIX kosam create chesadu.\n\n**Why Mother of Languages?**\n- Java, PHP, JS, C++ anni C nundi vachayi\n- Pointers ante intlo address - direct memory magic\n- OS, Embedded, Compilers, Game Engines antha C lone\n\n**Real World:**\n01 Unreal Engine - Low-level performance\n02 Epic Games - Rendering & AI\n03 Physics Engines - Realistic movement",
        "code": '#include <stdio.h>\n// Practice 1: Print Power\nint main(){\n int power=82;\n printf("BhavPath %d%% Power - TCS Ready\\n", power);\n // Practice 2: Factorial - TCS Pattern\n int n=5,f=1;\n for(int i=1;i<=n;i++) f*=i;\n printf("Fact %d", f);\n return 0;\n}',
        "interview": "**TCS NQT - C Interview Qs**\n\n**Q1:** What is pointer? -> Stores address\n**Q2:** malloc vs calloc? -> malloc single, calloc multiple + zero\n**Q3:** Dangling pointer? -> Points to freed memory\n**Q4:** Why C is mid-level? -> Low-level + High-level features\n**Q5:** Storage classes? -> auto, static, extern, register"
    },
    "Python": {
        "topics": ["01. Python Basics & Setup - 1991 Guido", "02. Variables, Data Types - list, tuple, dict", "03. Loops & Conditions", "04. Functions & Lambda", "05. OOPs in Python", "06. File Handling", "07. Libraries - numpy, pandas", "08. Exception Handling", "09. Decorators & Generators", "10. Django Basics - Web", "11. AI/ML Intro", "12. TCS/Infosys Patterns - Reverse, Duplicates"],
        "story": "**Python - The Simple King**\n\n1991 - Guido van Rossum - Simple like Telugu.\n- English lanti syntax: print('Hello')\n- Instagram, YouTube, Netflix backend Python\n- AI/ML antha Python lone\n\n**Use:** AI, Data Science, Automation, Web",
        "code": '# Practice 1: Reverse - TCS Pattern\ns="BhavPath"\nprint(s[::-1])\n\n# Practice 2: Remove Duplicates\nlst=[1,1,2,3,2]\nprint(list(set(lst)))\n\n# Practice 3: Factorial\ndef fact(n): return 1 if n==0 else n*fact(n-1)\nprint(fact(5))',
        "interview": "**Infosys - Python Qs**\n\n**Q1:** list vs tuple? -> List mutable, Tuple immutable\n**Q2:** Decorator? -> Function modifies function\n**Q3:** PEP8? -> Python style guide\n**Q4:** lambda? -> lambda x: x*2\n**Q5:** What is GIL?"
    },
    "C++": {
        "topics": ["01. C++ Basics - C with OOPs - 1985 Bjarne", "02. Data Types & Operators", "03. Loops, Functions", "04. OOPs - Class, Object", "05. Inheritance, Polymorphism", "06. Encapsulation, Abstraction", "07. STL - vector, map, set - TCS MUST", "08. Pointers & References", "09. Exception Handling", "10. File Handling", "11. Competitive Programming Tricks", "12. Wipro Coding Patterns"],
        "story": "**C++ - Power + Speed**\n\n1985 - Bjarne Stroustrup - C with OOPs\n- Fast + Objects\n- Game dev, Competitive Programming king\n- STL - TCS lo must",
        "code": '#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n // TCS NQT C++ Pattern - Unique\n vector<int> v={1,2,2,3};\n sort(v.begin(), v.end());\n v.erase(unique(v.begin(), v.end()), v.end());\n for(int x:v) cout<<x<<\" \";\n return 0;\n}',
        "interview": "**Wipro - C++ Qs**\n\n**Q1:** OOPs pillars? -> 4 pillars\n**Q2:** Virtual function?\n**Q3:** STL? -> Standard Template Library\n**Q4:** vector vs array?"
    },
    "Java": {
        "topics": ["01. Java Basics & JVM, JDK, JRE - 1995 James Gosling", "02. Data Types, Variables", "03. Operators, Loops", "04. OOPs - Class, Object", "05. Inheritance, Polymorphism", "06. Encapsulation, Abstraction", "07. String vs StringBuilder", "08. Collections - ArrayList, HashMap", "09. Exception Handling", "10. Multithreading", "11. Spring Basics", "12. Accenture Coding Patterns"],
        "story": "**Java - Job Machine**\n\n1995 - James Gosling - WORA - Write Once Run Anywhere\n- Platform Independent - JVM valla\n- Android, Banking Systems - Infosys, Accenture\n- 5-9 LPA jobs easy",
        "code": 'class Main{\n public static void main(String[] args){\n  System.out.println("BhavPath Java - 82% Power");\n  String s="BhavPath";\n  System.out.println(new StringBuilder(s).reverse());\n }\n}',
        "interview": "**Accenture - Java Qs**\n\n**Q1:** JDK vs JRE vs JVM?\n**Q2:** String vs StringBuilder? -> immutable vs mutable\n**Q3:** OOPs 4 pillars?\n**Q4:** Exception Handling?"
    },
    "SQL": {
        "topics": ["01. SQL Basics - What is DB?", "02. SELECT, WHERE, ORDER BY", "03. INSERT, UPDATE, DELETE", "04. Data Types & Constraints", "05. Primary Key, Foreign Key", "06. JOINs - INNER, LEFT, RIGHT, FULL - TCS MUST", "07. GROUP BY, HAVING", "08. Aggregate - COUNT, SUM, AVG", "09. Subqueries", "10. Indexes", "11. Views & Stored Procedures", "12. TCS/Infosys SQL Real Qs"],
        "story": "**SQL - Data King**\n\nStructured Query Language - Database kosam\n- Every company lo data undi - SQL must\n- SELECT * FROM students WHERE percent>=82\n- JOIN - TCS lo 100% adugutaru",
        "code": '-- Practice 1: Filter 82% students\nSELECT * FROM students WHERE percent >= 82;\n\n-- Practice 2: Group By - TCS Pattern\nSELECT company, COUNT(*) FROM placements GROUP BY company;\n\n-- Practice 3: JOIN\nSELECT s.name, c.package FROM students s JOIN companies c ON s.company_id=c.id;',
        "interview": "**Capgemini - SQL Qs**\n\n**Q1:** What is JOIN? Types?\n**Q2:** Primary vs Foreign key?\n**Q3:** GROUP BY vs ORDER BY?\n**Q4:** What is Index?"
    },
    "DSA": {
        "topics": ["01. What is DSA? Why Important for Placement?", "02. Time & Space Complexity - O(n), O(log n)", "03. Arrays - TCS Fav Topic", "04. Linked List - Single, Double", "05. Stack & Queue", "06. Sorting - Bubble, Merge, Quick Sort", "07. Searching - Binary Search", "08. Strings - Pattern Problems", "09. Recursion", "10. Trees & Binary Trees", "11. Graphs - BFS, DFS", "12. DP Basics - Infosys SP Must"],
        "story": "**DSA - Interview Clearance**\n\nData Structures + Algorithms - Placement Heart\n- Arrays, Linked List, Stack, Queue\n- Sorting, Searching\n- Graphs, Trees - Infosys SP must\n- Company coding round antha DSA lone\n\n**Tip:** C/Python lo DSA nerchuko - package double",
        "code": '# Practice 1: Binary Search - TCS NQT\ndef binary_search(arr, x):\n l,r=0,len(arr)-1\n while l<=r:\n  m=(l+r)//2\n  if arr[m]==x: return m\n  elif arr[m]<x: l=m+1\n  else: r=m-1\n return -1\n\narr=[2,3,4,10,40]\nprint(binary_search(arr, 10))\n\n# Practice 2: Reverse Array - Wipro Pattern',
        "interview": "**TCS Digital - DSA Qs**\n\n**Q1:** Time complexity of Binary Search? -> O(log n)\n**Q2:** Array vs Linked List?\n**Q3:** Stack vs Queue?\n**Q4:** Explain Bubble Sort?\n**Q5:** What is Recursion?"
    }
}

COMPANIES = [
    {"name":"TCS NQT", "min":60, "pkg":"7 LPA", "color":"#22c55e"},
    {"name":"Infosys SP", "min":65, "pkg":"9 LPA", "color":"#a855f7"},
    {"name":"Wipro", "min":60, "pkg":"3.5 LPA", "color":"#f59e0b"},
    {"name":"Accenture", "min":65, "pkg":"4.5 LPA", "color":"#06b6d4"},
    {"name":"Capgemini", "min":55, "pkg":"4 LPA", "color":"#ef4444"},
]

if "page" not in st.session_state: st.session_state.page="login"
if "skill" not in st.session_state: st.session_state.skill="C"
if "mode" not in st.session_state: st.session_state.mode="Learn"

# 1. LOGIN
if st.session_state.page=="login":
    st.markdown('<div class="top-bar"><span>BHAVPATH • ADVANCED • 82% POWER</span><span>820 XP</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass" style="max-width:420px; margin:30px auto; text-align:center;"><h3 style="color:white;">Login - Mail + College</h3>', unsafe_allow_html=True)
    mail = st.text_input("📧 Mail", placeholder="student@gmail.com")
    college = st.text_input("🎓 College Name", placeholder="Ongole College")
    if st.button("Launch Orbit →", use_container_width=True):
        if "@" in mail and len(college)>2:
            st.session_state.mail=mail; st.session_state.college=college; st.session_state.page="profile"; st.rerun()
        else: st.error("Valid Mail & College pettu")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 2. PERCENT + SKILL - 6 SKILLS
if st.session_state.page=="profile":
    st.markdown(f'<div class="top-bar"><span>BHAVPATH | {st.session_state.college}</span><span>{st.session_state.mail}</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass" style="max-width:700px; margin:20px auto;">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:white;">Your Power & Skills</h3>', unsafe_allow_html=True)
    percent = st.slider("Your Power %", 40, 100, 82)
    skills = st.multiselect("Select Skills - 6 Languages (C, Python, C++, Java, SQL, DSA)", list(FULL_DATA.keys()), default=["C","Python"])
    if st.button("Show Eligible Companies →", use_container_width=True):
        if skills:
            st.session_state.percent=percent; st.session_state.skills=skills; st.session_state.page="companies"; st.rerun()
        else: st.error("Atleast 1 skill select cheyyi")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. COMPANY LIST - Same as your screenshot
if st.session_state.page=="companies":
    p = st.session_state.percent
    st.markdown(f'<div class="top-bar"><span>BHAVPATH • {p}% POWER</span><span>{", ".join(st.session_state.skills)} • 820 XP</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="glass" style="margin-top:12px; text-align:center;"><h2 style="color:white; margin:0;">Eligible Companies - {p}% Base</h2><p style="color:#94a3b8; margin:5px 0 0 0;">Your Skills: {", ".join(st.session_state.skills)}</p></div>', unsafe_allow_html=True)
    st.write("")
    cols = st.columns(3)
    for i, comp in enumerate(COMPANIES):
        if p >= comp["min"]:
            with cols[i % 3]:
                st.markdown(f"""
                <div class="glass" style="text-align:center; margin-bottom:12px;">
                    <div style="width:80px; height:80px; border-radius:50%; background: conic-gradient({comp['color']} 85%, #1f2937 0); display:flex; align-items:center; justify-content:center; margin:auto;">
                        <div style="width:60px; height:60px; background:#0f172a; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:800; flex-direction:column;"><span>85%</span><span style="font-size:9px;">READY</span></div>
                    </div>
                    <h4 style="margin:10px 0 0 0; color:white;">{comp['name']}</h4>
                    <p style="color:#94a3b8; font-size:12px; margin:2px 0;">Need {comp['min']}% • {comp['pkg']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Enter {comp['name']} Orbit", key=comp["name"], use_container_width=True):
                    st.session_state.company=comp; st.session_state.page="detail"; st.session_state.skill=st.session_state.skills[0]; st.session_state.mode="Learn"; st.rerun()
    if st.button("← Change Skills"): st.session_state.page="profile"; st.rerun()
    st.stop()

# 4. SKILL PAGE - LEARN STORY WITH TOPIC LIST + CODE + INTERVIEW
if st.session_state.page=="detail":
    comp = st.session_state.company
    st.markdown(f'<div class="top-bar"><span>BHAVPATH X {comp["name"]} • ORBIT ACTIVE</span><span>{st.session_state.percent}% MATCH • {comp["pkg"]}</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; margin:0 0 10px 0; font-size:13px;">Select Skill Orbit - Python aithe Python Story, C aithe C Story - Full Original:</p>', unsafe_allow_html=True)
    scols = st.columns(len(st.session_state.skills))
    for i, s in enumerate(st.session_state.skills):
        if scols[i].button(s, key=f"sk_{s}", use_container_width=True, type="primary" if st.session_state.skill==s else "secondary"):
            st.session_state.skill=s; st.session_state.mode="Learn"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # 3 Modes
    m1, m2, m3 = st.columns(3)
    with m1:
        if st.button("📖 Learn Story", use_container_width=True, type="primary" if st.session_state.mode=="Learn" else "secondary"): st.session_state.mode="Learn"; st.rerun()
    with m2:
        if st.button("💻 Code Lab - Practice", use_container_width=True, type="primary" if st.session_state.mode=="Code" else "secondary"): st.session_state.mode="Code"; st.rerun()
    with m3:
        if st.button("🎯 Crack Interview", use_container_width=True, type="primary" if st.session_state.mode=="Crack" else "secondary"): st.session_state.mode="Crack"; st.rerun()

    curr = st.session_state.skill
    d = FULL_DATA[curr]

    left, right = st.columns([1.6, 1])
    with left:
        st.markdown('<div class="content-dark">', unsafe_allow_html=True)
        if st.session_state.mode=="Learn":
            st.markdown(f"### {curr} - Complete Topics List")
            for topic in d["topics"]:
                st.markdown(f'<div class="topic-item">{topic}</div>', unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(d["story"])
            if st.button(f"Start {curr} Chapter 1 → +20 XP", use_container_width=True): st.balloons(); st.success(f"{curr} Started! Rise {st.session_state.percent}% → {st.session_state.percent+3}%")
        elif st.session_state.mode=="Code":
            st.markdown(f"### {curr} - Practice Code + Run")
            st.code(d["code"], language="python" if curr in ["Python","DSA"] else "c")
            if st.button(f"▶️ Run {curr} Code - Earn 20 XP", use_container_width=True): st.balloons(); st.success(f"{curr} Code Executed! +20 XP | TCS Pattern Done")
        else:
            st.markdown(f"### {curr} - Interview Questions for {comp['name']}")
            st.markdown(d["interview"])
            st.info(f"BhavPath Tip: Ivi {comp['name']} lo adigina real Qs - {curr} lo prepare ayyi 100% crack")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown(f"""
        <div class="glass">
            <h4 style="color:white; margin:0;">{comp['name']} Mission</h4>
            <p style="color:#94a3b8; font-size:12px; margin:5px 0;">Package: {comp['pkg']}<br>Need: {comp['min']}%+<br>Your Power: {st.session_state.percent}%<br>Skill: {curr}</p>
            <div style="width:90px; height:90px; border-radius:50%; background: conic-gradient({comp['color']} 85%, #1f2937 0); display:flex; align-items:center; justify-content:center; margin:15px auto;">
                <div style="width:70px; height:70px; background:#0f172a; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:800; flex-direction:column;"><span>READY</span><span style="font-size:10px; color:#22c55e;">85%</span></div>
            </div>
            <p style="color:#7dd3fc; font-size:12px; text-align:center;">BhavPath Rise: 81% → 85%<br>820 XP + 50 XP on {curr}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
        doubt = st.text_input(f"Ask {curr} Doubt (Telugu ok)", placeholder=f"Ex: {curr} lo pointers ante?")
        if doubt: st.info(f"AI Answer for {curr}: {doubt} - Simple ga {curr} lo idi...")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("← Back to Companies", use_container_width=True): st.session_state.page="companies"; st.rerun()
