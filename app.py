import streamlit as st
import pandas as pd

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
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_detailed_content(skill, topic):
    return f"""
### {topic} in {skill} - Complete Detailed Tutorial with Diagrams

#### 1. INTRODUCTION
{topic} is a core concept in {skill}. Without mastering {topic}, you cannot crack placement interviews. Every company like TCS, Infosys, Wipro, Amazon, Google asks questions from this topic.

Definition: {topic} in {skill} is a technique that allows developers to handle data, logic and execution flow efficiently. It provides structure to code and improves performance and readability.

#### 2. CLASSIFICATION / TYPES OF {topic.upper()}

Type A - Basic {topic}: Simple to understand, used for beginners. Syntax straightforward.

Type B - Intermediate {topic}: Combination of {topic} with loops, functions, conditions. Used in medium projects and coding rounds.

Type C - Advanced {topic}: Optimized version for large data (1 million elements). Used in product based interviews. Focus on O(n log n) and O(1) space.

#### 3. REAL-LIFE EXAMPLE
If {skill} is a house, {topic} is the main pillar. Without it house collapses.

Example: In banking software, {topic} stores 1 lakh customer records. Without proper {topic}, searching one account takes 1 hour. With {topic}, it takes 1 second. TCS uses {topic} to manage employee data.

#### 4. MEMORY LAYOUT / DIAGRAM

{skill} - {topic} Architecture:
User Code ({topic}) -> Compiler / Interpreter -> Memory (Stack: temp vars, Heap: dynamic data) -> Output

Detailed Memory Diagram:
Address: 1000  1004  1008  1012
        +------+------+------+------+
        | Val1 | Val2 | Val3 | Val4 |
        +------+------+------+------+
Pointer -> Points to first address -> next address

Flow Chart:
Start -> Initialize {topic} -> Check Condition -> True -> Process {topic} -> Update -> Loop
                                False -> Exit -> End

Time Complexity: Access O(1), Search O(n) or O(log n) optimized, Insertion O(1) at end

#### 5. CODE EXAMPLES - 5 LEVELS

Level 1 Beginner:
topic_var = 10
print(topic_var)

Level 2 Intermediate with Condition:
if topic_var > 5:
    print("{topic} is greater")
else:
    print("{topic} is small")

Level 3 Advanced with Loops:
for i in range(0,5):
    print(f"{topic} item {{i}}")

Level 4 Placement Level (TCS, Infosys Pattern):
def solve_{topic.lower()}(arr):
    result = arr[0]
    for x in arr:
        if x > result:
            result = x
    return result

Level 5 Product Based Optimized O(n):
def optimized_{topic.lower()}(data):
    seen = {{}}
    for i, val in enumerate(data):
        if val in seen:
            return [seen[val], i]
        seen[val] = i
    return -1

#### 6. COMMON MISTAKES
1. Not initializing {topic} variable - garbage value
2. Confusing = with ==
3. Memory leak - malloc without free in C/C++
4. Off-by-one error in loops
5. Wrong format specifier
6. Ignoring edge cases like empty array

#### 7. ADVANTAGES, DISADVANTAGES, USE CASES
Advantages: Fast access, Reusable, Memory efficient, Used in OS, Banking, E-commerce
Disadvantages: Complex for beginners, Needs careful memory handling

Use Cases: Banking customer accounts, E-commerce product catalog, Social media feeds, OS process management

#### 8. WHY IMPORTANT FOR PLACEMENT?
TCS: 2-3 questions, Infosys: Coding round includes {topic}, Amazon/Google: DSA heavily uses {topic}

Top 10 Interview Questions on {topic}:
1. What is {topic}? Explain with example.
2. Difference between {topic} and similar concept?
3. How does {topic} work internally? Memory?
4. Write code without built-in functions.
5. Optimize for large input 10^6.
6. Where did you use {topic} in project?
7. Advantages / Disadvantages?
8. What happens if {topic} fails?
9. Explain in multi-threaded environment.
10. Design system using {topic}.

#### 9. PRACTICE QUESTIONS
Easy: Basic {topic} program, Print pattern
Medium: {topic} with array, Optimization O(n^2) to O(n log n)
Hard: Design mini project using {topic}, Solve 50+ problems

#### 10. SUMMARY
{topic} is core of {skill}. Mastering it means 20% closer to placement. Practice daily: 1 hour theory + 2 hours coding.

Next: After {topic}, learn next topic in {skill}. Build project using {topic} for resume.
"""

def get_interview_content(skill):
    data = {
    "C": """
### C Interview Questions - Detailed Answers with Code and Diagrams

Q1. What is a pointer? Why use it?
Answer: Pointer stores address of another variable. int *p = &a;
Why: 1. Dynamic memory (malloc) 2. Pass large data without copying 3. Build Linked List, Trees
Diagram: a=10 at 1000, p=1000, *p=10
Code: int a=10; int *p=&a; printf("%d", *p);
Tip: Initialize as NULL to avoid dangling pointer.

Q2. Array vs Pointer?
Array continuous memory fixed size, sizeof(arr) total size. Pointer stores address 8 bytes dynamic.

Q3. Dangling Pointer?
Pointer pointing to freed memory. Solution: Set to NULL after free(). Code: int *p=malloc(4); free(p); p=NULL;

Q4. malloc vs calloc?
malloc 1 arg size uninitialized. calloc 2 args count+size initialized 0.

Q5. Structure vs Union?
Structure all members separate memory. Union shares same memory only one member at a time. Size struct = sum, union = max member.

Q6-Q15: Storage classes auto static extern register, Recursion and stack overflow, Call by value vs reference, String vs char array, Memory leak prevention, Null vs void pointer, File modes r w a, etc. Each with diagram and code - asked in TCS, Wipro.
""",
    "Java": """
### Java Interview Questions - Detailed

Q1. What is OOP? 4 Pillars?
Encapsulation private data, Inheritance extends, Polymorphism overloading/overriding, Abstraction abstract/interface. Code: class Animal{} class Dog extends Animal{}

Q2. ArrayList vs LinkedList?
ArrayList dynamic array O(1) access O(n) insertion middle. LinkedList nodes via pointers O(n) access O(1) insertion.

Q3. HashMap Working?
Key-value hashing: key.hashCode() -> bucket index. Collision handled by linked list / tree. O(1) avg.

Q4. String vs StringBuilder?
String immutable, StringBuilder mutable faster for concatenation.

Q5-Q15: Exception try-catch-finally, throw vs throws, Multithreading, Synchronization, Spring Boot, JDBC steps, Collections etc.
""",
    "Python": """
### Python Interview Questions

Q1. List vs Tuple vs Set vs Dict?
List mutable ordered duplicate [1,2,2], Tuple immutable ordered (1,2), Set unique {1,2}, Dict key-value {"a":1}

Q2. *args and **kwargs?
*args tuple positional, **kwargs dict keyword. def func(*args, **kwargs)

Q3-Q15: Decorator, Generator, GIL, Django vs Flask, Pandas, NumPy vs List, OOP self __init__ etc.
""",
    "SQL": """
### SQL Interview Questions

Q1. WHERE vs HAVING?
WHERE filters rows before GROUP BY, HAVING filters groups after.

Q2. Types of JOINs?
INNER only matching, LEFT all left + matching right, RIGHT, FULL, CROSS.

Q3-Q15: Indexing clustered vs non-clustered, Normalization 1NF 2NF 3NF, Subquery vs JOIN, Window functions ROW_NUMBER RANK, Stored Procedure vs Function etc.
""",
    "DSA": """
### DSA Interview Questions - Product Based Level

Q1. Two Sum - Use HashMap O(n). Code: seen={}; for i,num in enumerate(arr): if target-num in seen: return [seen[target-num], i]

Q2. Reverse Linked List - Iterative with prev, curr, next. Diagram: Head->->->NULL becomes NULL<-<-<-[10][20][30]

Q3. Detect Loop (Floyd) - Slow and fast pointer. If meet, loop exists.

Q4-Q15: Stack LIFO Queue FIFO, Tree traversals inorder preorder postorder, BFS DFS, Sorting quick vs merge O(n log n), DP Fibonacci memoization, Greedy coin change etc.
""",
    "C++": """
### C++ Interview Questions

Q1. C vs C++? C procedural, C++ procedural + OOP.

Q2. OOP 4 Pillars with code example.

Q3. STL vector map set - Ready-made containers, sort algorithm.

Q4. Smart pointers unique_ptr shared_ptr - Auto delete.

Q5-Q15: Inheritance types, Polymorphism overloading vs overriding virtual, Templates generic code, Projects etc.
"""
    }
    return data.get(skill, data["C"])

# ========== ALL PAGES ==========
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
    st.markdown(f"<div class='center'><h1 style='color:white;'>Welcome to Placement Prediction</h1><p style='color:#a78bfa;'>{st.session_state.college}</p></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        if st.button("Next → Enter Details", use_container_width=True, type="primary"): st.session_state.page="placement_form"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "placement_form":
    st.markdown("<div class='center'><h1 style='color:white;'>Enter Your Details</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.3,1])
    with col:
        name=st.text_input("1. Name"); tenth=st.number_input("2. 10th %",0.0,100.0,85.0); inter=st.number_input("3. Inter %",0.0,100.0,80.0); btech=st.number_input("4. B.Tech %",0.0,100.0,75.0); skills=st.text_input("5. Skills?", placeholder="Python, Java")
        if st.button("Continue →", use_container_width=True, type="primary"): st.session_state.pdata=(name,tenth,inter,btech,skills); st.session_state.page="placement_result"; st.rerun()
        if st.button("← Back"): st.session_state.page="placement_welcome"; st.rerun()

elif st.session_state.page == "placement_result":
    name,tenth,inter,btech,skills=st.session_state.pdata; avg=(tenth+inter+btech)/3
    st.markdown(f"<div class='center'><h1 style='color:white;'>Company List - {avg:.1f}%</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        df=pd.DataFrame([["Google/Amazon","75%+"],["TCS Digital","70%+"],["Wipro","65%+"]], columns=["Company","Eligibility"])
        st.dataframe(df, use_container_width=True); st.bar_chart(pd.DataFrame({"Score":[tenth,inter,btech]}, index=["10th","Inter","BTech"])); st.progress(int(avg))
        if st.button("← Home"): st.session_state.page="welcome"; st.rerun()

elif st.session_state.page == "tech_welcome":
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - Complete Detailed Content with Diagrams</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Explore Skills →", use_container_width=True, type="primary"): st.session_state.page="tech_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "tech_skills":
    st.markdown("<div class='center'><h1 style='color:white;font-size:42px;'>Select Your Skill</h1><p style='color:#a78bfa;'>48 Topics - Detailed Content Ready</p></div>", unsafe_allow_html=True)
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
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Full Detailed Learning</h1></div>", unsafe_allow_html=True)
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
            content = get_detailed_content(skill, st.session_state.topic)
            st.markdown(f"<div class='detail-box'><h2 style='color:#fef08a;margin-top:0;'>📘 {st.session_state.topic} in {skill}</h2><div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div></div>", unsafe_allow_html=True)

elif st.session_state.page == "interview_welcome":
    st.markdown("""
    <div class='center' style='padding-top:14vh'>
        <h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br>
        <span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1>
        <div class='glass' style='display:inline-block;margin-top:25px;'>
            <p style='color:#c7f0ff;font-size:18px;'>Crack TCS, Infosys, Amazon, Google - Top Interview Questions with Detailed Answers, Code and Diagrams</p>
        </div>
    </div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Start Interview Prep →", use_container_width=True, type="primary"): st.session_state.page="interview_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "interview_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1><p style='color:#a78bfa;'>Detailed Questions with Answers, Code and Diagrams</p></div>", unsafe_allow_html=True)
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
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview - Detailed Q&A</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        content = get_interview_content(skill)
        st.markdown(f"<div class='detail-box'><div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div></div>", unsafe_allow_html=True)
        st.write("")
        if st.button("← Back to Interview Skills"): st.session_state.page="interview_skills"; st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon 🚀</h1></div>", unsafe_allow_html=True)
    if st.button("← Back"): st.session_state.page="purpose"; st.rerun()
