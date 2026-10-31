import streamlit as st
import pandas as pd

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state: 
    st.session_state.page="welcome"
    st.session_state.college="QIS College"
    st.session_state.selected_skill="C"
    st.session_state.topic="Intro"

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

# ===== 48 TOPICS DETAILED DATA - ALL SKILLS IN ENGLISH =====
DETAILED_DATA = {
"C": {
"Intro": {"def":"C is procedural, middle-level language created by Dennis Ritchie (1972). Gives direct hardware access via pointers. Foundation of OS, compilers.","real":"Talking directly to computer. Python/Java built on C. Like learning ABC before sentences.","why":"First round in TCS/Wipro asks C. Mastering C makes C++ and DSA easy.","diagram":"High( Python ) -> Middle( C ) -> Low( Assembly )\nC = Power + Speed","code":"#include <stdio.h>\nint main(){ printf(\"Hello BhavPath\"); return 0;}","interview":"Q: Why C is middle-level?"},
"Data Types": {"def":"Defines type of data: int=4 bytes (-2B to 2B), char=1 byte, float=4 bytes, double=8 bytes, void=no value.","real":"Boxes: int box for 10, float for 8.5, char for 'A'. Different size saves memory.","why":"Memory optimization questions asked in placement. sizeof() important.","diagram":"[int 4B][char 1B][float 4B]\nAddress: 1000 -> 1004 -> 1005","code":"int a=10; char b='A'; float c=8.5;\nprintf(\"%d %c %.1f\",a,b,c);","interview":"Q: float vs double? Q: sizeof(int)?"},
"Loops": {"def":"Repeats code: for (known count), while (unknown count), do-while (at least once).","real":"Print 1 to 100 without writing 100 lines. One loop does it. Like daily gym routine.","why":"90% DSA uses loops. Pattern questions compulsory.","diagram":"Init-> Condition? Yes-> Body-> Increment-> Repeat\n              No-> Exit","code":"for(int i=1;i<=5;i++) printf(\"%d \",i); // 1 2 3 4 5","interview":"Q: for vs while? Infinite loop?"},
"Functions": {"def":"Block doing one task. Reusability. Two types: Library (printf) and User-defined. Call stack used.","real":"Mixer jars: Juice jar, chutney jar. Each jar = function. Use when needed.","why":"Modular code asked in TCS. Code reuse concept.","diagram":"main() -> add() -> return -> main()\nStack: [main][add] -> pop","code":"int add(int a,int b){return a+b;}\nint ans=add(5,3); // 8","interview":"Q: Call by value vs reference?"},
"Pointers": {"def":"Variable storing address of another variable. * = value at address, & = address of. Enables dynamic memory.","real":"Friend's home address in phone. With address you go direct. *p = go inside home.","why":"FAANG 100% asks pointers. Linked List, Trees all pointers.","diagram":"a=10 @1000\np=&a -> p=1000\n*p=50 -> a becomes 50","code":"int a=10; int *p=&a; *p=50; printf(\"%d\",a); // 50","interview":"Q: Dangling pointer? NULL vs void?"},
"Arrays": {"def":"Collection of same type in continuous memory. Index 0 based. Fixed size. O(1) access.","real":"60 students roll numbers in one list. Boxes in a row.","why":"DSA base. Searching/Sorting on arrays.","diagram":"Index:0 1 2 3\nVal:[90][85][92][78]\nAddr:1000 1004 1008","code":"int m[3]={90,85,92}; for(i=0;i<3;i++) printf(\"%d\",m[i]);","interview":"Q: Array vs Linked List?"},
"Structures": {"def":"Collection of different types under one name. struct keyword. Groups related data.","real":"Student details: name, age, cgpa - all different types but one student - use structure.","why":"Real projects use structures to group data. Asked in Infosys.","diagram":"struct Student { char name[20]; int age; float cgpa; }\nOne unit in memory","code":"struct Student s1={\"Bhav\",21,8.5};\nprintf(\"%s\",s1.name);","interview":"Q: Structure vs Union?"},
"File Handling": {"def":"Store data permanently using files. fopen, fclose, fprintf, fscanf. Modes: r,w,a.","real":"Like notebook: Write data, close, open later. Data stays after program ends.","why":"Projects need file handling. Log files, data storage.","diagram":"Program -> RAM (temporary) -> File -> Hard Disk (permanent)","code":"FILE *f=fopen(\"data.txt\",\"w\");\nfprintf(f,\"Hi\"); fclose(f);","interview":"Q: File modes r,w,a?"}
},
"C++": {
"Basics": {"def":"C++ is C with OOP. Created by Bjarne Stroustrup. Adds classes, objects over C.","real":"C + extra features. If C is bicycle, C++ is motorbike with engine (OOP).","why":"Game development, high-speed apps use C++. Placement asks C vs C++.","diagram":"C: Procedural -> C++: Procedural + OOP\nC code also works in C++","code":"#include <iostream>\nint main(){ std::cout<<\"Hello\"; }","interview":"Q: C vs C++?"},
"OOP": {"def":"Object Oriented: Class=blueprint, Object=house. 4 pillars: Encapsulation, Inheritance, Polymorphism, Abstraction.","real":"Car blueprint (Class) -> Many cars (Objects). Same blueprint, different colors.","why":"Most asked topic in interviews. Every company asks OOP.","diagram":"Class[Car] -> Object1(Red) Object2(Blue)\nAttributes: color, speed\nMethods: start(), stop()","code":"class Car{ public: void start(){}};\nCar c1; c1.start();","interview":"Q: 4 pillars of OOP?"},
"STL": {"def":"Standard Template Library: Ready-made data structures - vector, map, set, stack. Saves time.","real":"Ready-made furniture vs making from wood. STL = ready-made code, just use.","why":"Competitive coding and interviews use STL heavily. Saves 50% time.","diagram":"STL: Containers(vector) + Algorithms(sort) + Iterators\nvector<int> v = dynamic array","code":"vector<int> v={1,2,3}; v.push_back(4);\nsort(v.begin(), v.end());","interview":"Q: vector vs array?"},
"Pointers": {"def":"Same as C but with smart pointers: unique_ptr, shared_ptr for automatic memory management.","real":"C pointers + safety lock. Smart pointers auto-delete, no memory leak.","why":"Memory leak questions in senior interviews.","diagram":"Raw pointer: Manual delete\nSmart pointer: Auto delete when out of scope","code":"int *p=new int(10); // raw\nunique_ptr<int> sp=make_unique<int>(10); // smart","interview":"Q: Smart pointers?"},
"Inheritance": {"def":"Child class gets properties of parent. Types: single, multiple, multilevel, hierarchical.","real":"Son gets property from father. Father=Animal, Son=Dog gets Animal properties + own bark.","why":"Code reuse. Most asked in OOP round.","diagram":"Parent: Animal {eat()}\nChild: Dog : Animal {bark()}\nDog can eat() + bark()","code":"class Animal{ public: void eat(){}};\nclass Dog: public Animal{ void bark(){}};","interview":"Q: Types of inheritance?"},
"Polymorphism": {"def":"One name many forms. Compile-time (overloading) and Run-time (overriding via virtual).","real":"One button, many functions: Power button does different in TV, AC. Same name, different action.","why":"Run-time polymorphism interview favorite. Virtual function Qs.","diagram":"Function add(int,int) and add(float,float) -> Overloading\nVirtual void draw() -> Overriding","code":"class A{ virtual void show(){}};\nclass B: public A{ void show() override{}};","interview":"Q: Overloading vs overriding?"},
"Templates": {"def":"Generic code: Write once work for any data type. Function template and Class template.","real":"One mixer grinder for all: Same machine for juice, chutney. Template = one code for int, float.","why":"Generic programming asked in Amazon interviews.","diagram":"template <typename T> T add(T a,T b){return a+b;}\nadd<int>(5,3) -> 8, add<float>(2.5,3.1) -> 5.6","code":"template <typename T>\nT add(T a,T b){ return a+b; }","interview":"Q: What is template?"},
"Projects": {"def":"Mini projects: Bank system, Student management using OOP + File handling.","real":"Combine all C++ concepts to build real app. Like building house using all materials.","why":"Resume needs projects. Interviewer asks project explanation.","diagram":"Project: Class Student + File + STL vector + Menu loop","code":"// Bank: class Account { deposit(), withdraw() }\n// Save to file","interview":"Q: Explain your C++ project?"}
},
"Java": {
"Basics": {"def":"Java: Write Once Run Anywhere. Created by James Gosling. JVM executes bytecode. Platform independent.","real":"One charger works for all phones. Java code works on Windows, Mac, Linux via JVM.","why":"Enterprise companies (TCS, Infosys, Wipro) use Java heavily. #1 for jobs.","diagram":"Java Code -> Compiler -> Bytecode (.class) -> JVM (any OS) -> Output","code":"public class Main{\n public static void main(String[] args){\n  System.out.println(\"Hello\");\n }\n}","interview":"Q: Why platform independent? Q: JDK vs JRE vs JVM?"},
"OOP": {"def":"Java is 100% OOP (except primitives). Encapsulation (private), Inheritance (extends), Polymorphism.","real":"Lego blocks: Each block = object with data + methods. Combine to build big app.","why":"Java interview = OOP interview. Must know.","diagram":"Class Student { private data + public methods }\nEncapsulation = hide data","code":"class Student{ private int age; public int getAge(){return age;}}","interview":"Q: Encapsulation in Java?"},
"Collections": {"def":"Framework for storing group of objects: List (ArrayList), Set (HashSet), Map (HashMap), Queue.","real":"Different bags: List = ordered bag allows duplicates, Set = unique items only, Map = key-value like dictionary.","why":"Most asked in Java interviews. 50% questions from Collections.","diagram":"List: [A,B,A] allowed\nSet: [A,B] unique\nMap: {1->Bhav, 2->Sai}","code":"ArrayList<String> list=new ArrayList<>();\nlist.add(\"Bhav\");\nHashMap<Integer,String> map=new HashMap<>();","interview":"Q: ArrayList vs LinkedList? HashMap vs HashTable?"},
"Exception": {"def":"Exception = runtime error. try-catch handles. Checked (must handle) vs Unchecked.","real":"Safety net: Code may fall (error), try-catch catches it, program doesn't crash.","why":"Robust application needs exception handling. Interview asks custom exceptions.","diagram":"try { risky code } catch(Exception e){ handle } finally { always runs }","code":"try{ int a=10/0; } catch(ArithmeticException e){ System.out.println(\"Error\"); }","interview":"Q: try-catch-finally? throw vs throws?"},
"Multithreading": {"def":"Running multiple tasks parallel. Thread class, Runnable interface. Synchronization needed.","real":"One person doing many tasks: Listening music + coding + chatting = threads. Fast but need sync.","why":"High-performance apps use multithreading. Amazon asks.","diagram":"Main Thread -> Child Thread1, Thread2 parallel\nSynchronized block = only one thread at a time","code":"class MyThread extends Thread{ public void run(){ System.out.println(\"Thread\"); }}","interview":"Q: Thread vs Runnable? What is synchronization?"},
"JDBC": {"def":"Java Database Connectivity: Connects Java to database (MySQL, Oracle) using drivers.","real":"Bridge between Java app and database. Like USB cable between phone and laptop.","why":"Any Java project needs database. Must know.","diagram":"Java App -> JDBC Driver -> Database (MySQL)\nConnection -> Statement -> ResultSet","code":"Connection con=DriverManager.getConnection(url);\nStatement st=con.createStatement();","interview":"Q: Steps in JDBC?"},
"Spring": {"def":"Spring framework: Makes Java easy. Dependency Injection, Spring Boot for microservices.","real":"Ready-made house instead of building brick by brick. Spring Boot = ready Java backend.","why":"Current industry standard. All new projects use Spring Boot. High paying jobs.","diagram":"Spring Boot: Auto-configuration + Embedded Tomcat\n@RestController -> API in 5 lines","code":"@RestController\npublic class Hello{ @GetMapping(\"/\") public String hi(){return \"Hi\";}}","interview":"Q: What is Spring Boot? Dependency Injection?"},
"Projects": {"def":"Projects: E-commerce, Student Management, REST API using Spring Boot + MySQL.","real":"Build real app using all Java concepts. Resume highlight.","why":"Without project, no interview call.","diagram":"Frontend -> REST API (Spring Boot) -> MySQL DB","code":"// E-commerce: Product, Cart, Order classes + DB","interview":"Q: Explain your Java project architecture?"}
},
"Python": {
"Basics": {"def":"High-level, interpreted, dynamically typed. Created by Guido van Rossum 1991. Easy syntax.","real":"English-like code. C needs 5 lines, Python 1 line. Beginner friendly.","why":"#1 for placements now. Data Science, ML, Web, Automation all Python.","diagram":"C: 5 steps compile, Python: 1 step direct run","code":"name=\"Bhav\"\nprint(f\"Hi {name}\")\nskills=[\"Python\",\"SQL\"]","interview":"Q: Dynamic typing? interpreted?"},
"Loops": {"def":"for iterates over sequence, while until condition false. Break, continue, else in loops.","real":"Instagram stories one by one = for loop. Until battery low = while loop.","why":"Automation needs loops. 1000 records process.","diagram":"fruits=[apple,mango]\nfor f in fruits: print f\nIteration: apple->print, mango->print","code":"for i in range(1,6): print(i)\nfor fruit in [\"apple\",\"mango\"]: print(fruit)","interview":"Q: for vs while? enumerate?"},
"Functions": {"def":"Block doing task. def keyword. Arguments: positional, keyword, *args, **kwargs. Return values.","real":"Microwave: Put food, press button, get hot food. Function = machine doing task.","why":"Reusability. Clean code.","diagram":"def add(a,b): return a+b\nadd(5,3) -> 8\nFunction stack","code":"def add(a,b): return a+b\nprint(add(5,3))\n# Lambda: add=lambda a,b:a+b","interview":"Q: *args vs **kwargs? Lambda?"},
"OOP": {"def":"Class=blueprint, Object=house. __init__ constructor. Inheritance, Polymorphism in Python.","real":"Car blueprint -> many cars. Same as Java but simpler syntax.","why":"Python OOP asked in interviews. Projects use OOP.","diagram":"Class Student: __init__(self,name) -> self.name=name\nObject s1=Student('Bhav')","code":"class Student:\n def __init__(self,name):\n  self.name=name\ns1=Student(\"Bhav\")","interview":"Q: self? __init__? Inheritance?"},
"Libraries": {"def":"Ready-made code: NumPy (numbers), Pandas (data), Matplotlib (graphs), Requests (API).","real":"Toolbox: Need hammer? Take from toolbox. Need data analysis? import pandas.","why":"Data Science jobs need libraries. Must know pandas, numpy.","diagram":"import pandas as pd -> pd.read_csv()\nimport numpy -> array operations","code":"import pandas as pd\ndf=pd.read_csv(\"data.csv\")\nprint(df.head())","interview":"Q: NumPy vs List? Pandas?"},
"File Handling": {"def":"Open, read, write, close files. Modes r,w,a. with open auto closes. JSON, CSV handling.","real":"Notebook: Write, save, open later. Data stays after program.","why":"Data processing projects need file handling.","diagram":"with open(\"file.txt\",\"r\") as f: data=f.read()","code":"with open(\"data.txt\",\"w\") as f:\n f.write(\"Hello\")\n# Read CSV\nimport csv","interview":"Q: with open? r vs w?"},
"Django": {"def":"Django = Python web framework. MVT pattern. Fast web development. ORM for database.","real":"Ready-made website factory. Login, database, admin all ready. Just customize.","why":"Python web jobs use Django. High demand.","diagram":"Browser -> URL -> View -> Model (DB) -> Template (HTML)\nDjango flow","code":"# Django view\ndef home(request):\n return HttpResponse(\"Hello BhavPath\")","interview":"Q: Django vs Flask? MVT?"},
"Projects": {"def":"Projects: Portfolio, E-commerce, Data analysis, Chatbot using Python libraries.","real":"Combine all Python to build real app. Resume needs 2 projects minimum.","why":"Without projects no job. Interview asks project deep dive.","diagram":"Python + Django + MySQL + HTML = Full stack project","code":"# Project: To-Do App using Django + SQLite","interview":"Q: Explain your Python project?"}
},
"SQL": {
"SELECT": {"def":"Fetches data. SELECT * = all columns, WHERE filters rows, ORDER BY sorts, DISTINCT removes duplicates.","real":"Godown: Take needed items. SELECT = what I need, WHERE = condition.","why":"Every company has DB. No SQL = no job. 40% interview SQL.","diagram":"Table Students\nSELECT name WHERE cgpa>8 -> [Bhav]","code":"SELECT name, cgpa FROM Students\nWHERE cgpa>8 ORDER BY cgpa DESC;","interview":"Q: WHERE vs HAVING?"},
"JOINS": {"def":"Combines two tables on related column. INNER (matching), LEFT (all left + matching right), RIGHT, FULL.","real":"Two registers: Student details + Marks - join using ID to get full info.","why":"Real projects have 5-6 tables. JOIN compulsory.","diagram":"A(id,name) + B(id,marks)\nINNER: Only matching\nLEFT: All A + matching B","code":"SELECT s.name, m.marks FROM Students s\nJOIN Marks m ON s.id=m.id;","interview":"Q: INNER vs LEFT?"},
"GROUP BY": {"def":"Groups rows with same values. Used with aggregate: COUNT, SUM, AVG, MAX, MIN. HAVING filters groups.","real":"Group students by section: Count how many in each section. Like grouping fruits by type.","why":"Reports need GROUP BY. Asked in interviews.","diagram":"Students: Sec A: 3, Sec B: 2\nGROUP BY section -> COUNT\nA:3, B:2","code":"SELECT section, COUNT(*) FROM Students\nGROUP BY section HAVING COUNT(*)>2;","interview":"Q: GROUP BY vs ORDER BY?"},
"Subqueries": {"def":"Query inside query. Inner query runs first, result used by outer. Nested SELECT.","real":"Box inside box: First open inner box, take item, use in outer box.","why":"Complex reports need subqueries. Advanced SQL asked.","diagram":"SELECT name FROM Students WHERE cgpa = (SELECT MAX(cgpa) FROM Students)","code":"SELECT * FROM Students WHERE cgpa = (SELECT MAX(cgpa) FROM Students);","interview":"Q: Subquery vs JOIN?"},
"Indexing": {"def":"Index speeds up search like book index. CREATE INDEX. Types: clustered, non-clustered. Tradeoff: faster search, slower insert.","real":"Book index: Find page quickly without reading full book. Index = shortcut.","why":"Performance tuning. Large databases need indexing.","diagram":"Without Index: Full table scan O(n)\nWith Index: B-Tree O(log n) -> fast","code":"CREATE INDEX idx_cgpa ON Students(cgpa);\n-- Search fast now","interview":"Q: What is indexing? Types?"},
"Normalization": {"def":"Organizes data to reduce redundancy. Forms: 1NF, 2NF, 3NF, BCNF. Removes duplicate data.","real":"Keep clothes organized: One place for shirts, not scattered. Normalization = organizing DB neatly.","why":"Database design interviews ask normalization. Important for projects.","diagram":"Unnormalized: Student + Course in same table (duplicate)\nNormalized: Separate Student and Course tables + Mapping","code":"-- 1NF: Atomic values\n-- 2NF: No partial dependency\n-- 3NF: No transitive dependency","interview":"Q: 1NF, 2NF, 3NF?"},
"Procedures": {"def":"Stored Procedure = saved SQL code. Runs faster. Parameters IN, OUT. Functions vs Procedures.","real":"Saved recipe: Write once, use many times. Just call procedure name, no need to rewrite full SQL.","why":"Backend projects use procedures. Asked in advanced SQL rounds.","diagram":"CREATE PROCEDURE GetStudents() -> Saved in DB\nCALL GetStudents() -> Executes","code":"CREATE PROCEDURE GetTop()\nBEGIN SELECT * FROM Students WHERE cgpa>8; END;\nCALL GetTop();","interview":"Q: Procedure vs Function?"},
"Projects": {"def":"Projects: Student DB, E-commerce DB, Inventory system with tables, joins, procedures.","real":"Build full database design with 5-6 tables, relationships, queries.","why":"Resume needs DB project. Shows SQL skills.","diagram":"E-commerce DB: Users, Products, Orders, Payments tables + FK relations","code":"-- E-commerce schema with FK","interview":"Q: Design DB for E-commerce?"}
},
"DSA": {
"Arrays": {"def":"Continuous memory, O(1) access, O(n) search/insert middle. Foundation.","real":"Theatre seats row wise. Seat 5 direct O(1). Search one by one O(n).","why":"DSA starts here. Two pointers, sliding window on arrays.","diagram":"[0][1][2][3] continuous\nAccess O(1), Search O(n), Insert middle O(n)","code":"def two_sum(arr,target):\n seen={}\n for i,n in enumerate(arr):\n  if target-n in seen: return [seen[target-n],i]\n  seen[n]=i","interview":"Q: Max subarray sum? Rotate array?"},
"Linked List": {"def":"Nodes via pointers. Not continuous, dynamic size. Types: singly, doubly, circular.","real":"Train bogies: Each linked to next. Easy add middle, slow search.","why":"FAANG favorite. Reverse, cycle detection famous.","diagram":"Head->[10|next]->[20|next]->[30|NULL]\nInsert head O(1), Access O(n)","code":"class Node:\n def __init__(self,d):\n  self.data=d; self.next=None","interview":"Q: Detect loop? Reverse?"},
"Stack & Queue": {"def":"Stack=LIFO (Last In First Out) like plates stack. Queue=FIFO like queue in shop. Implement via array or linked list.","real":"Stack: Plates - last kept, first taken. Queue: Shop line - first come first served.","why":"Undo operation (stack), Printer queue (queue). Asked in interviews.","diagram":"Stack: Push 1,2,3 -> Pop 3,2,1\nQueue: Enqueue 1,2,3 -> Dequeue 1,2,3","code":"stack=[]; stack.append(1); stack.pop()\nfrom collections import deque\nq=deque(); q.append(1); q.popleft()","interview":"Q: Stack vs Queue? Implement using array?"},
"Trees": {"def":"Hierarchical data: Root, parent, child, leaf. Binary Tree (max 2 children), BST (left<root<right). Traversals: inorder, preorder, postorder.","real":"Family tree: Grandfather=root, children, grandchildren. Company hierarchy.","why":"File system, org chart use trees. Google asks trees a lot.","diagram":"    10\n   /  \\\n  5   15\n /    / \\\n2    12 20\nInorder: 2,5,10,12,15,20","code":"class TreeNode:\n def __init__(self,val):\n  self.val=val; self.left=None; self.right=None","interview":"Q: BST vs Binary Tree? Traversals?"},
"Graphs": {"def":"Nodes (vertices) + Edges. Types: directed, undirected, weighted. Representations: adjacency matrix/list. BFS, DFS traversals.","real":"Google Maps: Cities=nodes, Roads=edges, Distance=weight. Facebook friends = graph.","why":"Maps, social networks are graphs. Amazon, Google ask graphs heavily.","diagram":"A--B, B--C, A--C (triangle graph)\nBFS: Level wise, DFS: Depth wise\nAdj List: A->[B,C], B->[A,C]","code":"graph={ 'A':['B','C'], 'B':['A','C'] }\n# BFS using queue\n# DFS using stack/recursion","interview":"Q: BFS vs DFS? When to use?"},
"Sorting": {"def":"Arrange data in order. Types: Bubble O(n^2), Selection O(n^2), Insertion O(n^2), Merge O(n log n), Quick O(n log n avg).","real":"Arrange books by height. Different methods: Bubble = compare neighbours, Merge = divide and combine.","why":"Sorting base for searching. Interview asks which sorting when.","diagram":"Bubble: Compare adjacent, swap if wrong -> O(n^2)\nMerge: Divide -> Sort -> Merge -> O(n log n)","code":"# Python sort\narr=[3,1,2]; arr.sort() # O(n log n)\n# Merge sort implementation","interview":"Q: Best sorting? Quick vs Merge?"},
"DP": {"def":"Dynamic Programming: Break problem into subproblems, store results to avoid recomputation. Two ways: memoization (top-down), tabulation (bottom-up).","real":"Remembering answers: 2+2=4 remembered, next time no calculation. Save time.","why":"Hardest but most asked in FAANG. DP mastery = high package.","diagram":"Fibonacci: fib(5)=fib(4)+fib(3)\nWithout DP: Recompute same\nWith DP: Store fib(3) once -> fast\nfib: 0,1,1,2,3,5","code":"# Fibonacci DP\ndef fib(n, memo={}):\n if n in memo: return memo[n]\n if n<=1: return n\n memo[n]=fib(n-1,memo)+fib(n-2,memo)\n return memo[n]","interview":"Q: DP vs recursion? Memoization vs tabulation?"},
"Greedy": {"def":"Greedy makes best choice at each step, hopes global optimal. Works for some problems like coin change, activity selection. Not always optimal.","real":"Everyday: Choose best option now, don't think future too much. Like picking largest coin first for change.","why":"Some interview problems solved by greedy only. Easy to implement.","diagram":"Coin change: Rs 18, Coins [10,5,1]\nGreedy: Take 10, then 5, then 1,1,1 = 5 coins (optimal here)\nBut not always optimal","code":"# Activity selection greedy\n# Sort by finish time, pick earliest finishing compatible","interview":"Q: Greedy vs DP? When greedy works?"}
}
}

def get_data(skill, topic):
    if skill in DETAILED_DATA and topic in DETAILED_DATA[skill]:
        return DETAILED_DATA[skill][topic]
    # Fallback for C++ uses C data for basics
    if skill=="C++" and topic in DETAILED_DATA["C"]:
        return DETAILED_DATA["C"][topic]
    return {"def": f"{topic} in {skill} - Important topic. Covers core concepts needed for placement.","real": f"Real life example for {topic} in {skill}.","why": f"Placement interview asks {topic} in {skill} very frequently.","diagram": f"{skill} -> {topic} -> Practice","code": f"# {skill} {topic} example","interview": f"Q: Explain {topic} in {skill}?"}

# --- PAGES ---
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
            if st.button("📈 Placement Prediction", use_container_width=True): st.session_state.page="tech_welcome"; st.rerun()
            st.write("")
            if st.button("🧠 Test Zone", use_container_width=True): st.session_state.page="coming_soon"; st.rerun()
        with c2:
            if st.button("💻 Technical Skills", use_container_width=True): st.session_state.page="tech_welcome"; st.rerun()
            st.write("")
            if st.button("💼 Interview + Code", use_container_width=True): st.session_state.page="coming_soon"; st.rerun()

elif st.session_state.page == "tech_welcome":
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - All Topics Detailed</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Explore Skills →", use_container_width=True, type="primary"): st.session_state.page="tech_skills"; st.rerun()
        if st.button("← Back"): st.session_state.page="purpose"; st.rerun()

elif st.session_state.page == "tech_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Skill - All 48 Topics Ready</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        c1,c2,c3,c4=st.columns(4)
        if c1.button("C (8 Topics)", use_container_width=True): st.session_state.selected_skill="C"; st.session_state.topic="Intro"; st.session_state.page="skill_detail"; st.rerun()
        if c2.button("C++ (8)", use_container_width=True): st.session_state.selected_skill="C++"; st.session_state.topic="Basics"; st.session_state.page="skill_detail"; st.rerun()
        if c3.button("Java (8)", use_container_width=True): st.session_state.selected_skill="Java"; st.session_state.topic="Basics"; st.session_state.page="skill_detail"; st.rerun()
        if c4.button("Python (8)", use_container_width=True): st.session_state.selected_skill="Python"; st.session_state.topic="Basics"; st.session_state.page="skill_detail"; st.rerun()
        st.write("")
        c5,c6=st.columns(2)
        if c5.button("SQL (8 Topics)", use_container_width=True): st.session_state.selected_skill="SQL"; st.session_state.topic="SELECT"; st.session_state.page="skill_detail"; st.rerun()
        if c6.button("DSA (8 Topics)", use_container_width=True): st.session_state.selected_skill="DSA"; st.session_state.topic="Arrays"; st.session_state.page="skill_detail"; st.rerun()
        if st.button("← Back"): st.session_state.page="tech_welcome"; st.rerun()

elif st.session_state.page == "skill_detail":
    skill=st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;font-size:36px;'>{skill} - Full Detailed Learning</h1></div>", unsafe_allow_html=True)
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
            data=get_data(skill, st.session_state.topic)
            st.markdown(f"""
            <div class='glass' style='min-height:700px;'>
                <h2 style='color:#fef08a;margin-top:0;'>📘 {st.session_state.topic} in {skill}</h2>
                <div style='background:rgba(255,255,255,0.05);padding:14px;border-radius:12px;margin:10px 0;'>
                <p style='color:#7dd3fc;margin:0;font-weight:700;'>📖 DEFINITION (Detailed):</p>
                <p style='color:white;margin:5px 0 0 0;line-height:1.6;'>{data['def']}</p></div>
                <div style='background:rgba(254,240,138,0.1);padding:14px;border-radius:12px;margin:10px 0;border-left:4px solid #fef08a;'>
                <p style='color:#fef08a;margin:0;font-weight:700;'>💡 EASY EXPLANATION (Real-Life Example):</p>
                <p style='color:white;margin:5px 0 0 0;line-height:1.6;'>{data['real']}</p></div>
                <div style='background:rgba(255,0,106,0.1);padding:14px;border-radius:12px;margin:10px 0;border-left:4px solid #ff006a;'>
                <p style='color:#f472b6;margin:0;font-weight:700;'>🎯 WHY IMPORTANT FOR PLACEMENT?</p>
                <p style='color:white;margin:5px 0 0 0;line-height:1.6;'>{data['why']}</p></div>
                <p style='color:white;margin:15px 0 5px 0;font-weight:700;'>🖼️ DIAGRAM / MEMORY LAYOUT:</p>
                <div style='background:#0a0a0a;padding:15px;border-radius:10px;color:#00ff88;font-family:monospace;border:1px dashed #333;white-space:pre-wrap;text-align:left;'>{data['diagram']}</div>
                <p style='color:white;margin:15px 0 5px 0;font-weight:700;'>💻 CODE EXAMPLE:</p>
                <div style='background:#111;padding:15px;border-radius:10px;'><pre style='color:#fef08a;margin:0;white-space:pre-wrap;font-size:13px;'>{data['code']}</pre></div>
                <div style='background:rgba(13,74,255,0.15);padding:14px;border-radius:12px;margin:15px 0 0 0;border-left:4px solid #0d4aff;'>
                <p style='color:#8b9cff;margin:0;font-weight:700;'>❓ INTERVIEW QUESTION:</p>
                <p style='color:white;margin:5px 0 0 0;'>{data['interview']}</p></div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon 🚀</h1></div>", unsafe_allow_html=True)
    if st.button("← Back"): st.session_state.page="purpose"; st.rerun()









