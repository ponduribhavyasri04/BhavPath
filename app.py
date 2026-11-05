import streamlit as st
import pandas as pd
import random
import datetime

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = "Rise Krishna Sai Gandhi Group Of Institutions"
    st.session_state.selected_skill = "C"
    st.session_state.topic = "Loops"
    st.session_state.pdata = None
    st.session_state.test_skill = "Python"
    st.session_state.test_questions = []
    st.session_state.test_answers = {}
    st.session_state.test_submitted = False
    st.session_state.test_week = 0

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
.detail-box{position:relative;z-index:10;max-height:85vh;overflow-y:auto;padding:25px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.qbox{background:rgba(13,74,255,0.14);border-left:4px solid #0d4aff;padding:14px 16px;margin:18px 0 6px 0;border-radius:8px}
.abox{background:rgba(0,255,136,0.09);border-left:4px solid #00ff88;padding:14px 16px;margin:6px 0 22px 0;border-radius:8px}
.cat{background:linear-gradient(90deg,#0d4aff,#ff006a);padding:8px 16px;border-radius:20px;color:white;font-weight:bold;margin:22px 0 12px 0;display:inline-block}
.diag{background:linear-gradient(135deg,#0d1a3a,#1a0a2a);border:1px solid #0d4aff;border-radius:10px;padding:10px;margin:12px 0;color:white;text-align:center;font-size:13px}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_current_week():
    today = datetime.date.today()
    return today.isocalendar()[1]

def get_test_questions_pool():
    pool = {
        "C": [
            {"q": "What is size of int in C (64-bit)?", "options": ["2 bytes", "4 bytes", "8 bytes", "16 bytes"], "ans": 1, "exp": "int is 4 bytes in 64-bit compiler. Pointer is 8 bytes."},
            {"q": "What is pointer? What does int *p store?", "options": ["Value of variable", "Address of variable", "Garbage value", "NULL always"], "ans": 1, "exp": "Pointer stores address of variable."},
            {"q": "Which is correct for malloc?", "options": ["malloc(4) returns zero init", "malloc needs 2 args", "malloc returns void* need cast", "malloc 1 arg size uninitialized"], "ans": 3, "exp": "malloc takes 1 arg size, returns uninitialized memory."},
            {"q": "What is dangling pointer?", "options": ["Points to NULL", "Points to freed memory", "Points to garbage random", "Points to stack"], "ans": 1, "exp": "Dangling points to freed memory. After free(p), p becomes dangling."},
            {"q": "Array vs Linked List - Which has O(1) random access?", "options": ["Linked List", "Array", "Both", "None"], "ans": 1, "exp": "Array has O(1) random access via index."},
            {"q": "What is output? int a=5/2; printf(\"%d\",a);", "options": ["2.5", "2", "3", "Error"], "ans": 1, "exp": "5/2 integer division gives 2."},
            {"q": "Which storage class keeps value between function calls?", "options": ["auto", "register", "static", "extern"], "ans": 2, "exp": "static keeps value between calls."},
            {"q": "What is segmentation fault?", "options": ["Memory leak", "Accessing not owned memory", "Stack overflow", "Infinite loop"], "ans": 1, "exp": "Segfault is accessing memory you don't own."},
            {"q": "How to reverse string without library?", "options": ["Use strrev()", "Two pointers i=0 j=len-1 swap", "Use recursion only", "Not possible"], "ans": 1, "exp": "Two pointers i=0 j=len-1 swap till i<j."},
            {"q": "What is structure padding? struct {char a; int b;} size?", "options": ["5 bytes", "6 bytes", "8 bytes", "4 bytes"], "ans": 2, "exp": "char 1 + padding 3 + int 4 = 8 due to alignment."},
            {"q": "Binary search time complexity?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "ans": 1, "exp": "Binary search O(log n) needs sorted array."},
            {"q": "Quick Sort worst case?", "options": ["O(n log n)", "O(n^2)", "O(n)", "O(log n)"], "ans": 1, "exp": "Quick Sort worst O(n^2) when pivot is smallest/largest always."},
            {"q": "What does free(p) do?", "options": ["Deletes pointer", "Releases memory pointed by p", "Sets p to NULL", "Nothing"], "ans": 1, "exp": "free releases memory. Pointer still exists dangling."},
            {"q": "Which is correct for string? char str[] = \"Hello\"; What is last char?", "options": ["o", "NULL", "\\0", "o with \\0 after"], "ans": 3, "exp": "String ends with \\0. Hello has H e l l o \\0."},
            {"q": "Which loop ensures at least one execution?", "options": ["for", "while", "do-while", "None"], "ans": 2, "exp": "do-while checks condition after body."},
        ],
        "Python": [
            {"q": "List vs Tuple - Which is mutable?", "options": ["List mutable Tuple immutable", "Both mutable", "Both immutable", "List immutable"], "ans": 0, "exp": "List mutable can change. Tuple immutable."},
            {"q": "What is output? my_list=[1,2,2,3] len(set(my_list))?", "options": ["4", "3", "2", "1"], "ans": 1, "exp": "set removes duplicates. [1,2,2,3] -> {1,2,3} len 3."},
            {"q": "What are args and kwargs?", "options": ["args tuple kwargs dict", "args dict kwargs tuple", "Both list", "Both dict"], "ans": 0, "exp": "args is tuple for positional unlimited, kwargs dict for keyword."},
            {"q": "What is decorator in Python?", "options": ["Wraps function adds behavior", "Deletes function", "Creates class", "Loop"], "ans": 0, "exp": "Decorator wraps function adds behavior without modifying."},
            {"q": "What is GIL in Python?", "options": ["Global Interpreter Lock - one thread executes bytecode", "Garbage collector", "Global variable", "Loop"], "ans": 0, "exp": "GIL only one thread executes Python bytecode at a time."},
            {"q": "Which is faster? List comprehension or for loop with append?", "options": ["For loop", "List comprehension faster", "Same speed", "While loop"], "ans": 1, "exp": "List comprehension faster because loop runs in C."},
            {"q": "What is output? [x*x for x in range(5) if x%2==0]?", "options": ["[0,1,4,9,16]", "[0,4,16]", "[0,2,4]", "[1,9]"], "ans": 1, "exp": "x%2==0 gives 0,2,4 squares 0,4,16."},
            {"q": "Shallow copy vs deep copy?", "options": ["Shallow copies reference only, deep copies full", "Both same", "Shallow deep", "Deep reference"], "ans": 0, "exp": "Shallow copies top level only inner mutable shared."},
            {"q": "What does with open() do?", "options": ["Auto closes file", "Deletes file", "Creates file only", "Nothing"], "ans": 0, "exp": "with open auto closes file even after exception."},
            {"q": "Which is correct for Two Sum O(n)?", "options": ["Brute force O(n^2)", "HashMap O(n) seen dict", "Sort O(n log n)", "Binary search"], "ans": 1, "exp": "Two Sum HashMap O(n) time O(n) space."},
            {"q": "What is output? s=\"BhavPath\" s[::-1]?", "options": ["BhavPath", "htaPvahB", "PathBhav", "Error"], "ans": 1, "exp": "s[::-1] reverses string."},
            {"q": "First non-repeating char in BhavPath?", "options": ["B", "h", "a", "P"], "ans": 0, "exp": "B appears once, first non-repeating."},
            {"q": "What is lambda?", "options": ["Anonymous function lambda x: x+10", "Named function", "Class", "Loop"], "ans": 0, "exp": "Lambda is anonymous function."},
            {"q": "Django vs Flask?", "options": ["Flask micro Django full batteries", "Both same", "Django micro", "Flask full"], "ans": 0, "exp": "Flask micro simple small API, Django full framework."},
            {"q": "What is output? bool([]) bool([0])?", "options": ["True True", "False True", "True False", "False False"], "ans": 1, "exp": "Empty list bool False, non-empty list True."},
        ],
        "Java": [
            {"q": "Why Java platform independent?", "options": ["Compiles to bytecode runs on JVM any OS", "Compiles to machine code", "Needs recompile per OS", "Not independent"], "ans": 0, "exp": "Java bytecode runs on JVM any OS WORA."},
            {"q": "String vs StringBuilder? Which faster for loop 10000 concat?", "options": ["String faster", "StringBuilder faster", "Same", "StringBuffer fastest"], "ans": 1, "exp": "String immutable creates 10000 objects waste. StringBuilder mutable."},
            {"q": "ArrayList vs LinkedList - O(1) random access?", "options": ["ArrayList O(1) get", "LinkedList O(1) get", "Both O(1)", "None"], "ans": 0, "exp": "ArrayList dynamic array O(1) get."},
            {"q": "How HashMap works internally?", "options": ["hashCode to bucket index", "Linear search", "Binary search", "Sort"], "ans": 0, "exp": "HashMap hashCode to bucket index hash & n-1."},
            {"q": "What is == vs equals in Java?", "options": ["== reference equals content", "Both same", "== content equals reference", "None"], "ans": 0, "exp": "== checks reference same object, equals checks content same."},
            {"q": "What is overloading vs overriding?", "options": ["Overloading compile time same name diff params, overriding runtime child redefines parent", "Both same", "Overloading runtime", "Overriding compile"], "ans": 0, "exp": "Overloading same class diff params compile time. Overriding child redefines parent runtime."},
            {"q": "Interface vs Abstract class?", "options": ["Abstract can have concrete + abstract methods single inheritance, Interface only abstract multiple implements", "Both same", "Interface single", "Abstract multiple"], "ans": 0, "exp": "Abstract class abstract+concrete single extends. Interface only abstract multiple implements."},
            {"q": "What is exception handling? finally always executes?", "options": ["Yes finally always executes even after return", "No never", "Only if exception", "Only if no exception"], "ans": 0, "exp": "finally always executes even after return."},
            {"q": "What is multithreading? How to create thread?", "options": ["extends Thread or implements Runnable", "Only extends Thread", "Only Runnable", "Not possible"], "ans": 0, "exp": "Create by extends Thread or implements Runnable second better."},
            {"q": "What is singleton pattern?", "options": ["Only one object exists like DB connection", "Many objects", "No objects", "Abstract"], "ans": 0, "exp": "Singleton only one object exists like DB connection config."},
        ],
        "SQL": [
            {"q": "WHERE vs HAVING difference?", "options": ["WHERE filters rows before GROUP BY, HAVING filters groups after", "Both same", "WHERE after HAVING before", "No difference"], "ans": 0, "exp": "WHERE filters rows before GROUP BY cannot use aggregate, HAVING filters groups after can use COUNT."},
            {"q": "Which JOIN returns only matching rows both tables?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "ans": 0, "exp": "INNER only matching both."},
            {"q": "What is index? Why use?", "options": ["Speeds search O(n) to O(log n) B-Tree", "Slows search", "No use", "Deletes data"], "ans": 0, "exp": "Index speeds search O(n) to O(log n) like book index B-Tree."},
            {"q": "What is normalization? 1NF?", "options": ["Atomic values no array in cell", "Non-atomic", "Duplicate", "None"], "ans": 0, "exp": "1NF atomic no array in cell."},
            {"q": "Subquery vs JOIN which faster generally?", "options": ["JOIN faster optimizer uses index", "Subquery faster", "Same", "Subquery always"], "ans": 0, "exp": "JOIN generally faster optimizer uses index."},
            {"q": "LEFT JOIN to find not placed students query?", "options": ["SELECT s.name FROM students s LEFT JOIN placements p ON s.id=p.student_id WHERE p.student_id IS NULL", "INNER JOIN", "RIGHT JOIN", "CROSS JOIN"], "ans": 0, "exp": "Not placed LEFT JOIN WHERE p.student_id IS NULL."},
            {"q": "UNION vs UNION ALL?", "options": ["UNION removes duplicate UNION ALL keeps duplicate faster", "Both same", "UNION ALL removes", "UNION keeps"], "ans": 0, "exp": "UNION combines removes duplicate, UNION ALL keeps duplicate faster."},
            {"q": "What is NULL? NULL=NULL?", "options": ["Unknown NULL=NULL false use IS NULL", "True", "False always", "Error"], "ans": 0, "exp": "NULL unknown NULL=NULL false. Use IS NULL."},
            {"q": "What is window function? PARTITION BY?", "options": ["ROW_NUMBER OVER PARTITION BY college ORDER BY avg DESC groups", "No grouping", "Only ORDER BY", "No window"], "ans": 0, "exp": "Window functions ROW_NUMBER OVER PARTITION BY college."},
            {"q": "How to find duplicate emails?", "options": ["SELECT email COUNT GROUP BY email HAVING COUNT>1", "SELECT DISTINCT", "SELECT WHERE", "SELECT ORDER BY"], "ans": 0, "exp": "Duplicate SELECT email COUNT GROUP BY email HAVING COUNT>1."},
        ],
        "DSA": [
            {"q": "Two Sum O(n) solution uses?", "options": ["HashMap seen dict", "Brute O(n^2)", "Sort", "Binary search"], "ans": 0, "exp": "Two Sum HashMap O(n) time O(n) space."},
            {"q": "Reverse Linked List iterative time?", "options": ["O(n) time O(1) space", "O(n^2)", "O(log n)", "O(1)"], "ans": 0, "exp": "Reverse iterative O(n) time O(1) space."},
            {"q": "Detect loop in Linked List uses?", "options": ["Floyd tortoise hare slow 1 fast 2", "Linear search", "Binary search", "HashMap only"], "ans": 0, "exp": "Floyd tortoise hare slow 1 fast 2 if meet loop exists."},
            {"q": "Stack vs Queue?", "options": ["Stack LIFO push pop Queue FIFO enqueue dequeue", "Both LIFO", "Both FIFO", "Stack FIFO"], "ans": 0, "exp": "Stack LIFO Last In First Out. Queue FIFO First In First Out."},
            {"q": "Tree inorder traversal order?", "options": ["Left Root Right - BST sorted", "Root Left Right", "Left Right Root", "Right Left Root"], "ans": 0, "exp": "Inorder Left Root Right BST sorted order."},
            {"q": "BFS vs DFS? BFS uses?", "options": ["Queue level by level shortest path", "Stack", "Recursion only", "No queue"], "ans": 0, "exp": "BFS uses queue level by level shortest path."},
            {"q": "Quick Sort vs Merge Sort? Quick Sort worst?", "options": ["Quick worst O(n^2) avg O(n log n) in-place, Merge always O(n log n) stable O(n) extra", "Both same", "Quick always O(n log n)", "Merge O(n^2)"], "ans": 0, "exp": "Quick Sort avg O(n log n) worst O(n^2) in-place fast. Merge always O(n log n) stable."},
            {"q": "Binary search needs?", "options": ["Sorted array O(log n)", "Unsorted", "Random", "Linked List"], "ans": 0, "exp": "Binary search needs sorted array O(log n)."},
            {"q": "What is Kadane's algorithm for?", "options": ["Maximum subarray sum O(n)", "Minimum subarray", "Sort", "Search"], "ans": 0, "exp": "Kadane max subarray currentSum=max(num, currentSum+num)."},
            {"q": "What is valid parentheses check uses?", "options": ["Stack push opening if closing check top matching pop", "Queue", "Array", "No stack"], "ans": 0, "exp": "Valid parentheses stack push opening if closing check top."},
        ]
    }
    return pool

def get_weekly_random_questions(skill, num_q=10):
    pool = get_test_questions_pool()
    all_q = pool.get(skill, pool["Python"])
    week = get_current_week()
    random.seed(week + hash(skill) % 1000)
    selected = random.sample(all_q, min(num_q, len(all_q)))
    for q in selected:
        opts = q["options"]
        correct_opt = opts[q["ans"]]
        random.shuffle(opts)
        new_ans = opts.index(correct_opt)
        q["options"] = opts
        q["ans"] = new_ans
    random.seed()
    return selected

def get_detailed_content(skill, topic):
    articles = {
        # ===== C - 8 =====
        ("C", "Intro"): ("C is mother language, Dennis Ritchie 1972. Procedural, fast, direct memory control. C nunchi C++, Java, Python vachayi.", "int main(){ printf(\"Hello\"); return 0; } // Hello", "Compiler -> Machine Code. Fast."),
        ("C", "Data Types"): ("int - 4 bytes, char - 1 byte, float - 4 bytes, double - 8 bytes. Type batti size, range maruthundi.", "int age=21; char g='A'; float m=85.5;", "int range -2147483648 to 2147483647."),
        ("C", "Loops"): ("Loop ante same code repeat. for - count telisinappudu, while - condition, do-while - atleast 1 time.", "for(i=1;i<=5;i++) printf(\"%d \",i); // 1 2 3 4 5", "i=1->print 1 ... i=6 False Exit. O(n)"),
        ("C", "Functions"): ("Function ante oka pani chese block. Code reuse. Call by Value - copy, Call by Reference - address.", "int add(int a,int b){ return a+b; } // 5", "Call -> Stack -> Return -> Clear."),
        ("C", "Pointers"): ("Pointer ante address store chese variable. int *p=&a. *p=value, p=address. malloc/free ki must.", "int a=10; int *p=&a; printf(\"%d\",*p); // 10", "a=10 at 1000, p=1000 at 2000."),
        ("C", "Arrays"): ("Array same type continuous memory. Index 0 nunchi. Address = Base + index*size.", "int arr[]={10,20,30}; printf(\"%d\",arr[1]); // 20", "Base 1000, arr[1]=1004. Access O(1)."),
        ("C", "Structures"): ("Structure different types ni okkate group lo. struct Student {int id; char name[20];}. Padding valla size peruguthundi.", "struct Student s1={1,\"Bhav\"};", "char 1 + padding 3 + int 4 = 8 bytes."),
        ("C", "File Handling"): ("File lo read/write. fopen, fclose, fprintf, fscanf. Modes r,w,a,r+,w+.", "FILE *f=fopen(\"a.txt\",\"w\"); fprintf(f,\"Hi\"); fclose(f);", "Open->Write->Close. Close lekapothe data loss."),
        # ===== C++ - 8 =====
        ("C++", "Basics"): ("C++ ante C + OOP. Bjarne Stroustrup 1985. Cin cout, namespace std, fast + OOP. Game, OS, DSA ki best.", "#include <iostream>\nusing namespace std;\nint main(){ cout<<\"Hi\"; }", "C code kuda C++ lo run avthundi."),
        ("C++", "OOP"): ("C++ OOP: Class, Object, Encapsulation, Inheritance, Polymorphism, Abstraction. C++ lo OOP + Pointer kalipi powerful.", "class Dog{ public: void bark(){ cout<<\"Bark\"; } };", "C++ lo private, public, protected access."),
        ("C++", "STL"): ("STL ante Standard Template Library. Ready-made containers. vector, map, set, stack, queue, sort(). Interview lo STL must.", "vector<int> v={1,2,3}; v.push_back(4); sort(v.begin(), v.end());", "vector dynamic array, map key-value O(log n)."),
        ("C++", "Pointers"): ("C++ Pointers C laage kani new/delete kuda untayi. int *p = new int(10); delete p; Smart pointer kuda undi.", "int *p = new int(10); cout<<*p; // 10 \ndelete p;", "malloc/free C style, new/delete C++ style."),
        ("C++", "Inheritance"): ("Inheritance ante parent properties child ki. public, private, protected inheritance. Code reuse.", "class Animal{ void eat(){} }; class Dog : public Animal{ void bark(){} };", "Single, Multiple, Multilevel, Hierarchical."),
        ("C++", "Polymorphism"): ("Polymorphism ante okkate name, different forms. Compile time - Overloading, Runtime - Overriding + virtual.", "void add(int a,int b){} void add(float a,float b){} // Overloading", "virtual function pettali ante runtime polymorphism."),
        ("C++", "Templates"): ("Template ante generic code. Okkate function int, float, string anni types ki pani chesthundi.", "template<typename T> T add(T a, T b){ return a+b; }", "Function template + Class template."),
        ("C++", "Projects"): ("C++ Projects: Bank Management, Library Management, Student Record, Tic-Tac-Toe, Snake Game.", "Project: Bank - class Account { deposit(), withdraw() }", "File handling + OOP + STL kalipi project chey."),
        # ===== JAVA - 8 =====
        ("Java", "Basics"): ("Java WORA - Write Once Run Anywhere. Code -> Bytecode -> JVM. public static void main() nunchi start.", "class Main{ public static void main(String[] a){ System.out.println(\"Hi\"); } }", "JDK-develop, JRE-run, JVM-execute."),
        ("Java", "OOP"): ("Java pure OOP. Class, Object, Inheritance extends, Polymorphism overloading/overriding, Encapsulation private.", "class Dog extends Animal{ void bark(){} }", "Overloading compile time, Overriding runtime."),
        ("Java", "Collections"): ("ArrayList dynamic O(1) get, HashMap key-value O(1), HashSet unique. List vs Set vs Map.", "ArrayList<String> l=new ArrayList<>(); l.add(\"Bhav\");", "HashMap hashCode -> bucket index."),
        ("Java", "Exception"): ("Exception ante runtime error. try-catch-finally. Checked - compile time, Unchecked - runtime. finally always run avthundi.", "try{ int x=10/0; } catch(Exception e){ System.out.println(e); } finally{ System.out.println(\"Done\"); }", "throw vs throws difference adugutharu."),
        ("Java", "Multithreading"): ("Multithreading ante okesari anni panulu. Thread create - extends Thread or implements Runnable. Runnable better.", "class MyThread extends Thread{ public void run(){ System.out.println(\"Run\"); } }", "sleep(), join(), synchronized() important."),
        ("Java", "JDBC"): ("JDBC ante Java tho Database connect cheyadam. Connection, Statement, ResultSet. MySQL tho connect.", "Connection con = DriverManager.getConnection(\"jdbc:mysql://localhost:3306/db\",\"root\",\"pass\");", "Steps: Load driver -> Connect -> Query -> Close."),
        ("Java", "Spring"): ("Spring ante Java popular framework. Dependency Injection, Spring Boot lo setup easy. Microservices ki Spring Boot.", "@SpringBootApplication\npublic class App{ public static void main(String[] a){ SpringApplication.run(App.class,a); } }", "Spring Boot vs Spring - Boot lo config thakkuva."),
        ("Java", "Projects"): ("Java Projects: ATM System, Online Exam, Hospital Management, E-Commerce, Chat App.", "Project: ATM - class ATM { withdraw(), deposit(), checkBalance() }", "OOP + Collections + JDBC kalipi project."),
        # ===== PYTHON - 8 =====
        ("Python", "Basics"): ("Python easy, readable, high-level. Guido 1991. Indentation tho block decide. No semicolon.", "print(\"Hello\") # No brackets", "Code -> Bytecode -> PVM."),
        ("Python", "Loops"): ("Python for loop direct values meedha. range(), list, string. While condition false ayye varaku.", "for i in range(1,6): print(i) # 1 2 3 4 5", "List comprehension [x*x for x in range(5)] faster."),
        ("Python", "Functions"): ("def tho function. args-tuple, kwargs-dict, lambda-one line, return-value.", "def add(a,b): return a+b\nprint(add(2,3)) # 5", "Mutable default argument vaddu."),
        ("Python", "OOP"): ("OOP Class+Object. 4 Pillars. __init__ constructor. self ante current object.", "class Dog:\n def __init__(self,n): self.name=n", "Inheritance, Polymorphism Python lo easy."),
        ("Python", "Libraries"): ("Pandas-data, Numpy-numbers, Matplotlib-graphs. pip install tho install.", "import pandas as pd\ndf=pd.DataFrame({'a':[1,2]})", "DataFrame ante Excel table."),
        ("Python", "File Handling"): ("with open() auto close. Modes r,w,a. Large file line by line.", "with open(\"a.txt\",\"r\") as f:\n print(f.read())", "with use chesthe close marchipovachu."),
        ("Python", "Django"): ("Django full web framework. MVT - Model View Template. Admin, Auth, ORM anni untayi.", "python manage.py runserver # Server start", "Flask micro, Django full."),
        ("Python", "Projects"): ("Python Projects: To-Do App, Weather App, Expense Tracker, Chatbot, Face Detection.", "Project: To-Do - list add/remove with file save", "Django + Pandas + Tkinter kalipi."),
        # ===== SQL - 8 =====
        ("SQL", "SELECT"): ("SELECT ante data chudatam. WHERE row filter, ORDER BY sort, LIMIT top N.", "SELECT name, avg FROM students WHERE avg>70;", "SELECT * ante anni columns."),
        ("SQL", "JOINS"): ("JOIN 2 tables kalapadam. INNER-matching only, LEFT-left anni, RIGHT-opposite, FULL-anni.", "SELECT s.name FROM students s LEFT JOIN placements p ON s.id=p.student_id WHERE p.student_id IS NULL; // Not placed", "students 100, placements 70 -> INNER 70, LEFT 100."),
        ("SQL", "GROUP BY"): ("GROUP BY group chesi aggregate. COUNT, SUM, AVG, MAX. HAVING group filter.", "SELECT college, COUNT(*) FROM students GROUP BY college HAVING COUNT(*)>10;", "WHERE before GROUP BY, HAVING after."),
        ("SQL", "Subqueries"): ("Subquery ante query lopala query. INNER query result OUTER query ki use. IN, EXISTS tho.", "SELECT name FROM students WHERE avg > (SELECT AVG(avg) FROM students);", "Subquery kante JOIN generally faster."),
        ("SQL", "Indexing"): ("Index ante book index lantidi. Search O(n) to O(log n) avthundi. B-Tree use chesthundi.", "CREATE INDEX idx_avg ON students(avg);", "Index ekkuva pettali ante INSERT slow avthundi."),
        ("SQL", "Normalization"): ("Normalization ante redundancy thagginchadam. 1NF-atomic, 2NF-no partial, 3NF-no transitive.", "1NF: One cell lo okkate value. 'Python,Java' vaddu, vere rows chey.", "BCNF, 4NF kuda untayi."),
        ("SQL", "Procedures"): ("Procedure ante save chesina SQL code. Malli malli call cheyochu. Function ki return undi, Procedure ki ledu.", "CREATE PROCEDURE get_top() BEGIN SELECT * FROM students ORDER BY avg DESC LIMIT 5; END;", "CALL get_top(); tho run."),
        ("SQL", "Projects"): ("SQL Projects: Student DB, E-Commerce DB, Hospital DB, Bank DB. Tables + JOINS + Procedures.", "Project: Student DB - students, placements, results tables", "ER Diagram first gey, tharuvatha tables."),
        # ===== DSA - 8 =====
        ("DSA", "Arrays"): ("Array O(1) access, O(n) search. Techniques: Two Pointers, Sliding Window, Prefix Sum, HashMap.", "def two_sum(arr,t): seen={} # O(n) HashMap", "Brute O(n^2), HashMap O(n)."),
        ("DSA", "Linked List"): ("Nodes chain. data + next address. Reverse, Detect Loop - Floyd tortoise-hare.", "Reverse: prev=None, curr=head # O(n) O(1)", "Slow 1, Fast 2 - kalisthe loop."),
        ("DSA", "Stack & Queue"): ("Stack LIFO-push pop, Queue FIFO-enqueue dequeue. Stack-Undo, Queue-BFS.", "Stack: push(10), pop()->10. Queue: enqueue(10), dequeue()->10", "Valid Parentheses - Stack."),
        ("DSA", "Trees"): ("Tree hierarchical. Inorder Left-Root-Right BST lo sorted. BFS Queue, DFS Stack.", "Inorder: Left -> Root -> Right", "BST search O(log n) avg."),
        ("DSA", "Graphs"): ("Graph nodes + edges. BFS Queue shortest path, DFS Stack recursion. Adjacency List better.", "BFS: Queue lo start petti, visited mark, neighbours add", "Dijkstra shortest path, Cycle detection."),
        ("DSA", "Sorting"): ("Bubble O(n^2), Merge O(n log n) stable, Quick avg O(n log n) worst O(n^2).", "Quick: pivot pick, small left, big right", "Merge stable, Quick in-place."),
        ("DSA", "DP"): ("DP ante Dynamic Programming. Same subproblem malli malli vaste store cheskovadam. Memoization + Tabulation.", "Fibonacci: dp[0]=0, dp[1]=1, dp[i]=dp[i-1]+dp[i-2]", "Recursion O(2^n), DP O(n)."),
        ("DSA", "Greedy"): ("Greedy ante prathi step lo best choose cheyadam. Future chudakunda present best. Activity Selection, Coin Change.", "Activity: End time batti sort chesi, overlapping kakunda pick", "Greedy anni chotla work avvadhu, DP kavali."),
    }
    if (skill, topic) in articles:
        intro, example, dry = articles[(skill, topic)]
    else:
        intro = f"{topic} is very important topic in {skill}."
        example = f"print('{topic} - {skill}')"
        dry = f"Input -> Process {topic} -> Output."
    html = ""
    html += f"<h2 style='color:#fef08a;margin-top:0;'>{topic} in {skill} - Complete Tutorial</h2>"
    html += f"<div class='diag'>Topic: {topic} | Skill: {skill} | Level: Beginner to Advanced</div>"
    html += f"<div class='cat'>1. What is {topic}?</div><p style='color:white;line-height:1.9;'>{intro}</p>"
    html += f"<div class='cat'>2. Syntax / Example</div><div class='qbox' style='color:white;'>{example}</div>"
    html += f"<div class='cat'>3. How it Works - Dry Run</div><div class='abox'>{dry}</div>"
    html += f"<div class='cat'>4. Practice Questions</div><p style='color:white;'>1. Write 3 basic programs on {topic}<br>2. Write 2 medium problems on {topic}<br>3. Explain {topic} without seeing notes</p>"
    html += f"<div class='cat'>5. Interview Questions</div><p style='color:white;'>1. Explain {topic} with example?<br>2. What is Time Complexity of {topic}?<br>3. Write code for {topic} without library?</p>"
    return html
def get_interview_content(skill):
    html = ""
    html += "<div class='cat'>Top Interview Questions - " + skill + "</div>"
    html += "<div class='diag'>Quick Diagram: Stack - Local vars | Heap - Objects malloc | Code - Text segment</div>"
    if skill == "C":
        html += "<div class='qbox'><b>Q1. What is pointer? Why use pointer? Explain pointer to pointer with diagram.</b></div><div class='abox'><b>Answer:</b> Pointer stores address. int a=10 at addr 1000. int *p = &a p stores 1000 at 2000. *p is value at address =10. Why use? 1 Dynamic memory malloc 2 Pass large data without copy 3 Build Linked List. Code int a=10; int *p=&a; printf percent d *p prints 10. Diagram a 1000=10 p 2000=1000 pp 3000=2000. Always init as NULL to avoid wild. TCS asks 90 percent times.</div>"
        html += "<div class='qbox'><b>Q2. Array vs Pointer? Explain size difference?</b></div><div class='abox'><b>Answer:</b> Array continuous fixed size int arr 5 =20 bytes sizeof arr 20. Pointer 8 bytes stores address dynamic. Array name constant p++ allowed arr++ error.</div>"
        html += "<div class='qbox'><b>Q3. What is dangling pointer? How to avoid?</b></div><div class='abox'><b>Answer:</b> Pointer pointing to freed memory. int *p=malloc 4; free p; Now p dangling using *p crashes segmentation fault. Solution After free set p=NULL. Code free p; p=NULL; if p not equal NULL safe.</div>"
        html += "<div class='qbox'><b>Q4. malloc vs calloc vs realloc vs free?</b></div><div class='abox'><b>Answer:</b> malloc 1 arg size uninitialized garbage fast. calloc 2 args count size zero init safe slow. realloc resize existing block. free release memory.</div>"
        html += "<div class='qbox'><b>Q5. Structure vs Union vs padding?</b></div><div class='abox'><b>Answer:</b> Structure all members separate memory sum plus padding for alignment. struct char a int b size not 5 but 8 due to 4-byte alignment padding. Union shares same memory size = max member only one active.</div>"
    else:
        html += "<div class='qbox'><b>Q1. List vs Tuple vs Set vs Dict? Explain with diagram and time complexity?</b></div><div class='abox'><b>Answer:</b> List mutable ordered duplicate 1 2 2 O1 access On search use scores 85 90. Tuple immutable ordered 1 2 faster hashable can be dict key. Set unordered unique 1 2 O1 search no duplicate. Dict key-value a 1 O1 key must be hashable immutable.</div>"
        html += "<div class='qbox'><b>Q2. args vs kwargs? How to use? Unpacking?</b></div><div class='abox'><b>Answer:</b> args tuple positional unlimited def add args sum args call add 1 2 3. kwargs dict keyword def func kwargs for k v in kwargs.items call func name Bhav college QIS. Unpacking list to args my_list 1 2 3 add *my_list. Dict to kwargs my_dict name Bhav func **my_dict.</div>"
        html += "<div class='qbox'><b>Q3. Decorator Generator Iterator GIL?</b></div><div class='abox'><b>Answer:</b> Decorator wraps function adds behavior without modifying login_required. Generator yields one by one saves memory def gen yield 1 yield 2 for large file 1GB not load all for line in open file yield line. GIL only one thread executes Python bytecode at a time CPU-bound threading not faster but IO-bound ok use multiprocessing for CPU.</div>"
    return html

def get_default_code(skill):
    if skill == "C":
        return "# Practice - Pointer and Array\na=10\np=id(a)\nprint(a, p)\narr=[10,20,30,40]\nprint(arr)\ns=list(\"BhavPath\")\ni,j=0,len(s)-1\nwhile i<j:\n    s[i],s[j]=s[j],s[i]\n    i+=1; j-=1\nprint(''.join(s))"
    return "# Practice - Two Sum\ndef two_sum(arr, target):\n    seen={}\n    for i,num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\nprint(two_sum([2,7,11,15], 9))"

if st.session_state.page == "welcome":
    st.markdown("""<div class='center' style='padding-top:22vh'><h1 style='color:#c7f0ff;font-size:78px;font-weight:900;'>Welcome to BhavPath</h1><div class='glass' style='display:inline-block;margin-top:20px;padding:28px 50px;'><h2 style='margin:0;font-size:34px;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>What is Your Placement Story..??</h2></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.4,1,1.4])
    with c:
        st.write("")
        st.write("")
        if st.button("Next", use_container_width=True):
            st.session_state.page="login"
            st.rerun()

elif st.session_state.page == "login":
    st.markdown("<div class='center'><h1 style='color:white;'>Login to BhavPath</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1.2,1,1.2])
    with col:
        st.write("")
        email=st.text_input("Email")
        college=st.text_input("College Name")
        if st.button("Continue", use_container_width=True, type="primary"):
            if email and college:
                st.session_state.college=college
                st.session_state.page="purpose"
                st.rerun()
        if st.button("Back"):
            st.session_state.page="welcome"
            st.rerun()

elif st.session_state.page == "purpose":
    st.markdown("<div class='center'><h1 style='color:white;'>What is the purpose?</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.5,1])
    with col:
        st.write("")
        c1,c2=st.columns(2)
        with c1:
            if st.button("Placement Prediction", use_container_width=True):
                st.session_state.page="placement_welcome"
                st.rerun()
            st.write("")
            if st.button("Test Zone", use_container_width=True):
                st.session_state.page="test_welcome"
                st.rerun()
        with c2:
            if st.button("Technical Skills", use_container_width=True):
                st.session_state.page="tech_welcome"
                st.rerun()
            st.write("")
            if st.button("Interview + Code", use_container_width=True):
                st.session_state.page="interview_welcome"
                st.rerun()

elif st.session_state.page == "placement_welcome":
    st.markdown(f"<div class='center'><h1 style='color:white;'>Welcome to Placement Prediction</h1><p style='color:#a78bfa;'>{st.session_state.college}</p></div>", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        if st.button("Next - Enter Details", use_container_width=True, type="primary"):
            st.session_state.page="placement_form"
            st.rerun()
        if st.button("Back"):
            st.session_state.page="purpose"
            st.rerun()

elif st.session_state.page == "placement_form":
    st.markdown("<div class='center'><h1 style='color:white;'>Enter Your Details</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([1,1.3,1])
    with col:
        name=st.text_input("1. Name")
        tenth=st.number_input("2. 10th %",0.0,100.0,85.0)
        inter=st.number_input("3. Inter %",0.0,100.0,80.0)
        btech=st.number_input("4. B.Tech %",0.0,100.0,75.0)
        skills=st.text_input("5. Skills?", placeholder="Python, Java")
        if st.button("Continue", use_container_width=True, type="primary"):
            st.session_state.pdata=(name,tenth,inter,btech,skills)
            st.session_state.page="placement_result"
            st.rerun()
        if st.button("Back"):
            st.session_state.page="placement_welcome"
            st.rerun()

elif st.session_state.page == "placement_result":
    name,tenth,inter,btech,skills=st.session_state.pdata
    avg=(tenth+inter+btech)/3
    st.markdown(f"<div class='center'><h1 style='color:white;'>Company List - {avg:.1f}%</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.5,2,0.5])
    with col:
        # --- SKILL BATTI COMPANIES - FIXED ---
        skills_str = skills if isinstance(skills, str) else ",".join(skills) if isinstance(skills, list) else ""
        skills_low = skills_str.lower()
        skill_comp = {
            "java": [["Oracle", 75], ["Infosys", 70], ["Accenture", 68], ["Capgemini", 65], ["TCS Digital", 70]],
            "python": [["Google/Amazon", 75], ["Flipkart", 72], ["TCS Digital", 70], ["Swiggy", 68]],
            "c": [["Wipro", 65], ["Tech Mahindra", 60], ["TCS Ninja", 60], ["HCL", 62]],
            "sql": [["Deloitte", 68], ["Infosys", 65], ["Wipro", 65], ["Accenture", 68]],
            "dsa": [["Google/Amazon", 75], ["Microsoft", 78], ["TCS Digital", 70]],
            "c++": [["Wipro", 65], ["HCL", 62], ["TCS Ninja", 60]],
        }
        comp_list = []
        found_skill = False
        for key, clist in skill_comp.items():
            if key in skills_low:
                found_skill = True
                for cname, elig in clist:
                    if avg >= elig and [cname, f"{elig}%+"] not in comp_list:
                        comp_list.append([cname, f"{elig}%+"])
        if not found_skill:
            comp_list = [["TCS Digital", "70%+"], ["Wipro", "65%+"]]
        if not comp_list:
            comp_list = [["Skill improve chey - basics strong chey", "-"]]
        df = pd.DataFrame(comp_list, columns=["Company", "Eligibility"])
        st.write(f"Your Skills: {skills_str} | Avg: {avg:.1f}%")
        st.dataframe(df, use_container_width=True)
        st.bar_chart(pd.DataFrame({"Score":[tenth,inter,btech]}, index=["10th","Inter","BTech"]))
        st.progress(int(avg))
               # --- BACK + HOME ---
        bc1, bc2 = st.columns(2)
        with bc1:
            if st.button("Back", use_container_width=True):
                st.session_state.page="placement_form"
                st.rerun()
        with bc2:
            if st.button("Home", use_container_width=True):
                st.session_state.page="welcome"
                st.rerun()

elif st.session_state.page == "tech_welcome":
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - Full Detailed Content with Diagrams</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write("")
        st.write("")
        if st.button("Explore Skills", use_container_width=True, type="primary"):
            st.session_state.page="tech_skills"
            st.rerun()
        if st.button("Back"):
            st.session_state.page="purpose"
            st.rerun()

elif st.session_state.page == "tech_skills":
    st.markdown("<div class='center'><h1 style='color:white;font-size:42px;'>Select Your Skill</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C", use_container_width=True):
                st.session_state.selected_skill="C"
                st.session_state.topic="Intro"
                st.session_state.page="skill_detail"
                st.rerun()
        with r1_c2:
            if st.button("C++", use_container_width=True):
                st.session_state.selected_skill="C++"
                st.session_state.topic="Basics"
                st.session_state.page="skill_detail"
                st.rerun()
        with r1_c3:
            if st.button("Java", use_container_width=True):
                st.session_state.selected_skill="Java"
                st.session_state.topic="Basics"
                st.session_state.page="skill_detail"
                st.rerun()
        st.write("")
        r2_c1, r2_c2, r2_c3 = st.columns(3)
        with r2_c1:
            if st.button("Python", use_container_width=True):
                st.session_state.selected_skill="Python"
                st.session_state.topic="Loops"
                st.session_state.page="skill_detail"
                st.rerun()
        with r2_c2:
            if st.button("SQL", use_container_width=True):
                st.session_state.selected_skill="SQL"
                st.session_state.topic="SELECT"
                st.session_state.page="skill_detail"
                st.rerun()
        with r2_c3:
            if st.button("DSA", use_container_width=True):
                st.session_state.selected_skill="DSA"
                st.session_state.topic="Arrays"
                st.session_state.page="skill_detail"
                st.rerun()
        st.write("")
        st.write("")
        if st.button("Back", use_container_width=True):
            st.session_state.page="tech_welcome"
            st.rerun()

elif st.session_state.page == "skill_detail":
    skill=st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Full Detailed Learning</h1></div>", unsafe_allow_html=True)
    all_topics={"C":["Intro","Data Types","Loops","Functions","Pointers","Arrays","Structures","File Handling"],"C++":["Basics","OOP","STL","Pointers","Inheritance","Polymorphism","Templates","Projects"],"Java":["Basics","OOP","Collections","Exception","Multithreading","JDBC","Spring","Projects"],"Python":["Basics","Loops","Functions","OOP","Libraries","File Handling","Django","Projects"],"SQL":["SELECT","JOINS","GROUP BY","Subqueries","Indexing","Normalization","Procedures","Projects"],"DSA":["Arrays","Linked List","Stack & Queue","Trees","Graphs","Sorting","DP","Greedy"]}
    topics_list=all_topics.get(skill, all_topics["C"])
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        col1,col2=st.columns([1,2.5])
        with col1:
            st.markdown(f"<div class='glass'><h3 style='color:white;margin:0;'>{skill} Topics</h3></div>", unsafe_allow_html=True)
            st.write("")
            for i,t in enumerate(topics_list,1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True):
                    st.session_state.topic=t
                    st.rerun()
            st.write("")
            if st.button("Back"):
                st.session_state.page="tech_skills"
                st.rerun()
        with col2:
            content = get_detailed_content(skill, st.session_state.topic)
            st.markdown("<div class='detail-box'>" + content + "</div>", unsafe_allow_html=True)

elif st.session_state.page == "interview_welcome":
    st.markdown("""<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;font-size:18px;'>Crack TCS, Infosys, Amazon, Google - Interview + Code Practice</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write("")
        st.write("")
        if st.button("Start Interview Prep", use_container_width=True, type="primary"):
            st.session_state.page="interview_skills"
            st.rerun()
        if st.button("Back"):
            st.session_state.page="purpose"
            st.rerun()

elif st.session_state.page == "interview_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C Interview", use_container_width=True):
                st.session_state.selected_skill="C"
                st.session_state.page="interview_detail"
                st.rerun()
        with r1_c2:
            if st.button("C++ Interview", use_container_width=True):
                st.session_state.selected_skill="C++"
                st.session_state.page="interview_detail"
                st.rerun()
        with r1_c3:
            if st.button("Java Interview", use_container_width=True):
                st.session_state.selected_skill="Java"
                st.session_state.page="interview_detail"
                st.rerun()
        st.write("")
        r2_c1, r2_c2, r2_c3 = st.columns(3)
        with r2_c1:
            if st.button("Python Interview", use_container_width=True):
                st.session_state.selected_skill="Python"
                st.session_state.page="interview_detail"
                st.rerun()
        with r2_c2:
            if st.button("SQL Interview", use_container_width=True):
                st.session_state.selected_skill="SQL"
                st.session_state.page="interview_detail"
                st.rerun()
        with r2_c3:
            if st.button("DSA Interview", use_container_width=True):
                st.session_state.selected_skill="DSA"
                st.session_state.page="interview_detail"
                st.rerun()
        st.write("")
        st.write("")
        if st.button("Back", use_container_width=True):
            st.session_state.page="interview_welcome"
            st.rerun()

elif st.session_state.page == "interview_detail":
    skill=st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Interview + Code Practice</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.05,3,0.05])
    with c:
        col1, col2 = st.columns([1.4, 1])
        with col1:
            content=get_interview_content(skill)
            st.markdown("<div class='detail-box'><h3 style='color:#fef08a;margin-top:0;'>Interview Questions - Detailed</h3><div style='color:white;line-height:1.8;font-size:13px;'>" + content + "</div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='detail-box'><h3 style='color:#00ff88;margin-top:0;'>Code Practice - Run Here</h3></div>", unsafe_allow_html=True)
            default_code=get_default_code(skill)
            code_input=st.text_area("Editor", value=default_code, height=420, key="editor_"+skill, label_visibility="collapsed")
            if st.button("Run Code", key="run_iv_"+skill, type="primary", use_container_width=True):
                import sys
                from io import StringIO
                try:
                    old_stdout=sys.stdout
                    sys.stdout=mystdout=StringIO()
                    exec(code_input, {"pd": pd})
                    sys.stdout=old_stdout
                    output=mystdout.getvalue()
                    st.success("Output:\n"+output)
                except Exception as e:
                    st.error("Error: "+str(e))
            st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("Back"):
            st.session_state.page="interview_skills"
            st.rerun()

elif st.session_state.page == "test_welcome":
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Test Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;font-size:18px;'>Weekly Tests - Practice Your Skills</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write("")
        st.write("")
        if st.button("Explore Tests", use_container_width=True, type="primary"):
            st.session_state.page="test_skills"
            st.rerun()
        if st.button("Back"):
            st.session_state.page="purpose"
            st.rerun()

elif st.session_state.page == "test_skills":
    week = get_current_week()
    st.markdown(f"<div class='center'><h1 style='color:white;'>Test Zone - Week {week}</h1><p style='color:#a78bfa;'>Select Skill for Test</p></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C Test", use_container_width=True):
                st.session_state.test_skill="C"
                st.session_state.test_questions=get_weekly_random_questions("C", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r1_c2:
            if st.button("Java Test", use_container_width=True):
                st.session_state.test_skill="Java"
                st.session_state.test_questions=get_weekly_random_questions("Java", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r1_c3:
            if st.button("Python Test", use_container_width=True):
                st.session_state.test_skill="Python"
                st.session_state.test_questions=get_weekly_random_questions("Python", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        st.write("")
        r2_c1, r2_c2, r2_c3 = st.columns(3)
        with r2_c1:
            if st.button("SQL Test", use_container_width=True):
                st.session_state.test_skill="SQL"
                st.session_state.test_questions=get_weekly_random_questions("SQL", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r2_c2:
            if st.button("DSA Test", use_container_width=True):
                st.session_state.test_skill="DSA"
                st.session_state.test_questions=get_weekly_random_questions("DSA", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r2_c3:
            if st.button("Mixed Test", use_container_width=True):
                all_q = []
                for sk in ["C", "Python", "Java", "SQL", "DSA"]:
                    all_q.extend(get_weekly_random_questions(sk, 2))
                random.shuffle(all_q)
                st.session_state.test_skill="Mixed"
                st.session_state.test_questions=all_q
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        st.write("")
        st.write("")
        if st.button("Back", use_container_width=True):
            st.session_state.page="test_welcome"
            st.rerun()

elif st.session_state.page == "test_attempt":
    skill = st.session_state.test_skill
    questions = st.session_state.test_questions
    week = st.session_state.test_week
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Test - Week {week}</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        if not st.session_state.test_submitted:
            st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
            for idx, q in enumerate(questions):
                st.markdown(f"<div class='qbox'><b>Q{idx+1}. {q['q']}</b></div>", unsafe_allow_html=True)
                key = f"test_q_{idx}"
                options = q["options"]
                selected = st.radio(f"Select for Q{idx+1}", options, key=key, index=None, label_visibility="collapsed")
                if selected is not None:
                    sel_idx = options.index(selected)
                    st.session_state.test_answers[idx] = sel_idx
                st.write("")
            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Submit Test - See Score", use_container_width=True, type="primary"):
                    st.session_state.test_submitted=True
                    st.rerun()
            with col2:
                if st.button("Back - Cancel Test", use_container_width=True):
                    st.session_state.page="test_skills"
                    st.rerun()
        else:
            score = 0
            for idx, q in enumerate(questions):
                user_ans = st.session_state.test_answers.get(idx, -1)
                if user_ans == q["ans"]:
                    score += 1
            st.markdown(f"<div class='center'><h2 style='color:#00ff88;'>Your Score: {score} / {len(questions)} - {score*10} %</h2><p style='color:#a78bfa;'>Week {week} Test Completed</p></div>", unsafe_allow_html=True)
            st.progress(score/len(questions))
            st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
            for idx, q in enumerate(questions):
                user_ans = st.session_state.test_answers.get(idx, -1)
                correct = q["ans"]
                is_correct = user_ans == correct
                color = "#00ff88" if is_correct else "#ff006a"
                status = "Correct" if is_correct else "Wrong"
                st.markdown(f"<div class='qbox' style='border-left-color:{color};'><b>Q{idx+1}. {q['q']}</b><br><span style='color:{color};font-weight:bold;'>{status}</span> - Your Answer: {q['options'][user_ans] if user_ans!=-1 else 'Not Answered'} | Correct: {q['options'][correct]}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='abox'><b>Explanation:</b> {q['exp']}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("Retake - New Questions", use_container_width=True, type="primary"):
                    st.session_state.test_questions=get_weekly_random_questions(skill, 10)
                    st.session_state.test_answers={}
                    st.session_state.test_submitted=False
                    st.rerun()
            with c2:
                if st.button("Change Skill", use_container_width=True):
                    st.session_state.page="test_skills"
                    st.rerun()
            with c3:
                if st.button("Home", use_container_width=True):
                    st.session_state.page="purpose"
                    st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon</h1></div>", unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.page="purpose"
        st.rerun()
