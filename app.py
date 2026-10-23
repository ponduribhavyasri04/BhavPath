import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="BhavPath Premium", page_icon="🚀", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: radial-gradient(ellipse at top left, #0f0c29 0%, #302b63 40%, #24243e 80%, #000000 100%) !important; background-attachment: fixed !important; }
.welcome-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important; padding: 80px 20px !important; border-radius: 30px !important; text-align: center !important; color: white !important; box-shadow: 0 20px 60px rgba(102,126,234,0.6) !important; }
.login-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; padding: 22px !important; border-radius: 20px !important; text-align: center !important; color: white !important; }
.glass-premium { background: rgba(255,255,255,0.08) !important; backdrop-filter: blur(20px) !important; border: 1px solid rgba(255,255,255,0.15) !important; border-radius: 20px !important; padding: 20px !important; box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important; }
div[data-testid="stButton"] > button { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; color: white !important; border-radius: 15px !important; font-weight: 700 !important; height: 75px !important; }
section[data-testid="stSidebar"] { background: linear-gradient(180deg, rgba(15,12,41,0.98) 0%, rgba(48,43,99,0.98) 100%) !important; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'completed' not in st.session_state: st.session_state.completed = []
if 'name' not in st.session_state: st.session_state.name = ""
if 'email' not in st.session_state: st.session_state.email = ""
if 'college' not in st.session_state: st.session_state.college = ""
if 'purpose' not in st.session_state: st.session_state.purpose = ""
if 'test_skill' not in st.session_state: st.session_state.test_skill = None
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'test_answers' not in st.session_state: st.session_state.test_answers = {}
if 'game_unlocked' not in st.session_state: st.session_state.game_unlocked = False
if 'game_score' not in st.session_state: st.session_state.game_score = 0
if 'cert_skill' not in st.session_state: st.session_state.cert_skill = None
if 'cert_stage' not in st.session_state: st.session_state.cert_stage = "select"
if 'cert_questions' not in st.session_state: st.session_state.cert_questions = []
if 'cert_answers' not in st.session_state: st.session_state.cert_answers = {}
if 'cert_score' not in st.session_state: st.session_state.cert_score = 0

TOPICS = {
    "C": ["Intro", "Data Types", "Variables", "Loops", "Functions", "Arrays", "Pointers", "Final Boss"],
    "C++": ["Intro", "Variables", "OOP Basics", "Classes", "Inheritance", "STL", "Final Boss"],
    "Python": ["Intro", "Variables", "Loops", "Functions", "Lists", "OOPS", "File Handling", "Final Boss"],
    "Java": ["Intro", "Variables", "OOP", "Collections", "Threads", "Final Boss"],
    "SQL": ["Basics", "Joins", "Group By", "Having", "Window Functions", "Final Boss"],
    "DSA": ["Arrays", "Stack", "Queue", "Linked List", "Binary Search", "Final Boss"]
}

FULL_DB = {
    "C": {
        "Intro": {"theory": """C Programming - Mother of All Languages - Complete Theory:
1. WHAT IS C? C is general-purpose, procedural, middle-level language developed by Dennis Ritchie in 1972 at AT&T Bell Labs. Mother of all languages because most modern languages derived from C. Fast, efficient, close to hardware.
2. WHY C IMPORTANT? Speed: Compiled fast direct memory access. Foundation: If you know C, learn C++, Java, Python easily 80% syntax similar. System Programming: OS like Windows, Linux, macOS written in C. Embedded systems IoT use C. Placements: TCS NQT, Wipro Elite, Infosys 60% companies ask C.
3. FEATURES: Procedural, Middle-Level, Portable, Rich Library, Pointers powerful.
4. STRUCTURE: #include <stdio.h> Header, int main() Main, { } Braces, printf() Print, return 0 Success.
5. REAL WORLD USE: OS Development Linux kernel, Embedded AC Washing Machine, Game Development, Database MySQL Oracle in C.""", "code": "#include <stdio.h>\nint main() {\n    printf(\"BhavPath C Premium\\n\");\n    int btech=81;\n    printf(\"B.Tech: %d\", btech);\n    return 0;\n}\n// Output: BhavPath C Premium B.Tech: 81", "interview": "Q1. Who developed C? Ans: Dennis Ritchie 1972\nQ2. Why mother of all languages? Ans: Most languages derived from C\nQ3. What is pointer? Ans: Stores address\nQ4. C vs Python? Ans: C compiled fast manual memory", "placement": "TCS NQT: 2 coding questions C Array reverse. Wipro: Pointers structures. Package C 3.5-5 LPA base must."},
        "Variables": {"theory": """C Variables - Complete Theory:
1. WHAT IS VARIABLE? Name given to memory location storing data value. In C container holds value which can change. Example int btech = 81; btech variable name, 81 value, int type, memory allocated.
2. WHY TYPE MANDATORY IN C? Unlike Python, C statically typed MUST declare type. Compiler needs to know memory size. int 4 bytes, char 1 byte, float 4 bytes. Makes C fast memory efficient!
3. TYPES: Local Inside function, Global Outside all functions, Static Retains value between calls, External extern keyword, Constant const int PI=3.
4. RULES: Start letter or underscore, Can contain letters numbers underscore, No space special char, Case sensitive, Cannot be keyword, Meaningful.
5. DATA TYPES: int 4 bytes, float 4 bytes decimal, char 1 byte, double 8 bytes, void 0 byte.
6. REAL EXAMPLE: TCS NQT Store 5 students B.Tech % variables find average. int s1=81,s2=75,s3=90; int avg=(s1+s2+s3)/3;""", "code": "#include <stdio.h>\nint main() {\n    int btech=81;\n    char grade='A';\n    float cgpa=8.1;\n    printf(\"B.Tech: %d\", btech);\n    return 0;\n}\n// Output: B.Tech: 81", "interview": "Q1. What is variable? Ans: Name to memory location\nQ2. Why type mandatory? Ans: Needs memory size at compile time\nQ3. Local vs Global? Ans: Local inside function, Global outside", "placement": "TCS NQT: Store student data variables average. Wipro: Local vs Global difference."},
        "Loops": {"theory": """C Loops - Complete Theory - Most Important:
1. WHAT IS LOOP? Control structure repeats block multiple times. Instead of printf 10 times loop writes once repeats 10 times. Saves code. Data Engineering loops process lakhs records Without loops no Data Engineer job!
2. TYPES:
A) FOR LOOP Known iterations: for(initialization; condition; increment) for(int i=0; i<10; i+=3) printf(\"%d \", i); Output 0 3 6 9 Explanation i=0 check 0<10 true print 0 i=0+3=3 check 3<10 true print 3 i=3+3=6 print 6 i=6+3=9 print 9 i=9+3=12 check false stop So 0,3,6,9! SAME as Python range(0,10,3)=0,3,6,9 Step logic!
B) WHILE LOOP Condition based: initialization; while(condition){code; increment;} int i=0; while(i<10){printf(\"%d \", i); i+=3;} Output same 0 3 6 9
C) DO-WHILE Executes at least once: do{code;}while(condition); Even if false first time runs once!
3. LOOP CONTROL: break Exit immediately, continue Skip current, goto Jump label.
4. NESTED LOOPS Loop inside loop for pattern printing TCS NQT asks star pattern!
5. PLACEMENT: TCS NQT 3-4 questions loops pattern printing Infosys loop through array find eligible Amazon process S3 files loops BhavPath Real Game uses range(0,10,3)=0,3,6,9 logic!""", "code": "#include <stdio.h>\nint main() {\n    for(int i=0; i<10; i+=3) printf(\"%d \", i);\n    // Output: 0 3 6 9\n    return 0;\n}", "interview": "Q1. Output for(i=0;i<10;i+=3)? Ans: 0 3 6 9\nQ2. For vs While? Ans: For known iterations While condition\nQ3. Do-While vs While? Ans: Do-While at least once", "placement": "TCS NQT: Pattern printing loops 10 marks! Print 0 3 6 9! Infosys Loop array average. BhavPath Game Collect 0,3,6,9!"}
    },
    "C++": {
        "Intro": {"theory": """C++ Extension of C with OOPs Bjarne Stroustrup 1979 Competitive programming game dev system software Classes objects inheritance polymorphism Fast like C + OOP power Infosys Wipro ask STL.""", "code": "#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n    cout<<\"BhavPath C++\";\n    return 0;\n}\n// Output: BhavPath C++", "interview": "Q1. C vs C++? Ans: C procedural C++ OOP\nQ2. What is OOP? Ans: 4 pillars\nQ3. STL? Ans: Vector Map", "placement": "Wipro: OOPs 5 marks Infosys SP STL must Package 5-9 LPA."},
        "STL": {"theory": """STL Standard Template Library vector dynamic array map key-value set unique stack queue Saves time! vector<int> arr={0,3,6,9}; push_back(12); Very important for placements! Infosys SP expects STL TCS Digital vector for array problems Amazon Map frequency!""", "code": "#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n    vector<int> arr={0,3,6,9};\n    arr.push_back(12);\n    for(int x:arr) cout<<x<<\" \";\n    // Output: 0 3 6 9 12\n    return 0;\n}", "interview": "Q1. Vector? Ans: Dynamic array\nQ2. Vector vs Array? Ans: Dynamic vs Fixed\nQ3. Map? Ans: Key-value", "placement": "Infosys SP expects STL TCS Digital vector Amazon Map frequency"}
    },
    "Python": {
        "Variables": {"theory": """Python Variables - Complete Theory:
1. WHAT IS VARIABLE? Container name given to memory location storing data value. Unlike C Python variable does NOT need type declaration Python automatically detects type! Dynamic Typing. Example name='Bhavya' Python knows string btech=81 Python knows int No need int btech=81 like C! Makes Python easy fast!
2. WHY SPECIAL DYNAMIC TYPING? In C int btech=81 You must say int In Python btech=81 No need! Python interpreter decides type at RUNTIME not compile time At runtime when you assign 81 Python checks value assigns type int automatically Dynamic Typing vs Static Typing C Advantage Fast coding less code For Data Engineering saves time!
3. TYPES: Local Inside function scope only, Global Outside all functions everywhere, Instance Inside class for objects self.btech=81, Class Variable Shared by all objects college=\"Rise College\".
4. RULES: Start letter or underscore Cannot start number 1btech invalid btech1 valid _btech valid, Can contain letters numbers underscore No space special char student btech invalid student_btech valid, Case sensitive btech BTECH Btech different, Cannot be keyword if for while def class import invalid, Meaningful snake_case student_btech_percent not x y, Constants CAPS PI=3.14 MAX_BTECH=100.
5. DATA TYPES: int 10 81 No limit! Python int very big! float 8.1 3.14 decimal, str 'Bhavya' \"Rise College\" '''Ongole''' String, bool True False Capital, list [81,75,90] Dynamic any type [1,'Bhavya',8.1] valid!, tuple (81,75,90) Like list but immutable, dict {'name':'Bhavya','btech':81} Key-value very important Data Engineering!, set {81,75,90} Unique no duplicates.
6. TYPE CHECKING CONVERSION: type(btech) returns <class 'int'> Check type, isinstance(btech,int) True False Check particular type, Conversion int('81') string to int str(81) int to string float(81)=81.0 Important Data Engineering Data comes as string convert!
7. REAL EXAMPLE TCS NQT Store 5 students B.Tech % variables check eligible >70%. s1=81 s2=75 s3=60 s4=90 s5=55 students=[s1,s2,s3,s4,s5] eligible=[s for s in students if s>70] => [81,75,90] Tests variables list condition! Amazon Data Engineer Process large dataset store millions records variables lists dicts!""", "code": "name='Bhavya'\nbtech=81\nprint(type(name))\nprint(f\"Name: {name}, B.Tech: {btech}%\")\n# Output: Name: Bhavya B.Tech: 81%\n\nstudents_btech=[81,75,90,85,88]\nprint(f\"Average: {sum(students_btech)/len(students_btech)}\")\n# Average: 83.8", "interview": "Q1. What is variable? Ans: Container no type declaration dynamic typing\nQ2. Rules naming? Ans: Start letter/_ no space special char case sensitive\nQ3. Dynamic vs static? Ans: Dynamic runtime Static compile time", "placement": "TCS NQT: Store student B.Tech % check eligibility >70% Tests variables list condition 5 marks! Infosys: What is dynamic typing? Difference Python vs C? Theory 3 marks! Amazon: Store millions records variables!"},
        "Loops": {"theory": """Python Loops - Complete Theory Most Important 0,3,6,9 Logic:
1. WHAT IS LOOP? Control structure repeats block multiple times Saves code time effort Data Engineering loops process lakhs student records files database rows Without loops no Data Engineer job! Loop 40% programming!
2. TYPES 2 TYPES:
A) FOR LOOP Known iterations Syntax for variable in sequence: code Sequence can be range() list string tuple dict
Most Important range() Function Heart of Python Loops and BhavPath Game! range() generates sequence.
- range(stop): range(10) => 0,1,2,3,4,5,6,7,8,9 Starts 0 till stop-1
- range(start,stop): range(0,10) => 0,1,2,3,4,5,6,7,8,9 Start to stop-1
- range(start,stop,step): range(0,10,3) => 0,3,6,9 Start till stop-1 step!
Detailed Logic range(0,10,3)=0,3,6,9 MOST ASKED!
- start=0 stop=10 excluded till 9 step=3
- First value start=0 => Print 0
- Second previous+step 0+3=3 => Print 3
- Third 3+3=6 => Print 6
- Fourth 6+3=9 => Print 9
- Fifth 9+3=12 Check 12<10? No stop! Final Output 0,3,6,9 4 values!
Why 0,3,6,9 important? TCS NQT asks What is output range(0,10,3)? Ans 0,3,6,9 Direct 2 marks! BhavPath Real Game Collect green coins order 0,3,6,9 win! Red bombs 1,2,4,5,7,8 avoid! Data Engineering Process every 3rd record sampling! Array Slicing arr[0:10:3] every 3rd element!
B) WHILE LOOP Condition based iterations not known Syntax initialization while condition: code increment Example count=0 while count<10: print(count) count+=3 Output 0,3,6,9 Same!
When use for vs while? For When know how many times loop range(10) 10 times list 5 students 5 times While When don't know how many times only know condition While user not entered correct B.Tech % while file not empty
3. LOOP CONTROL break continue pass else: break Exit immediately come out, continue Skip current go next, pass Do nothing placeholder, else with loop Else executes when loop completes normally without break For range(0,10,3): print(i) else: print(\"Completed!\") Output 0,3,6,9 Completed! If break else not executed
4. NESTED LOOPS Loop inside loop Example Print 3x3 star pattern for i in range(3): for j in range(3): print(\"*\", end=\" \") print() Output * * * * * * * * * TCS NQT asks pattern printing via nested loops Star pattern Number pattern 10 marks!
5. REAL PLACEMENT Loops 40% Programming: TCS NQT 3-4 questions loops Pattern printing star number pyramid 10-15 marks! Infosys SP Loop through array find >80% eligible Tests loop condition array 5 marks Wipro Elite While vs For difference infinite loop Theory 2 marks Amazon Data Engineer Process S3 bucket files lakhs student records loops Without loops cannot process Must! Flipkart Data Engineer ETL loops Extract Transform Load For each file for each row BhavPath Real Game Game logic uses range(0,10,3)=0,3,6,9 Collect green coins order 0,3,6,9 win Red bombs 1,2,4,5,7,8 avoid This is loop step logic interactive game! Data Science For each row dataset process clean analyze Loops!
6. INFINITE LOOP Danger Avoid while True or for with no condition Runs forever No stop Consumes CPU Use break exit!
7. LIST COMPREHENSION Python Special Loop in one line Normal result=[] for i in range(0,10,3): result.append(i) result=[0,3,6,9] Comprehension result=[i for i in range(0,10,3)] Same [0,3,6,9] one line Pythonic way Asked Infosys SP!
Loops 40% Python and 100% BhavPath Game! Master range(0,10,3)=0,3,6,9 = Master TCS NQT + BhavPath Game + Data Engineering!""", "code": "for i in range(0,10,3):\n    print(i)\n# Output:\n# 0\n# 3\n# 6\n# 9\n# Logic start=0 stop=10 till 9 step=3 => 0 0+3=3 3+3=6 6+3=9\n\nresult=[i for i in range(0,10,3)]\nprint(result) # [0,3,6,9]", "interview": "Q1. Output range(0,10,3)? Ans: 0,3,6,9 Start 0 stop 10 till 9 step 3 MOST ASKED!\nQ2. For vs While? Ans: For known iterations While condition based\nQ3. Break vs Continue vs Pass? Ans: Break exits Continue skips current Pass placeholder", "placement": "TCS NQT: Pattern printing star number pyramid 10-15 marks! Output range(0,10,3) 0,3,6,9 direct 2 marks! Infosys: Loop array find >80% eligible Tests loop condition array 5 marks! Amazon: Process S3 files lakhs records loops Must! BhavPath Game Collect 0,3,6,9 green coins win!"}
    },
    "DSA": {
        "Arrays": {"theory": """DSA Arrays Complete Theory Most Important for MAANG:
1. WHAT IS ARRAY? Collection similar data types stored contiguous continuous adjacent memory locations Index starts 0 In Python list used as array Example btech_scores=[81,75,90,85,88] 5 integers continuous memory Array foundation DSA Without arrays no DSA no MAANG job! Arrays 30% DSA interviews!
2. WHY ARRAY HEART OF PLACEMENTS MAANG? Amazon Google Flipkart Microsoft 100% DSA interviews start arrays First question array! TCS Digital Infosys SP Wipro Elite DSA coding rounds Arrays must! Package depends DSA Good DSA 10+ LPA Amazon Flipkart Poor DSA 3.5 LPA TCS Ninja Real World Student B.Tech % stored array Processed Sorted Searched Daily use! BhavPath Game Logic range(0,10,3)=0,3,6,9 array indexing arr[0]=0 arr[1]=3 arr[2]=6 arr[3]=9 Step 3 indexing!
3. TYPES: One Dimensional Single row [81,75,90,85,88] List B.Tech % Two Dimensional Matrix Rows Columns [[81,75,90],[85,88,92]] 2 students 3 subjects Image processing matrix, Dynamic Array Python list grows automatically arr.append(92) Unlike C fixed size, Associative Array Dict Python {'name':'Bhavya','btech':81} Key-value.
4. OPERATIONS Time Complexity Very Important: Access arr[0]=81 O(1) Direct via index Very Fast Best! Search Find 90 in [81,75,90,85,88] O(n) Linear Check each Slow large, Insert Insert 95 at 2 O(n) Shift elements [81,75,95,90,85,88] 90,85,88 shifted, Delete Delete at 2 O(n) Shift [81,75,85,88] 90 deleted, Traversal Visit all O(n) For loop, Sorting Sort O(n log n) Quick sort Merge sort Important!
5. INDEXING SLICING Python Special range(0,10,3) Logic! Indexing arr[0] First 81 arr[2] Third 90 arr[-1] Last 88 arr[-2] Second last 85 Slicing arr[0:5:2]=[81,90,88] Start 0 stop 5 till index 4 step 2 Every 2nd! Important arr[0:10:3]=Every 3rd element Logic same range(0,10,3)=0,3,6,9! Example btech=[81,75,90,85,88,92,78,85,90,88] btech[0:10:3]=[81,85,78,90] Index 0,3,6,9 => Values 81,85,78,90 Step 3!
6. REAL PLACEMENT COMPANY WISE: TCS NQT Easy Reverse array [81,75,90]=>[90,75,81] Use two pointers slicing [::-1] Find average sum/len 81+75+90/3=82 Find max max=90 min, Infosys SP Medium Array rotation [81,75,90,85,88] rotate 2 => [90,85,88,81,75] Last 2 come first Find duplicates [81,75,81,90,75] duplicates 81,75 Use set Second largest [81,75,90,85,88] second largest 88 Not 90 Need sort two loops, Amazon Data Engineer Medium Hard 10-15 LPA Find second largest without sorting O(n) Two variables max1 max2 Merge two sorted arrays [75,81,85] and [88,90,92]=>[75,81,85,88,90,92] Two pointers Find missing [0,1,2,4,5] missing 3 Sum formula n*(n+1)/2 - sum(arr) Kadane Maximum subarray sum Hard! Flipkart ETL Process array student records For each student check B.Tech %>70 add eligible list Loop condition array.
7. ARRAY VS LIST PYTHON: Array C Java Fixed size same type only int array only ints List Python Dynamic size any type [1,'Bhavya',8.1,True] valid! Python list dynamic array! So Python use list as array!
8. WHY range(0,10,3)=0,3,6,9 ARRAY INDEXING? Consider array arr=[10,20,30,40,50,60,70,80,90,100] 10 elements index 0-9 range(0,10,3) gives index 0,3,6,9 arr[0]=10 arr[3]=40 arr[6]=70 arr[9]=100 So arr[0:10:3]=[10,40,70,100] Every 3rd element starting 0! Array slicing step! Used data sampling every nth record!
9. BhavPath Game Connection Game has coins values 0,1,2,3,4,5,6,7,8,9 Array coins! You must collect coins values 0,3,6,9 IN ORDER This is arr[0:10:3]! If collect 1,2,4,5,7,8 Red bombs Lose life! So game teaches array indexing step!
Arrays foundation DSA Master arrays indexing 0,3,6,9 = Master 30% DSA + BhavPath Game + TCS NQT + Amazon! Without arrays no placement!""", "code": "btech_scores=[81,75,90,85,88,92,78,85,90,88]\nprint(f\"Array: {btech_scores}\")\nprint(f\"First element index 0: {btech_scores[0]}\") #81\nprint(f\"Every 3rd [0:10:3]: {btech_scores[0:10:3]}\")\n# [81,85,78,90] Index 0,3,6,9\n\navg=sum(btech_scores)/len(btech_scores)\nprint(f\"Average: {avg}\") #85.2\nprint(f\"Max: {max(btech_scores)}\") #92", "interview": "Q1. What is array? Ans: Collection similar types contiguous memory index 0 Python list array\nQ2. Time complexity Access Search Insert Delete? Ans: Access O(1) fast Search O(n) linear Insert Delete O(n) shift\nQ3. First last every 3rd? Ans: First arr[0] Last arr[-1] Every 3rd arr[0:10:3] Index 0,3,6,9 range(0,10,3) logic!", "placement": "TCS NQT Easy Reverse average max min 2 questions 5 marks! Infosys SP Medium Rotation duplicates second largest 3 questions 10 marks! Amazon Medium-Hard 10-15 LPA Second largest without sorting Merge sorted Missing Kadane! Flipkart ETL Process array! BhavPath Game Coins array 0-9 Collect 0,3,6,9 green win! Arrays 30% DSA Without arrays no MAANG!"}
    }
}

if st.session_state.page == "welcome":
    st.markdown("""<div class="welcome-box"><div style="font-size:70px">🚀</div><div style="font-size:60px; font-weight:900">BhavPath</div><div style="font-size:28px; margin-top:10px; font-weight:600">Welcome to your placement story</div><div style="font-size:16px; margin-top:10px; opacity:0.9">Learn. Grind. Game. Get Placed.</div></div>""", unsafe_allow_html=True)
    st.markdown("<br>")
    st.markdown("""<div class="glass-premium" style="text-align: center; padding: 30px 20px; background: linear-gradient(135deg, rgba(102,126,234,0.15) 0%, rgba(118,75,162,0.15) 100%) !important;"><div style="font-size:40px">✨</div><div style="font-size:20px; font-weight:600; color:white; font-style: italic; line-height: 1.6; margin-top:10px">"Your placement story is not about being perfect, it's about being persistent. <br> Every line of code you write today is a step closer to your dream offer."</div><div style="font-size:13px; color:#aaa; margin-top:15px; letter-spacing:1px">BHAVPATH PREMIUM | FOR RISE COLLEGE STUDENTS</div></div>""", unsafe_allow_html=True)
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.page = "login"; st.rerun()
    st.stop()

if st.session_state.page == "login":
    st.markdown('<div class="login-header"><div style="font-size:35px; font-weight:800">🚀 BhavPath</div><div>Premium - 6 Skills</div></div>', unsafe_allow_html=True)
    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        name = st.text_input("Full Name", value=st.session_state.name)
        email = st.text_input("Email", value=st.session_state.email)
        college = st.text_input("College", value=st.session_state.college, placeholder="Rise College, Ongole")
        if st.button("Continue →", use_container_width=True, type="primary"):
            if name and email and college:
                st.session_state.name = name; st.session_state.email = email; st.session_state.college = college
                st.session_state.page = "purpose"; st.rerun()
            else: st.error("Fill all fields")
        if st.button("Back"): st.session_state.page = "welcome"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

if st.session_state.page == "purpose":
    st.markdown(f'<div class="login-header"><div style="font-size:30px; font-weight:800">🚀 BhavPath</div><div>Hi {st.session_state.name}</div></div>', unsafe_allow_html=True)
    st.markdown('<h4 style="color:white">Why did you come to this link? Select Purpose:</h4>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("📊 Placement Percentage", use_container_width=True):
            st.session_state.purpose = "placement"; st.session_state.page = "main"; st.rerun()
    with col2:
        if st.button("📚 Skill Learning", use_container_width=True):
            st.session_state.purpose = "skill"; st.session_state.page = "main"; st.rerun()
    st.markdown("")
    col3, col4 = st.columns(2, gap="large")
    with col3:
        if st.button("📝 Test Zone", use_container_width=True):
            st.session_state.purpose = "test"; st.session_state.page = "main"; st.rerun()
    with col4:
        if st.button("📜 Certificate Zone", use_container_width=True):
            st.session_state.purpose = "certificate"; st.session_state.page = "main"; st.rerun()
    _, mid, _ = st.columns([1,1,1])
    with mid:
        if st.button("💼 Interview - Robot Face to Face Zoom", use_container_width=True):
            st.session_state.purpose = "interview"; st.session_state.page = "main"; st.rerun()
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"; st.rerun()
    st.stop()

st.sidebar.markdown(f'<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 15px; border-radius: 15px; color: white; text-align: center;"><div style="font-size:22px; font-weight:800">🚀 BhavPath</div><div style="font-size:11px">6 Skills Premium</div></div>', unsafe_allow_html=True)
st.sidebar.write(f"Name: {st.session_state.name}")
st.sidebar.metric("XP", st.session_state.xp)
if st.sidebar.button("Change Purpose"): st.session_state.page = "purpose"; st.rerun()
if st.sidebar.button("Logout"): st.session_state.page = "welcome"; st.rerun()

if st.session_state.purpose == "skill":
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">📚 Skill Learning Material - Detailed Theory</div></div>', unsafe_allow_html=True)
    left, middle, right = st.columns([1,2.5,1.2], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        selected_topic = st.radio("Select Skill - 6 Skills", ["C", "C++", "Python", "Java", "SQL", "DSA"])
        selected_module = st.radio(f"Materials in {selected_topic}", TOPICS[selected_topic])
        st.markdown('</div>', unsafe_allow_html=True)
    with middle:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown(f'<div style="background: rgba(102,126,234,0.15); padding: 15px; border-radius: 12px; border-left: 4px solid #667eea; margin-bottom: 15px;"><div style="color:#667eea; font-size:11px; font-weight:700">MATERIAL HEADING - FULL THEORY</div><div style="color:white; font-size:24px; font-weight:800">{selected_topic} - {selected_module}</div></div>', unsafe_allow_html=True)
        data = FULL_DB.get(selected_topic, {}).get(selected_module, None)
        if not data:
            data = {"theory": f"{selected_module} in {selected_topic} Full Detailed Theory: {selected_module} is core fundamental concept in {selected_topic} Used to store process manage data Without {selected_module} cannot write program Building block Important for placements TCS NQT 2-3 questions Infosys SP mandatory Amazon 10-15 LPA advanced Real World Data Engineering Backend Frontend Data Science daily Example Code prints 0,3,6,9 using range(0,10,3) Step logic This is {selected_module} logic Used BhavPath Game Collect 0,3,6,9 green coins win! {selected_module} MUST for placements!", "code": f"# {selected_topic} - {selected_module}\nfor i in range(0,10,3):\n    print(i)\n# Output: 0,3,6,9", "interview": f"Q1. What is {selected_module}? Ans: Core concept\nQ2. Why important? Ans: Placements TCS Infosys Amazon\nQ3. Example? Ans: range(0,10,3)=0,3,6,9", "placement": f"TCS NQT: 2-3 questions on {selected_module} Infosys SP mandatory Amazon advanced Package Without {selected_module} 3.5 LPA With 7-15 LPA!"}
        with st.expander(f"📖 Theory - {selected_topic} {selected_module} - Full Detailed - Click to Open", expanded=True):
            st.markdown(data["theory"])
        with st.expander("💻 Code Examples - Click to Open", expanded=True):
            lang = "python"
            if selected_topic == "C": lang = "c"
            elif selected_topic == "C++": lang = "cpp"
            elif selected_topic == "Java": lang = "java"
            elif selected_topic == "SQL": lang = "sql"
            st.code(data["code"], language=lang)
            st.success("Output: 0,3,6,9 - range(0,10,3) logic Step 3!")
        with st.expander("💼 Interview Qs - Click to Open", expanded=False):
            st.write(data["interview"])
        with st.expander("🏢 Placement - Click to Open", expanded=False):
            st.write(data["placement"])
        st.divider()
        key = f"{selected_topic}-{selected_module}"
        if key not in st.session_state.completed:
            if st.button(f"✅ Mark {selected_module} Completed +50 XP", type="primary", use_container_width=True):
                st.session_state.completed.append(key); st.session_state.xp+=50; st.balloons()
        else: st.success("✅ Completed")
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown(f"- **Skill:** {selected_topic}\n- **Heading:** {selected_module}\n- **Theory:** Full Detailed\n- **Language:** English")
        st.divider()
        st.markdown("##### 💻 Practice Editor")
        practice_code = st.text_area("Your Code", "for i in range(0,10,3):\n    print(i)", height=150)
        if st.button("▶️ Run Code", use_container_width=True):
            try:
                import io, sys
                old_stdout = sys.stdout; sys.stdout = buffer = io.StringIO()
                exec(practice_code); sys.stdout = old_stdout
                st.code(buffer.getvalue() or "No output")
            except Exception as e: st.error(e)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.purpose == "placement":
    st.markdown('<h2 style="color:white">📊 Placement Percentage</h2>', unsafe_allow_html=True)
    left,right = st.columns([1,2])
    with left:
        btech = st.number_input("B.Tech %", 0,100,81)
        btn = st.button("Check Companies", type="primary", use_container_width=True)
    with right:
        if btn:
            for comp in [{"name":"TCS NQT","min":60,"pkg":"3.5-7 LPA"},{"name":"Infosys SP","min":65,"pkg":"5-9 LPA"},{"name":"Amazon","min":70,"pkg":"10-15 LPA"}]:
                if btech >= comp["min"]:
                    st.markdown(f'<div class="glass-premium" style="margin-bottom:10px"><div style="color:white">{comp["name"]} - Eligible</div><div style="color:#aaa">{comp["pkg"]}</div></div>', unsafe_allow_html=True)

elif st.session_state.purpose == "test":
    st.markdown('<h2 style="color:white">📝 Test Zone + Real Game - 6 Skills</h2>', unsafe_allow_html=True)
    TEST_BANK = {"C": [{"q": "for(i=0;i<10;i+=3) output?", "o": ["0 3 6 9", "0 1 2"], "a": "0 3 6 9"}], "C++": [{"q": "OOP pillar?", "o": ["Inheritance", "Loop"], "a": "Inheritance"}], "Python": [{"q": "range(0,10,3)?", "o": ["0,3,6,9", "0,1,2"], "a": "0,3,6,9"}], "Java": [{"q": "Java is?", "o": ["Platform Independent", "Dependent"], "a": "Platform Independent"}], "SQL": [{"q": "AVG?", "o": ["AVG(btech)", "SUM"], "a": "AVG(btech)"}], "DSA": [{"q": "LIFO?", "o": ["Stack", "Queue"], "a": "Stack"}]}
    if not st.session_state.test_started and not st.session_state.game_unlocked:
        c1,c2,c3 = st.columns(3, gap="large")
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
                st.session_state.test_started=True; st.rerun()
    elif st.session_state.test_started and not st.session_state.game_unlocked:
        skill = st.session_state.test_skill
        questions = TEST_BANK.get(skill, TEST_BANK["Python"])
        for i,q in enumerate(questions):
            st.markdown(f'<div class="glass-premium"><b>Q{i+1}. {q["q"]}</b></div>', unsafe_allow_html=True)
            ans = st.radio("Select", q['o'], key=f"tq_{i}", index=None)
            if ans: st.session_state.test_answers[i]=ans
        if st.button("Submit & Unlock Game", type="primary", use_container_width=True):
            st.session_state.game_unlocked=True; st.session_state.test_started=False; st.session_state.xp+=50; st.rerun()
    else:
        game_html = """<!DOCTYPE html><html><head><style>body{margin:0;background:#0f0c29;display:flex;justify-content:center;align-items:center;flex-direction:column;font-family:Poppins}#gameCanvas{border:4px solid #667eea;border-radius:20px;background:#1a1a4e}#info{color:white;margin:10px;text-align:center;background:rgba(255,255,255,0.1);padding:12px 24px;border-radius:15px}</style></head><body><div id="info"><div>Score: <span id="score" style="color:#4ade80">0</span> | Target: <b style="color:#4ade80">0,3,6,9</b> | Lives: <span id="lives">3</span></div><div>Collected: <span id="collected">[]</span></div></div><canvas id="gameCanvas" width="600" height="400"></canvas><div id="message" style="color:#fbbf24; font-weight:bold; margin-top:10px"></div><script>const canvas=document.getElementById('gameCanvas');const ctx=canvas.getContext('2d');const scoreEl=document.getElementById('score');const livesEl=document.getElementById('lives');const collectedEl=document.getElementById('collected');const messageEl=document.getElementById('message');let player={x:300,y:200,size:22,speed:6,color:'#667eea'};let keys={};let score=0;let lives=3;let collected=[];let targetSequence=[0,3,6,9];let coins=[];let gameOver=false;let win=false;function spawnCoins(){coins=[];[0,3,6,9].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:true,size:20,color:'#4ade80',collected:false})});[1,2,4,5,7,8].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:false,size:17,color:'#ef4444',collected:false})});}function drawPlayer(){ctx.fillStyle=player.color;ctx.beginPath();ctx.arc(player.x,player.y,player.size,0,Math.PI*2);ctx.fill();}function drawCoins(){coins.forEach(coin=>{if(!coin.collected){ctx.fillStyle=coin.color;ctx.beginPath();ctx.arc(coin.x,coin.y,coin.size,0,Math.PI*2);ctx.fill();ctx.fillStyle='white';ctx.font='bold 14px Poppins';ctx.textAlign='center';ctx.fillText(coin.value,coin.x,coin.y+5);}});}function checkCollision(){coins.forEach(coin=>{if(!coin.collected){let dx=player.x-coin.x,dy=player.y-coin.y,dist=Math.sqrt(dx*dx+dy*dy);if(dist<player.size+coin.size){coin.collected=true;if(coin.isCorrect){if(collected.length<targetSequence.length&&coin.value===targetSequence[collected.length]){collected.push(coin.value);score+=25;messageEl.textContent=`Correct! ${coin.value}!`;messageEl.style.color='#4ade80';}else{messageEl.textContent=`Wrong order!`;messageEl.style.color='#ef4444';lives--;}}else{lives--;messageEl.textContent=`BOMB!`;messageEl.style.color='#ef4444';}updateUI();if(JSON.stringify(collected)===JSON.stringify(targetSequence)){win=true;messageEl.textContent='WIN! +100 XP!';}if(lives<=0&&!win){gameOver=true;messageEl.textContent='Game Over!';}}}});}function updateUI(){scoreEl.textContent=score;livesEl.textContent=lives;collectedEl.textContent='['+collected.join(', ')+']';}function update(){if(gameOver||win)return;if(keys['ArrowUp']||keys['w'])player.y-=player.speed;if(keys['ArrowDown']||keys['s'])player.y+=player.speed;if(keys['ArrowLeft']||keys['a'])player.x-=player.speed;if(keys['ArrowRight']||keys['d'])player.x+=player.speed;player.x=Math.max(player.size,Math.min(canvas.width-player.size,player.x));player.y=Math.max(player.size,Math.min(canvas.height-player.size,player.y));ctx.clearRect(0,0,canvas.width,canvas.height);drawCoins();drawPlayer();checkCollision();requestAnimationFrame(update);}window.addEventListener('keydown',e=>{keys[e.key]=true;});window.addEventListener('keyup',e=>{keys[e.key]=false;});spawnCoins();update();</script></body></html>"""
        components.html(game_html, height=580, width=650)
        if st.button("Claim Win +100 XP", use_container_width=True): st.session_state.xp+=100; st.session_state.game_score+=100; st.balloons()

elif st.session_state.purpose == "certificate":
    st.markdown('<h2 style="color:white">📜 Certificate Zone</h2>', unsafe_allow_html=True)
    if st.session_state.cert_stage == "select":
        c1,c2,c3 = st.columns(3, gap="large")
        with c1:
            if st.button("C Certificate", use_container_width=True): st.session_state.cert_skill="C"
            if st.button("Python Certificate", use_container_width=True): st.session_state.cert_skill="Python"
        with c2:
            if st.button("C++ Certificate", use_container_width=True): st.session_state.cert_skill="C++"
            if st.button("Java Certificate", use_container_width=True): st.session_state.cert_skill="Java"
        with c3:
            if st.button("SQL Certificate", use_container_width=True): st.session_state.cert_skill="SQL"
            if st.button("DSA Certificate", use_container_width=True): st.session_state.cert_skill="DSA"
        if st.session_state.cert_skill:
            if st.button(f"Start AI Interview for {st.session_state.cert_skill} →", type="primary", use_container_width=True):
                st.session_state.cert_questions=["Explain range(0,10,3)?", "Tell about yourself?", "Why hire you?", "OOPS?", "Project?"]
                st.session_state.cert_stage="interview"; st.rerun()
    elif st.session_state.cert_stage == "interview":
        for i,q in enumerate(st.session_state.cert_questions):
            st.markdown(f'<div class="glass-premium" style="margin-top:10px"><div style="color:#fbbf24">Q{i+1}: {q}</div></div>', unsafe_allow_html=True)
            ans = st.text_area(f"Answer Q{i+1}", key=f"cert_{i}")
            if ans and len(ans)>10: st.session_state.cert_answers[i]=ans
        if len(st.session_state.cert_answers)>=3:
            if st.button("Submit & Generate Certificate", type="primary", use_container_width=True):
                st.session_state.cert_score=85; st.session_state.cert_stage="result"; st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div style="background:white; border-radius:20px; padding:40px; text-align:center"><div style="font-size:50px">🏆</div><div style="font-size:36px; font-weight:900; color:#667eea">BHAVPATH PREMIUM</div><div style="letter-spacing:3px; color:#666">CERTIFICATE OF EXCELLENCE</div><div style="font-size:28px; font-weight:800; margin-top:15px">{st.session_state.name}</div><div>Skill: <b>{st.session_state.cert_skill}</b> | Score: <b>{st.session_state.cert_score}%</b></div><div style="background:#f0f4ff; padding:15px; border-radius:15px; color:green; font-weight:800">PLACEMENT READY</div></div>', unsafe_allow_html=True)

else:
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">💼 AI Interview - Face to Face with Robot - Zoom Style</div><div style="font-size:14px; opacity:0.9">Live Camera Simulation - Robot HR + Tech Interview</div></div>', unsafe_allow_html=True)
    robot_html = """<!DOCTYPE html><html><head><style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');*{font-family:'Poppins',sans-serif;margin:0;padding:0;box-sizing:border-box;}body{background:#0f0c29;}.zoom-container{background:#1a1a2e;border-radius:20px;padding:15px;border:2px solid #667eea;}.zoom-header{background:#000;padding:10px 15px;border-radius:12px 12px 0 0;display:flex;justify-content:space-between;align-items:center;color:white;}.zoom-dots{display:flex;gap:6px;}.dot{width:12px;height:12px;border-radius:50%;}.dot.red{background:#ef4444;}.dot.yellow{background:#fbbf24;}.dot.green{background:#4ade80;}.video-grid{display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-top:15px;}.video-box{background:#000;border-radius:15px;height:280px;position:relative;overflow:hidden;border:2px solid #333;}.video-box.robot{border-color:#667eea;background:linear-gradient(135deg,#0f0c29 0%,#302b63 100%);}.video-box.user{border-color:#4ade80;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);}.robot-avatar{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:white;}.robot-face{width:110px;height:110px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:60px;animation:pulse 2s infinite;box-shadow:0 0 30px rgba(102,126,234,0.6);}@keyframes pulse{0%{transform:scale(1);}50%{transform:scale(1.05);}100%{transform:scale(1);}}.robot-speaking{width:80px;height:4px;background:#4ade80;border-radius:2px;margin-top:15px;animation:speaking 0.5s infinite;}@keyframes speaking{0%{width:20px;}50%{width:80px;}100%{width:20px;}}.video-label{position:absolute;bottom:10px;left:10px;background:rgba(0,0,0,0.7);padding:5px 12px;border-radius:20px;color:white;font-size:12px;}.video-controls{display:flex;justify-content:center;gap:15px;margin-top:15px;background:#000;padding:12px;border-radius:0 0 12px 12px;}.control-btn{width:45px;height:45px;border-radius:50%;border:none;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;}.control-btn.mic{background:#4ade80;}.control-btn.video{background:#667eea;}.control-btn.end{background:#ef4444;}.question-panel{background:rgba(102,126,234,0.15);border:1px solid rgba(102,126,234,0.3);border-radius:15px;padding:20px;margin-top:15px;color:white;}.question-text{font-size:18px;font-weight:600;color:#fbbf24;margin-bottom:10px;}.timer{color:#4ade80;font-size:12px;}.transcript{background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;margin-top:10px;font-size:13px;color:#aaa;}</style></head><body><div class="zoom-container"><div class="zoom-header"><div style="display:flex;align-items:center;gap:10px;"><div class="zoom-dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div><span style="font-size:12px;">Zoom Meeting - BhavPath AI Interview</span></div><div style="font-size:11px;background:#ef4444;padding:4px 10px;border-radius:12px;">● REC 00:03:24</div></div><div class="video-grid"><div class="video-box robot"><div class="robot-avatar"><div class="robot-face">🤖</div><div style="margin-top:15px;font-weight:700;font-size:16px;">BhavPath AI Robot</div><div style="font-size:11px;opacity:0.7;margin-top:5px;">Senior Technical Interviewer</div><div class="robot-speaking"></div><div style="font-size:10px;color:#4ade80;margin-top:8px;">Speaking...</div></div><div class="video-label">🤖 Robot - Interviewer</div></div><div class="video-box user"><div class="robot-avatar"><div style="width:90px;height:90px;background:linear-gradient(135deg,#4ade80 0%,#22c55e 100%);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:50px;">👤</div><div style="margin-top:15px;font-weight:700;font-size:16px;">You - Candidate</div><div style="font-size:11px;opacity:0.7;margin-top:5px;">Rise College Ongole</div><div style="font-size:10px;color:#4ade80;margin-top:8px;">● Camera On | Mic On</div></div><div class="video-label" style="background:#4ade80;color:black;">👤 You - Live</div></div></div><div class="video-controls"><button class="control-btn mic">🎤</button><button class="control-btn video">📹</button><button class="control-btn" style="background:#333;">🖥️</button><button class="control-btn" style="background:#333;">💬</button><button class="control-btn end">📞</button></div><div class="question-panel"><div class="timer">⏱️ Question <span id="qNum">1</span> of 5 | Time: <span id="time">00:45</span> | Difficulty: Medium</div><div class="question-text" id="questionText">Q1. Tell me about yourself and why should we hire you? Explain range(0,10,3) logic?</div><div style="font-size:12px;color:#aaa;margin-top:8px;">🤖 Robot is listening... Please answer clearly. Your answer is being recorded.</div><div class="transcript" id="transcript">Transcript: Listening... Waiting for your answer...</div></div></div><script>const questions=["Q1. Tell me about yourself and why should we hire you? Explain range(0,10,3) logic?","Q2. What is difference between C and Python? Explain with example 0,3,6,9?","Q3. What is array? Explain time complexity O(1) access?","Q4. Write SQL query to find average B.Tech %? What is AVG(btech)?","Q5. Where do you see yourself in 5 years? Why BhavPath?"];let currentQ=0;let timeLeft=45;function nextQuestion(){if(currentQ<questions.length-1){currentQ++;document.getElementById('qNum').textContent=currentQ+1;document.getElementById('questionText').textContent=questions[currentQ];document.getElementById('transcript').textContent="Transcript: Robot asked new question. Please answer...";timeLeft=45;}else{document.getElementById('questionText').textContent="✅ Interview Completed! Great job! Click Submit to get certificate.";document.getElementById('transcript').textContent="Transcript: Interview completed. Generating score...";}}setInterval(()=>{timeLeft--;if(timeLeft<0)timeLeft=45;let s=timeLeft%60;document.getElementById('time').textContent=`00:${s<10?'0'+s:s}`;},1000);setInterval(nextQuestion,30000);</script></body></html>"""
    components.html(robot_html, height=650)
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown("##### 🎤 Your Answer - Robot is Listening")
        interview_skills = st.selectbox("Select Interview Type", ["Python Developer", "Java Developer", "SQL Data Engineer", "C Programming", "DSA Interview"])
        current_q = st.text_area("Your Answer", placeholder="Myself Bhavya from Rise College, Ongole. I know range(0,10,3) prints 0,3,6,9 because start 0 stop 10 till 9 step 3...", height=120)
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🎤 Start Speaking", use_container_width=True):
                st.success("Mic On - Robot listening..."); st.balloons()
        with col_b:
            if st.button("⏭️ Next Question", use_container_width=True, type="primary"):
                st.info("Robot: Next question coming..."); st.rerun()
        if current_q and len(current_q) > 20:
            if st.button("📜 Submit Interview & Get Certificate", use_container_width=True, type="primary"):
                st.session_state.cert_skill = interview_skills
                st.session_state.cert_score = 88
                st.session_state.cert_stage = "result"
                st.session_state.purpose = "certificate"
                st.balloons(); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
