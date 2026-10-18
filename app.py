import streamlit as st
from datetime import date

st.set_page_config(page_title="BhavPath - GFG Full", layout="centered", page_icon="💙")

st.markdown("""
<style>
.stApp { background-color: #EAF2FF !important; }
h1,h2,h3,p,div,span,label,li { color: #000000 !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; font-size: 28px !important; }
h2 { color: #1E40AF !important; font-size: 22px !important; font-weight: 800 !important; }
.white-card { background: #FFFFFF !important; color: #000000 !important; border-radius: 12px; padding: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 10px; border: 2px solid #2563EB; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 14px; padding: 16px; }
.blue-card b, .blue-card div, .blue-card li { color: #FFFFFF !important; }
.green-card { background: #F0FFF4 !important; border-left: 5px solid #22C55E; padding: 12px; border-radius: 8px; }
.locked-card { background: #D1D5DB !important; color: #6B7280 !important; border-radius: 12px; padding: 14px; border: 2px dashed #9CA3AF; }
.stButton>button { background: #2563EB !important; color: #FFFFFF !important; border-radius: 10px; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "login"
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'user' not in st.session_state: st.session_state.user = {}
if 'purpose' not in st.session_state: st.session_state.purpose = None
if 'completed' not in st.session_state: st.session_state.completed = {"Intro": False, "Syntax": False, "Variables": False, "Control": False, "OOP": False}

# --- GFG FULL DATA - LIKE GEEKSFORGEEKS ---
GFG_FULL = {
    "title": "C++ Programming Language - Complete Tutorial",
    "last_update": "Last Updated: 25 Aug 2025 | 15 min read | Recommended for 70% - 85% profiles",
    "what_is": """
    **What is C++?**
    C++ is a general-purpose programming language created by Bjarne Stroustrup at Bell Labs in 1983.
    It is an extension of C language with Object-Oriented Programming (OOP) features.
    C++ is known as C with Classes initially.
    It is a middle-level language - both low-level and high-level features.
    Used for: Operating Systems, Browsers (Chrome), Gaming Engines, Databases, Embedded Systems.
    """,
    "syntax": """
    **Basic Syntax of C++:**
    #include <iostream>  // Header file for input output
    using namespace std; // So we don't need to write std::
    
    int main() {         // Execution starts from main()
        cout << "Hello World!"; // cout for print
        return 0;        // Return 0 means success
    }
    """,
    "features": [
        "**1. Object-Oriented:** Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction - Helps build large apps like BhavPath",
        "**2. Platform Dependent but Portable:** Code can run on different machines with little change",
        "**3. Mid-level Language:** Can do low-level (memory management) + high-level (OOP)",
        "**4. Memory Management:** Pointers - Direct memory access - Crucial for Gaming Engines for speed",
        "**5. STL (Standard Template Library):** Ready-made containers - vector, map, set, stack, queue - Saves time in interviews",
        "**6. High Performance:** Faster than Java/Python - Used where speed matters - Gaming, OS",
        "**7. Rich Library:** Large standard library"
    ],
    "applications": [
        "🎮 **Gaming Engines:** Unreal Engine (Fortnite, PUBG), Godot Engine (Free), Source 2 (Dota 2), Unity Backend - All use C++ for speed - This is why BhavPath Final Boss game uses C++ logic!",
        "💻 **Operating Systems:** Windows, Linux parts, macOS parts written in C++",
        "🌐 **Browsers:** Google Chrome, Mozilla Firefox - Rendering engines in C++",
        "🗄️ **Databases:** MySQL, MongoDB core in C++",
        "✈️ **Embedded Systems:** Smart watches, medical devices"
    ],
    "hello_world": """
    #include <iostream>
    using namespace std;
    
    int main() {
        // This is your first C++ program
        cout << "Hello BhavPath! Welcome to C++ World";
        
        int a = 10;
        int b = 20;
        int sum = a + b;
        cout << "\\nSum is: " << sum;
        
        return 0;
    }
    // Output: Hello BhavPath! Welcome to C++ World
    //         Sum is: 30
    """,
    "variables_full": """
    **Variables & Data Types in C++ - Full GFG Style:**
    
    Variable: Name of memory location - Container to store data.
    Syntax: data_type variable_name = value;
    
    **Data Types:**
    1. **int:** Integer - 4 bytes - Range -2B to +2B
       Example: int btech_percentage = 70;
       
    2. **float:** Decimal - 4 bytes - 6-7 decimal digits
       Example: float cgpa = 7.5;
       
    3. **double:** Big decimal - 8 bytes - 15 digits
       Example: double pi = 3.14159265359;
       
    4. **char:** Single character - 1 byte
       Example: char grade = 'A';
       
    5. **string:** Collection of chars - Need #include <string>
       Example: string college = "QIS College";
       string name = "Bhav";
       
    6. **bool:** True/False - 1 byte
       Example: bool isPlaced = false;
    
    **Memory Example for your profile:**
    int percentage = 70; // 4 bytes in memory
    string clg = "Rise"; // Dynamic memory
    
    **Why Data Types?** To save memory and tell compiler what type of data.
    For 70% interview: Always say "Data types help in memory optimization"
    """,
    "control_full": """
    **Control Statements in C++ - Full GFG Style:**
    
    Used to control flow of program.
    
    **1. if-else - Decision Making:**
    Syntax:
    if (condition) { // if true
        // code
    } else {
        // code if false
    }
    
    Example - Placement Eligibility (Your use case):
    int btech = 70;
    if (btech >= 60) {
        cout << "Eligible for TCS NQT";
    } else {
        cout << "Not Eligible - Need to upskill";
    }
    // Output: Eligible for TCS NQT
    
    **2. for loop - Repetition - Loop Legends Game Logic:**
    Syntax:
    for (initialization; condition; increment) {
        // code
    }
    
    Example - Coins at 0,3,6,9 (Your Final Boss game):
    for (int i=0; i<10; i+=3) {
        cout << i << " "; // i = 0,3,6,9
    }
    // Output: 0 3 6 9 - This is exactly your game logic!
    // If i+=1, path is 0,1,2,3,4,5,6,7,8,9 - collects all
    // If i+=3, path is 0,3,6,9 - collects 4 coins - Optimal!
    
    **3. while loop:**
    int i=0;
    while (i<10) {
        cout << i;
        i+=3;
    }
    
    **4. switch:**
    switch(grade) {
        case 'A': cout << "Excellent"; break;
        case 'B': cout << "Good"; break;
        default: cout << "Need improvement";
    }
    """,
    "oop_full": """
    **OOP Concepts in C++ - Full GFG Style - Important for 70% Interview:**
    
    OOP = Object-Oriented Programming - Organizing code as objects with data + methods.
    
    **1. Class:** Blueprint / Template
    Syntax:
    class Student {
        public:
            string name;
            int percentage;
            void display() { cout << name; }
    };
    
    **2. Object:** Instance of class - Real entity
    Student s1;
    s1.name = "Bhav";
    s1.percentage = 81;
    
    **3. Inheritance:** One class inherits another - Code reuse
    Example - Your OOP Battle game:
    class Warrior { public: void attack() { cout << "Attack!"; } };
    class SuperWarrior : public Warrior { public: void superAttack() { cout << "Super Attack!"; } };
    SuperWarrior sw; sw.attack(); // Inherited
    
    **4. Polymorphism:** Same function name, different behavior
    void print(int a) { cout << a; }
    void print(string s) { cout << s; } // Same name, different work
    
    **5. Encapsulation:** Wrapping data + methods together - Data hiding using private
    class BankAccount { private: int balance; public: void setBalance(int b) { balance=b; } };
    
    **6. Abstraction:** Showing only essential, hiding complex
    Example: You click "Play Game" button - You don't need to know internal code - That's abstraction.
    
    **Why OOP for your profile?**
    For 70% Data Science student: Say "OOP helps me structure my projects like BhavPath - I made classes like Student, Game, Module - Makes code maintainable"
    """,
    "interview_full": [
        {"q": "1. What is C++? Who invented?", "a": "C++ is general-purpose, middle-level, object-oriented language invented by Bjarne Stroustrup at Bell Labs in 1983. It is extension of C with OOP. Initially called C with Classes. Used for gaming engines, OS, browsers because of speed. For your interview: Add 'I used C++ logic in my BhavPath Final Boss game - for loop for coin collection'"},
        {"q": "2. Difference between C and C++? (Most asked for 70% profile)", "a": "C is procedural, C++ is both procedural + OOP. C has no classes, objects, inheritance. C++ has STL, exception handling, references. C has malloc/free, C++ has new/delete + constructors/destructors. C is faster for low-level, C++ better for large apps. Memory: C has no OOP overhead, C++ has. Your answer: 'As a 70% student, I prefer C++ for projects like BhavPath because OOP helps manage code - I used classes for Student, Module'"},
        {"q": "3. What is OOP? Explain with real example - Your project", "a": "OOP is organizing code as objects with data + behavior. 4 pillars: Inheritance, Polymorphism, Encapsulation, Abstraction. Real example from BhavPath: I created class Module { bool isCompleted; void markDone(); } and class Game : public Module { void play(); } - Inheritance. Same function play() behaves differently for Loop Legends vs Variable Vault - Polymorphism. Private XP variable - Encapsulation. User just clicks Play - Abstraction. This answer will impress for 81% profile!"},
        {"q": "4. What is pointer? Why use? Dangling pointer? (Important for Gaming)", "a": "Pointer is variable that stores address of another variable. Syntax: int a=10; int *p = &a; // p stores address of a. cout << *p // 10. Why? 1. Dynamic memory 2. Efficient arrays 3. Gaming engine memory control - Direct memory access for speed. Types: Null pointer (int *p=null), Dangling pointer (points to deleted memory) - Dangerous - Causes crash. Wild pointer (uninitialized). For interview: Say 'Pointer used in Unreal Engine for memory optimization - In BhavPath, I understand pointer logic for game performance'"},
        {"q": "5. What is STL? Name components? (Asked in TCS NQT)", "a": "STL = Standard Template Library - Ready-made library with 3 parts: 1. Containers: vector (dynamic array), map (key-value), set (unique), stack, queue, list. 2. Algorithms: sort(), find(), binary_search. 3. Iterators: To traverse containers. Example: vector<int> coins = {0,3,6,9}; sort(coins.begin(), coins.end()); Saves time in coding round. For TCS NQT coding: Use vector, map heavily. Say 'I used vector logic in Loop Legends - path vector'"},
        {"q": "6. Tell me about yourself? - Perfect answer for 81% Rise College", "a": "Sure! I'm Bhav from Rise College, Ongole with 81% in BTech. I built BhavPath - a game-based learning platform where students must complete C++ modules (Variables, Control, OOP) to unlock Final Boss game - Loop Legends. It has GFG-style full tutorials, placement eligibility checker based on %, skill gap analyzer, and auto resume builder. My BTech is 81%, XP 820, completed 2/5 modules. My strength is converting theory into game - like for loop coins at 0,3,6,9. I'm looking for a role where I can use both my Data Science knowledge and C++ game logic. That's about me!"},
        {"q": "7. What is virtual function? Pure virtual?", "a": "Virtual function is function in base class that is overridden in derived class - Achieves runtime polymorphism. Syntax: virtual void attack() {} in base. Pure virtual: No body, must override - virtual void attack() = 0; Makes class abstract. Example: class Game { virtual void play()=0; }; class LoopLegends : public Game { void play() { // for loop logic } }; Used for Final Boss games with different play() but same interface. Important for gaming engines!"},
        {"q": "8. What is constructor? Destructor? Types?", "a": "Constructor: Special function called when object created - Same name as class, no return type. Initializes object. Types: Default (no args), Parameterized (Student(int p)), Copy (Student(Student &s)). Destructor: Called when object destroyed - ~Student() - Frees memory. Important for gaming - When game ends, destructor frees memory. Example: Student s1(81) calls constructor, when s1 goes out of scope destructor called."}
    ]
}

def login():
    st.title("🚀 BhavPath - Login")
    email = st.text_input("Email", placeholder="bhav@gmail.com")
    clg = st.text_input("College Name", placeholder="QIS College, Ongole")
    if st.button("Login - Continue 🔐"):
        if email and clg and "@" in email:
            st.session_state.user = {"email": email, "clg": clg, "name": email.split("@")[0]}
            st.session_state.page = "btech"
            st.rerun()
        else:
            st.error("Drop a valid email fr")

def btech_page():
    st.title("📊 One More Step! - No Cap")
    st.markdown(f'<div class="white-card">Yo <b>{st.session_state.user["name"]}</b>! Welcome to the squad 🚀<br>🏫 {st.session_state.user["clg"]}<br>Let\'s lock in your stats to level up your grind - fr fr</div>', unsafe_allow_html=True)
    btech = st.slider("What's your BTech flex? Drop your %", 0, 100, 81)
    st.markdown(f'<div class="blue-card"><b>Bet! Locked in: {btech}% 🔥</b><br>We\'re about to cook a custom GFG-style prep just for you</div>', unsafe_allow_html=True)
    if st.button(f"Let's roll with {btech}% →"):
        st.session_state.user["btech"] = btech
        st.session_state.page = "purpose"
        st.balloons()
        st.rerun()

def purpose():
    st.header(f"Yo {st.session_state.user['name']}! 👋")
    st.markdown(f'<div class="white-card">🏫 {st.session_state.user["clg"]} | Flex: <b>{st.session_state.user["btech"]}%</b> | XP: <b>{st.session_state.xp}</b></div>', unsafe_allow_html=True)
    total_done = sum(st.session_state.completed.values())
    total = len(st.session_state.completed)
    progress = int((total_done/total)*100)
    st.subheader(f"Your Grind: {progress}% Complete - {total_done}/{total} modules")
    st.progress(progress/100)
    if progress < 100:
        st.warning(f"🔒 Final Boss Locked - Finish {total-total_done} more modules to unlock - Keep grinding fr!")
    else:
        st.success("🔥 FINAL BOSS UNLOCKED! You ate! Let's end with a banger game!")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="white-card">🎯 <b>For Placement</b><br>Eligibility + Skill Gap</div>', unsafe_allow_html=True)
        if st.button("Placement →", key="pl"): st.session_state.purpose="placement"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">📚 <b>Study Modules - GFG Full</b><br>5 Modules - Complete to unlock game</div>', unsafe_allow_html=True)
        if st.button("Materials - GFG Full →", key="mt"): st.session_state.purpose="materials"; st.session_state.page="main"; st.rerun()
    with c2:
        st.markdown('<div class="white-card">📄 <b>Resume Builder</b><br>Auto drip resume</div>', unsafe_allow_html=True)
        if st.button("Resume →", key="rs"): st.session_state.purpose="resume"; st.session_state.page="main"; st.rerun()
        if progress == 100:
            st.markdown('<div class="blue-card"><b>🎮 FINAL BOSS - Game Zone</b><br>Modules done! Time to end with a banger 🔥</div>', unsafe_allow_html=True)
            if st.button("FINAL BOSS - Game Zone 🔥 →", key="gm"):
                st.session_state.purpose="gaming"; st.session_state.page="main"; st.rerun()
        else:
            st.markdown(f'<div class="locked-card"><b>🔒 🎮 FINAL BOSS - Locked</b><br>Complete {total-total_done} modules<br>{progress}% done</div>', unsafe_allow_html=True)

def main():
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["clg"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP</b></div><br>', unsafe_allow_html=True)
    if st.button("← Back to Home"): st.session_state.page="purpose"; st.rerun()

    if st.session_state.purpose=="placement":
        b=st.session_state.user['btech']
        st.subheader("Placement Dashboard - No cap check")
        if b>=60: st.success(f"✅ You good for TCS NQT - Need 60%, You got {b}% - W rizz!")
        else: st.error(f"❌ Need 60%, You got {b}% - Gotta lock in more fr")
        st.markdown(f'<div class="white-card"><b>Skill Gap - Real talk for {b}% profile:</b><br>Variables: {"✅ Done" if st.session_state.completed["Variables"] else "❌ Pending - Need to lock in"}<br>Control: {"✅ Done" if st.session_state.completed["Control"] else "❌ Pending"}<br>OOP: {"✅ Done" if st.session_state.completed["OOP"] else "❌ Pending - Important for TCS Digital"}</div>', unsafe_allow_html=True)
        st.divider()
        for item in GFG_FULL["interview_full"][:3]:
            with st.expander(item["q"]):
                st.write(item["a"])

    elif st.session_state.purpose=="materials":
        st.title(GFG_FULL["title"])
        st.caption(GFG_FULL["last_update"].replace("70% - 85%", f"{st.session_state.user['btech']}%"))
        
        st.markdown(f'<div class="white-card"><b>📑 Table of Contents - Like GFG:</b><br>1. What is C++?<br>2. Basic Syntax<br>3. Features of C++<br>4. Applications / Gaming Engines<br>5. Hello World Program<br>6. Variables & Data Types - Module 3<br>7. Control Statements - Module 4<br>8. OOP Concepts - Module 5<br>9. Interview Qs - 8 Qs for {st.session_state.user["btech"]}% profile</div>', unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["📖 Full Tutorial - GFG Style", "💼 Interview Qs - 8 Qs", "💻 Code Examples"])
        
        with tab1:
            st.header("What is C++?")
            st.write(GFG_FULL["what_is"])
            if not st.session_state.completed["Intro"]:
                if st.button("Mark Intro Done +50 XP", key="intro"): st.session_state.completed["Intro"]=True; st.session_state.xp+=50; st.rerun()
            else: st.success("✅ Intro Done")
            
            st.divider()
            st.header("Basic Syntax of C++")
            st.write(GFG_FULL["syntax"])
            st.code('#include <iostream>\nusing namespace std;\nint main(){\n  cout << "Hello World";\n  return 0;\n}', language="cpp")
            if not st.session_state.completed["Syntax"]:
                if st.button("Mark Syntax Done +50 XP", key="syn"): st.session_state.completed["Syntax"]=True; st.session_state.xp+=50; st.rerun()
            else: st.success("✅ Syntax Done")

            st.divider()
            st.header("Features of C++")
            for f in GFG_FULL["features"]:
                st.markdown(f'<div class="green-card">{f}</div>', unsafe_allow_html=True)
            
            st.divider()
            st.header("Applications of C++ - Gaming Engines")
            for app in GFG_FULL["applications"]:
                st.markdown(f'<div class="blue-card">{app}</div>', unsafe_allow_html=True)
            
            st.divider()
            st.header("Hello World Program")
            st.code(GFG_FULL["hello_world"], language="cpp")
            
            st.divider()
            st.header("Module 3: Variables & Data Types - Full GFG")
            st.write(GFG_FULL["variables_full"])
            st.code('int btech = 81;\nstring college = "Rise";\nbool isPlaced = false;\nfloat cgpa = 8.1;', language="cpp")
            if not st.session_state.completed["Variables"]:
                if st.button("Mark Variables Module Done +100 XP 🔥", key="var"): st.session_state.completed["Variables"]=True; st.session_state.xp+=100; st.balloons(); st.rerun()
            else: st.success("✅ Variables Done - You ate!")
            
            st.divider()
            st.header("Module 4: Control Statements - Full GFG - Final Boss Logic")
            st.write(GFG_FULL["control_full"])
            st.code('int btech=81;\nif(btech>=60) cout<<"Eligible";\nelse cout<<"Not Eligible";\n\nfor(int i=0;i<10;i+=3) cout<<i<<" "; // 0 3 6 9', language="cpp")
            if not st.session_state.completed["Control"]:
                if st.button("Mark Control Module Done +100 XP 🔥", key="ctrl"): st.session_state.completed["Control"]=True; st.session_state.xp+=100; st.balloons(); st.rerun()
            else: st.success("✅ Control Done")
            
            st.divider()
            st.header("Module 5: OOP Concepts - Full GFG - Important for 81%")
            st.write(GFG_FULL["oop_full"])
            st.code('class Student{\n  public:\n    string name;\n    int percentage;\n    void display(){ cout<<name; }\n};\n\nStudent s1;\ns1.name="Bhav";\ns1.percentage=81;', language="cpp")
            if not st.session_state.completed["OOP"]:
                if st.button("Mark OOP Module Done +100 XP 🔥", key="oop"): st.session_state.completed["OOP"]=True; st.session_state.xp+=100; st.balloons(); st.rerun()
            else: st.success("✅ OOP Done")
            
            st.divider()
            done = sum(st.session_state.completed.values())
            st.write(f"**Progress: {done}/5 Modules Done**")
            st.progress(done/5)
            if done==5:
                st.success("🔥 All 5 modules done! Go back - Final Boss Game unlocked at bottom! Time to end with a banger fr!")
                if st.button("Go to Final Boss →"): st.session_state.purpose="gaming"; st.rerun()
            else:
                st.warning(f"Complete {5-done} more modules to unlock Final Boss at end!")

        with tab2:
            st.header(f"Interview Questions - 8 Qs for {st.session_state.user['btech']}% - TCS NQT Style")
            st.markdown('<div class="white-card"><b>These are top asked in TCS NQT, Infosys, Wipro - With perfect answers for 81% Rise profile - No cap, these will make you slay!</b></div>', unsafe_allow_html=True)
            for item in GFG_FULL["interview_full"]:
                with st.expander(item["q"]):
                    st.write(item["a"])
                    if st.button(f"Mark Prepared +10 XP", key=item["q"][:20]): st.session_state.xp+=10; st.success("+10 XP!")

        with tab3:
            st.header("Code Examples - Try Yourself")
            st.subheader("1. Hello World + Sum")
            st.code(GFG_FULL["hello_world"], language="cpp")
            if st.button("Run Code - Simulate"): st.success("Output:\nHello BhavPath! Welcome to C++ World\nSum is: 30")
            st.subheader("2. Eligibility Checker - Your Use Case")
            st.code('int main(){\n  int btech=81;\n  if(btech>=60) cout<<"Eligible for TCS NQT";\n  else cout<<"Not Eligible";\n  return 0;\n}', language="cpp")
            if st.button("Run Eligibility Code"): st.success("Output: Eligible for TCS NQT")
            st.subheader("3. Final Boss Logic - Loop Legends")
            st.code('for(int i=0; i<10; i+=3){\n  cout << i << " "; // Coins at 0,3,6,9\n}\n// Path: 0 3 6 9 - Collects 4 coins - Optimal!', language="cpp")
            if st.button("Run Final Boss Logic"): st.success("Output: 0 3 6 9 - Perfect path! + You collected 4 coins!")

    elif st.session_state.purpose=="gaming":
        st.title("🎮 FINAL BOSS - Game Zone - You made it! 🔥")
        st.markdown('<div class="blue-card"><b>Sheesh! You completed all 5 GFG modules - Now end with a banger!</b><br>You locked in fr - This is your final test - No cap</div>', unsafe_allow_html=True)
        st.balloons()
        st.divider()
        st.markdown('<div class="white-card"><b>FINAL BOSS: Loop Legends - From Module 4 Control Statements</b><br>You learned for loop in GFG tutorial - Now prove it! Coins at 0,3,6,9 - From GFG Control example</div>', unsafe_allow_html=True)
        step=st.slider("for(i=0; i<10; i+=?) - Final answer? - GFG logic", 1,5,3, key="final")
        if st.button("PLAY FINAL BOSS - RUN IT! 🔥"):
            coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
            st.write(f"Path {path} | Collected {coll}/4 - GFG Control logic")
            if coll==4:
                st.balloons()
                st.success(f"YOU SLAYED THE FINAL BOSS! 🔥 +200 XP - Total {st.session_state.xp+200} - You ate and left no crumbs! GFG Modules = Game mastered!")
                st.session_state.xp+=200
                st.snow()
            else:
                st.error(f"Almost! You got {coll}/4 - Need i+=3 - From GFG Control - Run it back, you got this fr")
        st.divider()
        st.markdown('<div class="white-card"><b>Bonus Round: Variable Vault - From Module 3 Variables</b></div>', unsafe_allow_html=True)
        box=st.selectbox("Box? - GFG Data Types", ["Gold Count (100)","Name (Bhav)","Is Win? True"], key="bonus")
        dtype=st.radio("Type? - GFG int, string, bool", ["int","string","bool"], horizontal=True, key="bonus2")
        if st.button("PLAY Bonus Round - Variables"):
            corr={"Gold Count (100)":"int","Name (Bhav)":"string","Is Win? True":"bool"}
            if dtype==corr[box]:
                st.balloons(); st.success(f"Bonus slayed! +50 XP - GFG Variables mastered! Total {st.session_state.xp+50}"); st.session_state.xp+=50
            else:
                st.error(f"Nah fam need {corr[box]} - Check Module 3 again - GFG Variables")

    elif st.session_state.purpose=="resume":
        st.title("📄 Auto Resume - Drip Check")
        done = sum(st.session_state.completed.values())
        st.markdown(f'<div class="white-card"><b>Name:</b> {st.session_state.user["name"]}<br><b>College:</b> {st.session_state.user["clg"]}<br><b>Flex:</b> {st.session_state.user["btech"]}%<br><b>Skills:</b> C++ (GFG Modules {done}/5 - Intro, Syntax, Variables, Control, OOP), STL, Gaming Logic<br><b>Project:</b> BhavPath - GFG Full Tutorial Platform - 5 Modules + 8 Interview Qs + Final Boss Game Logic - Complete modules to unlock Final Boss (Innovative fr)<br><b>XP:</b> {st.session_state.xp} - Grind is real - {done*20}% Complete<br><b>Eligibility:</b> TCS NQT Eligible (60% needed, you {st.session_state.user["btech"]}%)</div>', unsafe_allow_html=True)
        if st.button("Download Resume - It's giving professional"): st.balloons(); st.success("Resume Downloaded! LinkedIn ready - You ate!")

if st.session_state.page=="login": login()
elif st.session_state.page=="btech": btech_page()
elif st.session_state.page=="purpose": purpose()
else: main()
