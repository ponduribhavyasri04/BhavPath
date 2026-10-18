import streamlit as st

st.set_page_config(page_title="BhavPath - All Topics Final", layout="centered", page_icon="🚀")

# --- THEME - FIXED FOR VISIBILITY ---
st.markdown("""
<style>
.stApp { background-color: #EAF2FF !important; }
h1,h2,h3,p,div,span,label,li { color: #000000 !important; }
h1 { color: #0F2C61 !important; font-weight: 900 !important; font-size: 28px !important; }
h2 { color: #1E40AF !important; font-size: 22px !important; font-weight: 800 !important; }
.white-card { background: #FFFFFF !important; color: #000000 !important; border-radius: 12px; padding: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 10px; border: 2px solid #2563EB; }
.blue-card { background: #2563EB !important; color: #FFFFFF !important; border-radius: 14px; padding: 16px; }
.blue-card b, .blue-card div, .blue-card li { color: #FFFFFF !important; }
.green-card { background: #F0FFF4 !important; border-left: 5px solid #22C55E; padding: 12px; border-radius: 8px; margin-bottom:8px; }
.topic-card { background: #FFFFFF !important; border-radius: 16px; padding: 18px; border: 2px solid #2563EB; margin-bottom:12px; }
.topic-card:hover { background: #EFF6FF !important; }
.locked-card { background: #D1D5DB !important; color: #6B7280 !important; border-radius: 12px; padding: 14px; border: 2px dashed #9CA3AF; }
.stButton>button { background: #2563EB !important; color: #FFFFFF !important; border-radius: 10px; font-weight: bold !important; }
input { color: #000000 !important; }
</style>
""", unsafe_allow_html=True)

# --- SESSION ---
if 'page' not in st.session_state: st.session_state.page = "login"
if 'xp' not in st.session_state: st.session_state.xp = 820
if 'user' not in st.session_state: st.session_state.user = {}
if 'purpose' not in st.session_state: st.session_state.purpose = None
if 'selected_topic' not in st.session_state: st.session_state.selected_topic = "C++"
if 'completed' not in st.session_state: st.session_state.completed = {"Intro": False, "Syntax": False, "Core": False}

# --- ALL TOPICS - FULL INFO - LIKE GEEKS BUT NO GFG WORD ---
TOPICS = {
    "C": {
        "title": "C Programming - Complete Tutorial",
        "desc": "Mother of all languages - Dennis Ritchie 1972 - Foundation for everything",
        "what_is": "**What is C?**\nC is procedural, middle-level language created by Dennis Ritchie in 1972. It is the mother of all languages - C++, Java, Python all came from C. No OOP. Fastest for system programming. Used for OS (Linux Kernel), Embedded Systems, Drivers, Compilers. For your 81% profile, C is must for basics.",
        "syntax": "#include <stdio.h>\n\nint main(){\n    // Your first C program\n    printf(\"Hello BhavPath!\\n\");\n    printf(\"Welcome to C World\");\n    return 0;\n}\n// Output: Hello BhavPath!",
        "features": [
            "Procedural Language - Step by step execution",
            "Fast & Efficient - Closest to hardware after Assembly",
            "Memory Management with malloc() / free() - You control memory",
            "Rich set of operators - 45+ operators",
            "Used in OS Development - Linux, Windows Kernel parts in C",
            "Portable - Write once, compile anywhere"
        ],
        "hello": "#include <stdio.h>\nint main(){\n int a=10, b=20;\n int sum=a+b;\n printf(\"Sum is %d\", sum);\n return 0;\n}\n// Output: Sum is 30",
        "variables": "**Variables & Data Types in C:**\nVariable is name of memory location.\n\n1. **int:** 4 bytes - int btech=81;\n2. **float:** 4 bytes - float cgpa=8.1;\n3. **char:** 1 byte - char grade='A';\n4. **array:** Collection - int marks[5]={81, 75, 80};\n5. **pointer:** Stores address - int *p=&a;\n\nSyntax: data_type name = value;\nExample: int percentage=81; // 4 bytes\nWhy? Memory optimization - Important for interview!",
        "control": "**Control Statements in C:**\n\n1. **if-else:**\nif(btech>=60) printf(\"Eligible\"); else printf(\"Not\");\n\n2. **for loop - Final Boss Logic:**\nfor(int i=0;i<10;i+=3) printf(\"%d \", i); // 0 3 6 9 - Coins!\nIf i+=1 -> 0 1 2 3 4 5 6 7 8 9\nIf i+=3 -> 0 3 6 9 -> Optimal for game!\n\n3. **while loop:**\nint i=0; while(i<10){ printf(\"%d\", i); i+=3; }\n\n4. **switch:**\nswitch(grade){ case 'A': printf(\"Excellent\"); break; }",
        "oop_extra": "**Functions & Pointers in C:**\n\n**Function:** Block of code - Reuse\nSyntax: int add(int a, int b){ return a+b; }\n\n**Pointer:** Variable that stores address\nint a=10; int *p=&a; // p stores address of a\nprintf(\"%d\", *p); // 10 - Value at address\nWhy pointer? 1. Dynamic memory 2. Efficient arrays 3. For Gaming Engine speed\nTypes: Null pointer (int *p=NULL), Dangling pointer (points to deleted memory)",
        "applications": ["🖥️ Operating Systems: Linux, Windows Kernel", "⌚ Embedded Systems: Watches, AC, Washing Machine", "🎮 Compilers: GCC compiler written in C", "🗄️ Databases: MySQL core in C"],
        "interview": [
            {"q": "What is C? Who invented? Why use?", "a": "C is procedural, middle-level language invented by Dennis Ritchie in 1972. Mother of all languages. Used for OS, Embedded because fast and close to hardware. For interview: Say 'I started with C for basics, then moved to C++ for BhavPath Final Boss game - for loop logic from C'"},
            {"q": "What is pointer? Types? Why used in Gaming?", "a": "Pointer stores address. int a=10; int *p=&a; Types: Null (int *p=NULL), Dangling (points to deleted memory - dangerous), Wild (uninitialized). Why? Dynamic memory, efficient arrays, Gaming Engine memory control - Direct memory access for speed. In Unreal Engine, pointers used for optimization. Say 'I understand pointer logic for game performance in BhavPath'"},
            {"q": "malloc vs calloc vs free?", "a": "malloc: Single block, uninitialized - malloc(4) - 4 bytes. calloc: Multiple blocks + zero initialized - calloc(4, sizeof(int)) - 4 ints zeroed. free: Frees memory - free(p). Must free else memory leak. For interview: Always say 'After malloc, must free to avoid leak'"},
            {"q": "Tell me about yourself? - C background", "a": "I'm Bhav from Rise College, Ongole with 81%. I started my coding journey with C - Learned pointers, memory management. Then built BhavPath in Python/Streamlit where I used C logic - for loop 0,3,6,9 for Final Boss coins. My strength is strong basics in C which helps me understand other languages like Python, Java faster."}
        ]
    },
    "C++": {
        "title": "C++ Programming Language - Complete Tutorial",
        "desc": "C with Classes - Bjarne Stroustrup 1983 - OOP + Gaming Engines",
        "what_is": "**What is C++?**\nC++ is general-purpose language created by Bjarne Stroustrup at Bell Labs in 1983. Extension of C with Object-Oriented Programming. Initially called 'C with Classes'. Middle-level language - Both low-level (memory) and high-level (OOP). Used for: Operating Systems, Browsers (Chrome), Gaming Engines (Unreal Engine - Fortnite, PUBG), Databases, Embedded Systems. For your 81% profile, C++ is important for TCS NQT, Gaming.",
        "syntax": "#include <iostream>  // Header for input output\nusing namespace std; // So we don't write std::\n\nint main(){ // Execution starts from main\n    cout << \"Hello BhavPath!\"; // cout for print\n    return 0; // Success\n}\n// Output: Hello BhavPath!",
        "features": [
            "Object-Oriented: Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction - Helps build large apps like BhavPath",
            "Platform Dependent but Portable - Code runs on different machines with little change",
            "Mid-level Language - Low-level memory + High-level OOP",
            "Memory Management: Pointers - Direct memory access - Crucial for Gaming Engines for speed",
            "STL (Standard Template Library): Ready-made containers - vector, map, set, stack, queue - Saves time in interviews",
            "High Performance: Faster than Java/Python - Used where speed matters - Gaming, OS",
            "Rich Library: Large standard library"
        ],
        "hello": "#include <iostream>\nusing namespace std;\nint main(){\n cout << \"Hello BhavPath! Welcome to C++ World\";\n int a=10, b=20;\n int sum=a+b;\n cout << \"\\nSum is: \" << sum;\n return 0;\n}\n// Output: Hello BhavPath! Sum is 30",
        "variables": "**Variables & Data Types in C++:**\nVariable: Name of memory location.\nSyntax: data_type variable_name = value;\n\n1. **int:** 4 bytes - int btech_percentage=81;\n2. **float:** 4 bytes - float cgpa=8.1f;\n3. **double:** 8 bytes - double pi=3.14159265359;\n4. **char:** 1 byte - char grade='A';\n5. **string:** Dynamic - Need #include <string> - string college=\"Rise\"; string name=\"Bhav\";\n6. **bool:** 1 byte - bool isPlaced=false;\n\nMemory Example: int percentage=81; // 4 bytes\nWhy Data Types? To save memory. For 70% interview: Say 'Data types help in memory optimization'",
        "control": "**Control Statements in C++ - Final Boss Logic:**\n\n**1. if-else - Decision Making:**\nint btech=81;\nif(btech>=60) cout<<\"Eligible for TCS NQT\"; else cout<<\"Not Eligible\";\n// Output: Eligible\n\n**2. for loop - Loop Legends Game Logic:**\nfor(int i=0; i<10; i+=3) cout<<i<<\" \"; // i=0,3,6,9 - Coins!\nThis is exactly your game logic! If i+=1, path 0,1,2,3,4,5,6,7,8,9 - collects all. If i+=3, path 0,3,6,9 - 4 coins - Optimal!\n\n**3. while loop:**\nint i=0; while(i<10){ cout<<i; i+=3; }\n\n**4. switch:**\nswitch(grade){ case 'A': cout<<\"Excellent\"; break; default: cout<<\"Need improvement\"; }",
        "oop_extra": "**OOP Concepts in C++ - Important for 81% Interview:**\n\n**1. Class:** Blueprint - class Student{ public: string name; int percentage; void display(){ cout<<name; } };\n**2. Object:** Instance - Student s1; s1.name=\"Bhav\"; s1.percentage=81;\n**3. Inheritance:** One class inherits another - Code reuse - class Warrior{ public: void attack(){ cout<<\"Attack!\"; } }; class SuperWarrior : public Warrior{ public: void superAttack(){} }; SuperWarrior sw; sw.attack(); // Inherited\n**4. Polymorphism:** Same function name, different behavior - void print(int a) and void print(string s)\n**5. Encapsulation:** Wrapping data + methods - Data hiding using private - class BankAccount{ private: int balance; public: void setBalance(int b){ balance=b; } };\n**6. Abstraction:** Showing only essential - You click Play Game button - You don't need to know internal code",
        "applications": ["🎮 Gaming Engines: Unreal Engine (Fortnite, PUBG), Godot Engine, Source 2 (Dota 2) - All use C++ for speed - This is why BhavPath Final Boss uses C++ logic!", "💻 Operating Systems: Windows, Linux parts, macOS parts", "🌐 Browsers: Google Chrome, Mozilla Firefox - Rendering engines in C++", "🗄️ Databases: MySQL, MongoDB core in C++"],
        "interview": [
            {"q": "What is C++? Who invented?", "a": "C++ is general-purpose, middle-level, object-oriented language invented by Bjarne Stroustrup at Bell Labs in 1983. Extension of C with OOP. Initially called C with Classes. Used for gaming engines, OS, browsers because of speed. For your interview: Add 'I used C++ logic in my BhavPath Final Boss game - for loop for coin collection'"},
            {"q": "Difference between C and C++? (Most asked for 81% profile)", "a": "C is procedural, C++ is both procedural + OOP. C has no classes, objects, inheritance. C++ has STL, exception handling, references. C has malloc/free, C++ has new/delete + constructors/destructors. C is faster for low-level, C++ better for large apps. Your answer: 'As a 81% student, I prefer C++ for projects like BhavPath because OOP helps manage code - I used classes for Student, Module'"},
            {"q": "What is OOP? Explain with real example - Your project", "a": "OOP is organizing code as objects with data + behavior. 4 pillars: Inheritance, Polymorphism, Encapsulation, Abstraction. Real example from BhavPath: I created class Module { bool isCompleted; void markDone(); } and class Game : public Module { void play(); } - Inheritance. Same function play() behaves differently for Loop Legends vs Variable Vault - Polymorphism. Private XP variable - Encapsulation. User just clicks Play - Abstraction. This answer will impress for 81% profile!"},
            {"q": "What is pointer? Why use? (Important for Gaming)", "a": "Pointer is variable that stores address. Syntax: int a=10; int *p = &a; Why? 1. Dynamic memory 2. Efficient arrays 3. Gaming engine memory control - Direct memory access for speed. Types: Null pointer (int *p=null), Dangling pointer (points to deleted memory) - Dangerous - Causes crash. For interview: Say 'Pointer used in Unreal Engine for memory optimization'"},
            {"q": "Tell me about yourself? - Perfect answer for 81% Rise College", "a": "Sure! I'm Bhav from Rise College, Ongole with 81% in BTech. I built BhavPath - a game-based learning platform where students must complete C++ modules (Variables, Control, OOP) to unlock Final Boss game - Loop Legends. It has full tutorials, placement eligibility checker based on %, skill gap analyzer, and auto resume builder. My BTech is 81%, XP 820, completed 2/5 modules. My strength is converting theory into game - like for loop coins at 0,3,6,9. I'm looking for a role where I can use both my Data Science knowledge and C++ game logic."}
        ]
    },
    "Python": {
        "title": "Python Programming - Complete Tutorial",
        "desc": "Most popular for Data Science, AI - Guido van Rossum 1991 - Easy af",
        "what_is": "**What is Python?**\nPython is high-level, interpreted, easy syntax language created by Guido van Rossum in 1991. No need to declare type - Dynamic typing - a=10, a='Bhav' same variable works. Huge libraries: Pandas, Numpy, TensorFlow for Data Science, AI. Used for Data Science, AI/ML, Web (Django, Flask), Automation, Scripting. For your 81% Data Science profile, Python is MUST - Most important for placements 2025!",
        "syntax": "# No need for #include - Simple af\nprint(\"Hello BhavPath!\")\n\n# Variables - No type declaration\nbtech=81\nname=\"Bhav\"\ncollege=\"Rise College\"\nprint(f\"My BTech is {btech}%\")\n\n# Output: Hello BhavPath! My BTech is 81%",
        "features": [
            "Easy Syntax - No semicolon, No brackets - Just indentation - Beginner friendly",
            "Dynamic Typing: a=10, a='Bhav' - Same variable can hold different types - No declaration needed",
            "Huge Libraries: Pandas for Data, Numpy for math, TensorFlow for AI - For your 81% Data Science profile - Most important",
            "Interpreted Language - No compilation - Run directly - Fast development",
            "Used in AI/ML, Data Science, Automation, Web Development - Trending 2025",
            "Large Community - Lots of tutorials, Stack Overflow answers"
        ],
        "hello": "print(\"Hello BhavPath! Welcome to Python World\")\na=10\nb=20\nsum=a+b\nprint(f\"Sum is: {sum}\")\n\n# List example - Important for Data Science\nmarks=[81, 75, 80, 85]\nprint(f\"My marks: {marks}\")\nprint(f\"Average: {sum(marks)/len(marks)}\")\n# Output: Sum is: 30, Average: 80.25",
        "variables": "**Variables & Data Types in Python:**\nNo need to declare type - Dynamic!\n\n1. **int:** btech=81\n2. **float:** cgpa=8.1\n3. **str:** name='Bhav', college=\"Rise\" - String - Need quotes\n4. **list:** marks=[81, 75, 80] - Mutable, ordered - Most used in Data Science\n5. **tuple:** coordinates=(10, 20) - Immutable\n6. **dict:** student={'name':'Bhav', 'btech':81} - Key-value - Like map in C++\n7. **bool:** isPlaced=False - True/False capital T/F\n\nExample: btech=81 # No int needed - Python knows!\nWhy? Easy to code - Fast for Data Science projects!",
        "control": "**Control Statements in Python - Final Boss Logic Python Way:**\n\n**1. if-else:**\nbtech=81\nif btech>=60:\n    print(\"Eligible for TCS NQT\")\nelse:\n    print(\"Not Eligible\")\n# Note: No brackets, only indentation - Python style!\n\n**2. for loop - Loop Legends Game - Python Version:**\n# Coins at 0,3,6,9\nfor i in range(0, 10, 3):\n    print(i, end=\" \") # i=0,3,6,9 - Same logic as C++ but Python syntax!\n# Output: 0 3 6 9 - This is Final Boss!\n# If range(0,10,1) -> 0 1 2 3 4 5 6 7 8 9\n# If range(0,10,3) -> 0 3 6 9 -> Optimal!\n\n**3. while loop:**\ni=0\nwhile i<10:\n    print(i)\n    i+=3",
        "oop_extra": "**Functions, OOP & Data Science in Python:**\n\n**Function:**\ndef add(a, b):\n    return a+b\nprint(add(10,20)) # 30\n\n**OOP in Python:**\nclass Student:\n    def __init__(self, name, per):\n        self.name=name\n        self.per=per\n    def display(self):\n        print(self.name)\ns1=Student(\"Bhav\", 81)\ns1.display()\n\n**Data Science - For your profile:**\nimport pandas as pd\nimport numpy as np\ndf=pd.read_csv('students.csv')\nprint(df.head()) # First 5 rows\nprint(df['btech'].mean()) # Average btech %\n# Pandas is must for Data Engineering role!",
        "applications": ["📊 Data Science: Pandas, Numpy, Matplotlib - For your 81% profile - Most important!", "🤖 AI/ML: TensorFlow, PyTorch - Trending 2025", "🌐 Web Development: Django, Flask - Instagram backend in Django", "🤖 Automation: Script to automate boring tasks", "📈 Data Engineering: ETL pipelines - Your future role!"],
        "interview": [
            {"q": "Python vs C++? Which is better for Data Science?", "a": "Python easy syntax, dynamic typing, huge libraries (Pandas, Numpy) - Best for Data Science, fast development. C++ fast performance, static typing, memory control - Best for Gaming Engines, OS. For Data Science 81% profile, Python is better because Pandas makes data handling easy. But for speed, C++ better. In BhavPath, I used Python for backend (Streamlit) and C++ logic for game - Best of both!"},
            {"q": "What is list vs tuple vs dict? (Most asked)", "a": "List: Mutable, ordered, [] - marks=[81,75,80] - Can change marks[0]=85. Tuple: Immutable, ordered, () - coordinates=(10,20) - Can't change - Faster than list. Dict: Key-value, {} - student={'name':'Bhav', 'btech':81} - Like map in C++ - Fast lookup by key. For Data Science, list and dict most used. Example: df as list of dicts."},
            {"q": "Explain Pandas? Why important for Data Engineering?", "a": "Pandas is Python library for Data manipulation - DataFrame is table like Excel. df=pd.read_csv('students.csv') - Reads CSV. df.head() - First 5 rows. df['btech'].mean() - Average. df.groupby('college')['btech'].mean() - Avg per college - Important for Data Engineering interview! For your profile: Say 'I used Pandas in BhavPath to analyze student data - Avg BTech % per college'"},
            {"q": "Tell me about yourself? - Python + Data Science", "a": "I'm Bhav from Rise College, Ongole with 81% in Data Science. I love Python because easy syntax and powerful for Data Science - I built BhavPath using Streamlit (Python) - It has topic selector for Python, C++, Java, Data Engineering. I used Python logic for Final Boss game - for i in range(0,10,3) coins at 0,3,6,9. My skills: Python, Pandas, Numpy, SQL, Data Engineering concepts like ETL. Looking for Data Engineer role."}
        ]
    },
    "Java": {
        "title": "Java Programming - Complete Tutorial",
        "desc": "Write Once Run Anywhere - James Gosling 1995 - Android, Enterprise",
        "what_is": "**What is Java?**\nJava is OOP, platform independent language created by James Gosling at Sun Microsystems in 1995. WORA - Write Once Run Anywhere - Code compiled to bytecode, runs on JVM (Java Virtual Machine) on any OS. Pure OOP - Everything is object. Automatic Memory Management - Garbage Collector frees memory. Used for Android Apps (Android Studio), Enterprise Apps (Banking, E-commerce), Big Data (Hadoop). For placements, Java is must for Infosys, Wipro, TCS.",
        "syntax": "public class Main{\n    public static void main(String[] args){\n        // Your first Java program\n        System.out.println(\"Hello BhavPath!\");\n        System.out.println(\"Welcome to Java World\");\n    }\n}\n// Output: Hello BhavPath!",
        "features": [
            "Platform Independent - WORA - Write Once Run Anywhere - Bytecode runs on JVM on any OS - Windows, Linux, Mac",
            "Pure OOP - Everything is object - Strong OOP than C++",
            "Automatic Memory Management - Garbage Collector - No need for free() like C - No memory leak",
            "Robust & Secure - Exception handling, No pointers (safer than C++)",
            "Multithreading - Multiple tasks at same time - Used in servers",
            "Used in Android, Enterprise (Banking), Big Data - Most jobs in Java"
        ],
        "hello": "public class Main{\n public static void main(String[] args){\n  System.out.println(\"Hello BhavPath! Welcome to Java World\");\n  int a=10, b=20;\n  int sum=a+b;\n  System.out.println(\"Sum is: \" + sum);\n }\n}\n// Output: Hello BhavPath! Sum is 30",
        "variables": "**Variables & Data Types in Java:**\nNeed to declare type - Static typing like C++\n\n1. **int:** 4 bytes - int btech=81;\n2. **float:** 4 bytes - float cgpa=8.1f; // Need f\n3. **double:** 8 bytes - double pi=3.14159;\n4. **char:** 2 bytes (Unicode) - char grade='A';\n5. **String:** String college=\"Rise\"; // Capital S - String is object in Java\n6. **boolean:** boolean isPlaced=false; // Small b, not capital\n\nSyntax: data_type name = value;\nExample: int percentage=81;\nString name=\"Bhav\"; // Capital S\nWhy? Strong typing - Catches errors at compile time!",
        "control": "**Control Statements in Java - Final Boss Logic Java Way:**\n\n**1. if-else:**\nint btech=81;\nif(btech>=60) System.out.println(\"Eligible for TCS NQT\"); else System.out.println(\"Not Eligible\");\n\n**2. for loop - Loop Legends Game - Java Version:**\nfor(int i=0; i<10; i+=3){\n    System.out.print(i + \" \"); // i=0,3,6,9 - Same logic!\n}\n// Output: 0 3 6 9 - Final Boss!\n\n**3. while loop:**\nint i=0; while(i<10){ System.out.print(i); i+=3; }",
        "oop_extra": "**OOP & Collections in Java:**\n\n**Class & Object:**\nclass Student{ String name; int per; void display(){ System.out.println(name); } }\nStudent s1=new Student(); s1.name=\"Bhav\"; s1.per=81;\n\n**Inheritance:**\nclass Warrior{ void attack(){ System.out.println(\"Attack!\"); } }\nclass SuperWarrior extends Warrior{ void superAttack(){ System.out.println(\"Super!\"); } }\n\n**Collections - Like STL in C++:**\nArrayList<Integer> coins=new ArrayList<>(); coins.add(0); coins.add(3); coins.add(6); coins.add(9);\nHashMap<String, Integer> student=new HashMap<>(); student.put(\"Bhav\", 81);\n// ArrayList = vector in C++, HashMap = map in C++ - Important for coding rounds!",
        "applications": ["📱 Android Apps: Android Studio uses Java/Kotlin - Most Android apps in Java", "🏦 Enterprise Apps: Banking, E-commerce - Infosys, TCS use Java", "🗄️ Big Data: Hadoop written in Java", "🌐 Web Apps: Spring Boot framework for backend"],
        "interview": [
            {"q": "Java vs C++? Why Java for Enterprise?", "a": "Java platform independent (WORA - JVM), has Garbage Collector (no memory leak), no pointers (safer), pure OOP. C++ platform dependent, manual memory (new/delete), has pointers, faster performance. For Enterprise (Banking), Java better because secure, portable, robust. For Gaming Engines, C++ better because speed, memory control. Say 'For BhavPath backend, if I used Java, it would be platform independent via JVM'"},
            {"q": "What is JVM, JRE, JDK?", "a": "JVM: Java Virtual Machine - Converts bytecode to machine code - Makes Java platform independent. JRE: Java Runtime Environment - JVM + Libraries to run Java apps. JDK: Java Development Kit - JRE + Compiler (javac) to develop Java apps. For interview: Draw diagram - JDK contains JRE, JRE contains JVM. Say 'I write code in JDK, compile to bytecode, JVM runs it anywhere'"},
            {"q": "What is OOP pillars in Java? With example", "a": "4 pillars: 1. Inheritance: extends - SuperWarrior extends Warrior - Code reuse. 2. Polymorphism: Same method name different behavior - Overloading (same class, different params) and Overriding (subclass overrides). 3. Encapsulation: private variables + public getters/setters - Data hiding. 4. Abstraction: abstract class, interface - Shows only essential. Example from BhavPath: Game is abstract class with abstract play() method, LoopLegends overrides play() with for loop logic - Abstraction + Polymorphism."},
            {"q": "Tell me about yourself? - Java profile", "a": "I'm Bhav from Rise College, Ongole with 81%. I have strong Java basics - OOP, Collections (ArrayList, HashMap), JVM concept. I built BhavPath where I applied Java logic - for(int i=0;i<10;i+=3) for Final Boss coins at 0,3,6,9. My skills: Java, OOP, SQL, Data Structures. I understand Java is used in Enterprise and Android - I'm interested in backend development with Spring Boot. Looking for Software Engineer role."}
        ]
    },
    "Data Engineering": {
        "title": "Data Engineering - Complete Tutorial - Trending 2025",
        "desc": "Build pipelines for Data Science - Most demanding for 81% Data Science profile",
        "what_is": "**What is Data Engineering?**\nData Engineering is building systems to collect, store, process, and make data available for Data Science. You are Data Science student - This is YOUR CORE! Data Engineer builds pipelines, Data Scientist analyzes data. Tools: SQL (must), Python (Pandas, Numpy), ETL (Extract Transform Load), Big Data (Hadoop, Spark), Cloud (AWS, GCP), Data Warehousing (Snowflake, BigQuery). For 81% Data Science student, Data Engineering is best role - Highest demand 2025 - Salary 8-15 LPA for freshers!",
        "syntax": "-- SQL for Data Engineering - Must know!\nSELECT college, AVG(btech_percent) as avg_percent\nFROM students\nWHERE btech_percent >= 60\nGROUP BY college\nORDER BY avg_percent DESC;\n\n# Python ETL for Data Engineering\nimport pandas as pd\n# Extract\nprint(\"Extracting...\")\ndf = pd.read_csv('students.csv')\n# Transform\nprint(\"Transforming...\")\ndf['eligible'] = df['btech'] >= 60\n# Load\nprint(\"Loading...\")\ndf.to_csv('processed_students.csv', index=False)\nprint(\"ETL Done!\")",
        "features": [
            "ETL: Extract Transform Load - Core concept - Extract from source (DB, CSV), Transform (clean, filter), Load to warehouse (Snowflake) - Like BhavPath: Extract user data, Transform %, Load to dashboard",
            "SQL: Must for Data Eng - Joins, Group By, Window functions, CTEs - 80% of interview questions from SQL - For your 81% profile, SQL is must!",
            "Big Data: Hadoop (HDFS, MapReduce), Spark (PySpark) - For large data - TBs of data - Traditional DB can't handle - Spark is fast - 100x faster than Hadoop",
            "Data Pipeline: Data flows from source to warehouse via pipeline - Automated - Daily runs - Like BhavPath data flow: Login -> BTech % -> Topics -> Game -> XP",
            "Data Warehousing: Snowflake, BigQuery, Redshift - Stores processed data for analysis - Data Scientists query warehouse",
            "Cloud: AWS (S3, Glue, Redshift), GCP (BigQuery), Azure - All companies moving to cloud - Cloud DE is trending"
        ],
        "hello": "-- Hello World in Data Engineering - SQL\nSELECT 'Hello BhavPath! Welcome to Data Engineering World' as message;\n\n-- Find eligible students for TCS NQT (60% needed) - Your use case!\nSELECT name, btech_percent, college\nFROM students\nWHERE btech_percent >= 60\nORDER BY btech_percent DESC;\n\n# Python - Hello Data Engineering\nimport pandas as pd\nprint(\"Hello BhavPath! Data Engineering\")\ndf = pd.DataFrame({'name':['Bhav', 'Aarav'], 'btech':[81, 75]})\nprint(df)\nprint(f\"Average BTech: {df['btech'].mean()}%\")\n# Output: Average BTech: 78.0%",
        "variables": "**SQL & Python for Data Engineering - Must for 81%:**\n\n**SQL Basics:**\n1. **SELECT:** SELECT name, btech FROM students;\n2. **WHERE:** WHERE btech>=60 - Filter\n3. **GROUP BY:** GROUP BY college - Group\n4. **JOIN:** JOIN - Combine tables - INNER, LEFT, RIGHT\n   SELECT s.name, c.college_name FROM students s JOIN colleges c ON s.college_id=c.id;\n5. **Aggregation:** COUNT(), AVG(), SUM(), MAX(), MIN() - SELECT AVG(btech) FROM students;\n6. **Window Functions:** ROW_NUMBER(), RANK() - Advanced - For interviews\n\n**Python for DE:**\nimport pandas as pd\nimport numpy as np\ndf=pd.read_csv('students.csv') # Extract\ndf['eligible']=df['btech']>=60 # Transform\ndf.to_csv('out.csv') # Load - Full ETL!",
        "control": "**ETL Pipeline - Control Flow in Data Engineering:**\n\n**ETL = Extract Transform Load - Like for loop control:**\n\n**1. Extract - Like initialization:**\n# Extract from multiple sources\nimport pandas as pd\ndf1=pd.read_csv('students.csv') # From CSV\ndf2=pd.read_sql('SELECT * FROM students', connection) # From DB\n# Like for loop: for(i=0;...) initialization - Extract is start\n\n**2. Transform - Like condition & increment:**\n# Transform - Clean, filter, aggregate - Like if-else and for logic\n# if btech>=60 eligible - Same as placement logic!\ndf['eligible']=df['btech'].apply(lambda x: 'Yes' if x>=60 else 'No')\ndf['grade']=df['btech'].apply(lambda x: 'A' if x>=80 else 'B')\n# Like for loop: for(i=0;i<10;i+=3) - Transform is logic\n\n**3. Load - Like final output 0 3 6 9:**\n# Load to warehouse\ndf.to_csv('warehouse/students_processed.csv')\ndf.to_sql('processed_students', connection)\n# Like for loop output - Final coins collected!\n\n**Pipeline Example - BhavPath:**\n# Extract: User login data (email, college, btech %)\n# Transform: Calculate eligibility, skill gap, XP\n# Load: Show dashboard, resume, game unlock - Full pipeline!",
        "oop_extra": "**Big Data & Tools for Data Engineering - For TCS Digital:**\n\n**Big Data:**\nWhen data is too large for normal DB - TBs, PBs\nTraditional: MySQL can handle GBs\nBig Data: Hadoop, Spark can handle TBs/PBs\n\n**Hadoop:**\nHDFS: Storage - Distributed - Data split across machines\nMapReduce: Processing - Map (filter) + Reduce (aggregate) - Old, slow\n\n**Spark - Trending 2025:**\n100x faster than Hadoop MapReduce - In-memory processing\nPySpark: Spark with Python - For Data Engineers\n# PySpark Example\nfrom pyspark.sql import SparkSession\nspark=SparkSession.builder.appName(\"BhavPath\").getOrCreate()\ndf=spark.read.csv(\"students.csv\", header=True)\ndf.groupBy(\"college\").avg(\"btech\").show() # Avg per college - Like SQL GROUP BY!\n\n**Data Warehousing:**\nSnowflake, BigQuery, Redshift - Stores processed data\nData Scientists query warehouse - SELECT AVG(btech) FROM warehouse.students\n\n**Cloud:**\nAWS S3 (Storage), Glue (ETL), Redshift (Warehouse) - Most companies use AWS\nFor interview: Say 'I know ETL pipeline like BhavPath - Extract user data, Transform eligibility, Load to dashboard - Same as Data Engineering'",
        "applications": ["🏢 Data Engineer Role: Build pipelines - Highest demand 2025 - 8-15 LPA for freshers with 81% - Your best role!", "📊 Data Warehousing: Snowflake, BigQuery - Stores data for analysis", "☁️ Cloud DE: AWS, GCP, Azure - Cloud Data Engineer - Trending", "🔄 ETL Tools: Informatica, Talend, Apache Airflow - Automate pipelines", "📈 Big Data: Hadoop, Spark for TBs data - For large companies like TCS, Infosys"],
        "interview": [
            {"q": "What is Data Engineering vs Data Science? Which role for 81% profile?", "a": "Data Engineering: Builds systems to collect, store, process data - Builds pipelines - Tools: SQL, Python, ETL, Spark, Cloud. Data Science: Analyzes data built by DE - Builds models - Tools: Python, ML, Statistics. For 81% Data Science profile, Data Engineering is best because: 1. Higher demand 2025 - Every company needs DE, 2. Less competition than DS, 3. Your BhavPath project is actually Data Engineering - Extract login data, Transform eligibility, Load to dashboard - You already did DE! So say 'I built ETL pipeline in BhavPath - Extract user data, Transform BTech %, Load to placement dashboard' - This will impress!"},
            {"q": "What is ETL? Explain with BhavPath example - Most asked!", "a": "ETL = Extract Transform Load - Core of Data Engineering. Extract: Get data from sources - DB, CSV, APIs. Transform: Clean, filter, aggregate, calculate - Remove nulls, calculate eligibility. Load: Store to warehouse for analysis. BhavPath Example: Extract: User enters email, college, BTech 81% - From login page. Transform: Check if BTech>=60 for TCS NQT eligibility, calculate skill gap (Variables 100%, Control 60%), calculate XP. Load: Show placement dashboard, resume builder, unlock Final Boss game. This is ETL pipeline! Extract from login, Transform eligibility, Load to dashboard. For interview, always give BhavPath example - Shows practical understanding!"},
            {"q": "SQL Query: Find average BTech % per college? And eligible students?", "a": "-- Average per college\nSELECT college, AVG(btech_percent) as avg_btech, COUNT(*) as total_students\nFROM students\nGROUP BY college\nORDER BY avg_btech DESC;\n\n-- Eligible for TCS NQT (60% needed) - Your use case!\nSELECT name, btech_percent, college\nFROM students\nWHERE btech_percent >= 60\nORDER BY btech_percent DESC;\n\n-- Count eligible per college\nSELECT college, COUNT(*) as eligible_count\nFROM students\nWHERE btech_percent >= 60\nGROUP BY college;\nFor interview: Write these 3 queries - Shows you know GROUP BY, WHERE, ORDER BY, COUNT, AVG - Must for DE role!"},
            {"q": "What is Big Data? Hadoop vs Spark? Why Spark trending 2025?", "a": "Big Data: Data too large for traditional DB - TBs, PBs - 3 Vs: Volume (large), Velocity (fast), Variety (different types). Traditional MySQL handles GBs, Big Data handles TBs. Hadoop: Old - HDFS for storage (distributed), MapReduce for processing - Slow - Disk based. Spark: New - Trending 2025 - 100x faster than Hadoop - In-memory processing - PySpark (Python + Spark) - For Data Engineers. Example: TCS has TBs of employee data - MySQL can't handle, need Spark. For interview: Say 'For BhavPath, if we had 1M students, MySQL would be slow, need Spark - df.groupBy(\"college\").avg(\"btech\") - Same as SQL but for Big Data'"},
            {"q": "Tell me about yourself? - Data Engineering focus - Perfect for 81%", "a": "I'm Bhav from Rise College, Ongole with 81% in Data Science. I'm passionate about Data Engineering because I love building pipelines - I built BhavPath which is actually a Data Engineering project - Extract: User login data (email, college, BTech %), Transform: Calculate TCS NQT eligibility (60% needed), skill gap, XP, Load: Show dashboard, resume, unlock Final Boss game with for loop logic 0,3,6,9. My skills: SQL (GROUP BY, JOINs, Window functions), Python (Pandas, Numpy), ETL concepts, Basics of Spark, Cloud basics. I know ETL pipeline like BhavPath - Extract, Transform, Load - Same as Data Engineering role. I'm looking for Data Engineer role where I can build pipelines for 81% profile students like me. My BTech is 81%, XP 820, completed 3/3 modules in BhavPath."}
        ]
    },
    "Software Engineering": {
        "title": "Software Engineering - Complete Tutorial",
        "desc": "Building software like BhavPath - SDLC, Agile, Design - Must for all",
        "what_is": "**What is Software Engineering?**\nSoftware Engineering is systematic, disciplined approach to build software. Not just coding - Full process: Planning, Requirement Analysis, Design, Coding, Testing, Deployment, Maintenance. Your BhavPath followed Software Engineering! SDLC Models: Waterfall (linear), Agile (iterative - Trending 2025), Scrum (sprints). For 81% profile, SE concepts must for interviews - Every company asks SDLC, Agile, Testing.",
        "syntax": "// SDLC for BhavPath - Real example - Software Engineering\n\n// 1. Requirement Analysis: What user wants?\n// - Login with email, college\n// - BTech % input\n// - Topics selector: C, C++, Python, Java, Data Engineering, Software Engineering\n// - Full tutorial with Table of Contents, Syntax, Features, Code, Interview Qs\n// - Game at end - Final Boss - Unlocks after modules\n// - Resume builder\n\n// 2. Design:\n// - UI: White cards, Blue cards, Topic cards - Like Geeks\n// - Pages: login, btech, purpose (home), topics, topic_detail, gaming, resume\n// - Session state: page, user, xp, completed, selected_topic\n// - Data: TOPICS dict with title, what_is, syntax, features, modules, interview\n\n// 3. Coding:\n// - Streamlit + Python\n// - Functions: login(), btech_page(), purpose(), main()\n// - TOPICS dict for all topics\n\n// 4. Testing:\n// - Test login with valid/invalid email\n// - Test BTech slider 0-100\n// - Test topic selection - Direct open\n// - Test game unlock - 3 modules needed\n// - Test game logic - for loop 0,3,6,9\n\n// 5. Deployment:\n// - Push to GitHub\n// - Deploy to Streamlit Cloud - bhavpath.streamlit.app\n// - Share link for demo\n\n// 6. Maintenance:\n// - Add new topics - AI/ML\n// - Fix bugs - UnboundLocalError\n// - Update content - Last Updated: 25 Aug 2025",
        "features": [
            "SDLC: Software Development Life Cycle - Step by step process to build software - Like BhavPath - Requirement to Deployment",
            "Waterfall Model: Linear - Requirement -> Design -> Coding -> Testing -> Deployment -> Maintenance - Old model - One phase after another - If requirement changes, need to go back",
            "Agile Model: Iterative - Trending 2025 - Build in sprints - 2 weeks sprint - Requirement -> Design -> Coding -> Testing -> Demo -> Next sprint - Fast, flexible - BhavPath used Agile - We built login, then BTech %, then topics, then game - Sprint by sprint!",
            "Scrum: Agile framework - Roles: Product Owner (what to build), Scrum Master (process), Developers (build) - Ceremonies: Daily standup, Sprint planning, Retrospective - For interview: Say 'We used Scrum for BhavPath'",
            "Design Patterns: Singleton, Factory, Observer - Reusable solutions - For scalable apps - Important for senior roles",
            "Testing: Unit testing (test one function), Integration testing (test multiple functions), System testing (test full app) - Must before deployment - BhavPath testing: Test login, test game logic"
        ],
        "hello": "// Hello World in Software Engineering - BhavPath SDLC\nprint(\"Hello BhavPath! Welcome to Software Engineering\")\n\n# Agile Sprint Example for BhavPath\nsprint1 = [\"Login page\", \"BTech % page\"]\nsprint2 = [\"Purpose page with progress\", \"Topics selector\"]\nsprint3 = [\"Topic detail with TOC\", \"Code examples\"]\nsprint4 = [\"Final Boss game - Locked logic\", \"Resume builder\"]\n\nprint(f\"Sprint 1: {sprint1}\")\nprint(f\"Sprint 4: {sprint4} - Game at end!\")\n# Output: Sprint 4: ['Final Boss game - Locked logic', 'Resume builder'] - Game at end!",
        "variables": "**Requirement Analysis & Design - Variables in SE:**\n\n**Requirement Analysis:**\nWhat user wants? - Functional and Non-functional\nFunctional: Login, BTech %, Topics (C, C++, Python, Java, Data Eng, SE), Full tutorial with TOC, Syntax, Features, Modules, Interview Qs, Game at end, Resume\nNon-functional: Fast, Clean UI (white/blue cards), No GFG word, American slang, Game locked until modules done\n\n**Design:**\nUI Design: White cards for info, Blue cards for important, Topic cards for selection - Like Geeks structure - TOC, Tabs (Full Tutorial, Code, Interview Qs)\nDatabase Design: TOPICS dict - title, desc, what_is, syntax, features, modules, interview - Session state for user, xp, completed\n\n**Variables in SE = Requirements, Design docs, Code, Tests**\nRequirement doc: What to build - Variables\nDesign doc: How to build - Data types\nCode: Implementation - Values\nTests: Verification - Checks",
        "control": "**SDLC Models - Control Flow in Software Engineering:**\n\n**1. Waterfall Model - Like simple for loop:**\nRequirement -> Design -> Coding -> Testing -> Deployment -> Maintenance\nLinear - One after another - Like for(i=0;i<10;i++) - Step by step\nIf requirement changes in Testing, need to go back to Requirement - Costly!\nExample: Build BhavPath fully in Waterfall - If after deployment user says 'Add Python topic', need to go back to Requirement - Costly!\n\n**2. Agile Model - Like nested loops with condition - Trending 2025:**\nIterative - Build in sprints - 2 weeks per sprint\nSprint 1: Requirement + Design + Coding + Testing for Login\nSprint 2: Requirement + Design + Coding + Testing for BTech %\nSprint 3: Requirement + Design + Coding + Testing for Topics selector\nSprint 4: Requirement + Design + Coding + Testing for Final Boss game\nAfter each sprint, demo to user - If user says 'Add Python', add in next sprint - Flexible!\nLike: for each sprint { for each task { if user feedback -> adjust } }\nBhavPath used Agile - We added topics one by one - C, C++, Python, Java, Data Eng, SE - Sprint by sprint!\n\n**3. Scrum - Agile framework:**\nRoles: Product Owner (Bhav - what to build), Scrum Master (process), Developers (build)\nCeremonies: Daily standup (what did yesterday, what today, blockers), Sprint planning (what to build next sprint), Retrospective (what went well, what to improve)\nFor interview: Say 'For BhavPath, we used Agile Scrum - 4 sprints - Daily standup via WhatsApp - Sprint planning for topics'",
        "oop_extra": "**Testing & Deployment - OOP Extra in SE:**\n\n**Testing:**\nUnit Testing: Test one function - Test login() with valid/invalid email - Isolated\nIntegration Testing: Test multiple functions - Test login -> BTech % -> Purpose flow - Combined\nSystem Testing: Test full app - Login -> BTech % -> Topics -> Topic detail -> Game -> Resume - End to end\nUser Acceptance Testing: User tests - Bhav tests BhavPath - Does game unlock after 3 modules? Does topic direct open work?\n\n**Deployment:**\nGitHub: Push code to GitHub - git push origin main\nStreamlit Cloud: Connect GitHub repo to Streamlit Cloud - Auto deploy - bhavpath.streamlit.app - Share link\nMonitoring: Check logs - Any error? - UnboundLocalError fixed!\n\n**Maintenance:**\nAdd new topics: AI/ML, DevOps - Like new modules\nFix bugs: If game logic fails for i+=3 - Fix\nUpdate content: Last Updated: 25 Aug 2025 - Keep updated\n\n**Why SE for 81% profile?**\nEvery company asks: What is SDLC? What is Agile? What is testing? - If you say 'I built BhavPath using Agile Scrum - 4 sprints - Testing for login, game logic - Deployed to Streamlit Cloud' - You will slay interview!",
        "applications": ["🏗️ Software Engineer Role: Build apps like BhavPath - Most common role - 6-12 LPA for freshers", "📱 Product Development: Build products - Like BhavPath product - From idea to deployment", "☁️ DevOps: CI/CD - Automated testing and deployment - Trending 2025", "🧪 Testing Engineer: Test apps - Manual + Automation - Important role", "📊 Project Management: Scrum Master, Product Owner - Manage sprints"],
        "interview": [
            {"q": "What is SDLC? Explain with BhavPath example - Most asked!", "a": "SDLC = Software Development Life Cycle - Step by step process to build software: 1. Requirement Analysis - What user wants? For BhavPath: Login, BTech %, Topics selector (C, C++, Python, Java, Data Eng, SE), Full tutorial with TOC, Syntax, Features, Modules, Interview Qs, Game at end locked, Resume. 2. Design - How to build? UI: White/blue cards, Topic cards, TOC, Tabs. Database: TOPICS dict, session state. 3. Coding - Build - Streamlit + Python - Functions login(), btech_page(), purpose(), main(). 4. Testing - Test login valid/invalid, BTech slider, topic direct open, game unlock after 3 modules, game logic 0,3,6,9. 5. Deployment - Push to GitHub, deploy to Streamlit Cloud - bhavpath.streamlit.app. 6. Maintenance - Add new topics, fix bugs, update content. For interview, always give BhavPath example - Shows practical SDLC!"},
            {"q": "Agile vs Waterfall? Which did you use for BhavPath? Why?", "a": "Waterfall: Linear - Requirement -> Design -> Coding -> Testing -> Deployment - One phase after another - If requirement changes in Testing, need to go back to Requirement - Costly, slow, old model. Agile: Iterative - Build in sprints - 2 weeks sprint - Requirement + Design + Coding + Testing + Demo in each sprint - Flexible, fast, trending 2025 - If requirement changes, add in next sprint - Easy! For BhavPath, we used Agile - 4 sprints: Sprint 1 Login + BTech %, Sprint 2 Purpose + Topics selector, Sprint 3 Topic detail with TOC + Code + Interview Qs, Sprint 4 Final Boss game locked logic + Resume. We added topics sprint by sprint - C, then C++, then Python, Java, Data Eng, SE - If user said 'Add AI/ML topic', we can add in next sprint - Flexible! So Agile is better for BhavPath because requirements changed - Initially only C++, then user asked for C, Python, Java, Data Eng, SE - Agile allowed easy addition."},
            {"q": "What is testing? Types? Why important before deployment?", "a": "Testing is verifying app works as expected - Find bugs before user finds. Types: Unit Testing - Test one function - Test login() with valid email (bhav@gmail.com) should pass, invalid (bhav) should fail - Isolated. Integration Testing - Test multiple functions together - Test login -> BTech % -> Purpose flow - Does BTech % page show after login? Does XP increase after module completion? System Testing - Test full app end to end - Login -> BTech % -> Topics -> Open Python -> Complete 3 modules -> Game unlock -> Play game 0,3,6,9 -> Resume - Full flow. User Acceptance Testing - User (Bhav) tests - Does topic direct open work? Does game unlock after 3 modules? For BhavPath, we tested: login valid/invalid, BTech slider 0-100, topic cards direct open, game logic for i+=3 gives 0,3,6,9, resume builder. Why important? If we deploy without testing, user may see UnboundLocalError (like screenshot) - Bad experience - Testing catches bugs before deployment - Saves reputation!"},
            {"q": "What is Scrum? Roles, Ceremonies? Did you follow Scrum for BhavPath?", "a": "Scrum is Agile framework - Most used for Agile. Roles: 1. Product Owner - What to build? - For BhavPath, Bhav is Product Owner - Decides topics: C, C++, Python, Java, Data Eng, SE, Game at end. 2. Scrum Master - How to build? Process - Ensures sprints happen, removes blockers. 3. Developers - Build - Code login(), btech_page(), etc. Ceremonies: 1. Sprint Planning - What to build next sprint? - Sprint 1 planning: Login + BTech %. 2. Daily Standup - What did yesterday, what today, blockers? - For BhavPath, WhatsApp daily update - 'Yesterday login done, today BTech % page, no blockers'. 3. Sprint Review - Demo after sprint - After Sprint 1, demo login + BTech % to user - User feedback 'Add topics selector'. 4. Retrospective - What went well, what to improve? - After Sprint 2, retro: 'Topic selector works well, but need to add direct open - Improve next sprint'. For BhavPath, we followed Scrum informally - 4 sprints, daily WhatsApp standup, sprint planning for topics, review after each sprint - For interview, say 'We followed Scrum - 4 sprints - Daily standup - Sprint planning for topics' - Shows you know Agile practically!"},
            {"q": "Tell me about yourself? - Software Engineering focus", "a": "I'm Bhav from Rise College, Ongole with 81% in BTech. I love Software Engineering because I love building products end to end - I built BhavPath using full SDLC - Requirement Analysis: Login, BTech %, Topics (C, C++, Python, Java, Data Eng, SE), Full tutorial with TOC, Syntax, Features, Modules, Interview Qs, Game at end locked, Resume builder. Design: UI with white/blue cards, Topic cards, TOC, Tabs, Session state for user, xp, completed, selected_topic, TOPICS dict. Coding: Streamlit + Python - Functions login(), btech_page(), purpose(), main() - TOPICS dict with full info. Testing: Tested login valid/invalid, BTech slider, topic direct open, game unlock after 3 modules, game logic 0,3,6,9 - Fixed UnboundLocalError. Deployment: Pushed to GitHub, deployed to Streamlit Cloud - bhavpath.streamlit.app. Maintenance: Added new topics as user requested - C, Python, Java, Data Eng, SE - Initially only C++. We used Agile Scrum - 4 sprints - Daily standup via WhatsApp - Sprint planning for topics. My skills: SDLC, Agile, Scrum, Streamlit, Python, Testing, Deployment. Looking for Software Engineer role where I can build products like BhavPath end to end. My BTech is 81%, XP 820, completed 3/3 modules."}
        ]
    }
}

def login():
    st.title("🚀 BhavPath - Login")
    # No extra card - Clean login as you asked
    email = st.text_input("Email", placeholder="bhav@gmail.com")
    clg = st.text_input("College Name", placeholder="Rise College, Ongole")
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
    st.markdown(f'<div class="blue-card"><b>Bet! Locked in: {btech}% 🔥</b><br>We\'re about to cook a custom prep just for you - No cap, this gonna be fire</div>', unsafe_allow_html=True)
    if st.button(f"Let's roll with {btech}% →"):
        st.session_state.user["btech"] = btech
        st.session_state.page = "purpose"
        st.balloons()
        st.rerun()

def purpose():
    st.header(f"Yo {st.session_state.user['name']}! 👋")
    st.markdown(f'<div class="white-card">🏫 {st.session_state.user["clg"]} | Flex: <b>{st.session_state.user["btech"]}%</b> | XP: <b>{st.session_state.xp}</b></div>', unsafe_allow_html=True)
    done = sum(st.session_state.completed.values())
    total = len(st.session_state.completed)
    progress = int((done/total)*100) if total else 0
    st.subheader(f"Your Grind: {progress}% Complete - {done}/{total} modules")
    st.progress(progress/100)
    if progress < 100:
        st.warning(f"🔒 Final Boss Locked - Finish {total-done} more modules to unlock - Keep grinding fr!")
    else:
        st.success("🔥 FINAL BOSS UNLOCKED! You ate! Let's end with a banger game!")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="white-card">🎯 <b>For Placement</b><br>Eligibility + Skill Gap</div>', unsafe_allow_html=True)
        if st.button("Placement →", key="pl"): st.session_state.purpose="placement"; st.session_state.page="main"; st.rerun()
        st.markdown('<div class="white-card">📚 <b>Study Hub - All Topics</b><br>6 Topics - Select directly - Full info</div>', unsafe_allow_html=True)
        if st.button("Browse Topics →", key="mt"): st.session_state.purpose="topics"; st.session_state.page="main"; st.rerun()
    with c2:
        st.markdown('<div class="white-card">📄 <b>Resume Builder</b><br>Auto drip resume</div>', unsafe_allow_html=True)
        if st.button("Resume →", key="rs"): st.session_state.purpose="resume"; st.session_state.page="main"; st.rerun()
        if progress == 100:
            st.markdown('<div class="blue-card"><b>🎮 FINAL BOSS - Game Zone</b><br>Modules done! Time to end with a banger 🔥</div>', unsafe_allow_html=True)
            if st.button("FINAL BOSS - Game Zone 🔥 →", key="gm"):
                st.session_state.purpose="gaming"; st.session_state.page="main"; st.rerun()
        else:
            st.markdown(f'<div class="locked-card"><b>🔒 🎮 FINAL BOSS - Locked</b><br>Complete {total-done} modules<br>{progress}% done</div>', unsafe_allow_html=True)

def main():
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["clg"]} | {st.session_state.user["btech"]}% | {st.session_state.xp} XP | Topic: {st.session_state.selected_topic}</b></div><br>', unsafe_allow_html=True)
    if st.button("← Back to Home"):
        if st.session_state.purpose=="topic_detail":
            st.session_state.purpose="topics"
        else:
            st.session_state.page="purpose"
        st.rerun()

    if st.session_state.purpose=="placement":
        b=st.session_state.user['btech']
        st.subheader("Placement Dashboard - No cap check")
        if b>=60: st.success(f"✅ You good for TCS NQT - Need 60%, You got {b}% - W rizz!")
        else: st.error(f"❌ Need 60%, You got {b}% - Gotta lock in more fr")
        st.markdown(f'<div class="white-card"><b>Skill Gap - Real talk for {b}% profile:</b><br>Intro: {"✅ Done" if st.session_state.completed["Intro"] else "❌ Pending"}<br>Syntax: {"✅ Done" if st.session_state.completed["Syntax"] else "❌ Pending"}<br>Core: {"✅ Done" if st.session_state.completed["Core"] else "❌ Pending - Important for TCS Digital"}</div>', unsafe_allow_html=True)

    elif st.session_state.purpose=="topics":
        st.title("📚 Select Your Topic - Direct Open")
        st.caption("Click any card - Direct full tutorial opens - Like complete structure - TOC, Syntax, Features, Modules, Code, Interview Qs")
        st.markdown(f'<div class="white-card"><b>👇 Pick a topic - Direct full page opens - For {st.session_state.user["btech"]}% Rise profile - 6 Topics: C, C++, Python, Java, Data Engineering, Software Engineering</b></div>', unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, tname in enumerate(TOPICS.keys()):
            col = cols[i%2]
            with col:
                st.markdown(f'<div class="topic-card"><b>📖 {tname}</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
                if st.button(f"Open {tname} →", key=f"open_{tname}"):
                    st.session_state.selected_topic = tname
                    st.session_state.purpose = "topic_detail"
                    st.session_state.completed = {"Intro": False, "Syntax": False, "Core": False}
                    st.rerun()
        st.divider()
        st.info("💡 Tip: Each topic has full structure - What is?, Syntax, Features, Applications, Hello World, Variables, Control (Final Boss logic 0,3,6,9), OOP Extra, Interview Qs - Like full tutorial!")

    elif st.session_state.purpose=="topic_detail":
        t = TOPICS[st.session_state.selected_topic]
        st.title(t["title"])
        st.caption(f"For {st.session_state.user['btech']}% profile | Last Updated: 25 Aug 2025 | {st.session_state.selected_topic} Complete Course")
        
        st.markdown(f'<div class="white-card"><b>📑 Table of Contents:</b><br>1. What is {st.session_state.selected_topic}?<br>2. Basic Syntax<br>3. Features<br>4. Applications<br>5. Hello World Program<br>6. Variables & Data Types<br>7. Control Statements - Final Boss Logic<br>8. Extra (OOP / ETL / SDLC)<br>9. Interview Qs - For {st.session_state.user["btech"]}% profile</div>', unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["📖 Full Tutorial", "💻 Code Examples", "💼 Interview Qs"])

        with tab1:
            st.header(f"What is {st.session_state.selected_topic}?")
            st.write(t["what_is"])
            if not st.session_state.completed["Intro"]:
                if st.button("Mark Intro Done +50 XP 🔥", key="intro"): st.session_state.completed["Intro"]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
            else: st.success("✅ Intro Done - You ate!")

            st.divider()
            st.header("Basic Syntax")
            st.code(t["syntax"], language="python" if st.session_state.selected_topic in ["Python", "Data Engineering"] else "cpp")
            if not st.session_state.completed["Syntax"]:
                if st.button("Mark Syntax Done +50 XP 🔥", key="syn"): st.session_state.completed["Syntax"]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
            else: st.success("✅ Syntax Done!")

            st.divider()
            st.header(f"Features of {st.session_state.selected_topic}")
            for f in t["features"]:
                st.markdown(f'<div class="green-card">✅ {f}</div>', unsafe_allow_html=True)

            st.divider()
            st.header(f"Applications of {st.session_state.selected_topic}")
            for app in t["applications"]:
                st.markdown(f'<div class="blue-card" style="margin-bottom:8px;">{app}</div>', unsafe_allow_html=True)

            st.divider()
            st.header("Hello World Program")
            st.code(t["hello"], language="python" if st.session_state.selected_topic in ["Python", "Data Engineering"] else "cpp")
            if st.button("Run Hello World - Simulate"): st.success(f"Output: Hello BhavPath! Welcome to {st.session_state.selected_topic} World - Running for {st.session_state.user['btech']}%")

            st.divider()
            st.header(f"Variables & Data Types - Full Info")
            st.write(t["variables"])
            st.code(t["hello"].split("\n")[-4:], language="python" if st.session_state.selected_topic in ["Python", "Data Engineering"] else "cpp")

            st.divider()
            st.header(f"Control Statements - Final Boss Logic - 0,3,6,9")
            st.write(t["control"])
            st.code(f"for(int i=0; i<10; i+=3) print(i) // 0 3 6 9 - Final Boss!" if st.session_state.selected_topic!="Python" else "for i in range(0,10,3): print(i) # 0 3 6 9 - Final Boss!")

            st.divider()
            st.header(f"Extra - {st.session_state.selected_topic} Deep Dive")
            st.write(t["oop_extra"])
            st.code(t["syntax"][:200])

            if not st.session_state.completed["Core"]:
                if st.button(f"Mark {st.session_state.selected_topic} Core Done +100 XP 🔥 - Unlock Game", key="core"):
                    st.session_state.completed["Core"]=True
                    st.session_state.xp+=100
                    st.balloons()
                    st.success(f"🔥 {st.session_state.selected_topic} Core Done! All modules done! Final Boss unlocked! Go back to Home!")
                    st.rerun()
            else:
                st.success(f"✅ {st.session_state.selected_topic} Core Done - You already ate this!")

            st.divider()
            done = sum(st.session_state.completed.values())
            st.write(f"**Progress: {done}/3 Modules Done - For {st.session_state.selected_topic}**")
            st.progress(done/3)
            if done==3:
                st.success("🔥 All 3 modules done! Go back to Home - Game Zone unlocked at bottom - Final Boss ready! Time to end with a banger fr!")
                if st.button("Go to Final Boss Game → 🔥"):
                    st.session_state.purpose="gaming"
                    st.rerun()
            else:
                st.warning(f"Complete {3-done} more modules to unlock Final Boss at end! Keep grinding!")

        with tab2:
            st.header(f"Code Examples - {st.session_state.selected_topic} - Try Yourself")
            st.subheader("1. Hello World + Sum")
            st.code(t["hello"])
            if st.button("Run Code 1 - Simulate", key="run1"): st.success(f"Output: Hello BhavPath! Welcome to {st.session_state.selected_topic} World\nSum is: 30")
            st.subheader("2. Eligibility Checker - Your Use Case - TCS NQT 60%")
            st.code(t["syntax"])
            if st.button("Run Code 2 - Eligibility", key="run2"): st.success(f"Output: Eligible for TCS NQT - You got {st.session_state.user['btech']}%")
            st.subheader("3. Final Boss Logic - Loop Legends - 0,3,6,9")
            st.code("for i in range(0,10,3): print(i) # 0 3 6 9 - Coins at 0,3,6,9 - Optimal path! - Final Boss!")
            if st.button("Run Code 3 - Final Boss Logic", key="run3"): st.success("Output: 0 3 6 9 - Perfect path! You collected 4/4 coins - Optimal!")

        with tab3:
            st.header(f"Interview Questions - For {st.session_state.user['btech']}% - {st.session_state.selected_topic} - TCS NQT Style")
            st.markdown(f'<div class="white-card"><b>These are top asked in TCS NQT, Infosys, Wipro for {st.session_state.selected_topic} - With perfect answers for {st.session_state.user["btech"]}% Rise profile - No cap, these will make you slay interview fr!</b></div>', unsafe_allow_html=True)
            for item in t["interview"]:
                with st.expander(item["q"]):
                    st.write(item["a"])
                    if st.button(f"Mark Prepared +10 XP", key=item["q"][:25]): st.session_state.xp+=10; st.success("+10 XP - You locked in!")

    elif st.session_state.purpose=="gaming":
        st.title("🎮 FINAL BOSS - Game Zone - You made it! 🔥")
        st.markdown(f'<div class="blue-card"><b>Sheesh! You completed {st.session_state.selected_topic} modules - Now end with a banger!</b><br>You locked in fr - This is your final test - For {st.session_state.selected_topic} logic - No cap</div>', unsafe_allow_html=True)
        st.balloons()
        st.divider()
        st.markdown(f'<div class="white-card"><b>FINAL BOSS: Loop Legends - From {st.session_state.selected_topic} Control Statements</b><br>You learned for loop - Now prove it! Coins at 0,3,6,9 - Logic from {st.session_state.selected_topic}</div>', unsafe_allow_html=True)
        step=st.slider(f"for(i=0; i<10; i+=?) - Final answer? - {st.session_state.selected_topic} logic", 1,5,3, key="final")
        if st.button("PLAY FINAL BOSS - RUN IT! 🔥"):
            coins=[0,3,6,9]; path=list(range(0,10,step)); coll=len([x for x in path if x in coins])
            st.write(f"Path {path} | Collected {coll}/4 - {st.session_state.selected_topic} logic")
            if coll==4:
                st.balloons()
                st.success(f"YOU SLAYED THE FINAL BOSS! 🔥 +200 XP - Total {st.session_state.xp+200} - You ate and left no crumbs! {st.session_state.selected_topic} = Game mastered!")
                st.session_state.xp+=200
                st.snow()
            else:
                st.error(f"Almost! You got {coll}/4 - Need i+=3 - From {st.session_state.selected_topic} Control - Run it back, you got this fr")
        st.divider()
        st.markdown('<div class="white-card"><b>Bonus Round: Variable Vault - From Variables Module</b></div>', unsafe_allow_html=True)
        box=st.selectbox("Box? - Data Types", ["Gold Count (100)","Name (Bhav)","Is Win? True"], key="bonus")
        dtype=st.radio("Type?", ["int","string","bool"], horizontal=True, key="bonus2")
        if st.button("PLAY Bonus Round - Variables"):
            corr={"Gold Count (100)":"int","Name (Bhav)":"string","Is Win? True":"bool"}
            if dtype==corr[box]:
                st.balloons(); st.success(f"Bonus slayed! +50 XP - Variables mastered! Total {st.session_state.xp+50}"); st.session_state.xp+=50
            else:
                st.error(f"Nah fam need {corr[box]} - Check Variables module again")

    elif st.session_state.purpose=="resume":
        st.title("📄 Auto Resume - Drip Check")
        done = sum(st.session_state.completed.values())
        st.markdown(f'<div class="white-card"><b>Name:</b> {st.session_state.user["name"]}<br><b>College:</b> {st.session_state.user["clg"]}<br><b>Flex:</b> {st.session_state.user["btech"]}%<br><b>Current Topic:</b> {st.session_state.selected_topic} - {TOPICS[st.session_state.selected_topic]["title"]}<br><b>Skills:</b> {st.session_state.selected_topic} (Modules {done}/3 done - Intro, Syntax, Core), {", ".join([k for k in TOPICS.keys() if k!=st.session_state.selected_topic][:3])}, Gaming Logic, Problem Solving<br><b>Project:</b> BhavPath - Multi-Topic Learning Platform - 6 Topics (C, C++, Python, Java, Data Engineering, Software Engineering) - Full Tutorial with TOC, Syntax, Features, Applications, Hello World, Variables, Control (Final Boss logic 0,3,6,9), Extra, Interview Qs - Complete modules to unlock Final Boss - Innovative fr<br><b>XP:</b> {st.session_state.xp} - Grind is real - {done*33}% Complete<br><b>Eligibility:</b> TCS NQT Eligible (60% needed, you {st.session_state.user["btech"]}%) - For {st.session_state.selected_topic} roles</div>', unsafe_allow_html=True)
        if st.button("Download Resume - It's giving professional"): st.balloons(); st.success("Resume Downloaded! LinkedIn ready - You ate!")

# --- ROUTER - FIXED NO ERROR ---
if st.session_state.page=="login":
    login()
elif st.session_state.page=="btech":
    btech_page()
elif st.session_state.page=="purpose":
    purpose()
else:
    main()
