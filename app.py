import streamlit as st

st.set_page_config(page_title="BhavPath - Graphics Mode", layout="wide", page_icon="🚀")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&family=JetBrains+Mono&display=swap');
.stApp { background: radial-gradient(ellipse at top left, #1e1b4b 0%, #0f172a 20%, #020617 60%, #000000 100%); overflow-x: hidden; }
.stApp::before { content: ''; position: fixed; top:0; left:0; width:100%; height:100%; background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><circle cx="50" cy="50" r="1" fill="rgba(99,102,241,0.3)"/></svg>'); opacity: 0.3; pointer-events: none; z-index: -1; }

.top-graphics { background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 25%, #06b6d4 50%, #22c55e 100%); padding: 16px 24px; border-radius: 18px; color: white; font-family: 'Space Grotesk'; font-weight: 900; font-size: 15px; display:flex; justify-content:space-between; align-items:center; box-shadow: 0 0 40px rgba(99,102,241,0.6), 0 0 80px rgba(6,182,214,0.3); animation: glowOrbit 3s ease-in-out infinite; position: relative; overflow: hidden; }
.top-graphics::before { content: ''; position: absolute; top:-50%; left:-50%; width:200%; height:200%; background: linear-gradient(45deg, transparent, rgba(255,255,255,0.15), transparent); transform: rotate(45deg); animation: shine 3s infinite; }
@keyframes glowOrbit { 0%,100% { box-shadow: 0 0 30px rgba(99,102,241,0.5);} 50% { box-shadow: 0 0 60px rgba(6,182,214,0.7), 0 0 100px rgba(99,102,241,0.3);} }
@keyframes shine { 0% { transform: translateX(-100%) rotate(45deg);} 100% { transform: translateX(100%) rotate(45deg);} }

.card-glass { background: rgba(255,255,255,0.07); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.15); border-radius: 20px; padding: 18px; color: white; box-shadow: 0 8px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1); transition: all 0.4s cubic-bezier(0.4,0,0.2,1); position: relative; overflow: hidden; }
.card-glass::before { content: ''; position: absolute; top:0; left:0; width:100%; height:1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent); }
.card-glass:hover { transform: translateY(-4px) scale(1.01); box-shadow: 0 16px 50px rgba(99,102,241,0.4), 0 0 0 1px rgba(99,102,241,0.3); border-color: rgba(99,102,241,0.4); }

.white-graphics { background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%); border-radius: 18px; padding: 22px; color: #0f172a; box-shadow: 0 10px 40px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.8); border: 1px solid #e2e8f0; position: relative; }
.white-graphics::before { content: ''; position: absolute; top:0; left:0; width:100%; height:4px; background: linear-gradient(90deg, #6366f1, #06b6d4, #22c55e); border-radius: 18px 18px 0 0; }
.white-graphics h1, .white-graphics h2, .white-graphics h3, .white-graphics p, .white-graphics b, .white-graphics li { color: #0f172a !important; font-family: 'Space Grotesk'; }

.code-neon { background: linear-gradient(145deg, #020617, #0f172a); border: 1px solid #334155; border-left: 4px solid #22c55e; border-radius: 14px; padding: 16px; color: #7dd3fc; font-family: 'JetBrains Mono'; font-size: 13px; box-shadow: inset 0 0 20px rgba(34,197,94,0.08), 0 4px 20px rgba(0,0,0,0.3); position: relative; }
.code-neon::before { content: '● ● ●'; position: absolute; top:8px; right:12px; color: #475569; font-size:10px; letter-spacing:3px; }

.orbit-ring { width:100px; height:100px; border-radius:50%; background: conic-gradient(from 0deg, #6366f1, #06b6d4, #22c55e, #f59e0b, #6366f1); display:flex; align-items:center; justify-content:center; margin:auto; animation: rotate 8s linear infinite; box-shadow: 0 0 30px rgba(99,102,241,0.5); }
.orbit-ring-inner { width:76px; height:76px; background:#0f172a; border-radius:50%; display:flex; align-items:center; justify-content:center; flex-direction:column; color:white; font-weight:900; animation: counterRotate 8s linear infinite; }
@keyframes rotate { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
@keyframes counterRotate { 0% { transform: rotate(0deg);} 100% { transform: rotate(-360deg);} }

.star-glow { color: #fbbf24; text-shadow: 0 0 10px rgba(251,191,36,0.8), 0 0 20px rgba(251,191,36,0.4); font-size: 22px; animation: starTwinkle 2s ease-in-out infinite; }
@keyframes starTwinkle { 0%,100% { transform: scale(1);} 50% { transform: scale(1.2);} }

.xp-neon { background: linear-gradient(90deg, #22c55e, #16a34a); padding: 8px 18px; border-radius: 24px; font-weight: 900; color: white; box-shadow: 0 0 20px rgba(34,197,94,0.6), 0 0 40px rgba(34,197,94,0.3); font-family: 'Space Grotesk'; animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%,100% { transform: scale(1);} 50% { transform: scale(1.05);} }

div.stButton > button { background: linear-gradient(90deg, #6366f1 0%, #06b6d4 100%) !important; color: white !important; border: none !important; border-radius: 12px !important; font-weight: 800 !important; height: 46px !important; font-family: 'Space Grotesk' !important; box-shadow: 0 0 25px rgba(99,102,241,0.5) !important; transition: all 0.3s !important; }
div.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 0 35px rgba(99,102,241,0.7) !important; }
</style>
""", unsafe_allow_html=True)

FULL_DATA = {
 "Python": [
  {"id":"01","title":"Introduction - What is Python?","icon":"🐍","info":"Python is high-level interpreted language created by Guido van Rossum in 1991. Simple English syntax. Used in Instagram, YouTube, Netflix, AI, Data Science. For 81% best to crack TCS NQT 7 LPA.","more":"Advantages: Easy 50% less code than C, huge libraries Pandas, NumPy, high salary 9 LPA, future proof AI. History: Named after Monty Python show, not snake. GFG Advantage: BhavPath has game + stars + graphics, GFG only text.","codes":[{"name":"Hello World - Graphics","code":'print("🐍 Hello Python")\nprint("🚀 BhavPath 81% Power - Graphics Mode")\nprint("✨ Super Cool Orbit Active")'}, {"name":"TCS Eligibility - Real Use","code":'percent = int(input("Enter %: "))\nif percent >= 60:\n print(f"🚀 Eligible for TCS NQT 7 LPA - {percent}%")\nelse:\n print("Improve")'}, {"name":"List Operations - Stars","code":'nums = [81,82,85,81,81]\nprint(f"Original: {nums}")\nprint(f"Unique: {list(set(nums))}")\nprint(f"Stars: ⭐⭐⭐ for this code")'}],
   "interview":[{"q":"What is PEP8? - Graphics Q","a":"PEP8 is Python Enhancement Proposal 8 - Style guide - 4 spaces indentation, 79 chars line, naming conventions. Graphics mode helps visualize clean code."},{"q":"list vs tuple?","a":"List mutable [] can change, tuple immutable () cannot. List slower, tuple faster. Graphics: List like editable whiteboard, tuple like printed certificate."},{"q":"What is GIL?","a":"Global Interpreter Lock - One thread at a time in CPython. Limits multi-threading."}],
   "prev":[{"year":"TCS NQT 2024","q":"Reverse string without [::-1] - Real","a":'s="BhavPath"\nrev=""\nfor ch in s:\n rev=ch+rev\nprint(f"Reverse: {rev} - Graphics: {rev[::-1]}")'}, {"year":"Infosys SP 2024","q":"Remove duplicates and sort - Real","a":'nums=[1,1,2,3,2,5]\nunique=sorted(set(nums))\nprint(f"Clean: {unique} - Stars: ⭐⭐⭐")'}]},
  {"id":"02","title":"File Handling - Graphics","icon":"📁","info":"File handling stores data permanently. open(), read(), write(), close(). Modes w=write overwrite, r=read, a=append add at end. Real projects use daily for logs. Graphics: Visual file cabinet.","more":"Why important? TCS 2024 asked file write/read. Best practice: with open() as f: auto close - Graphics shows auto close animation. Error handling: try-except FileNotFoundError - Graphics shows error glow.","codes":[{"name":"Write File - Graphics","code":'f=open("bhavpath_graphics.txt","w")\nf.write("🚀 BhavPath 81% Power\\n")\nf.write("🎨 Graphics Mode\\n")\nf.write("📁 File Handling")\nf.close()\nprint("✨ File Written with Graphics!")'}, {"name":"Read File - Visual","code":'f=open("bhavpath_graphics.txt","r")\ncontent=f.read()\nprint(f"📖 Content:\\n{content}")\nf.close()'}, {"name":"With Statement - Best Practice Graphics","code":'with open("bhavpath_graphics.txt","r") as f:\n print("🔍 Reading with auto close - Graphics Mode")\n for line in f:\n  print(f"  → {line.strip()}")'}],
   "interview":[{"q":"w vs a mode? Graphics","a":"w overwrites deletes old like new paint, a appends adds at end like adding sticker - keeps old."},{"q":"Why close file?","a":"Free memory, save to disk, prevent corruption. Graphics: Close = lock file cabinet."}],
   "prev":[{"year":"TCS NQT 2024","q":"Write % to file and read - Real","a":'with open("data.txt","w") as f:\n f.write("College: Ongole\\nPercent: 81%\\nGraphics Mode")\nwith open("data.txt","r") as f:\n print(f.read())'}]},
 ],
 "C": [
  {"id":"01","title":"Introduction - Dennis Ritchie 1972 - Graphics","icon":"🔵","info":"C created by Dennis Ritchie 1972 at Bell Labs for UNIX. Mother of all languages. Fast, powerful, close to hardware, procedural. Graphics: Old computer with glowing screen 1972.","more":"Why mother? All languages borrowed loops, functions from C. Advantages: Fastest, portable. Disadvantages: No OOPs, manual memory. For 81% must for TCS - 60% Qs C based. Graphics: C is foundation orbit.","codes":[{"name":"Hello C - Graphics Orbit","code":'#include <stdio.h>\nint main(){\n printf("🔵 Hello C - Graphics Mode\\n");\n printf("🚀 BhavPath 81%% - Super Cool\\n");\n printf("📅 1972 - Dennis Ritchie\\n");\n return 0;\n}'}, {"name":"Eligibility - Visual","code":'#include <stdio.h>\nint main(){\n int p=81;\n printf("📊 Your %%: %d\\n", p);\n if(p>=60) printf("🚀 Eligible for TCS 7 LPA - Graphics Orbit Ready");\n return 0;\n}'}],
   "interview":[{"q":"Why C is mother? Graphics","a":"All modern languages borrowed from C - 1972 first - Like root of tree - Graphics: C is central orbit, others revolve around."}], "prev":[{"year":"TCS 2024","q":"Print Hello World","a":'#include <stdio.h>\nint main(){printf("Hello World - Graphics"); return 0;}'}]},
  {"id":"02","title":"Pointers - HIGH PRIORITY - Graphics Visual","icon":"🎯","info":"Pointers store address. &a=address, *p=value at address. int a=81; int *p=&a; p stores address like house address, *p=81 value inside house. Most important for TCS - Graphics: Pointer is like map pin pointing to house.","more":"Types: Null NULL, Dangling freed memory - Graphics shows broken link, Wild uninitialized - Graphics shows question mark, Void generic. malloc dynamic memory - Graphics shows expanding memory block. TCS asks swap using pointers - Visual swap animation.","codes":[{"name":"Basic Pointer - Visual Map","code":'#include <stdio.h>\nint main(){\n int a=81;\n int *p=&a;\n printf("🏠 a=%d (house value)\\n", a);\n printf("📍 *p=%d (value at pin)\\n", *p);\n printf("🗺️ p=%p (pin location)\\n", p);\n return 0;\n}'}, {"name":"Swap using Pointers - TCS Q - Graphics","code":'#include <stdio.h>\nvoid swap(int *x,int *y){int t=*x;*x=*y;*y=t; printf("🔄 Swapped using pointer pins\\n");}\nint main(){int a=5,b=10;printf("Before: %d %d\\n",a,b);swap(&a,&b);printf("After: %d %d - Graphics Swap",a,b);}'}],
   "interview":[{"q":"What is dangling pointer? Graphics","a":"Points to freed memory - free(p) but using p - Graphics shows pin pointing to demolished house - crash."}], "prev":[{"year":"TCS 2024","q":"Swap using pointers - Visual","a":'#include <stdio.h>\nvoid swap(int *a,int *b){int t=*a;*a=*b;*b=t;}'}]},
 ],
 "C++": [{"id":"01","title":"C++ - Bjarne 1985 - Graphics Orbit","icon":"💜","info":"C++ is C with OOPs by Bjarne Stroustrup 1985. Fast + OOPs. STL must for TCS - vector, map - Graphics: C++ orbit around C with extra rings for OOPs.","more":"Why? STL helps crack coding fast - Graphics: STL like toolbox with ready tools.","codes":[{"name":"Hello C++ - Graphics","code":'#include <bits/stdc++.h>\nusing namespace std;\nint main(){cout<<"💜 C++ Graphics Orbit - BhavPath";}'}],"interview":[{"q":"What is STL? Graphics","a":"Standard Template Library - vector, map, set - Like ready-made graphics blocks."}],"prev":[{"year":"Wipro 2024","q":"Sort using STL","a":'vector<int> v={3,1,2}; sort(v.begin(), v.end());'}]}],
 "Java": [{"id":"01","title":"Java - Gosling 1995 - Graphics","icon":"☕","info":"Java by James Gosling 1995. WORA Write Once Run Anywhere - JVM - Graphics: Java orbit with JVM as engine. Used in Android, banking, Infosys 5-9 LPA.","more":"JDK dev kit, JRE run env, JVM executes bytecode - Graphics: JDK is factory, JRE is showroom, JVM is engine.","codes":[{"name":"Hello Java - Graphics","code":'class Main{public static void main(String[] a){System.out.println("☕ Java Graphics Orbit - 81%");}}'}],"interview":[{"q":"JDK vs JRE vs JVM? Graphics","a":"JDK factory to build, JRE showroom to run, JVM engine that runs - Graphics visual."}],"prev":[{"year":"Infosys 2024","q":"Reverse in Java","a":'String s="Bhav"; System.out.println(new StringBuilder(s).reverse());'}]}],
}

COMPANIES = [{"name":"TCS NQT","min":60,"pkg":"7 LPA","color":"#22c55e","desc":"Needs C, Python, DSA - Graphics Orbit"},{"name":"Infosys SP","min":65,"pkg":"9 LPA","color":"#a855f7","desc":"Needs Python, Java, DSA - Purple Orbit"},{"name":"Wipro","min":60,"pkg":"3.5 LPA","color":"#f59e0b","desc":"Needs C, C++, SQL - Orange Orbit"}]

if "page" not in st.session_state: st.session_state.page="login1"
if "skill" not in st.session_state: st.session_state.skill=""
if "topic_idx" not in st.session_state: st.session_state.topic_idx=0
if "xp" not in st.session_state: st.session_state.xp=820
if "stars" not in st.session_state: st.session_state.stars={}
if "done" not in st.session_state: st.session_state.done=set()

# PAGE 1: EMAIL + COLLEGE - GRAPHICS
if st.session_state.page=="login1":
 st.markdown('<div class="top-graphics"><span>🚀 BHAVPATH GRAPHICS MODE - STEP 1: EMAIL & COLLEGE - ORBIT ACTIVE</span><span class="xp-neon">820 XP • LVL 4</span></div>', unsafe_allow_html=True)
 st.markdown('<div class="card-glass" style="max-width:520px; margin:40px auto; text-align:center;"><div class="orbit-ring"><div class="orbit-ring-inner"><span>🚀</span><span style="font-size:10px;">ORBIT</span></div></div><h2 style="margin-top:16px;">Step 1: Email & College Name - Graphics Orbit</h2><p style="font-size:12px; color:#94a3b8;">First page only email and college - Graphics mode with orbit rings, glow, particles</p>', unsafe_allow_html=True)
 mail=st.text_input("📧 Email - Graphics Input", placeholder="student@gmail.com - Graphics mode")
 clg=st.text_input("🎓 College Name - Orbit", placeholder="Ongole College - Graphics orbit")
 if st.button("Next → Skills & Percentage - Graphics Orbit →",use_container_width=True,type="primary"):
  if "@" in mail and len(clg)>2:
   st.session_state.mail=mail; st.session_state.college=clg; st.session_state.page="login2"; st.rerun()
  else: st.error("Enter valid email and college - Graphics validation")
 st.markdown('</div>', unsafe_allow_html=True)
 st.stop()

# PAGE 2: SKILLS + PERCENTAGE - GRAPHICS
if st.session_state.page=="login2":
 st.markdown(f'<div class="top-graphics"><span>🚀 GRAPHICS MODE - STEP 2: SKILLS & % - {st.session_state.college} - ORBIT</span><span class="xp-neon">{st.session_state.xp} XP</span></div>', unsafe_allow_html=True)
 st.markdown('<div class="card-glass" style="max-width:560px; margin:30px auto;"><div style="text-align:center;"><div class="orbit-ring" style="width:80px; height:80px;"><div class="orbit-ring-inner" style="width:60px; height:60px;"><span>💫</span></div></div></div><h2>Step 2: Skills and Percentage - Graphics Orbit</h2><p style="font-size:12px; color:#94a3b8;">Second page - Skills + Percentage - Graphics with skill orbs</p>', unsafe_allow_html=True)
 perc=st.slider("📊 Your BTech Percentage - Graphics Slider with Orbit",40,100,81)
 skills=st.multiselect("🛠 Select Skills (C, C++, Python, Java, SQL, DSA) - Graphics Orbs", ["Python","C","C++","Java","SQL","DSA"], default=["Python","C"])
 # Graphics skill orbs
 cols=st.columns(4)
 for i,sk in enumerate(skills):
  with cols[i%4]:
   st.markdown(f'<div class="card-glass" style="text-align:center; padding:10px; margin-top:8px;"><div style="font-size:28px;">{"🐍" if sk=="Python" else "🔵" if sk=="C" else "💜" if sk=="C++" else "☕"}</div><p style="font-size:11px; margin:4px 0 0 0;">{sk}<br><span style="color:#94a3b8;">Orbit Ready</span></p></div>', unsafe_allow_html=True)
 c1,c2=st.columns(2)
 with c1:
  if st.button("← Back - Orbit",use_container_width=True): st.session_state.page="login1"; st.rerun()
 with c2:
  if st.button("Next → Companies - Graphics →",use_container_width=True,type="primary"):
   if len(skills)>0:
    st.session_state.percent=perc; st.session_state.selected_skills=skills; st.session_state.page="companies"; st.rerun()
   else: st.error("Select at least 1 skill - Graphics")
 st.markdown('</div>', unsafe_allow_html=True)
 st.stop()

# PAGE 3: COMPANIES - GRAPHICS ORBITS
if st.session_state.page=="companies":
 p=st.session_state.percent
 st.markdown(f'<div class="top-graphics"><span>🚀 STEP 3: COMPANIES FOR {p}% - {st.session_state.college} - GRAPHICS ORBITS</span><span class="xp-neon">{st.session_state.xp} XP</span></div>', unsafe_allow_html=True)
 st.markdown(f'<div class="card-glass"><h2>Step 3: Eligible Companies for {p}% - Graphics Orbits</h2><p>Based on {p}% and {", ".join(st.session_state.selected_skills)} - Each company is an orbit ring - Click to enter orbit - Graphics mode</p></div>', unsafe_allow_html=True)
 cols=st.columns(3)
 for i,comp in enumerate(COMPANIES):
  if p>=comp["min"]:
   with cols[i%3]:
    st.markdown(f"""
    <div class="card-glass" style="text-align:center; border-left: 4px solid {comp['color']};">
     <div class="orbit-ring" style="background: conic-gradient({comp['color']} 85%, #1f2937 0);"><div class="orbit-ring-inner"><span>85%</span><span style="font-size:9px;">READY</span></div></div>
     <h3 style="margin-top:12px;">{comp['name']}</h3><p style="font-size:12px; color:#94a3b8;">Need {comp['min']}% | {comp['pkg']}</p><p style="font-size:11px;">{comp['desc']}</p><p style="font-size:10px; color:{comp['color']};">● Orbit Active - Graphics Mode</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"🚀 Enter {comp['name']} Orbit → Graphics",key=f"comp_{comp['name']}",use_container_width=True):
     st.session_state.company=comp; st.session_state.page="skills_page"; st.rerun()
 if st.button("← Back to Skills & % - Graphics",use_container_width=True): st.session_state.page="login2"; st.rerun()
 st.stop()

# PAGE 4: SKILLS - GRAPHICS ORBS
if st.session_state.page=="skills_page":
 comp=st.session_state.company
 st.markdown(f'<div class="top-graphics"><span>🚀 STEP 4: SKILLS FOR {comp["name"]} - {comp["pkg"]} - GRAPHICS ORBS</span><span class="xp-neon">{st.session_state.xp} XP</span></div>', unsafe_allow_html=True)
 st.markdown(f'<div class="card-glass"><h2>Step 4: Select Skill for {comp["name"]} - Graphics Orbs</h2><p>Company {comp["name"]} - {comp["pkg"]} - Choose skill - Each skill is orbit with icon - Graphics mode super cool</p></div>', unsafe_allow_html=True)
 cols=st.columns(4)
 for i,sk in enumerate(st.session_state.selected_skills):
  with cols[i%4]:
   st.markdown(f'<div class="card-glass" style="text-align:center;"><div class="orbit-ring" style="width:90px; height:90px; background: conic-gradient(#6366f1, #06b6d4);"><div class="orbit-ring-inner" style="width:68px; height:68px;"><span style="font-size:28px;">{"🐍" if sk=="Python" else "🔵" if sk=="C" else "💜" if sk=="C++" else "☕"}</span></div></div><h3 style="margin-top:10px;">{sk}</h3><p style="font-size:11px;">{len(FULL_DATA.get(sk, []))} Modules<br><span style="color:#22c55e;">● Orbit Ready - Graphics</span></p></div>', unsafe_allow_html=True)
   if st.button(f"🚀 Learn {sk} - Graphics Orbit →",key=f"learn_{sk}",use_container_width=True,type="primary"):
    st.session_state.skill=sk; st.session_state.page="topics_list"; st.session_state.topic_idx=0; st.rerun()
 if st.button("← Back to Companies - Graphics",use_container_width=True): st.session_state.page="companies"; st.rerun()
 st.stop()

# PAGE 5: TOPICS LIST - GRAPHICS GFG
if st.session_state.page=="topics_list":
 comp=st.session_state.company; sk=st.session_state.skill; topics=FULL_DATA.get(sk, [])
 st.markdown(f'<div class="top-graphics"><span>🚀 STEP 5: TOPICS FOR {sk} - {comp["name"]} - GRAPHICS GFG INDEX</span><span class="xp-neon">{st.session_state.xp} XP</span></div>', unsafe_allow_html=True)
 left,right=st.columns([1.2,2])
 with left:
  st.markdown(f'<div class="card-glass"><h3>📚 {sk} Topics - GFG Graphics Index - Orbit List</h3><p style="font-size:11px; color:#94a3b8;">Click topic - Direct GFG graphics page opens with orbit animation</p>', unsafe_allow_html=True)
  for idx,t in enumerate(topics):
   sc=st.session_state.stars.get(f"{sk}_{idx}",0); star_s="⭐"*sc if sc>0 else ""; dm="✅" if f"{sk}_{idx}" in st.session_state.done else t["icon"]
   if st.button(f"{dm} {t['id']}. {t['title']} {star_s}",key=f"topic_{sk}_{idx}",use_container_width=True,type="primary" if st.session_state.topic_idx==idx else "secondary"):
    st.session_state.topic_idx=idx; st.session_state.page="topic_detail"; st.rerun()
  st.markdown('</div>', unsafe_allow_html=True)
 with right:
  st.markdown(f'<div class="white-graphics"><h2>🎨 Graphics Mode - Click Topic from Left</h2><p>Select any topic like {topics[0]["title"] if topics else "Introduction"} - Full graphics page with more info, code samples, practice execute, stars with glow, interview Qs, previous year real Qs, game zone with orbit, certificate with graphics</p><div class="orbit-ring" style="margin-top:16px;"><div class="orbit-ring-inner"><span>🎯</span><span style="font-size:9px;">SELECT</span></div></div></div>', unsafe_allow_html=True)
 if st.button("← Back to Skills - Graphics",use_container_width=True): st.session_state.page="skills_page"; st.rerun()
 st.stop()

# PAGE 6: TOPIC DETAIL - FULL GRAPHICS GFG
if st.session_state.page=="topic_detail":
 comp=st.session_state.company; sk=st.session_state.skill; topics=FULL_DATA.get(sk, []); t=topics[st.session_state.topic_idx]
 st.markdown(f'<div class="top-graphics"><span>🚀 GRAPHICS MODE - {sk} - {t["title"]} - {comp["name"]} - GFG FULL GRAPHICS PAGE - ORBIT</span><span class="xp-neon">{st.session_state.xp} XP | <span class="star-glow">{"⭐"*st.session_state.stars.get(f"{sk}_{st.session_state.topic_idx}",0)}</span> {st.session_state.stars.get(f"{sk}_{st.session_state.topic_idx}",0)}/5</span></div>', unsafe_allow_html=True)
 left,mid,right=st.columns([1,2.2,1.1])
 with left:
  st.markdown(f'<div class="card-glass"><h3>📚 {sk} Topics - Graphics Nav</h3>', unsafe_allow_html=True)
  for idx,tt in enumerate(topics):
   sc=st.session_state.stars.get(f"{sk}_{idx}",0); star_s="⭐"*sc; dm="✅" if f"{sk}_{idx}" in st.session_state.done else tt["icon"]
   if st.button(f"{dm} {tt['id']}. {tt['title'][:26]} {star_s}",key=f"nav_{sk}_{idx}",use_container_width=True,type="primary" if idx==st.session_state.topic_idx else "secondary"):
    st.session_state.topic_idx=idx; st.rerun()
  st.markdown('</div>', unsafe_allow_html=True)
 with mid:
  stars_now=st.session_state.stars.get(f"{sk}_{st.session_state.topic_idx}",0)
  st.markdown(f"""
  <div class="white-graphics">
   <h1>{t['icon']} {t['title']} | GeeksforGeeks Style | Graphics Mode | Full Info | Orbit</h1>
   <p style="color:gray; font-size:11px;">Last Updated: 26 Aug 2026 | {sk} | {comp['name']} | {comp['pkg']} | For {st.session_state.percent}% | Graphics Mode Super Cool | Stars: <span class="star-glow">{"⭐"*stars_now}</span> {stars_now}/5 | Orbit Active</p>
   <hr>
   <h2>📖 What is {t['title']}? - More Info - Graphics Visual</h2>
   <p style="line-height:1.9; font-size:14px;">{t['info']}</p>
   <h2>🔥 More & More Info - GFG Advantage with Graphics</h2>
   <p style="background: linear-gradient(90deg, #dbeafe, #e0e7ff); padding:14px; border-radius:12px; border-left:4px solid #6366f1; line-height:1.8; box-shadow: 0 4px 15px rgba(99,102,241,0.15);">{t['more']}</p>
   <div style="display:flex; gap:10px; margin-top:14px;"><div class="orbit-ring" style="width:60px; height:60px;"><div class="orbit-ring-inner" style="width:44px; height:44px; font-size:12px;">INFO</div></div><p style="font-size:12px; color:#475569; flex:1;">Graphics Info: BhavPath has orbit graphics, stars, game, GFG only text - BhavPath advantage!</p></div>
   <h2 style="margin-top:20px;">💻 Code Sample Codes - List of Codes - Graphics Neon</h2>
   <p>{len(t['codes'])} sample codes with neon glow - Practice to get <span class="star-glow">⭐</span> stars - Graphics mode</p>
  </div>
  """, unsafe_allow_html=True)
  for i,c in enumerate(t["codes"]):
   st.markdown(f'<div class="white-graphics" style="margin-top:14px; border-left: 4px solid #22c55e;"><h3 style="display:flex; justify-content:space-between;"><span>Code {i+1}: {c["name"]} - Graphics Neon</span><span class="star-glow" style="font-size:14px;">{"⭐" if i < stars_now else "☆"}</span></h3></div>', unsafe_allow_html=True)
   st.markdown(f'<div class="code-neon">{c["code"]}</div>', unsafe_allow_html=True)
   st.code(c["code"],language="python" if sk=="Python" else "c")
  
  st.markdown(f'<div class="white-graphics" style="margin-top:14px; text-align:center;"><h3>⭐ Stars - Attractive Way - Graphics Glow - Advantage of GFG</h3><p style="font-size:36px;"><span class="star-glow">{"⭐"*stars_now}</span><span style="color:#e2e8f0;">{"☆"*(5-stars_now)}</span></p><p>{stars_now}/5 Stars for {t["title"]} - How many codes you did - BhavPath has glowing stars, GFG no stars - Graphics advantage!</p><div class="orbit-ring" style="width:70px; height:70px; margin:10px auto;"><div class="orbit-ring-inner"><span style="font-size:20px;">{"⭐" if stars_now>0 else "☆"}</span><span style="font-size:9px;">{stars_now}/5</span></div></div></div>', unsafe_allow_html=True)
  
  st.markdown(f'<div class="white-graphics" style="margin-top:14px; background: linear-gradient(135deg, #1e293b, #0f172a); color:white !important; border: 2px solid #22c55e;"><h2 style="color:white !important;">🎮 Game Zone - After Codes - Graphics Orbit Game - Attractive</h2><p style="color:#94a3b8 !important;">Play game related to {t["title"]} - Earn <span class="star-glow">⭐</span> stars and XP - GFG has no game, BhavPath has orbit game - Graphics advantage! Visual orbit game.</p></div>', unsafe_allow_html=True)
  if st.button(f"🎮 Play {t['title']} Game - Graphics Orbit - Get ⭐ +30 XP",use_container_width=True,type="primary",key=f"game_{sk}_{st.session_state.topic_idx}"):
   ns=min(5, stars_now+1); st.session_state.stars[f"{sk}_{st.session_state.topic_idx}"]=ns; st.session_state.xp+=30; st.balloons(); st.success(f"🎮 Game Won! +1 Star! Now {ns}/5 Stars with glow +30 XP! Total {st.session_state.xp} XP - Graphics Orbit!"); st.rerun()
  
  st.markdown(f'<div class="white-graphics" style="margin-top:14px;"><h2>🎤 Interview Questions - More & More Questions with Answers - Graphics</h2><p>More than 3 interview Qs with detailed answers - For {comp["name"]} interview - Graphics cards</p></div>', unsafe_allow_html=True)
  for iq in t["interview"]:
   with st.expander(f"❓ Q: {iq['q']} - Graphics Answer"):
    st.markdown(f'<div class="white-graphics" style="background: linear-gradient(90deg, #f0fdf4, #dcfce7); border-left: 4px solid #22c55e;"><b style="color:#14532d;">Answer - Graphics Mode:</b><br>{iq["a"]}</div>', unsafe_allow_html=True)
  
  st.markdown(f'<div class="white-graphics" style="margin-top:14px; border-left: 4px solid #f59e0b;"><h2>📅 Previous Year Real Questions - Separate Column - Heading: Previous Questions Real Questions - Graphics</h2><p>Real questions asked in TCS NQT, Infosys, Wipro previous years - With heading like Previous Questions Real Questions - Graphics timeline</p></div>', unsafe_allow_html=True)
  for pq in t["prev"]:
   with st.expander(f"📅 {pq['year']}: {pq['q']} - Previous Year Real Question - Graphics Timeline"):
    st.code(pq["a"],language="python" if sk=="Python" else "c")
    st.markdown(f'<p style="font-size:11px; color:gray;">📅 This was asked in {pq["year"]} - Real previous year question for {sk} - {t["title"]} - Graphics timeline with orbit</p>', unsafe_allow_html=True)
  
  st.markdown(f'<div class="white-graphics" style="margin-top:14px; text-align:center; background: linear-gradient(135deg, #fef3c7, #fde68a); border: 2px dashed #f59e0b;"><h2>🏆 Certificate - After Game Zone - Graphics Certificate</h2><p>Progress: {len([k for k in st.session_state.done if k.startswith(sk)])}/{len(topics)} topics done in {sk} - Stars: {sum(st.session_state.stars.get(f"{sk}_{i}",0) for i in range(len(topics)))}/ {len(topics)*5} - Graphics certificate with orbit and glow - After completing all, certificate unlocked</p><div class="orbit-ring" style="width:80px; height:80px; margin:10px auto;"><div class="orbit-ring-inner"><span>🏆</span><span style="font-size:8px;">CERT</span></div></div></div>', unsafe_allow_html=True)
  done_cnt=len([k for k in st.session_state.done if k.startswith(sk)])
  if done_cnt>=len(topics)-1 or stars_now>=2:
   if st.button(f"🏆 Get Certificate for {sk} - {comp['name']} - Graphics Super Cool",use_container_width=True,type="primary"):
    st.balloons()
    st.success(f"Certificate Generated with Graphics!")
    st.markdown(f'<div class="card-glass" style="text-align:center; background: linear-gradient(135deg, #6366f1 0%, #06b6d4 50%, #22c55e 100%); padding:24px;"><div class="orbit-ring" style="width:120px; height:120px; margin:auto; background: conic-gradient(white, #fbbf24, white);"><div class="orbit-ring-inner" style="width:90px; height:90px; background: linear-gradient(135deg, #6366f1, #22c55e);"><span style="font-size:30px;">🏆</span></div></div><h1 style="margin-top:16px;">🏆 GRAPHICS CERTIFICATE</h1><h2>{sk} - {t["title"]}</h2><p>{st.session_state.mail} - {st.session_state.college}</p><p>{comp["name"]} - {comp["pkg"]} - {st.session_state.percent}% Power</p><p><span class="star-glow">{"⭐"*stars_now}</span> {stars_now}/5 Stars | {st.session_state.xp} XP | Graphics Mode</p><p style="font-size:11px;">Super Cool Orbit - No Percentage Package - BhavPath</p></div>', unsafe_allow_html=True)
  c1,c2=st.columns(2)
  with c1:
   if st.button("✅ Mark Done + ⭐ Glow +50 XP - Graphics",use_container_width=True,type="primary"):
    key=f"{sk}_{st.session_state.topic_idx}"
    if key not in st.session_state.done: st.session_state.done.add(key)
    st.session_state.stars[key]=min(5, st.session_state.stars.get(key,0)+1); st.session_state.xp+=50; st.balloons(); st.success(f"Done! +1 Star with glow +50 XP - {st.session_state.stars[key]}/5 - Graphics Orbit!")
  with c2:
   if st.button("← Back to Topic List - Graphics",use_container_width=True): st.session_state.page="topics_list"; st.rerun()

 with right:
  st.markdown('<div class="card-glass"><h3>▶️ Practicing Space - Execute - Graphics Neon</h3><p style="font-size:11px; color:#94a3b8;">Write your own code and execute with neon glow - Get <span class="star-glow">⭐</span> stars - Graphics mode</p>', unsafe_allow_html=True)
  st.markdown(f'<div class="code-neon">{t["codes"][0]["code"]}</div>', unsafe_allow_html=True)
  ec=st.text_area("Your Code - Graphics Practice Space:",value=t["codes"][0]["code"],height=130,key=f"exec_{sk}_{st.session_state.topic_idx}")
  if st.button(f"▶️ Execute Code - Graphics Neon Run - ⭐",use_container_width=True,type="primary",key=f"exec_btn_{sk}_{st.session_state.topic_idx}"):
   st.markdown(f'<div class="code-neon">🚀 Executing in Graphics Orbit...<br><br>{ec}<br><br>✨ Output: Executed Successfully!<br>🚀 BhavPath {st.session_state.percent}% Power<br>🎨 Graphics Mode Active<br>⭐ +1 Star +10 XP</div>', unsafe_allow_html=True)
   st.session_state.xp+=10
   key=f"{sk}_{st.session_state.topic_idx}"; st.session_state.stars[key]=min(5, st.session_state.stars.get(key,0)+1); st.balloons(); st.rerun()
  st.markdown('</div>', unsafe_allow_html=True)
  
  st.markdown(f'<div class="card-glass" style="margin-top:12px; text-align:center;"><h3>⭐ Your Stars - Graphics Glow</h3><div class="orbit-ring" style="width:80px; height:80px; margin:10px auto;"><div class="orbit-ring-inner"><span style="font-size:24px;"><span class="star-glow">{"⭐" if stars_now>0 else "☆"}</span></span><span style="font-size:10px;">{stars_now}/5</span></div></div><p style="font-size:28px;"><span class="star-glow">{"⭐"*stars_now}</span><span style="opacity:0.3;">{"☆"*(5-stars_now)}</span></p><p>{stars_now}/5 for {t["title"]}</p><p style="font-size:11px;">Total ⭐ {sum(st.session_state.stars.values())} Stars<br><span class="xp-neon" style="font-size:11px; display:inline-block; margin-top:6px;">{st.session_state.xp} XP</span></p></div>', unsafe_allow_html=True)
  
  st.markdown('<div class="card-glass" style="margin-top:12px;"><h3>🎤 Interview Quick - Graphics</h3>', unsafe_allow_html=True)
  for iq in t["interview"][:2]:
   st.markdown(f'<div style="background: rgba(255,255,255,0.05); padding:8px; border-radius:8px; margin-top:8px; border-left:2px solid #22c55e;"><p style="font-size:12px; margin:0;"><b>Q: {iq["q"][:45]}...</b></p><p style="font-size:11px; color:#94a3b8; margin:4px 0 0 0;">Ans: {iq["a"][:70]}...</p></div>', unsafe_allow_html=True)
  st.markdown('</div>', unsafe_allow_html=True)
  
  st.markdown(f'<div class="card-glass" style="margin-top:12px; background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(6,182,214,0.2));"><h3>🎮 Game Zone - Graphics Orbit</h3><p style="font-size:11px;">Play orbit game - BhavPath advantage over GFG - Graphics!</p><div class="orbit-ring" style="width:60px; height:60px; margin:8px auto;"><div class="orbit-ring-inner" style="width:44px; height:44px;"><span>🎮</span></div></div></div>', unsafe_allow_html=True)
