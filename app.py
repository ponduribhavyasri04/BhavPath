import streamlit as st
import io, zipfile, textwrap
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="BhavPath - What's Your Placement Story?", layout="wide", page_icon="🎯")

def get_font(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except:
        return ImageFont.load_default()

def draw_para(d, x, y, text):
    for line in textwrap.wrap(text, width=105):
        d.text((x,y), line, font=get_font(9), fill="black")
        y+=15
        if y>1080: break
    return y

MEGA = """Python is high-level interpreted OOP language by Guido van Rossum 1991. Dynamically typed, garbage-collected. Supports procedural, OOP, functional. Why Python? TCS NQT, Wipro Elite, Infosys SP, Cognizant GenC all allow Python. 90% of 58% students clear coding round using Python.

VARIABLES: int a=10, float b=10.5, str c='Bhavya', list d=[1,2,3] mutable, tuple e=(1,2,3) immutable, dict f={'name':'Bhavya','perc':58}, set g={1,2,3} unique. Memory private heap, reference counting. OPERATORS: Arithmetic + - * / % ** //, Comparison ==!= > <, Logical and or not, Assignment = += -=, Identity is is not, Membership in not in, Bitwise & | ^ ~ << >>. CONTROL: if-elif-else. Loops: for loop iterating sequence, while loop till false. break exit, continue skip, pass placeholder. Indentation 4 spaces.

FUNCTIONS: Reusable block def. Built-in print() len(), User-defined. Arguments: Positional order matters, Keyword name=value, Default def add(a,b=10), Variable *args tuple, **kwargs dict. Recursion calls itself, base case mandatory. Lambda lambda x:x*2. Map, Filter, Reduce. INPUT OUTPUT: input() string, int(input()) integer. f-string f"Hi {name}". File Handling open() modes r,w,a,r+,w+,a+. with open() best practice. Exception try-except. TIME COMPLEXITY: Big O O(1) constant, O(n) linear, O(n^2) quadratic, O(log n). REAL WORLD: Web Django Flask, Data Science Pandas Numpy, AIML Tensorflow, Automation. For 58% students Python best 30 days. Practice 50 programs daily. ERRORS: IndentationError, NameError, TypeError, ValueError. PROJECTS: Calculator, To-do List, Placement Predictor like BhavPath. TIP: TCS NQT 2024 asked Reverse string, Palindrome, Armstrong, Prime, Fibonacci, GCD LCM, Anagram. All 10 lines Python. So master Python.

Loops Heart. Without loops cannot repeat, without functions cannot reuse. 80% NQT questions involve loops. FOR LOOP: for i in range(5): range(start,stop,step). range(5)=0-4. Iterating list for item in list:. Enumerate idx,val. Nested loops for pattern pyramid diamond. WHILE LOOP: while condition till false. Infinite loop risk. while True with break for menu. CONTROL: break exit, continue skip, pass placeholder. Search if found break. Skip negative if num<0 continue. FUNCTIONS: Reusability, Readability, Debugging, Modularity. Defining def function_name(params): docstring, body, return. Calling function_name(args). Parameters definition, Arguments calling. ARGS: Positional, Keyword, Default, Variable *args tuple, **kwargs dict. def total(*nums): return sum(nums). Recursion calls itself base case mandatory. Factorial fibonacci. Recursion stack memory may cause RecursionError. SCOPE LEGB: Local, Enclosing, Global, Built-in. global keyword, nonlocal, Closure remembering enclosing scope. ERROR HANDLING: try-except-finally raise custom. PRACTICE: Prime 1-100 function, Armstrong, Fibonacci recursive, Pattern * ** *** ****, GCD function. INTERVIEW: function vs method? Recursion limit 1000 sys.setrecursionlimit. pure function? first-class function? For 58% focus 20 patterns 10 functions daily 15 days NQT clear. SQL JOIN is Structured Query Language. SELECT fetch, WHERE filters, JOIN combines 2 tables INNER common, LEFT all left, RIGHT, FULL. JOIN most asked TCS Infosys Wipro. GROUP BY groups same values with aggregate COUNT SUM AVG MAX MIN. HAVING filters groups WHERE filters rows. ORDER BY sorts ASC default DESC. Very important NQT interviews. ACID Atomicity Consistency Isolation Durability. Keys Primary unique, Foreign reference, Normalization 1NF 2NF 3NF BCNF removes redundancy. Transactions commit rollback. Indexing fast search B-Tree. Deadlock two transactions waiting each other. JAVA Oops 4 pillars Encapsulation Inheritance Polymorphism Abstraction. Class blueprint Object instance. __init__ constructor self current object. Inheritance single multiple multilevel. Collections List ArrayList LinkedList Set HashSet Map HashMap. Exception try catch finally. Multithreading Thread Runnable. C Pointers address, Structures collection different types, Memory malloc calloc free, File Handling. C++ OOP STL vector map set algorithm. Aptitude Percentages Profit Loss Time Speed Distance Permutation Combination Probability. DataScience Pandas DataFrame Series, Numpy array, Visualization Matplotlib Seaborn, ML Basics supervised unsupervised. AIML AI Fundamentals, ML Algorithms Linear Regression Decision Tree Random Forest, Deep Learning Neural Network, NLP tokenization.
"""

SKILLS = {
"Python": ["Python Basics","Loops & Functions","Oops Concepts","File Handling","TCS NQT Coding"],
"SQL": ["SELECT & JOIN","GROUP BY","Sub Queries","Window Functions","NQT SQL"],
"DBMS": ["ACID Properties","Keys & Normalization","Transactions","Indexing","Deadlock"],
"Java": ["Oops Java","Collections","Exception Handling","Multithreading","Java NQT"],
"C": ["Pointers","Structures","Memory Management","File C","C NQT"],
"Cpp": ["Oops C++","STL Library","Pointers C++","Templates","Cpp NQT"],
"Aptitude": ["Percentages","Profit & Loss","Time Speed Distance","Permutations","NQT Aptitude"],
"DataScience": ["Pandas","Numpy","Data Visualization","ML Basics","Projects DS"],
"AIML": ["AI Fundamentals","ML Algorithms","Deep Learning","NLP","Projects AIML"]
}

COMPANIES={"TCS NQT":58,"Wipro":60,"Infosys":60,"Cognizant":60,"Capgemini":60,"HCL":60,"Accenture":65,"TCS Digital":70,"Microsoft":70,"Amazon":65,"Deloitte":60,"IBM":65}

def make_pdf(course, name, perc, branch):
    W,H=850,1150
    pages=[]
    img=Image.new("RGB",(W,H),"white")
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,W,240], fill="#0a1628")
    d.text((30,25), "BhavPath", font=get_font(28,True), fill="#42a5f5")
    d.text((30,65), "What's Your Placement Story..? 🚀", font=get_font(20,True), fill="white")
    d.text((30,100), f"{course} - Complete Guide for {name}", font=get_font(14,True), fill="#90caf9")
    d.text((30,130), f"Name: {name} | Branch: {branch} | {perc}%", font=get_font(11), fill="white")
    d.text((30,160), "9 Courses | 500+ Words Per Topic | For 58% Students", font=get_font(10,True), fill="#ffcc80")
    y=260
    d.text((25,y), f"What's Your Placement Story..? {name} - Let's Build It!", font=get_font(13,True), fill="#0a1628"); y+=30
    d.text((25,y), f"Eligible Companies for {perc}%:", font=get_font(11,True), fill="#2e7d32"); y+=25
    for comp,cut in COMPANIES.items():
        ok=int(perc)>=cut
        d.text((35,y), f"{'✅' if ok else '🔒'} {comp} ({cut}%) - {'ELIGIBLE' if ok else 'Need '+str(cut-int(perc))+'%'}", font=get_font(9), fill="#2e7d32" if ok else "#b71c1c"); y+=18
    pages.append(img)

    for topic in SKILLS[course]:
        words=MEGA.split()
        for part in range(3):
            img=Image.new("RGB",(W,H),"white")
            d=ImageDraw.Draw(img)
            d.rectangle([0,0,W,55], fill="#0a1628")
            d.text((15,18), f"BhavPath | What's Your Placement Story..? | {course} | {topic} | {name} {perc}%", font=get_font(8,True), fill="white")
            y=70
            d.rectangle([15,y,W-15,y+30], fill="#e3f2fd")
            d.text((25,y+7), f"📖 {topic} - 500+ WORDS - Part {part+1}/3", font=get_font(11,True), fill="#0a1628"); y+=40
            s=part*len(words)//3
            e=s+len(words)//3 if part<2 else len(words)
            draw_para(d,25,y," ".join(words[s:e]))
            pages.append(img)
        img=Image.new("RGB",(W,H),"white")
        d=ImageDraw.Draw(img)
        d.rectangle([0,0,W,55], fill="#0a1628")
        d.text((15,18), f"BhavPath | CODE | {name}", font=get_font(8,True), fill="white")
        y=70
        d.rectangle([15,y,W-15,y+30], fill="#0a1628")
        d.text((25,y+7), f"💻 CODE - {topic}", font=get_font(11,True), fill="#42a5f5"); y+=40
        d.rectangle([20,y,W-20,y+120], fill="#1e1e1e")
        code=f"# {topic}\ndef solve():\n print('Hi {name} - {topic}')\n for i in [1,2,3,4,5]:\n if i%2==0: print(f'Even {{i}} {perc}%')\n return 'Ready'\nprint(solve())"
        for i,line in enumerate(code.split("\n")): d.text((30,y+5+i*14), line, font=get_font(8), fill="#d4d4d4")
        y+=140
        d.rectangle([15,y,W-15,y+28], fill="#e8f5e9")
        d.text((25,y+6), "🟢 OUTPUT: Even 2 Even 4 Ready", font=get_font(9,True), fill="#2e7d32"); y+=35
        d.rectangle([15,y,W-15,y+28], fill="#fce4ec")
        d.text((25,y+6), f"🎯 10 Interview Q for {topic}", font=get_font(10,True), fill="#b71c1c"); y+=35
        for i in range(1,6): d.text((25,y), f"{i}. Explain {topic}? Example? Complexity? Project?", font=get_font(8), fill="black"); y+=18
        pages.append(img)

    fname=f"{course}_WhatsYourPlacementStory_{name}.pdf"
    pages[0].save(fname, save_all=True, append_images=pages[1:])
    return fname

# UI - MOTHAM KALIPI
st.markdown("<h1 style='text-align:center;color:#0a1628'>BhavPath</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#1565c0'>What's Your Placement Story..? 🚀</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>9 Courses | 500+ Words Per Topic | For 58% Students | MEGA BOOK</p>", unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
with c1: name=st.text_input("Your Name", "Bhavya Ponduri")
with c2: perc=st.text_input("Your Percentage", "58")
with c3: branch=st.text_input("Your Branch", "AIML")

course=st.selectbox("Select Course - BhavPath 9 Courses", list(SKILLS.keys()))
st.info(f"📚 {course} - {', '.join(SKILLS[course])} - Each 500+ words!")

if st.button("🧬 Generate - What's Your Placement Story..?", type="primary", use_container_width=True):
    pdf=make_pdf(course, name, int(perc) if perc.isdigit() else 58, branch)
    with open(pdf,"rb") as f:
        st.download_button(f"📥 Download {course} - {name} - What's Your Placement Story..?", f, file_name=pdf, mime="application/pdf", use_container_width=True)
    st.success(f"Done! {course} - 20 Pages - What's Your Placement Story..?"); st.balloons()

if st.button("📦 Generate All 9 PDFs - MOTHAM KALIPI", use_container_width=True):
    zbuf=io.BytesIO()
    with zipfile.ZipFile(zbuf,"w") as z:
        for c in SKILLS.keys():
            fp=make_pdf(c, name, int(perc) if perc.isdigit() else 58, branch)
            z.write(fp)
    zbuf.seek(0)
    st.download_button("📦 Download All 9 PDFs ZIP - MOTHAM KALIPI - What's Your Placement Story..?", zbuf, file_name=f"BhavPath_MOTHAM_{name}.zip", mime="application/zip", use_container_width=True)
