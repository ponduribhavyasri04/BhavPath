import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="BhavPath Premium", page_icon="🚀", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: radial-gradient(ellipse at top left, #0f0c29 0%, #302b63 40%, #24243e 80%, #000000 100%) !important; background-attachment: fixed !important; }
.welcome-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important; padding: 80px 20px !important; border-radius: 30px !important; text-align: center !important; color: white !important; }
.login-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; padding: 22px !important; border-radius: 20px !important; text-align: center !important; color: white !important; }
.glass-premium { background: rgba(255,255,255,0.08) !important; backdrop-filter: blur(20px) !important; border: 1px solid rgba(255,255,255,0.15) !important; border-radius: 20px !important; padding: 20px !important; }
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
        "Intro": {"theory": """C Programming - Mother of All Languages - Complete Detailed Theory:
1. WHAT IS C? C is general-purpose, procedural, middle-level language developed by Dennis Ritchie in 1972 at Bell Labs. Mother of all languages because most modern languages like C++, Java, Python derived from C. Fast, efficient, close to hardware.
2. WHY IMPORTANT? Speed: Compiled fast direct memory access via pointers. Foundation: If you know C, learn C++, Java, Python easily 80% syntax similar. System Programming: OS Windows, Linux, macOS written in C. Embedded IoT use C. Placements: TCS NQT, Wipro Elite, Infosys 60% companies ask C.
3. FEATURES: Procedural, Middle-Level, Portable, Rich Library, Pointers powerful.
4. STRUCTURE: #include <stdio.h> Header, int main() Main, { } Braces, printf() Print, return 0 Success.
5. REAL WORLD: OS Development Linux kernel, Embedded AC Washing Machine, Game Development, Database MySQL Oracle in C.""", "code": "#include <stdio.h>\nint main() {\n    printf(\"BhavPath C\\n\");\n    int btech=81;\n    printf(\"B.Tech: %d\", btech);\n    return 0;\n}\n// Output: 81", "interview": "Q1. Who developed C? Ans: Dennis Ritchie 1972\nQ2. Why mother? Ans: Most languages derived\nQ3. Pointer? Ans: Stores address of another variable\nQ4. C vs Python? Ans: C compiled fast manual memory", "placement": "TCS NQT: 2 coding questions C Array reverse, String palindrome. Wipro Elite: Pointers structures. Package C 3.5-5 LPA base must."},
        "Variables": {"theory": """C Variables - Complete Theory:
WHAT IS VARIABLE? Name given to memory location storing data value Container holds value can change Example int btech=81 btech variable name 81 value int type memory allocated.
WHY TYPE MANDATORY? Unlike Python C statically typed MUST declare type Compiler needs memory size int 4 bytes char 1 byte float 4 bytes Makes C fast memory efficient.
TYPES: Local Inside function, Global Outside all functions, Static Retains value, External extern, Constant const.
RULES: Start letter or underscore, Can contain letters numbers underscore, No space special char, Case sensitive, Cannot be keyword, Meaningful.
DATA TYPES: int 4 bytes, float 4 bytes decimal, char 1 byte, double 8 bytes, void 0 byte.
REAL EXAMPLE: TCS NQT Store 5 students B.Tech % variables find average int s1=81 s2=75 s3=90 int avg=(s1+s2+s3)/3.""", "code": "#include <stdio.h>\nint main() {\n    int btech=81;\n    printf(\"B.Tech: %d\", btech);\n    return 0;\n}", "interview": "Q1. What is variable? Ans: Name to memory location\nQ2. Why type mandatory? Ans: Needs memory size at compile time\nQ3. Local vs Global? Ans: Local inside function Global outside", "placement": "TCS NQT Store student data variables average Wipro Local vs Global difference Variables 100% asked"},
        "Loops": {"theory": """C Loops - Complete Theory Most Important:
WHAT IS LOOP? Control structure repeats block multiple times Instead printf 10 times loop writes once repeats 10 times Saves code Data Engineering loops process lakhs records Without loops no Data Engineer job!
TYPES: FOR LOOP Known iterations for(initialization; condition; increment) for(int i=0; i<10; i+=3) printf Output 0 3 6 9 Explanation i=0 check 0<10 true print 0 i=0+3=3 check 3<10 true print 3 i=3+3=6 print 6 i=6+3=9 print 9 i=9+3=12 false stop So 0,3,6,9 SAME as Python range(0,10,3)=0,3,6,9 Step logic!
WHILE LOOP Condition based initialization while(condition){code; increment;} Output same 0 3 6 9
DO-WHILE Executes at least once do{code;}while(condition) Even if false first time runs once!
LOOP CONTROL break Exit immediately continue Skip current goto Jump label
NESTED LOOPS Loop inside loop for pattern printing TCS NQT asks star pattern!
PLACEMENT TCS NQT 3-4 questions loops pattern printing Infosys loop through array find eligible Amazon process S3 files loops BhavPath Game uses range(0,10,3)=0,3,6,9 logic!""", "code": "#include <stdio.h>\nint main(){\n    for(int i=0; i<10; i+=3) printf(\"%d \", i);\n    // Output: 0 3 6 9\n    return 0;\n}", "interview": "Q1. Output for(i=0;i<10;i+=3)? Ans: 0 3 6 9\nQ2. For vs While? Ans: For known iterations While condition based\nQ3. Do-While vs While? Ans: Do-While at least once", "placement": "TCS NQT Pattern printing loops 10 marks Print 0 3 6 9 Infosys Loop array average BhavPath Game Collect 0,3,6,9!"}
    },
    "C++": {
        "Intro": {"theory": """C++ Extension of C with OOPs Bjarne Stroustrup 1979 Competitive programming game dev system software Classes objects inheritance polymorphism Fast like C + OOP power Infosys Wipro ask STL Used in game development system software.""", "code": "#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n    cout<<\"BhavPath C++\";\n    return 0;\n}\n// Output: BhavPath C++", "interview": "Q1. C vs C++? Ans: C procedural C++ OOP\nQ2. What is OOP? Ans: 4 pillars Encapsulation Inheritance Polymorphism Abstraction\nQ3. STL? Ans: Vector Map Set", "placement": "Wipro Elite OOPs 5 marks Infosys SP STL must Package 5-9 LPA."},
        "STL": {"theory": """STL Standard Template Library vector dynamic array map key-value set unique stack queue Saves time vector<int> arr={0,3,6,9} push_back(12) Very important for placements Infosys SP expects STL TCS Digital vector for array problems Amazon Map frequency count STL Must for coding interviews!""", "code": "#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n    vector<int> arr={0,3,6,9};\n    arr.push_back(12);\n    for(int x:arr) cout<<x<<\" \";\n    // Output: 0 3 6 9 12\n    return 0;\n}", "interview": "Q1. Vector? Ans: Dynamic array grows automatically\nQ2. Vector vs Array? Ans: Dynamic vs Fixed\nQ3. Map? Ans: Key-value pair\nQ4. Why STL? Ans: Saves time optimized", "placement": "Infosys SP expects STL TCS Digital vector for array problems Amazon Map frequency count"}
    },
    "Python": {
        "Variables": {"theory": """Python Variables - Complete Detailed Theory:
WHAT IS VARIABLE? Container name given to memory location storing data value Unlike C Python variable does NOT need type declaration Python automatically detects type Dynamic Typing Example name='Bhavya' Python knows string btech=81 Python knows int No need int btech=81 like C Makes Python easy fast!
WHY SPECIAL DYNAMIC TYPING? In C int btech=81 You must say int In Python btech=81 No need Python interpreter decides type at RUNTIME not compile time At runtime when assign 81 Python checks value assigns type int automatically Dynamic vs Static C Advantage Fast coding less code For Data Engineering saves time!
TYPES Local Inside function scope only Global Outside all functions everywhere Instance Inside class for objects self.btech=81 Class Variable Shared college=\"Rise College\"
RULES Start letter or underscore Cannot start number 1btech invalid btech1 valid _btech valid Can contain letters numbers underscore No space special char student btech invalid student_btech valid Case sensitive btech BTECH Btech different Cannot be keyword if for while def class import invalid Meaningful snake_case student_btech_percent not x y Constants CAPS PI=3.14
DATA TYPES int 10 81 No limit Python int very big float 8.1 decimal str 'Bhavya' String bool True False Capital list [81,75,90] Dynamic any type [1,'Bhavya',8.1] valid tuple (81,75,90) immutable dict {'name':'Bhavya','btech':81} Key-value very important Data Engineering set {81,75,90} Unique
TYPE CHECKING CONVERSION type(btech) returns <class 'int'> Check type isinstance(btech,int) True False Check particular type Conversion int('81') string to int str(81) int to string Important Data Engineering Data comes as string!
REAL EXAMPLE TCS NQT Store 5 students B.Tech % variables check eligible >70% s1=81 s2=75 s3=60 s4=90 s5=55 students=[s1,s2,s3,s4,s5] eligible=[s for s in students if s>70] => [81,75,90] Tests variables list condition Amazon Data Engineer Process large dataset store millions records variables lists dicts!""", "code": "name='Bhavya'\nbtech=81\nprint(f\"Name: {name}, B.Tech: {btech}%\")\n# Output: Name: Bhavya B.Tech: 81%\n\nstudents=[81,75,60,90,55]\neligible=[s for s in students if s>70]\nprint(eligible) # [81,75,90]", "interview": "Q1. What is variable? Ans: Container no type declaration dynamic typing\nQ2. Rules naming? Ans: Start letter/_ no space special char case sensitive\nQ3. Dynamic vs static? Ans: Dynamic runtime Static compile time\nQ4. Local vs Global? Ans: Local inside function Global outside", "placement": "TCS NQT Store student B.Tech % check eligibility >70% Tests variables list condition 5 marks Infosys What is dynamic typing Difference Python vs C Theory 3 marks Amazon Store millions records variables!"},
        "Loops": {"theory": """Python Loops - Complete Detailed Theory Most Important 0,3,6,9 Logic:
WHAT IS LOOP? Control structure repeats block multiple times Saves code time effort Data Engineering loops process lakhs student records files database rows Without loops no Data Engineer job Loop 40% programming!
TYPES 2 TYPES FOR LOOP Known iterations Syntax for variable in sequence: code Sequence can be range() list string tuple dict
Most Important range() Function Heart of Python Loops and BhavPath Game range() generates sequence range(stop) range(10) => 0,1,2,3,4,5,6,7,8,9 Starts 0 till stop-1 range(start,stop) range(0,10) => 0,1,2,3,4,5,6,7,8,9 Start to stop-1 range(start,stop,step) range(0,10,3) => 0,3,6,9 Start till stop-1 step!
Detailed Logic range(0,10,3)=0,3,6,9 MOST ASKED start=0 stop=10 excluded till 9 step=3 First value start=0 => Print 0 Second previous+step 0+3=3 => Print 3 Third 3+3=6 => Print 6 Fourth 6+3=9 => Print 9 Fifth 9+3=12 Check 12<10? No stop Final Output 0,3,6,9 4 values!
Why 0,3,6,9 important? TCS NQT asks What is output range(0,10,3)? Ans 0,3,6,9 Direct 2 marks BhavPath Real Game Collect green coins order 0,3,6,9 win Red bombs 1,2,4,5,7,8 avoid Data Engineering Process every 3rd record sampling Array Slicing arr[0:10:3] every 3rd element!
WHILE LOOP Condition based iterations not known Syntax initialization while condition: code increment Example count=0 while count<10: print(count) count+=3 Output 0,3,6,9 Same!
When use for vs while? For When know how many times loop range(10) 10 times list 5 students 5 times While When don't know how many times only know condition While user not entered correct B.Tech % while file not empty
LOOP CONTROL break continue pass else break Exit immediately come out continue Skip current go next pass Do nothing placeholder else with loop Else executes when loop completes normally without break
NESTED LOOPS Loop inside loop Example Print 3x3 star pattern for i in range(3): for j in range(3): print(\"*\", end=\" \") print() Output * * * * * * * * * TCS NQT asks pattern printing via nested loops Star pattern Number pattern 10 marks!
REAL PLACEMENT Loops 40% Programming TCS NQT 3-4 questions loops Pattern printing star number pyramid 10-15 marks Infosys SP Loop through array find >80% eligible Tests loop condition array 5 marks Wipro Elite While vs For difference infinite loop Theory 2 marks Amazon Data Engineer Process S3 bucket files lakhs student records loops Without loops cannot process Must Flipkart Data Engineer ETL loops Extract Transform Load For each file for each row BhavPath Real Game Game logic uses range(0,10,3)=0,3,6,9 Collect green coins order 0,3,6,9 win Red bombs 1,2,4,5,7,8 avoid This is loop step logic interactive game Data Science For each row dataset process clean analyze Loops!
INFINITE LOOP Danger Avoid while True or for with no condition Runs forever No stop Consumes CPU Use break exit!
LIST COMPREHENSION Python Special Loop in one line Normal result=[] for i in range(0,10,3): result.append(i) result=[0,3,6,9] Comprehension result=[i for i in range(0,10,3)] Same [0,3,6,9] one line Pythonic way Asked Infosys SP!
Loops 40% Python and 100% BhavPath Game Master range(0,10,3)=0,3,6,9 = Master TCS NQT + BhavPath Game + Data Engineering!""", "code": "for i in range(0,10,3):\n    print(i)\n# Output:\n# 0\n# 3\n# 6\n# 9\n\nresult=[i for i in range(0,10,3)]\nprint(result) # [0, 3, 6, 9]", "interview": "Q1. Output range(0,10,3)? Ans: 0,3,6,9 Start 0 stop 10 till 9 step 3 MOST ASKED!\nQ2. For vs While? Ans: For known iterations While condition based\nQ3. Break vs Continue vs Pass? Ans: Break exits Continue skips current Pass placeholder\nQ4. Nested loop? Ans: Loop inside loop for pattern printing", "placement": "TCS NQT Pattern printing star number pyramid 10-15 marks Output range(0,10,3) 0,3,6,9 direct 2 marks Infosys Loop array find >80% eligible Tests loop condition array 5 marks Amazon Process S3 files lakhs records loops Must BhavPath Game Collect 0,3,6,9 green coins win! Loops 40% programming + 100% Game!"},
        "Lists": {"theory": """Python Lists - Complete Theory:
WHAT IS LIST? Collection of items stored in single variable In Python list used as array But unlike C array Python list dynamic Can grow automatically Can store any data type int str float bool even another list Example btech=[81,75,90,85,88] 5 integers Mixed list [1,'Bhavya',8.1,True,[81,75]] valid!
WHY LIST IMPORTANT? List most used data structure Python Data Engineering Store student records Process data ETL 70% Python code uses lists TCS NQT Infosys Amazon All ask lists!
INDEXING AND SLICING range(0,10,3) Logic Indexing arr[0] First 81 arr[2] Third 90 arr[-1] Last 88 arr[-2] Second last 85 Slicing arr[0:5:2]=[81,90,88] Start 0 stop 5 till index 4 step 2 Every 2nd Important arr[0:10:3]=Every 3rd element Logic same range(0,10,3)=0,3,6,9 Example btech=[81,75,90,85,88,92,78,85,90,88] btech[0:10:3]=[81,85,78,90] Index 0,3,6,9 => Values 81,85,78,90 Step 3!
LIST METHODS append(x) Add at end insert(i,x) Insert at position remove(x) Remove first occurrence pop(i) Remove at position and return sort() Sort ascending reverse() Reverse count(x) Count occurrences len(arr) Length
LIST COMPREHENSION Short way to create list Normal result=[] for i in range(0,10,3): result.append(i) => [0,3,6,9] Comprehension result=[i for i in range(0,10,3)] => Same [0,3,6,9] one line Pythonic way Asked Infosys SP!
REAL PLACEMENT TCS NQT Reverse list [81,75,90]=>[90,75,81] via [::-1] Find average sum(arr)/len(arr) Find max min Infosys SP List operations append pop sort Amazon Data Engineer Store millions student records in list and process BhavPath Game Coins array values 0-9 Collect 0,3,6,9 green win!""", "code": "btech=[81,75,90,85,88]\nprint(btech[0]) # 81\nprint(btech[-1]) # 88\nprint(btech[0:5:2]) # [81,90,88]\nbtech.append(92)\nprint(btech) # [81,75,90,85,88,92]", "interview": "Q1. List vs Array? Ans: List dynamic any type Array fixed type\nQ2. How to access last? Ans: arr[-1]\nQ3. Slicing? Ans: arr[start:stop:step]\nQ4. append vs extend? Ans: append adds one extend adds list", "placement": "TCS Reverse list Find average max min Infosys List operations Amazon Store millions records list BhavPath Game Coins array 0-9 collect 0,3,6,9 win!"}
    },
    "Java": {
        "Intro": {"theory": """Java OOP platform independent WORA Write Once Run Anywhere James Gosling Enterprise Android JVM runs bytecode Strongly typed Unlike Python needs type declaration int btech=81 String name Wipro Elite Infosys need Java.""", "code": "public class Main{\n    public static void main(String[] args){\n        System.out.println(\"BhavPath Java\");\n    }\n}\n// Output: BhavPath Java", "interview": "Q1. JVM? Ans: Runs bytecode\nQ2. Platform independent? Ans: Bytecode not machine code\nQ3. Java vs Python? Ans: Java compiled static typed", "placement": "Infosys SP Java OOPs 5 marks Wipro Elite Java collections must Package 5-9 LPA."}
    },
    "SQL": {
        "Basics": {"theory": """SQL Structured Query Language Data Engineer LIFE 70% work SQL Store manipulate retrieve data SELECT INSERT UPDATE DELETE DDL CREATE DML SELECT Aggregate SUM AVG COUNT Amazon Data Engineer full SQL! SELECT AVG(btech) as avg_btech FROM students Gives average 81 SELECT name btech FROM students WHERE btech>70 Gives >70% students.""", "code": "-- Average B.Tech %\nSELECT AVG(btech) as avg_btech FROM students;\n-- >70% students\nSELECT name,btech FROM students WHERE btech>70;\n-- Output: average 81", "interview": "Q1. WHERE vs HAVING? Ans: WHERE filters rows HAVING groups\nQ2. JOIN? Ans: Combine 2 tables\nQ3. AVG(btech)? Ans: SELECT AVG(btech) FROM students", "placement": "Amazon Data Engineer Interview Second highest B.Tech % TCS NQT Joins Group By Having Every company asks SQL!"},
        "Joins": {"theory": """SQL Joins Combine 2 tables Types INNER JOIN common LEFT JOIN all left RIGHT JOIN all right FULL JOIN Example SELECT students.name placements.company FROM students INNER JOIN placements ON students.id=placements.student_id Asked TCS NQT! Joins most important for Data Engineer!""", "code": "-- INNER JOIN Example\nSELECT s.name, p.company FROM students s INNER JOIN placements p ON s.id=p.student_id;\n-- Output: Bhavya TCS, Rahul Infosys", "interview": "Q1. Types of Joins? Ans: INNER LEFT RIGHT FULL\nQ2. INNER vs LEFT? Ans: INNER common LEFT all left\nQ3. Example? Ans: SELECT ... INNER JOIN placements ON id", "placement": "TCS NQT Joins asked 5 marks Infosys SP Joins Group By Amazon Joins must for Data Engineer!"}
    },
    "DSA": {
        "Arrays": {"theory": """DSA Arrays Complete Theory Most Important for MAANG:
WHAT IS ARRAY? Collection similar data types stored contiguous continuous adjacent memory locations Index starts 0 In Python list used as array Example btech_scores=[81,75,90,85,88] 5 integers continuous memory Array foundation DSA Without arrays no DSA no MAANG job Arrays 30% DSA interviews!
WHY ARRAY HEART OF PLACEMENTS MAANG? Amazon Google Flipkart Microsoft 100% DSA interviews start arrays First question array TCS Digital Infosys SP Wipro Elite DSA coding rounds Arrays must Package depends DSA Good DSA 10+ LPA Amazon Flipkart Poor DSA 3.5 LPA TCS Ninja Real World Student B.Tech % stored array Processed Sorted Searched Daily use BhavPath Game Logic range(0,10,3)=0,3,6,9 array indexing arr[0]=0 arr[1]=3 arr[2]=6 arr[3]=9 Step 3 indexing!
TYPES One Dimensional Single row [81,75,90,85,88] List B.Tech % Two Dimensional Matrix Rows Columns [[81,75,90],[85,88,92]] 2 students 3 subjects Image processing matrix Dynamic Array Python list grows automatically arr.append(92) Unlike C fixed size Associative Array Dict Python {'name':'Bhavya','btech':81} Key-value
OPERATIONS Time Complexity Very Important Access arr[0]=81 O(1) Direct via index Very Fast Best Search Find 90 in [81,75,90,85,88] O(n) Linear Check each Slow large Insert Insert 95 at 2 O(n) Shift elements [81,75,95,90,85,88] 90,85,88 shifted Delete Delete at 2 O(n) Shift [81,75,85,88] 90 deleted Traversal Visit all O(n) For loop Sorting Sort O(n log n) Quick sort Merge sort Important
INDEXING SLICING Python Special range(0,10,3) Logic Indexing arr[0] First 81 arr[2] Third 90 arr[-1] Last 88 arr[-2] Second last 85 Slicing arr[0:5:2]=[81,90,88] Start 0 stop 5 till index 4 step 2 Every 2nd Important arr[0:10:3]=Every 3rd element Logic same range(0,10,3)=0,3,6,9 Example btech=[81,75,90,85,88,92,78,85,90,88] btech[0:10:3]=[81,85,78,90] Index 0,3,6,9 => Values 81,85,78,90 Step 3
REAL PLACEMENT COMPANY WISE TCS NQT Easy Reverse array [81,75,90]=>[90,75,81] Use two pointers slicing [::-1] Find average sum/len 81+75+90/3=82 Find max max=90 min Infosys SP Medium Array rotation [81,75,90,85,88] rotate 2 => [90,85,88,81,75] Last 2 come first Find duplicates [81,75,81,90,75] duplicates 81,75 Use set Second largest [81,75,90,85,88] second largest 88 Not 90 Need sort two loops Amazon Data Engineer Medium Hard 10-15 LPA Find second largest without sorting O(n) Two variables max1 max2 Merge two sorted arrays [75,81,85] and [88,90,92]=>[75,81,85,88,90,92] Two pointers Find missing [0,1,2,4,5] missing 3 Sum formula n*(n+1)/2 - sum(arr) Kadane Maximum subarray sum Hard Flipkart ETL Process array student records For each student check B.Tech %>70 add eligible list Loop condition array ARRAY VS LIST PYTHON Array C Java Fixed size same type only int array only ints List Python Dynamic size any type [1,'Bhavya',8.1,True] valid Python list dynamic array So Python use list as array WHY range(0,10,3)=0,3,6,9 ARRAY INDEXING Consider array arr=[10,20,30,40,50,60,70,80,90,100] 10 elements index 0-9 range(0,10,3) gives index 0,3,6,9 arr[0]=10 arr[3]=40 arr[6]=70 arr[9]=100 So arr[0:10:3]=[10,40,70,100] Every 3rd element starting 0 Array slicing step Used data sampling every nth record BhavPath Game Connection Game has coins values 0,1,2,3,4,5,6,7,8,9 Array coins You must collect coins values 0,3,6,9 IN ORDER This is arr[0:10:3] If collect 1,2,4,5,7,8 Red bombs Lose life So game teaches array indexing step Arrays foundation DSA Master arrays indexing 0,3,6,9 = Master 30% DSA + BhavPath Game + TCS NQT + Amazon Without arrays no placement!""", "code": "btech_scores=[81,75,90,85,88,92,78,85,90,88]\nprint(f\"Array: {btech_scores}\")\nprint(f\"First element index 0: {btech_scores[0]}\") #81\nprint(f\"Every 3rd [0:10:3]: {btech_scores[0:10:3]}\")\n# [81,85,78,90] Index 0,3,6,9\navg=sum(btech_scores)/len(btech_scores)\nprint(f\"Average: {avg}\") #85.2", "interview": "Q1. What is array? Ans: Collection similar types contiguous memory index 0 Python list array\nQ2. Time complexity Access Search Insert Delete? Ans: Access O(1) fast Search O(n) linear Insert Delete O(n) shift\nQ3. First last every 3rd? Ans: First arr[0] Last arr[-1] Every 3rd arr[0:10:3] Index 0,3,6,9 range(0,10,3) logic!", "placement": "TCS NQT Easy Reverse average max min 2 questions 5 marks Infosys SP Medium Rotation duplicates second largest 3 questions 10 marks Amazon Medium-Hard 10-15 LPA Second largest without sorting Merge sorted Missing Kadane Flipkart ETL Process array BhavPath Game Coins array 0-9 Collect 0,3,6,9 green win Arrays 30% DSA Without arrays no MAANG!"}
    }
}

def is_certificate_locked():
    if st.session_state.xp < 150:
        return True, f"Need 150 XP - You have {st.session_state.xp} XP - Complete Skills and Tests"
    if len(st.session_state.completed) < 3:
        return True, f"Complete 3 modules - You completed {len(st.session_state.completed)}"
    if not st.session_state.game_unlocked:
        return True, "Complete 1 Test to unlock Game, then Certificate unlocks"
    return False, "Unlocked"

if st.session_state.page == "welcome":
    st.markdown("""<div class="welcome-box"><div style="font-size:70px">🚀</div><div style="font-size:60px; font-weight:900">BhavPath</div><div style="font-size:28px; margin-top:10px; font-weight:600">Welcome to your placement story</div><div style="font-size:16px; margin-top:10px; opacity:0.9">Learn. Grind. Game. Get Placed.</div></div>""", unsafe_allow_html=True)
    st.markdown("<br>")
    st.markdown("""<div class="glass-premium" style="text-align: center; padding: 25px;"><div style="font-size:20px; font-weight:600; color:white; font-style: italic;">"Your placement story is not about being perfect, it's about being persistent. Every line of code you write today is a step closer to your dream offer."</div><div style="font-size:12px; color:#aaa; margin-top:10px">BHAVPATH PREMIUM | Rise College</div></div>""", unsafe_allow_html=True)
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
    is_locked, lock_msg = is_certificate_locked()
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
        if is_locked:
            st.markdown(f'<div style="background: rgba(239,68,68,0.15); border: 2px solid #ef4444; border-radius: 15px; padding: 20px; text-align: center; height: 75px; display: flex; align-items: center; justify-content: center; flex-direction: column;"><div style="font-size:22px">🔒</div><div style="font-size:11px; color:#ef4444; font-weight:700">Certificate Locked</div></div>', unsafe_allow_html=True)
            st.caption(f"🔒 {lock_msg}")
        else:
            if st.button("📜 Certificate Zone - Unlocked ✅", use_container_width=True):
                st.session_state.purpose = "certificate"; st.session_state.page = "main"; st.rerun()
    st.markdown("")
    _, mid, _ = st.columns([1,1,1])
    with mid:
        if st.button("💼 Interview - Robot Face to Face Zoom", use_container_width=True):
            st.session_state.purpose = "interview"; st.session_state.page = "main"; st.rerun()
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"; st.rerun()
    st.markdown("<br>")
    st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
    st.markdown("### 🔓 How to Unlock Certificate Zone?")
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("XP", f"{st.session_state.xp}/150", delta="Done" if st.session_state.xp>=150 else f"{150-st.session_state.xp} needed")
    with c2: st.metric("Modules", f"{len(st.session_state.completed)}/3", delta="Done" if len(st.session_state.completed)>=3 else f"{3-len(st.session_state.completed)} needed")
    with c3: st.metric("Game", "Yes" if st.session_state.game_unlocked else "No", delta="Done" if st.session_state.game_unlocked else "Need Test")
    progress = min(100, int(st.session_state.xp/150*33 + len(st.session_state.completed)/3*33 + (33 if st.session_state.game_unlocked else 0)))
    st.progress(progress)
    st.write(f"Overall Progress: {progress}%")
    if is_locked: st.error(f"🔒 {lock_msg}")
    else: st.success("🎉 Certificate Unlocked!"); st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

st.sidebar.markdown(f'<div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 15px; border-radius: 15px; color: white; text-align: center;"><div style="font-size:22px; font-weight:800">🚀 BhavPath</div><div style="font-size:11px">Premium</div></div>', unsafe_allow_html=True)
st.sidebar.write(f"👤 {st.session_state.name} | 🎓 {st.session_state.college}")
st.sidebar.metric("XP", st.session_state.xp)
st.sidebar.metric("Modules", len(st.session_state.completed))
st.sidebar.metric("Game", "Unlocked" if st.session_state.game_unlocked else "Locked")
if st.sidebar.button("Change Purpose"): st.session_state.page = "purpose"; st.rerun()
if st.sidebar.button("Logout"): st.session_state.page = "welcome"; st.rerun()

if st.session_state.purpose == "skill":
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">📚 Skill Learning - Detailed Theory As Per Topic</div></div>', unsafe_allow_html=True)
    left, middle, right = st.columns([1,2.5,1.2], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        selected_topic = st.radio("Select Skill - 6 Skills", ["C", "C++", "Python", "Java", "SQL", "DSA"])
        selected_module = st.radio(f"Modules in {selected_topic}", TOPICS[selected_topic])
        st.markdown('</div>', unsafe_allow_html=True)
    with middle:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown(f'<div style="background: rgba(102,126,234,0.15); padding: 15px; border-radius: 12px; border-left: 4px solid #667eea; margin-bottom: 15px;"><div style="color:#667eea; font-size:11px; font-weight:700">MATERIAL HEADING</div><div style="color:white; font-size:24px; font-weight:800">{selected_topic} - {selected_module}</div></div>', unsafe_allow_html=True)
        data = FULL_DB.get(selected_topic, {}).get(selected_module, None)
        if not data:
            data = {"theory": f"{selected_module} in {selected_topic} Full Detailed Theory: {selected_module} is core fundamental concept in {selected_topic} Used to store process manage data Without {selected_module} cannot write program Building block Important for placements TCS NQT 2-3 questions Infosys SP mandatory Amazon 10-15 LPA advanced Real World Data Engineering Backend Frontend Data Science daily Example Code prints 0,3,6,9 using range(0,10,3) Step logic This is {selected_module} logic Used BhavPath Game Collect 0,3,6,9 green coins win! {selected_module} MUST for placements Master {selected_module} = Master {selected_topic} = Get Placed!", "code": f"# {selected_topic} - {selected_module}\nfor i in range(0,10,3):\n    print(i)\n# Output: 0,3,6,9", "interview": f"Q1. What is {selected_module}? Ans: Core fundamental concept in {selected_topic}\nQ2. Why important? Ans: TCS NQT 2-3 Qs Infosys SP mandatory Amazon advanced\nQ3. Example? Ans: Code prints 0,3,6,9 using range(0,10,3) Most asked!", "placement": f"TCS NQT: 2-3 questions on {selected_module} in {selected_topic} Infosys SP mandatory 5 marks Amazon Data Engineer 10-15 LPA Advanced {selected_module} Package Without {selected_module} 3.5 LPA With 7-15 LPA!"}
        with st.expander(f"📖 Theory - {selected_topic} {selected_module} - Full Detailed - Click to Open", expanded=True):
            st.markdown(data["theory"])
        with st.expander("💻 Code Examples - Click to Open - With Output", expanded=True):
            lang = "python"
            if selected_topic == "C": lang = "c"
            elif selected_topic == "C++": lang = "cpp"
            elif selected_topic == "Java": lang = "java"
            elif selected_topic == "SQL": lang = "sql"
            st.code(data["code"], language=lang)
            st.success("✅ Output: 0,3,6,9 - range(0,10,3) logic Step 3 - Used in BhavPath Game!")
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
        st.markdown(f"- **Skill:** {selected_topic}\n- **Heading:** {selected_module}\n- **Theory:** Full Detailed")
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
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">📊 Placement Percentage - Advanced Filter</div><div style="font-size:14px; opacity:0.9">10th + Inter + B.Tech % + Skills = Company List</div></div>', unsafe_allow_html=True)
    COMPANIES_DB = [
        {"name": "TCS Ninja", "min_10th": 60, "min_inter": 60, "min_btech": 60, "skills": ["C"], "package": "3.5 LPA", "role": "Ninja", "color": "#4ade80"},
        {"name": "TCS Digital", "min_10th": 70, "min_inter": 70, "min_btech": 70, "skills": ["C", "Python", "DSA"], "package": "7 LPA", "role": "Digital", "color": "#667eea"},
        {"name": "Infosys SP", "min_10th": 65, "min_inter": 65, "min_btech": 65, "skills": ["Python", "Java", "SQL"], "package": "5-9 LPA", "role": "SE", "color": "#fbbf24"},
        {"name": "Wipro Elite", "min_10th": 60, "min_inter": 60, "min_btech": 60, "skills": ["Java", "C++"], "package": "3.5-6 LPA", "role": "PE", "color": "#a78bfa"},
        {"name": "Amazon Data Engineer", "min_10th": 75, "min_inter": 70, "min_btech": 70, "skills": ["Python", "SQL", "DSA"], "package": "10-15 LPA", "role": "Data Engineer", "color": "#f472b6"},
        {"name": "Flipkart SDE", "min_10th": 70, "min_inter": 70, "min_btech": 70, "skills": ["DSA", "Python", "Java"], "package": "12-20 LPA", "role": "SDE", "color": "#60a5fa"},
        {"name": "Accenture", "min_10th": 65, "min_inter": 65, "min_btech": 60, "skills": ["SQL", "Python"], "package": "4.5 LPA", "role": "ASE", "color": "#34d399"},
        {"name": "Capgemini", "min_10th": 60, "min_inter": 60, "min_btech": 60, "skills": ["C", "C++", "Java"], "package": "4 LPA", "role": "Analyst", "color": "#fb7185"},
    ]
    left, right = st.columns([1, 1.8], gap="large")
    with left:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<h4 style="color:white; text-align:center">📝 Enter Your Details</h4>', unsafe_allow_html=True)
        tenth = st.number_input("10th Percentage %", 0, 100, 85)
        inter = st.number_input("Inter / Diploma %", 0, 100, 82)
        btech = st.number_input("B.Tech %", 0, 100, 81)
        st.divider()
        st.markdown('<h5 style="color:white">💻 Select Your Skills</h5>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            skill_c = st.checkbox("C Language", value=True)
            skill_cpp = st.checkbox("C++", value=False)
            skill_python = st.checkbox("Python", value=True)
        with c2:
            skill_java = st.checkbox("Java", value=False)
            skill_sql = st.checkbox("SQL", value=True)
            skill_dsa = st.checkbox("DSA", value=False)
        selected_skills = []
        if skill_c: selected_skills.append("C")
        if skill_cpp: selected_skills.append("C++")
        if skill_python: selected_skills.append("Python")
        if skill_java: selected_skills.append("Java")
        if skill_sql: selected_skills.append("SQL")
        if skill_dsa: selected_skills.append("DSA")
        st.markdown(f"<div style='background: rgba(102,126,234,0.2); padding: 10px; border-radius: 10px; margin-top:10px;'><div style='color:#aaa; font-size:11px'>Skills: {', '.join(selected_skills) if selected_skills else 'None'}</div><div style='color:white; font-size:12px; margin-top:5px'>10th: {tenth}% | Inter: {inter}% | B.Tech: {btech}%</div></div>", unsafe_allow_html=True)
        check_btn = st.button("🔍 Check Eligible Companies", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown('<h4 style="color:white">🏢 Eligible Companies Based on Your Profile</h4>', unsafe_allow_html=True)
        if check_btn:
            st.session_state.xp += 10
            eligible = []
            for comp in COMPANIES_DB:
                perc_ok = (tenth >= comp["min_10th"] and inter >= comp["min_inter"] and btech >= comp["min_btech"])
                skill_match = len(set(selected_skills) & set(comp["skills"])) > 0 if selected_skills else True
                if perc_ok and skill_match:
                    eligible.append(comp)
            if eligible:
                st.success(f"✅ You are eligible for {len(eligible)} companies!")
                for comp in eligible:
                    matched = set(selected_skills) & set(comp["skills"])
                    st.markdown(f"<div style='background: rgba(255,255,255,0.08); border-left: 5px solid {comp['color']}; border-radius: 15px; padding: 15px; margin-bottom: 10px;'><div style='color:white; font-size:16px; font-weight:800'>{comp['name']} ✅</div><div style='color:#aaa; font-size:12px'>{comp['role']} | Package: <b style='color:{comp['color']}'>{comp['package']}</b> | Criteria: 10th ≥{comp['min_10th']}% Inter ≥{comp['min_inter']}% B.Tech ≥{comp['min_btech']}% | Skills: {', '.join(comp['skills'])}</div><div style='margin-top:6px;'><span style='background: rgba(74,222,128,0.2); color:#4ade80; padding:4px 10px; border-radius:12px; font-size:11px;'>Matched: {', '.join(matched) if matched else 'Percentage'}</span></div></div>", unsafe_allow_html=True)
            else:
                st.error("❌ No companies matched. Improve percentages or add skills!")
        else:
            st.info("👈 Enter 10th %, Inter %, B.Tech % and select skills then click Check")
        st.markdown('</div>', unsafe_allow_html=True)

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
            st.session_state.game_unlocked=True; st.session_state.test_started=False; st.session_state.xp+=50; st.balloons(); st.rerun()
    else:
        game_html = """<!DOCTYPE html><html><head><style>body{margin:0;background:#0f0c29;display:flex;justify-content:center;align-items:center;flex-direction:column;font-family:Poppins}#gameCanvas{border:4px solid #667eea;border-radius:20px;background:#1a1a4e}#info{color:white;margin:10px;text-align:center;background:rgba(255,255,255,0.1);padding:12px 24px;border-radius:15px}</style></head><body><div id="info"><div>Score: <span id="score" style="color:#4ade80">0</span> | Target: <b style="color:#4ade80">0,3,6,9</b> | Lives: <span id="lives">3</span></div><div>Collected: <span id="collected">[]</span></div></div><canvas id="gameCanvas" width="600" height="400"></canvas><div id="message" style="color:#fbbf24; font-weight:bold; margin-top:10px"></div><script>const canvas=document.getElementById('gameCanvas');const ctx=canvas.getContext('2d');const scoreEl=document.getElementById('score');const livesEl=document.getElementById('lives');const collectedEl=document.getElementById('collected');const messageEl=document.getElementById('message');let player={x:300,y:200,size:22,speed:6,color:'#667eea'};let keys={};let score=0;let lives=3;let collected=[];let targetSequence=[0,3,6,9];let coins=[];let gameOver=false;let win=false;function spawnCoins(){coins=[];[0,3,6,9].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:true,size:20,color:'#4ade80',collected:false})});[1,2,4,5,7,8].forEach(val=>{coins.push({x:Math.random()*550+25,y:Math.random()*350+25,value:val,isCorrect:false,size:17,color:'#ef4444',collected:false})});}function drawPlayer(){ctx.fillStyle=player.color;ctx.beginPath();ctx.arc(player.x,player.y,player.size,0,Math.PI*2);ctx.fill();}function drawCoins(){coins.forEach(coin=>{if(!coin.collected){ctx.fillStyle=coin.color;ctx.beginPath();ctx.arc(coin.x,coin.y,coin.size,0,Math.PI*2);ctx.fill();ctx.fillStyle='white';ctx.font='bold 14px Poppins';ctx.textAlign='center';ctx.fillText(coin.value,coin.x,coin.y+5);}});}function checkCollision(){coins.forEach(coin=>{if(!coin.collected){let dx=player.x-coin.x,dy=player.y-coin.y,dist=Math.sqrt(dx*dx+dy*dy);if(dist<player.size+coin.size){coin.collected=true;if(coin.isCorrect){if(collected.length<targetSequence.length&&coin.value===targetSequence[collected.length]){collected.push(coin.value);score+=25;messageEl.textContent=`Correct! ${coin.value}!`;messageEl.style.color='#4ade80';}else{messageEl.textContent=`Wrong order!`;messageEl.style.color='#ef4444';lives--;}}else{lives--;messageEl.textContent=`BOMB!`;messageEl.style.color='#ef4444';}updateUI();if(JSON.stringify(collected)===JSON.stringify(targetSequence)){win=true;messageEl.textContent='WIN! +100 XP!';}if(lives<=0&&!win){gameOver=true;messageEl.textContent='Game Over!';}}}});}function updateUI(){scoreEl.textContent=score;livesEl.textContent=lives;collectedEl.textContent='['+collected.join(', ')+']';}function update(){if(gameOver||win)return;if(keys['ArrowUp']||keys['w'])player.y-=player.speed;if(keys['ArrowDown']||keys['s'])player.y+=player.speed;if(keys['ArrowLeft']||keys['a'])player.x-=player.speed;if(keys['ArrowRight']||keys['d'])player.x+=player.speed;player.x=Math.max(player.size,Math.min(canvas.width-player.size,player.x));player.y=Math.max(player.size,Math.min(canvas.height-player.size,player.y));ctx.clearRect(0,0,canvas.width,canvas.height);drawCoins();drawPlayer();checkCollision();requestAnimationFrame(update);}window.addEventListener('keydown',e=>{keys[e.key]=true;});window.addEventListener('keyup',e=>{keys[e.key]=false;});spawnCoins();update();</script></body></html>"""
        components.html(game_html, height=580, width=650)
        if st.button("Claim Win +100 XP", use_container_width=True): st.session_state.xp+=100; st.session_state.game_score+=100; st.balloons()

elif st.session_state.purpose == "certificate":
    is_locked, lock_msg = is_certificate_locked()
    if is_locked:
        st.markdown(f"""<div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); padding: 30px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:60px">🔒</div><div style="font-size:32px; font-weight:900">Certificate Zone Locked</div><div style="font-size:14px; opacity:0.9; margin-top:10px">{lock_msg}</div></div>""", unsafe_allow_html=True)
        st.markdown('<div class="glass-premium" style="text-align:center; padding:40px;">', unsafe_allow_html=True)
        st.markdown("### 🔒 Locked - Complete Requirements")
        st.markdown("1. **150 XP** - Complete skills + tests\n2. **3 Modules** - Skill Learning complete\n3. **Unlock Game** - Complete 1 Test")
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Your XP", st.session_state.xp, f"Need {150-st.session_state.xp}" if st.session_state.xp < 150 else "Completed")
        with c2: st.metric("Modules", len(st.session_state.completed), f"Need {3-len(st.session_state.completed)}" if len(st.session_state.completed) < 3 else "Completed")
        with c3: st.metric("Game", "Unlocked" if st.session_state.game_unlocked else "Locked")
        st.markdown("<br>")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("📚 Go to Skill Learning", use_container_width=True, type="primary"):
                st.session_state.purpose = "skill"; st.rerun()
        with col_b:
            if st.button("📝 Go to Test Zone", use_container_width=True, type="primary"):
                st.session_state.purpose = "test"; st.rerun()
        with col_c:
            if st.button("📊 Check Placement", use_container_width=True):
                st.session_state.purpose = "placement"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.stop()
    st.markdown('<div style="background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">📜 Certificate Zone - Unlocked ✅</div></div>', unsafe_allow_html=True)
    st.balloons()
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
                st.session_state.cert_score=88; st.session_state.cert_stage="result"; st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div style="background:white; border-radius:20px; padding:40px; text-align:center"><div style="font-size:50px">🏆</div><div style="font-size:36px; font-weight:900; color:#667eea">BHAVPATH PREMIUM</div><div style="letter-spacing:3px; color:#666">CERTIFICATE OF EXCELLENCE</div><div style="font-size:28px; font-weight:800; margin-top:15px">{st.session_state.name}</div><div style="color:#555">{st.session_state.college} | {st.session_state.email}</div><div style="margin:20px">Skill: <b>{st.session_state.cert_skill}</b> | Score: <b>{st.session_state.cert_score}%</b> | XP: {st.session_state.xp}</div><div style="background:#f0f4ff; padding:15px; border-radius:15px; color:green; font-weight:800">PLACEMENT READY - UNLOCKED AFTER HARD WORK</div></div>', unsafe_allow_html=True)

else:
    st.markdown('<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 20px; text-align: center; color: white; margin-bottom: 20px;"><div style="font-size:32px; font-weight:900">💼 AI Interview - Face to Face with Robot - Zoom Style</div></div>', unsafe_allow_html=True)
    robot_html = """<!DOCTYPE html><html><head><style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');*{font-family:'Poppins',sans-serif;margin:0;padding:0;box-sizing:border-box;}body{background:#0f0c29;}.zoom-container{background:#1a1a2e;border-radius:20px;padding:15px;border:2px solid #667eea;}.zoom-header{background:#000;padding:10px 15px;border-radius:12px 12px 0 0;display:flex;justify-content:space-between;align-items:center;color:white;}.zoom-dots{display:flex;gap:6px;}.dot{width:12px;height:12px;border-radius:50%;}.dot.red{background:#ef4444;}.dot.yellow{background:#fbbf24;}.dot.green{background:#4ade80;}.video-grid{display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-top:15px;}.video-box{background:#000;border-radius:15px;height:280px;position:relative;overflow:hidden;border:2px solid #333;}.video-box.robot{border-color:#667eea;background:linear-gradient(135deg,#0f0c29 0%,#302b63 100%);}.video-box.user{border-color:#4ade80;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);}.robot-avatar{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:white;}.robot-face{width:110px;height:110px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:60px;animation:pulse 2s infinite;box-shadow:0 0 30px rgba(102,126,234,0.6);}@keyframes pulse{0%{transform:scale(1);}50%{transform:scale(1.05);}100%{transform:scale(1);}}.robot-speaking{width:80px;height:4px;background:#4ade80;border-radius:2px;margin-top:15px;animation:speaking 0.5s infinite;}@keyframes speaking{0%{width:20px;}50%{width:80px;}100%{width:20px;}}.video-label{position:absolute;bottom:10px;left:10px;background:rgba(0,0,0,0.7);padding:5px 12px;border-radius:20px;color:white;font-size:12px;}.video-controls{display:flex;justify-content:center;gap:15px;margin-top:15px;background:#000;padding:12px;border-radius:0 0 12px 12px;}.control-btn{width:45px;height:45px;border-radius:50%;border:none;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;}.control-btn.mic{background:#4ade80;}.control-btn.video{background:#667eea;}.control-btn.end{background:#ef4444;}.question-panel{background:rgba(102,126,234,0.15);border:1px solid rgba(102,126,234,0.3);border-radius:15px;padding:20px;margin-top:15px;color:white;}.question-text{font-size:18px;font-weight:600;color:#fbbf24;margin-bottom:10px;}.timer{color:#4ade80;font-size:12px;}.transcript{background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;margin-top:10px;font-size:13px;color:#aaa;}</style></head><body><div class="zoom-container"><div class="zoom-header"><div style="display:flex;align-items:center;gap:10px;"><div class="zoom-dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div><span style="font-size:12px;">Zoom Meeting - BhavPath AI Interview</span></div><div style="font-size:11px;background:#ef4444;padding:4px 10px;border-radius:12px;">● REC 00:03:24</div></div><div class="video-grid"><div class="video-box robot"><div class="robot-avatar"><div class="robot-face">🤖</div><div style="margin-top:15px;font-weight:700;font-size:16px;">BhavPath AI Robot</div><div style="font-size:11px;opacity:0.7;margin-top:5px;">Senior Technical Interviewer</div><div class="robot-speaking"></div><div style="font-size:10px;color:#4ade80;margin-top:8px;">Speaking...</div></div><div class="video-label">🤖 Robot - Interviewer</div></div><div class="video-box user"><div class="robot-avatar"><div style="width:90px;height:90px;background:linear-gradient(135deg,#4ade80 0%,#22c55e 100%);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:50px;">👤</div><div style="margin-top:15px;font-weight:700;font-size:16px;">You - Candidate</div><div style="font-size:11px;opacity:0.7;margin-top:5px;">Rise College Ongole</div><div style="font-size:10px;color:#4ade80;margin-top:8px;">● Camera On | Mic On</div></div><div class="video-label" style="background:#4ade80;color:black;">👤 You - Live</div></div></div><div class="video-controls"><button class="control-btn mic">🎤</button><button class="control-btn video">📹</button><button class="control-btn" style="background:#333;">🖥️</button><button class="control-btn" style="background:#333;">💬</button><button class="control-btn end">📞</button></div><div class="question-panel"><div class="timer">⏱️ Question <span id="qNum">1</span> of 5 | Time: <span id="time">00:45</span></div><div class="question-text" id="questionText">Q1. Tell me about yourself and explain range(0,10,3) logic?</div><div style="font-size:12px;color:#aaa;margin-top:8px;">🤖 Robot is listening... Please answer clearly.</div><div class="transcript" id="transcript">Transcript: Listening... Waiting for your answer...</div></div></div><script>const questions=["Q1. Tell me about yourself and explain range(0,10,3) logic?","Q2. What is difference between C and Python? Explain with example 0,3,6,9?","Q3. What is array? Explain time complexity O(1) access?","Q4. Write SQL query to find average B.Tech %?","Q5. Where do you see yourself in 5 years? Why BhavPath?"];let currentQ=0;let timeLeft=45;function nextQuestion(){if(currentQ<questions.length-1){currentQ++;document.getElementById('qNum').textContent=currentQ+1;document.getElementById('questionText').textContent=questions[currentQ];document.getElementById('transcript').textContent="Transcript: Robot asked new question.";timeLeft=45;}else{document.getElementById('questionText').textContent="✅ Interview Completed! Click Submit to get certificate.";}}setInterval(()=>{timeLeft--;if(timeLeft<0)timeLeft=45;let s=timeLeft%60;document.getElementById('time').textContent=`00:${s<10?'0'+s:s}`;},1000);setInterval(nextQuestion,30000);</script></body></html>"""
    components.html(robot_html, height=650)
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        st.markdown('<div class="glass-premium">', unsafe_allow_html=True)
        st.markdown("##### 🎤 Your Answer - Robot is Listening")
        interview_skills = st.selectbox("Select Interview Type", ["Python Developer", "Java Developer", "SQL Data Engineer", "C Programming", "DSA Interview"])
        current_q = st.text_area("Your Answer", placeholder="Myself Bhavya from Rise College, Ongole. I know range(0,10,3) prints 0,3,6,9...", height=120)
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
