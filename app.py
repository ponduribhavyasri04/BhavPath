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
    # intro, why, syntax, example, dry, deep, comp, adv, disadv, mistake, use
    articles = {
        ("C", "Intro"): ("C is a powerful, general-purpose procedural programming language developed by Dennis Ritchie in 1972 at Bell Labs. C is called the 'Mother of all languages' because C++, Java, Python and Go were all inspired by C. In C, we work very close to computer hardware and we can control memory directly. That is why Operating Systems, Compilers and Embedded Systems are written in C. If you learn C, your base becomes very strong and all other languages will feel easy.", "If you learn C, you will understand programming logic, how memory works, and what happens inside a computer. C questions are compulsory in placements. DSA also becomes deeper if you learn it in C.", "Structure:\n#include <stdio.h>\nint main(){\n  printf(\"Hello\");\n  return 0;\n}", "int main(){ printf(\"Hello\"); return 0; }\nOutput: Hello", "main() starts -> printf() is called -> 'Hello' is printed on screen -> return 0 -> program ends.", "C code is converted directly into machine code. The compiler checks the code and converts it into 0s and 1s that the machine understands. Then the CPU runs it. There is no extra layer, that is why C is very fast.", "Time: O(1) | Space: O(1) | Compile: Very Fast", "Fastest language, Portable, Memory Control, Close to Hardware.", "Limitation: No OOP, String handling is difficult, You must manage memory manually.", "Mistake: Forgetting #include, Forgetting ;, Forgetting return in main().", "Used in OS, Embedded, Drivers, Compilers, Game Engines."),
        ("C", "Data Types"): ("A Data Type is a rule that tells what kind of data a variable will store. It tells the computer how much memory is needed and what type of value will be there. For example int means number, char means single letter, float means decimal number. If you use wrong Data Type, memory is wasted or data is lost. That is why Data Types are very important in every language. In C there are 5 basic types - int, char, float, double, void.", "Without Data Types you cannot create a variable. In interviews they compulsory ask 'What is difference between int and float? What is size of char?' Memory management starts from here.", "Syntax:\nint age = 21; // 4 bytes\nchar grade = 'A'; // 1 byte\nfloat marks = 85.5; // 4 bytes\ndouble pi = 3.14; // 8 bytes", "int age=21; char g='A'; float m=85.5;\nOutput: age=21, g=A, m=85.5", "age gets 4 bytes memory -> 21 stored -> g gets 1 byte -> 'A' stored -> m gets 4 bytes -> 85.5 stored.", "int is stored in memory in 2's complement form. char is stored as ASCII value - 'A' means 65. float is stored in IEEE 754 format. That is why some decimals in float are not exact.", "Time: O(1) | Space: int 4B, char 1B, float 4B, double 8B", "Correct type saves memory, Speed is fast, No data loss.", "Limitation: Range is fixed - int has a limit, If you put bigger value it overflows.", "Mistake: Putting float in int and losing data, Using \"A\" with double quotes for char, Using uninitialized variable.", "Bank balance - double, age - int, grade - char, marks - float."),
        ("C", "Loops"): ("A Loop means repeating the same work again and again. If we want to print 1 to 100, we do not need to write 100 lines, with a loop it finishes in 3 lines. In C there are 3 loops. for loop - when count is known, while loop - based on condition, do-while loop - when it should run at least once. Without loops there is no programming, DSA runs totally on loops.", "Without loops you cannot traverse an Array, cannot print Patterns, 90% of DSA problems are with loops. In interviews, pattern questions from loops are compulsory.", "Syntax:\nfor(start; condition; update){\n  // code\n}\nwhile(cond){ // code }\ndo{ // code }while(cond);", "for(i=1;i<=5;i++){ printf(\"%d \",i); }\nOutput: 1 2 3 4 5", "i=1 -> 1<=5 True -> print 1 -> i=2 -> print 2 -> i=3 -> print 3 -> i=4 -> print 4 -> i=5 -> print 5 -> i=6 -> 6<=5 False -> Exit.", "A loop has 3 parts - Initialization, Condition Check, Update. As long as condition is True, body runs. When condition becomes False, we come out of loop. If you do not update loop variable correctly, it becomes infinite loop.", "Time: O(n) | Space: O(1) | n = iterations", "No code repeat, 100 lines code in 3 lines, Automation.", "Limitation: Infinite loop hangs system, Too many nested loops become slow.", "Mistake: Infinite loop - forgetting i++, Putting ; like for(i=0;i<5;i++); - body becomes separate.", "Print 1 to 100, Table print, Array traverse, Patterns."),
        ("C", "Functions"): ("A Function is a named code block that does one specific work. If we need to do same work many times, we write it once as a function and call it wherever needed. Example add() means adding two numbers. Because of functions, code becomes clean and small. In C there are two types - Call by Value where copy goes, original does not change. Call by Reference where address goes, original changes.", "Without functions you cannot make a big project. In a team, each person writes one function and together it becomes a project. Functions are the base for code reuse.", "Syntax:\nreturn_type name(params){\n  return value;\n}\nint add(int a, int b){ return a+b; }", "int add(int a,int b){ return a+b; }\nadd(2,3)\nOutput: 5", "add(2,3) call -> a=2,b=3 copy -> a+b=5 -> return 5 -> main gets 5.", "When a function is called, a frame is created in Stack. It has parameters and local variables. When function returns, that frame is deleted. That is why in recursion if calls are too many, Stack Overflow comes.", "Time: O(1) for add | Space: O(1) + Stack", "Code reuse, Testing easy, Team can divide work, Debugging easy.", "Limitation: Function call has some overhead, Too many functions makes tracking difficult.", "Mistake: Return type and return value not matching, Calling function without declaring it.", "Calculator, Banking - deposit(), withdraw() are all functions."),
        ("C", "Pointers"): ("A Pointer is a special variable that stores the address of another variable. A normal variable stores value, a Pointer variable stores address. Example int a = 10 means a has 10, int *p = &a means p has address of a. *p means value at that address, p means address. With pointers we can create dynamic memory, change original value in functions, and build Linked List, Tree like data structures. Pointers are the heart of C.", "Without pointers you cannot do Linked List, Tree, Graph in DSA. In interviews, many questions come from Pointers. C++, Java base is also this.", "Syntax:\nint a = 10;\nint *p = &a;\nprintf(\"%d\", *p); // 10\nprintf(\"%p\", p); // address", "int a=10; int *p=&a;\nprintf(\"%d\", *p);\nOutput: 10", "a=10 at address 1000 -> p=1000 at 2000 -> *p means go to 1000 and take value -> 10.", "Every variable in memory has an address. Pointer holds that address. * means Dereferencing - taking value from address. & means Address-of - taking address of variable. With malloc() we can ask memory in heap, with free() we can release it.", "Time: O(1) | Space: Pointer 8 bytes (64-bit)", "Dynamic memory, Array + Function fast, Base for Data Structures, Direct memory access.", "Limitation: Little risky - wrong address causes crash, Difficult for beginners.", "Mistake: Dangling pointer - using after free, Dereferencing NULL pointer, Confusing *p vs p.", "Linked List, Tree, Dynamic Array are all with pointers."),
        ("C", "Arrays"): ("An Array means storing many values of same type with one name, in continuous memory. Example instead of putting marks of 100 students in 100 variables, we put in one array - int marks[100]. Every value in array has an index, index starts from 0. Address formula of array - Base Address + index * size. That is why any element in array can be accessed in O(1).", "Without Arrays there is no DSA. Sorting, Searching, Two Pointers are all on Arrays. In interviews 50% problems are from Arrays.", "Syntax:\nint arr[3] = {10,20,30};\narr[0] = 10, arr[1] = 20, arr[2] = 30", "int arr[]={10,20,30};\nprintf(\"%d\",arr[1]);\nOutput: 20", "Base 1000 -> arr[0]=1000 -> arr[1]=1000+1*4=1004 -> value 20.", "Array is continuous in memory. That is why CPU cache is fast. arr[1] means compiler directly goes to Base + 1*4 and takes value. But size is fixed - whatever you give at creation stays same, cannot increase later. For that we need Dynamic Array / Linked List.", "Time: Access O(1), Search O(n), Insert O(n) | Space: O(n)", "Random access O(1), Cache friendly, Simple, Sorting easy.", "Limitation: Size fixed, Insert/delete in middle is slow, Only same type.", "Mistake: Index out of bounds arr[10] - garbage / crash, Forgetting array size is fixed.", "Marks list, Images pixels, Matrix, Leaderboard."),
        ("C", "Structures"): ("A Structure means grouping different types of data into one group. Example a Student has id - int, name - string, marks - float. These are three different types, but they belong to one Student. Instead of keeping them separate, we put them together in struct Student. With Structure we can easily represent a real world entity in code. In Structure, size increases a little because of Padding - CPU leaves some empty space to read fast.", "To represent real world data, Structures are a must. Student, Employee, Bank Account are all Structures. This is the base for Class in C++.", "Syntax:\nstruct Student{\n  int id;\n  char name[20];\n  float marks;\n};\nstruct Student s1 = {1, \"Bhav\", 90.5};", "struct Student s1={1,\"Bhav\"};\nprintf(\"%d %s\", s1.id, s1.name);\nOutput: 1 Bhav", "s1 gets memory allocated -> id=1 -> name='Bhav' -> s1.id means go to id field.", "Structure members are in memory one after another continuously. But CPU leaves empty bytes in middle for 4 bytes alignment - that is called Padding. That is why struct size is a little more than expected. With typedef we can use Student instead of struct Student - short form.", "Time: O(1) | Space: Sum of members + Padding", "Different types in one place, Can represent real world entity, Code clean.", "Limitation: Cannot put functions inside structure - In C++ you can in Class, Padding wastes memory.", "Mistake: Forgetting ; after struct, Struct size is more than expected because of Padding.", "Student record, Employee record, Bank account."),
        ("C", "File Handling"): ("File Handling means saving data permanently even after program closes. Data we put in variable in program is lost when program ends. But if we write in File, it is saved in computer. In C for File Handling we use fopen(), fclose(), fprintf(), fscanf(). Modes - r means read, w means write (old data deleted), a means append (add to old data). With File Handling we can save Student Data, Logs, Config files.", "To save data in a real project, File Handling is a must. Before Database, File Handling is the base. In interviews they ask 'What is difference between w and a?'", "Syntax:\nFILE *f = fopen(\"a.txt\",\"w\");\nfprintf(f,\"Hi\");\nfclose(f);", "FILE *f=fopen(\"a.txt\",\"w\");\nfprintf(f,\"Hi\"); fclose(f);\nOutput: 'Hi' is saved in File", "fopen -> file opens -> fprintf -> 'Hi' written -> fclose -> save + close.", "fopen() opens file and gives a pointer. With fprintf() we can write, with fscanf() we can read. If we do not do fclose(), data stays in buffer and is not saved in file. That is why fclose() is compulsory. Large files should be read line by line, if we read whole file at once memory becomes full.", "Time: O(n) n=file size | Space: O(1)", "Data stays permanent, Does not go after program closes, Can handle large data.", "Limitation: If file corrupts, data is lost, Slower than Database, Searching is difficult.", "Mistake: Forgetting fclose() - data loss, Using w mode without knowing old data will be deleted.", "Student data save, Logs, Config files, Attendance."),
        ("C++", "Basics"): ("C++ is an upgraded version of C language with Object Oriented Programming added. Developed by Bjarne Stroustrup in 1985. C speed + C++ OOP together make C++ very powerful. In C++ we take input/output with cin/cout, we use namespace std. All C code also runs in C++. Game Development, Operating Systems, Browsers, DSA - all in C++. For placements, C++ is No.1 choice for DSA.", "If you learn C++, you get C + OOP both. C++ is best for DSA, Competitive Coding, Placements. Because of Speed + STL you can write code fast in interviews.", "Syntax:\n#include <iostream>\nusing namespace std;\nint main(){ cout << \"Hi\"; return 0; }", "#include <iostream>\nusing namespace std;\nint main(){ cout<<\"Hi\"; }\nOutput: Hi", "main starts -> cout -> 'Hi' on screen -> return 0 -> end.", "C++ code is converted by compiler into machine code. cout means Console Output, cin means Console Input. namespace std means we can directly use cout, cin from standard library. Otherwise we have to write std::cout.", "Time: O(1) | Space: O(1)", "C speed + OOP power, STL ready, Large community.", "Limitation: Memory must be managed manually, Slightly big language for beginners.", "Mistake: Forgetting using namespace std, Missing ;, Using stdio.h instead of iostream.", "Games, OS, Browsers, DSA, Placements."),
        ("C++", "OOP"): ("OOP means Object Oriented Programming. Seeing real world things as objects in code. Example Dog is a Class - blueprint, Tom is an Object - real dog. OOP has 4 pillars - Encapsulation means hiding data, Inheritance means child gets from parent, Polymorphism means one name different work, Abstraction means hiding unnecessary details. With OOP we can divide big projects into small parts and manage easily.", "All big projects are with OOP. In interviews OOP questions are compulsory. Java, Python are all on OOP.", "Syntax:\nclass Dog{\n public:\n  void bark(){ cout<<\"Bark\"; }\n};\nDog d; d.bark();", "class Dog{ public: void bark(){ cout<<\"Bark\"; } };\nDog d; d.bark();\nOutput: Bark", "Class blueprint -> Dog d object created -> d.bark() called -> Bark printed.", "Class means blueprint, Object means real thing created with that blueprint. When object is created, place comes in memory. public means can access from outside, private means only inside class. Constructor runs automatically when object is created.", "Time: O(1) | Space: O(object size)", "Code reuse, Real world mapping, Maintenance easy, Team work easy.", "Limitation: For small things OOP feels too much, If design is wrong, whole project is wrong.", "Mistake: Forgetting ; after Class, Accessing private member directly.", "Bank, Game characters, E-commerce, College Management."),
        ("C++", "STL"): ("STL means Standard Template Library. A powerful ready-made tools box in C++. We do not need to write Linked List, Stack, Queue, Map again and again, they are ready in STL. vector means dynamic array, map means key-value, set means unique values, stack, queue are all ready. sort() means sorting in one line. Without STL, in interviews and Competitive Coding you cannot write code fast. If you learn STL, DSA becomes very easy.", "With STL, 100 lines code becomes 10 lines. If you use STL in interview, interviewer understands you are practical.", "Syntax:\nvector<int> v;\nv.push_back(10);\nsort(v.begin(), v.end());", "vector<int> v={3,1,2};\nsort(v.begin(), v.end());\nOutput: 1 2 3", "vector created -> 3,1,2 pushed -> sort() -> 1,2,3 -> print.", "Inside vector there is dynamic array. When size is full, it automatically creates new array with double size and copies old data. Inside map there is Red-Black Tree, that is why search is O(log n). Inside sort() there is IntroSort - Quick + Heap + Insertion combined.", "vector access O(1), map O(log n), sort O(n log n)", "Less code, Less bugs, Fast, Tested code.", "Limitation: If you do not know how it works inside, you cannot explain in interview, Memory is a little more.", "Mistake: Thinking vector size is fixed, Using [] in map auto inserts.", "DSA problems, Competitive coding, Placements."),
        ("C++", "Pointers"): ("C++ Pointers are like C, but more advanced. In C we use malloc/free, in C++ we use new/delete. int *p = new int(10) means we asked memory in heap for 10. delete p means we released that memory. Smart Pointer means pointer that deletes automatically - no memory leak. With pointers we can create Dynamic Objects, Linked List, Tree. Pointers + OOP together make C++ very powerful.", "For DSA + System programming, Pointers are a must. Memory leak, Dangling pointer concepts are asked in interviews.", "Syntax:\nint *p = new int(10);\ncout << *p;\ndelete p;", "int *p = new int(10);\ncout<<*p;\nOutput: 10", "new -> memory in heap -> 10 stored -> *p -> 10 -> delete -> free.", "Memory in Stack is cleared automatically, Memory in Heap we must clear ourselves. new means asking in heap, delete means releasing. If we do not delete, Memory Leak - memory becomes full. Smart pointer - unique_ptr, shared_ptr - deletes automatically.", "Time: O(1) | Space: O(1) + heap", "Dynamic memory, Performance, Full control.", "Limitation: If you make mistake, crash, Memory leak, Difficult for beginners.", "Mistake: Memory leak without delete, Double delete - crash.", "Linked List, Dynamic objects, Games."),
        ("C++", "Inheritance"): ("Inheritance means giving properties of one class to another class. Parent class Animal - eat(), sleep(). Child class Dog - automatically gets eat(), sleep() from Animal, plus Dog has extra bark(). No need to write code again. In Inheritance there are 3 types - public, private, protected. In C++ Multiple Inheritance is also there - one child has two parents. With Inheritance, code reuse and hierarchy is clear.", "Inheritance is best for code reuse. To show real world hierarchy in code, Inheritance. In interviews, Types are compulsory.", "Syntax:\nclass Animal{ void eat(){} };\nclass Dog : public Animal{ void bark(){} };", "class Animal{ void eat(){ cout<<\"Eat\"; } };\nclass Dog : public Animal{};\nDog d; d.eat();\nOutput: Eat", "Dog object -> search eat() in parent -> found -> Eat printed.", "When Child object is created, first Parent constructor runs, then Child constructor. Destructor is reverse - Child first, Parent later. In public inheritance, Parent public members stay public in Child. Private members are not visible even to Child.", "Time: O(1) | Space: O(parent + child)", "Code reuse, Hierarchy clear, Maintenance easy.", "Limitation: Too much inheritance makes code complex, Diamond problem - solved with virtual inheritance in C++.", "Mistake: Thinking private parent member is accessible in child, Diamond problem.", "Vehicle -> Car/Bike, Employee -> Manager/Developer."),
        ("C++", "Polymorphism"): ("Polymorphism means one name, different forms. In Greek Poly - many, Morph - forms. Two types - Compile Time Function Overloading - one name, different parameters. Runtime Function Overriding - writing Parent function again in Child, with virtual keyword. Example Shape draw() is one, Circle draw() is circle, Square draw() is square. One name, different work.", "In interviews, Polymorphism is a compulsory question. They never leave without asking Overloading vs Overriding difference.", "Syntax:\nvoid add(int a,int b){}\nvoid add(float a,float b){} // Overloading\nvirtual void draw(){ } // Overriding", "void add(int a,int b){ cout<<a+b; }\nvoid add(float a,float b){ cout<<a+b; }\nadd(2,3) -> 5, add(2.5,3.5) -> 6.0", "add(2,3) -> int version selected -> 5. add(2.5,3.5) -> float version.", "In Overloading, compiler sees parameters and decides which function to call - Compile Time. In Overriding, virtual table (vtable) has function address, it is decided at runtime - Runtime. Without virtual, overriding will run Parent version.", "Time: O(1) | Space: O(1)", "Flexibility, Same name different work, Code clean.", "Limitation: Runtime polymorphism has some overhead, vtable memory.", "Mistake: Overriding without virtual runs parent version.", "Shape -> draw(), Payment -> pay(), Animal -> sound()."),
        ("C++", "Templates"): ("Template means writing generic code. Writing one function that works for int, float, string - all types. Example instead of writing add() function once for int, once for float, with template we write once. Compiler automatically creates code for whatever type we call. STL is fully built with Templates - vector<int>, vector<string> are all Templates. With Templates, code reuse becomes 100%.", "If you know Templates, you understand what is inside STL. Templates are base for Generic programming.", "Syntax:\ntemplate<typename T>\nT add(T a, T b){ return a+b; }", "template<typename T> T add(T a,T b){ return a+b; }\nadd(2,3)=5, add(2.5,3.5)=6.0", "add(2,3) -> T=int -> 5. add(2.5,3.5) -> T=float -> 6.0", "Template means a blueprint for compiler. When we call add(2,3), compiler creates add<int> function. For add(2.5,3.5) it creates add<float>. We write code once, compiler generates for all types.", "Time: O(1) | Space: O(1)", "One code for all types, Type safe, Code reuse.", "Limitation: Error messages are big and difficult, Compilation time is more.", "Mistake: Putting Template definition in .cpp and getting link error - should be in header.", "vector, map, sort() are all with templates."),
        ("C++", "Projects"): ("C++ Projects means combining everything you learnt - OOP, STL, File Handling, Pointers - and making a real app. Example Bank Management System - Account create, Deposit, Withdraw, Balance check. Library Management - Book add, Issue, Return. Without projects, only theory stays, in interview there is nothing to tell. With project, interviewer believes you really wrote code. Project is very important in Resume.", "For placement, Project is a must. In interview they ask 20 mins about project. Without project, resume is weak.", "Structure:\nclass Account{\n int balance;\n void deposit(int amt){ balance+=amt; }\n void withdraw(int amt){ balance-=amt; }\n};", "Project: Bank - class Account { deposit(), withdraw(), checkBalance() }\nOutput: Balance update - Deposit 1000 -> 1000, Withdraw 200 -> 800", "Account created -> deposit 1000 -> balance 1000 -> withdraw 200 -> balance 800.", "In a project first decide Requirement - what features are needed. Then Classes design - Account, Customer, Bank. Then Functions - deposit, withdraw. Then File Handling to save data. Finally Testing - test all cases.", "Time: Depends on feature | Space: O(n) records", "Resume strong, Story to tell in interview, Real learning.", "Limitation: Takes time, Without planning it becomes messy.", "Mistake: Writing everything in main(), Without OOP, Without File Handling.", "Resume, Placement demo, GitHub."),
        ("Java", "Basics"): ("Java is a powerful, object oriented programming language. Developed by Sun Microsystems in 1995. Main slogan of Java - WORA - Write Once Run Anywhere. Means code written once can run on any computer - Windows, Mac, Linux. How? Java code is not converted directly to machine code, it is converted to Bytecode. That Bytecode can be run by JVM - Java Virtual Machine - on any system. That is why Java is used more in Banking, Android, Enterprise apps.", "If you learn Java, there are many placement opportunities. Banking, Enterprise, Android are all Java. With Spring Boot, job market is big.", "Syntax:\nclass Main{\n public static void main(String[] a){\n  System.out.println(\"Hi\");\n }\n}", "class Main{ public static void main(String[] a){ System.out.println(\"Hi\"); } }\nOutput: Hi", "javac -> .class Bytecode -> JVM -> Hi printed.", "Java code is converted by javac compiler into .class file - Bytecode. That Bytecode is read by JVM and converted into machine code for that system and run. JDK is for Developing, JRE is for Running, JVM is for Executing. These three together are Java Platform.", "Time: O(1) | Space: O(1)", "Portable, Secure, Large community, Platform independent.", "Limitation: A little slow compared to C++, More memory, Startup time more.", "Mistake: Forgetting File name = Class name, Spelling of main wrong.", "Android, Banking, Enterprise, E-commerce."),
        ("Java", "OOP"): ("In Java, OOP is the main concept everyone follows. Java is called Pure OOP, because everything is with Class, Object. OOP has 4 pillars - Encapsulation means making data private and accessing with getter/setter, Inheritance means child from parent with extends, Polymorphism means Overloading/Overriding, Abstraction means hiding details with abstract class/interface. With OOP in Java, code becomes very clean, reusable, secure.", "Java interview is totally on OOP. Without OOP you cannot get job in Java.", "Syntax:\nclass Dog extends Animal{\n void bark(){ System.out.println(\"Bark\"); }\n}", "class Dog extends Animal{ void bark(){ System.out.println(\"Bark\"); } }\nOutput: Bark", "Dog object -> bark() -> Bark.", "In Java every code must be inside Class. To create Object we must use new keyword. extends means Inheritance, implements means Interface. private member cannot be accessed directly from outside class, only with getter/setter. static means can call with Class name without Object.", "Time: O(1) | Space: O(object)", "Clean code, Reuse, Asked more in interviews, Secure.", "Limitation: For small things you have to write more code, Performance a little less.", "Mistake: Accessing non-static directly in static, Comparing String with == instead of .equals().", "Banking, E-commerce, Android."),
        ("Java", "Collections"): ("Collections means ready-made Data Structures group in Java. We can use Array, Linked List, Map without writing again, they are ready in Collections. ArrayList means dynamic array - size increases automatically, get O(1). HashMap means key-value - with name we can take value in O(1). HashSet means only unique values - no duplicates. If you learn Collections, DSA in Java becomes very easy.", "For DSA in Java, Collections are a must. In interviews Collections questions are compulsory - ArrayList vs LinkedList, How does HashMap work?", "Syntax:\nArrayList<String> l = new ArrayList<>();\nl.add(\"Bhav\");\nHashMap<String,Integer> m = new HashMap<>();", "ArrayList<String> l=new ArrayList<>(); l.add(\"Bhav\");\nOutput: [Bhav]", "ArrayList created -> add Bhav -> stored in list.", "Inside HashMap, hashCode() converts key into number, based on that number it stores in bucket. If collision happens, it stores in Linked List / Tree. In Java 8, if bucket has more than 8, it becomes Tree. Inside ArrayList there is array, when full it creates new array with 1.5x size.", "ArrayList get O(1), add O(1) avg, HashMap get O(1) avg, HashSet O(1)", "Dynamic size, Ready methods, Fast, Tested.", "Limitation: If you do not know how it works inside, you fail in interview, Without Generics no type safety.", "Mistake: Only one null key in HashMap, Using == instead of .equals() in ArrayList, Using Raw type.", "Student list, Cache, Unique users, Frequency count."),
        ("Java", "Exception"): ("Exception means unexpected error when program is running. Example 10/0 means ArithmeticException, if file is not there FileNotFoundException. When Exception comes, program stops - crashes. For that we use try-catch-finally. try has risky code, catch has what to do when error comes, finally has code that must run whether error comes or not - like file close. Checked Exception means checked at compile time - IOException, Unchecked means at runtime - NullPointerException.", "Without Exception handling you cannot make real app. To show user a good message instead of 'Error', Exception is a must.", "Syntax:\ntry{ int x=10/0; }\ncatch(Exception e){ System.out.println(e); }\nfinally{ System.out.println(\"Done\"); }", "try{ int x=10/0; } catch(Exception e){ System.out.println(e); }\nOutput: / by zero + Done", "try -> 10/0 error -> jump to catch -> print error -> finally always runs.", "When Exception comes, JVM creates an Exception object and throws it. It goes from try to catch. In catch we handle that exception. In finally there is cleanup code like file close, DB close. throw means we ourselves throw exception, throws means this method may have exception.", "Time: O(1) | Space: O(1)", "App does not crash, User gets good message, Debugging easy.", "Limitation: Too much try-catch makes code messy, Performance decreases a little.", "Mistake: Empty catch block - error not visible, Swallowing Exception, Catching only Generic Exception.", "Login, Payment, File read, API calls."),
        ("Java", "Multithreading"): ("Multithreading means doing many works at same time in one program. Example in YouTube, video plays, comments also load, download also happens - all at same time. In Java there are two ways to create Thread - extending Thread class, implementing Runnable interface. Runnable is better, because in Java you can extend only one class, but you can implement many interfaces. With sleep(), join(), synchronized() we can control threads.", "For Performance, Responsive apps, Multithreading is a must. In interviews Thread vs Runnable, synchronized are compulsory.", "Syntax:\nclass MyThread extends Thread{\n public void run(){ System.out.println(\"Run\"); }\n}\nMyThread t = new MyThread(); t.start();", "MyThread t = new MyThread(); t.start();\nOutput: Run", "t.start() -> JVM creates new thread -> run() called -> Run printed.", "Thread start() means telling JVM to create new thread. JVM gives CPU time to that thread. run() means what that thread should do. synchronized means only one thread can access that code at a time - data safe. Deadlock means two threads waiting for each other - program hangs.", "Time: Parallel | Space: O(threads)", "Speed, Responsive UI, Full CPU use.", "Limitation: Debugging difficult, Deadlock, Race Condition - data can corrupt.", "Mistake: Calling run() directly - it does not become thread, must use start(), Using shared data without synchronized.", "Video + Download + Chat at same time, Server - for all users at same time."),
        ("Java", "JDBC"): ("JDBC means Java Database Connectivity. Talking to Database from Java program. Code we wrote in Java can take data from MySQL, save, update with JDBC. In JDBC there are 4 main parts - Connection means connection with DB, Statement means sending query, ResultSet means result that came, DriverManager means managing driver. If you learn JDBC, you can make real project with Java + Database.", "Real project means Database is a must. Without JDBC, Java project is not complete. In interviews they ask JDBC steps.", "Syntax:\nConnection con = DriverManager.getConnection(\"jdbc:mysql://localhost:3306/db\",\"root\",\"pass\");\nStatement st = con.createStatement();\nResultSet rs = st.executeQuery(\"SELECT * FROM students\");", "Connection -> Statement -> SELECT -> ResultSet\nOutput: DB rows - students list", "Load driver -> Connect -> Query -> ResultSet -> Close.", "In JDBC first load Driver - Class.forName(). Then connect to DB with DriverManager.getConnection(). Then create Statement and send query. Read rows one by one in ResultSet. Finally close Connection - otherwise leak. If you use PreparedStatement, you are safe from SQL Injection.", "Time: O(n) rows | Space: O(n)", "Connects Java + DB, Real project, Secure with PreparedStatement.", "Limitation: More code, Must manage connection manually, Slower than ORM - Hibernate is better.", "Mistake: Not closing Connection - leak, Using Statement instead of PreparedStatement for SQL Injection, Hardcoding password in code.", "Bank, College DB, E-commerce - all JDBC/Hibernate."),
        ("Java", "Spring"): ("Spring is No.1 popular framework in Java. Framework means ready-made structure - we write code in structure given by Spring instead of writing everything from scratch. Main concept in Spring - Dependency Injection - means object is not created by us, Spring creates and gives it. Spring Boot is easy version of Spring - setup is very less, server starts with one click. Microservices - dividing into small services - are all done with Spring Boot. 80% of Java jobs are Spring Boot.", "If you want job in Java, Spring Boot is a must. Without Spring Boot it is difficult to get Java job now.", "Syntax:\n@SpringBootApplication\npublic class App{\n public static void main(String[] a){ SpringApplication.run(App.class,a); }\n}", "@SpringBootApplication\nOutput: Server started on 8080 - Website opens", "Run -> Spring Boot starts -> Tomcat starts -> Server 8080.", "In Spring Boot, @SpringBootApplication means - Configuration + ComponentScan + EnableAutoConfiguration - three together. When we write code, Spring Boot automatically starts Tomcat server, connects Database, makes everything ready. Controller means class that handles request, Service means business logic, Repository means talking to DB. Project has these 3 layers.", "Time: Startup few sec | Space: O(app)", "Fast development, Production ready, Large community, More jobs.", "Limitation: Too much magic - if you do not know what happens inside, debugging is difficult, More memory.", "Mistake: Forgetting Annotation, Wrong DB config in application.properties, Writing business logic in Controller.", "Microservices, APIs, Banking, E-commerce."),
        ("Java", "Projects"): ("Java Projects means combining everything you learnt - OOP, Collections, JDBC, Spring - and making a real app. Example ATM System - withdraw, deposit, balance check. Online Exam - questions, timer, result. Hospital Management - patient add, doctor, appointment. With projects, theory and practical get linked. In interviews they ask 20 mins about project - what did you do, how did you do, what problem came, how did you solve. Without project there is nothing to tell in resume.", "For placement, Project is a must. With project, interviewer believes you really did it.", "Structure:\nclass ATM{ withdraw(); deposit(); checkBalance(); }\n+ Collections + JDBC + Spring Boot", "Project: ATM - withdraw 500\nOutput: Balance updated - 1000 -> 500", "ATM -> withdraw -> balance check -> update -> receipt.", "To make project, first Requirement - what features. Then Design - Classes, Tables. Then Code - Layer by layer. Then Testing - all cases. Finally put in GitHub and write README. In interview questions come from that README.", "Time: O(n) | Space: O(n)", "Resume + Interview story, Real learning, GitHub strong.", "Limitation: Takes time, Without planning becomes messy.", "Mistake: Writing everything in main, Project without DB, Not putting in GitHub.", "Resume, Placement, GitHub."),
        ("Python", "Basics"): ("Python is an easy, readable, high-level programming language. Created by Guido van Rossum in 1991. Code in Python looks like English, that is why it is very easy for beginners. In Python no semicolon, no brackets needed - we decide block with Indentation. In Python Code -> Bytecode -> PVM - Python Virtual Machine - runs. Python is used in AI, Data Science, Web Development, Automation - everywhere. Now Python is No.1 popular language in the world.", "If you learn Python, AI, Data, Web - all doors open. Python is best start for beginners.", "Syntax:\nprint(\"Hello\")\n# No brackets, no semicolon\nx = 10\nif x > 5:\n print(\"Big\")", "print(\"Hello\")\nOutput: Hello", "print() -> Hello on screen.", "In Python, Interpreter reads code line by line, converts to Bytecode, runs with PVM. Indentation means space - with 4 spaces we tell block. If Indentation is wrong, IndentationError comes. Python is dynamically typed - no need to tell type to variable, type comes automatically based on value.", "Time: O(1) | Space: O(1)", "Easy, Fast to learn, Less code, Huge libraries.", "Limitation: Slow - compared to C, Less for Mobile apps, More memory.", "Mistake: Wrong Indentation - IndentationError, Confusing = vs ==, Python 2 vs 3.", "AI, Web, Automation, Data Science."),
        ("Python", "Loops"): ("Python Loops means repeating same work. In Python for loop is very simple - we can directly loop on values. for i in range(1,6) means 1 to 5. for name in names means all names in list. While loop runs until condition becomes False. List Comprehension means loop + condition in one line - [x*x for x in range(5)] - this is faster than normal loop. With Python loops we can do Data Processing, Automation.", "To process Data in Python, Loops are a must. In Data Science everything is Loops + Libraries.", "Syntax:\nfor i in range(1,6):\n print(i)\nwhile x < 5:\n print(x)\n x += 1", "for i in range(1,6): print(i)\nOutput: 1 2 3 4 5", "range(1,6) -> 1,2,3,4,5 -> print one by one.", "range(1,6) means 1,2,3,4,5 - 6 is not included. In Python range works lazily - it does not put all numbers in memory at once, it gives one by one. That is why range(1,1000000) also takes less memory. List Comprehension runs with C speed inside, that is why it is fast.", "Time: O(n) | Space: O(1)", "Simple, Readable, List comprehension fast, Less code.", "Limitation: If you forget update in while, infinite loop, Nested loops slow.", "Mistake: Forgetting range(5) means 0-4, Forgetting i+=1 in while.", "Data processing, Automation, Web scraping."),
        ("Python", "Functions"): ("Python Functions means code block created with def keyword. def add(a,b): return a+b - means function that adds two numbers. In Python functions are very flexible - args means all arguments in tuple, kwargs means key-value in dict, lambda means small function in one line. Function means organizing code and using again and again. return means sending value out of function. Without return, function gives None.", "Without functions you cannot manage big code. In Python everything is functions + libraries.", "Syntax:\ndef add(a,b):\n return a+b\nprint(add(2,3)) # 5\nadd_lambda = lambda a,b: a+b", "def add(a,b): return a+b\nprint(add(2,3))\nOutput: 5", "add(2,3) -> a=2,b=3 -> return 5 -> print 5.", "When Python function is called, a frame is created in Stack. Parameters, local variables are in it. On return, frame is deleted. Mutable default argument - def f(l=[]) - is a mistake - that list is created only once, if you call again same list comes. That is why we should use def f(l=None).", "Time: O(1) | Space: O(1)", "Reuse, Clean code, Flexible - args, kwargs, lambda.", "Limitation: No type check - if you send wrong type, you know only at runtime.", "Mistake: Mutable default argument - def f(l=[]), Forgetting return -> None comes.", "Calculator, API, Automation, Data."),
        ("Python", "OOP"): ("Python OOP means programming with Class + Object. Class means blueprint, Object means real thing. __init__ means constructor - runs automatically when object is created. self means current object - d.nenu means that object itself. In OOP there are 4 pillars - Encapsulation, Inheritance, Polymorphism, Abstraction - all are easy in Python. With OOP in Python we can make Game, Web App, Automation tools.", "For big projects in Python, OOP is a must. Django, Flask are all on OOP.", "Syntax:\nclass Dog:\n def __init__(self,n):\n  self.name=n\n def bark(self):\n  print(\"Bark\")\nd = Dog(\"Tom\")", "class Dog:\n def __init__(self,n): self.name=n\nd=Dog(\"Tom\")\nOutput: Tom object created", "Dog('Tom') -> __init__ -> self.name='Tom' -> object ready.", "In Python Class is like a dictionary - methods, attributes are all in it. When Object is created, __init__ runs and object gets attributes. self means address of that object. Inheritance means class Dog(Animal) - everything in Animal comes to Dog. In Python Multiple Inheritance is also there.", "Time: O(1) | Space: O(object)", "Real world mapping, Code organized, Reuse, Easy.", "Limitation: Private means no big protection - _name is only convention, Speed a little less.", "Mistake: Forgetting self, Wrong spelling of __init__ - writing _init_.", "Game, Web apps, Automation."),
        ("Python", "Libraries"): ("Python Libraries means ready-made code packets. We can take them with pip install and use without writing again. Pandas means handling Data like Excel table - DataFrame. Numpy means numbers, arrays - fast calculations. Matplotlib means graphs - showing data visually. Because of Libraries, Python became this popular. Data Science means 90% Libraries - Pandas, Numpy, Scikit-learn, TensorFlow.", "Without Libraries you cannot do Data Science in Python. For jobs, Libraries are a must.", "Syntax:\nimport pandas as pd\ndf = pd.DataFrame({'a':[1,2]})\nprint(df)", "import pandas as pd\ndf=pd.DataFrame({'a':[1,2]})\nOutput: Table with a column - 1, 2", "pandas import -> DataFrame created -> table.", "Inside Pandas DataFrame there are Numpy arrays. That is why it is fast. DataFrame means rows + columns - like Excel sheet. Numpy array means like C array in continuous memory, that is why it is 100x fast. With Matplotlib we can directly make graph from DataFrame.", "Time: O(n) | Space: O(n)", "Ready code, Data analysis fast, Less code, Big community.", "Limitation: If library version is wrong, code breaks, Too many libraries make app big.", "Mistake: Importing without installing library, Confusing pandas vs numpy, pip vs pip3.", "Data Science, ML, AI, Automation."),
        ("Python", "File Handling"): ("Python File Handling means reading/writing data in file. with open() is best way - it opens file, after work it automatically closes. Modes - r means read, w means write, a means append. Large file should not be read at once, should be read line by line - for line in f: - means memory saved. With File Handling we can do Logs, Data save, Config files. In Python File Handling is very simple - in 2 lines it finishes.", "To save data, File Handling is a must. In Automation work is with Files.", "Syntax:\nwith open(\"a.txt\",\"r\") as f:\n print(f.read())\nwith open(\"a.txt\",\"w\") as f:\n f.write(\"Hi\")", "with open(\"a.txt\",\"r\") as f: print(f.read())\nOutput: File content - Hi", "open -> read -> auto close.", "with means Context Manager - it opens file, after block it automatically closes. f.read() means reading whole file at once - dangerous for big file. f.readline() means one line, for line in f means line by line - best. In w mode if file is not there it is created, if it is there old data is deleted.", "Time: O(n) | Space: O(file)", "Auto close, Safe, Simple, Less code.", "Limitation: If you read large file at once, memory becomes full, For binary files different mode needed - rb, wb.", "Mistake: Deleting old data with w mode, Reading large file with read() at once, Forgetting close() - should use with.", "Logs, Data save, Automation, Config."),
        ("Python", "Django"): ("Django is No.1 full web framework in Python. Full means - Database, Admin, Login, Security - all are in Django. In Django MVT pattern - Model means Database table, View means Logic, Template means HTML. In Django Admin Panel comes automatically - to manage data. Flask means micro - for small, Django means full - for big websites. Instagram, parts of YouTube are with Django. If you learn Django, you can make full website alone.", "If you want Python job in Web Development, Django is a must. Django + Python means full stack.", "Syntax:\npython manage.py runserver\n# Server start - http://127.0.0.1:8000", "python manage.py runserver\nOutput: Server on 8000 - Website opens", "runserver -> Django starts -> 8000 port -> website opens.", "In Django when request comes - URL -> View -> Model (DB) -> Template (HTML) -> Response. ORM means Object Relational Mapping - we can write DB queries in Python code, no need to write SQL. Migrations means updating table in DB - makemigrations + migrate. In Admin panel we can directly see data, change it.", "Time: O(request) | Space: O(app)", "Full package, Secure, Fast, Admin ready.", "Limitation: For small things it feels big, Learning curve more, Less for Real-time apps - Channels needed.", "Mistake: Forgetting Migrations - makemigrations + migrate, Not adding app in settings, Putting SECRET_KEY in GitHub.", "E-commerce, Blog, College site, Instagram."),
        ("Python", "Projects"): ("Python Projects means combining everything you learnt - Basics, OOP, Libraries, Django - and making a real app. To-Do App - tasks add/remove, Weather App - weather from API, Expense Tracker - money track, Chatbot - answers to questions, Face Detection - face with OpenCV. With projects, theory and practical get linked. In interviews they ask about project - what did you do, which library did you use, what problem came. If GitHub has Projects, resume becomes very strong.", "For placement, Projects are a must. Without projects there is nothing in resume.", "Structure:\nTo-Do - list add/remove + file save\nWeather - API + Tkinter / Django", "Project: To-Do - add 'Study'\nOutput: List has 'Study' added - Saved in File", "Add -> list -> save file -> show.", "To make project, first Idea - start small. Then Design - what features. Then Code - step by step. Then Testing - all cases. Finally put in GitHub and write README about what you did. In interview questions come from that README.", "Time: O(n) | Space: O(n)", "Resume, Practical learning, GitHub strong, Interview story.", "Limitation: Takes time, Without planning becomes messy.", "Mistake: Making project and not putting in GitHub, Not writing README, Copy-paste without understanding.", "Resume, Placement, GitHub."),
        ("SQL", "SELECT"): ("SELECT means seeing data in Database, taking it. In Database, Table is like Excel sheet - rows + columns. SELECT name, avg FROM students means take name, avg columns from students table. WHERE means filter - avg > 70 means only those with more than 70. ORDER BY means sort - by avg from high to low. LIMIT means only top N. Without SELECT you cannot do anything in Database - all queries start with SELECT.", "In SQL 90% queries are SELECT. Reports, Dashboard are all SELECT.", "Syntax:\nSELECT name, avg FROM students\nWHERE avg > 70\nORDER BY avg DESC\nLIMIT 5;", "SELECT name, avg FROM students WHERE avg>70;\nOutput: Students with more than 70 - name + avg", "Table scan -> WHERE filter -> ORDER BY sort -> Result.", "SQL Query is parsed by Database Engine, it creates Execution Plan. If Index is there, it searches fast with Index, otherwise full table scan. WHERE filters first, ORDER BY sorts later. LIMIT gives only top N at end. That is why we should not use SELECT *, we should ask only needed columns - fast + memory saved.", "Time: O(n) without index, O(log n) with index | Space: O(result)", "Easy, Powerful filtering, Reports fast.", "Limitation: If data is more, it becomes slow - Index needed, For complex queries JOINs needed.", "Mistake: Using SELECT * - slow, Using == instead of = in WHERE, Forgetting ;.", "Reports, Dashboard, App data."),
        ("SQL", "JOINS"): ("JOIN means combining two tables and taking as one result. Example students table has student details, placements table has placement details. If we combine both, we know which student got placement. INNER JOIN means only matching in both tables. LEFT JOIN means all in left table, if matching in right it comes, otherwise NULL. RIGHT JOIN means opposite. FULL JOIN means all in both tables. Without JOINs you cannot do anything in real Database.", "In real Database, Tables join with JOINs only. In interviews, JOINs questions are compulsory.", "Syntax:\nSELECT s.name FROM students s\nLEFT JOIN placements p ON s.id=p.student_id\nWHERE p.student_id IS NULL; // Not placed", "SELECT s.name FROM students s LEFT JOIN placements p ON s.id=p.student_id WHERE p.student_id IS NULL;\nOutput: Not placed students", "students 100, placements 70 -> LEFT -> 100 rows -> WHERE filter -> not placed 30.", "In JOIN, ON means telling on which column to join - s.id = p.student_id. Database first keeps small table in memory, searches in big table - Hash Join / Nested Loop. If Index is there, JOIN is fast. If you forget ON, Cartesian Product - 100*70=7000 rows - wrong result.", "Time: O(n*m) without index, O(n log n) with index", "Tables together give full data, Real reports.", "Limitation: Wrong JOIN gives wrong data, Too many JOINs make it slow.", "Mistake: Forgetting ON condition - Cartesian product, Confusing LEFT vs INNER, Confusing USING vs ON.", "Student + Placement report, E-commerce Order + Customer."),
        ("SQL", "GROUP BY"): ("GROUP BY means grouping rows and giving one result for each group. Example if we want College wise students count - GROUP BY college. COUNT(*) means how many in group, SUM() means total, AVG() means average, MAX() means biggest. HAVING means filter after grouping - WHERE means filter before grouping. Without GROUP BY we cannot make summary reports. Example College wise, Branch wise, Year wise reports are all with GROUP BY.", "For reports GROUP BY is a must. In interviews WHERE vs HAVING difference is compulsory.", "Syntax:\nSELECT college, COUNT(*) FROM students\nGROUP BY college\nHAVING COUNT(*)>10;", "SELECT college, COUNT(*) FROM students GROUP BY college HAVING COUNT(*)>10;\nOutput: College wise count >10 - College A 50, College B 30", "Rows grouped -> COUNT -> HAVING filter.", "Database first sorts / hashes rows by GROUP BY column and groups them. Then for each group it calculates aggregate function - COUNT, SUM. Then with HAVING it filters groups. WHERE filters rows before grouping. That is why we should not use aggregate in WHERE, we should use in HAVING.", "Time: O(n log n) | Space: O(groups)", "Summary reports fast, Analysis easy.", "Limitation: Column not in GROUP BY cannot be used in SELECT, Too many groups make it slow.", "Mistake: Using aggregate in WHERE - should use HAVING, Using column in SELECT that is not in GROUP BY, Using COUNT in WHERE instead of HAVING.", "College wise report, Sales per month, Branch wise."),
        ("SQL", "Subqueries"): ("Subquery means one Query inside another Query. Result of inside Query is used for outside Query. Example if we want students with more marks than Average - inside we calculate AVG, outside we compare with it. In Subquery IN means in list, EXISTS means check if it exists. With Subquery we can write complex logic simply, step by step. But in big tables, JOIN is generally faster than Subquery.", "To write complex logic step by step, Subquery is easy. In interviews they ask Subquery vs JOIN difference.", "Syntax:\nSELECT name FROM students\nWHERE avg > (SELECT AVG(avg) FROM students);", "SELECT name FROM students WHERE avg > (SELECT AVG(avg) FROM students);\nOutput: Students with more than Average", "INNER avg calculated -> OUTER compared -> result.", "Database first runs INNER query and takes result, then uses it in OUTER query. Correlated Subquery means INNER query changes based on OUTER query row - for each row INNER runs - slow. Non-Correlated means only once - fast. EXISTS means only checks if row exists, does not take value - fast.", "Time: O(n) to O(n^2) correlated | Space: O(1)", "Complex logic simple, Step by step, Readable.", "Limitation: Correlated Subquery slow, Takes more time than JOIN, Debugging difficult.", "Mistake: If Subquery has many rows, should use IN instead of =, Using Correlated Subquery too much - should use JOIN.", "Top students, Filter, Exists check."),
        ("SQL", "Indexing"): ("Indexing means making searching in Database fast. Like Index in Book - without searching 500 pages, we see page number in Index and go directly. In Database also, if Index is there, without scanning full table, it searches in B-Tree and goes directly to row. Search goes from O(n) to O(log n). Example to search one student in 1 lakh rows, without Index we have to see 1 lakh, with Index it is found in 17 steps. But if we put too many Indexes, INSERT, UPDATE become slow - because Index also must be updated.", "In Large Database without Index app becomes slow. In interviews Index is compulsory - B-Tree, O(n) vs O(log n).", "Syntax:\nCREATE INDEX idx_avg ON students(avg);\nSELECT * FROM students WHERE avg = 90; // Fast", "CREATE INDEX idx_avg ON students(avg);\nOutput: Search becomes fast - even in 1 lakh it is fast", "Index created -> B-Tree -> Search in tree.", "Inside Index there is B-Tree - Balanced Tree. It searches from Root to Leaf. In Leaf there is address of row. That is why O(log n). Columns with Index - WHERE, JOIN, ORDER BY are all fast. But on INSERT we have to update Table + Index both - that is why slow. Index on Low cardinality - like Gender - column is waste.", "Search: O(log n) | Insert: O(log n) + overhead", "Search super fast, JOIN fast, ORDER BY fast.", "Limitation: INSERT/UPDATE slow, More storage, Should not give Index to all columns.", "Mistake: Giving Index to all columns - INSERT slow, Index on low cardinality column waste, Using SELECT * even with Index.", "Large tables - 1 lakh rows, E-commerce Search, Banking."),
        ("SQL", "Normalization"): ("Normalization means organizing data in Database cleanly, without redundancy. Redundancy means repeating same data again and again - example writing same student's college name in all rows. With Normalization we divide data into tables and store only once. 1NF means in one cell only one value - 'Python,Java' in one cell is wrong, make separate rows. 2NF means no Partial Dependency, 3NF means no Transitive Dependency. With Normalization, Update is easy, Storage saved, Data consistent.", "For Database Design, Normalization is a must. In interviews 1NF, 2NF, 3NF are compulsory.", "Syntax:\n1NF: One cell one value\n'Python,Java' wrong -> Row1 Python, Row2 Java\n2NF: Full dependency, 3NF: No transitive", "1NF Example: 'Python,Java' -> Row1 Python, Row2 Java\nOutput: Clean table - No repeat", "Split -> Separate rows -> Redundancy reduced.", "In Normalization we divide Tables - Students table, Colleges table - College name only once in Colleges table. In Students table only College ID. With JOIN we get full data. Over-Normalization means too many tables - too many JOINs - Query slow. That is why sometimes we do Denormalization - a little redundancy - for performance.", "Time: O(n) | Space: Saved - Redundancy reduced", "Data clean, Update easy, Storage saved, Consistent.", "Limitation: Over-normalization means too many JOINs, Query slow, Design complex.", "Mistake: Over-normalization - too many JOINs, Query slow, Forgetting 1NF - values with comma.", "Student DB, E-commerce, Banking - all Normalized."),
        ("SQL", "Procedures"): ("Stored Procedure means SQL code saved in Database. Query we do again and again can be saved once as Procedure and called again and again with CALL. Example if we want to see Top 5 students again and again - save that query in Procedure and CALL get_top() is enough. Function has return value, Procedure has no return - but with OUT parameter it can give value. With Procedures, code reuse, Security - user can be given Procedure access without table access, Speed - pre-compiled.", "In Reports, Banking, Procedures are used more. In interviews Procedure vs Function difference is asked.", "Syntax:\nCREATE PROCEDURE get_top()\nBEGIN SELECT * FROM students ORDER BY avg DESC LIMIT 5; END;\nCALL get_top();", "CALL get_top();\nOutput: Top 5 students - Name + Avg", "CALL -> Procedure runs -> Top 5 returned.", "When Procedure is saved in Database, it is compiled and stored. When we CALL, it runs directly - no need to parse - that is why fast. In Procedure we can use Variables, IF, Loops, Cursor. DELIMITER means to tell end of Procedure with different symbol like $$, instead of ; inside Procedure.", "Time: O(n log n) | Space: O(n)", "Reuse, Security, Speed - Pre-compiled, Less network traffic.", "Limitation: Code changes with Database - MySQL vs Oracle, Debugging difficult, Version control difficult.", "Mistake: Forgetting DELIMITER for ; handling in Procedure, Putting too much business logic in Procedure.", "Reports, Banking, Daily jobs."),
        ("SQL", "Projects"): ("SQL Projects means combining everything you learnt - SELECT, JOINS, GROUP BY, Indexing, Procedures - and designing a real Database. Example Student DB - students, placements, results tables. E-Commerce DB - customers, orders, products. Hospital DB - patients, doctors, appointments. In Project first ER Diagram - which tables, which relations - then Tables created, Data inserted, Queries - JOINs, Procedures. With Project you learn Database Design. In interviews they ask about Project - how did you make ER Diagram, which tables, how did you do Normalization.", "For Database job, Project is a must. Without Project you cannot get job in SQL.", "Structure:\nTables: students, placements, results\n+ JOINS + Procedures + Indexing", "Project: Student DB - students + placements JOIN\nOutput: Placed / Not placed report - 70 placed, 30 not placed", "Tables created -> Data inserted -> JOIN -> Report.", "In Project first Requirement - what data is needed. Then ER Diagram - Entities, Relations - One-to-Many, Many-to-Many. Then Normalization - up to 3NF. Then Tables - Primary Key, Foreign Key. Then Indexing - Search fast. Finally Queries - Reports, Procedures. Put ER Diagram + SQL file in GitHub.", "Time: O(n) | Space: O(n)", "Learn real DB design, Resume strong, Interview story.", "Limitation: Without planning becomes messy, Takes time.", "Mistake: Direct tables without ER Diagram, Without Foreign Key, Forgetting Indexing.", "Resume, Placement, GitHub."),
        ("DSA", "Arrays"): ("Array is No.1 important topic in DSA. Data in Array is in continuous memory, that is why it can be accessed in O(1). In DSA there are 4 main techniques on Arrays - Two Pointers means searching from both ends, Sliding Window means moving a window and searching, Prefix Sum means storing sum till now and getting fast answer, HashMap means storing value with index and searching in O(1). Two Sum, Max Subarray, Trapping Rain Water are all Arrays. In interviews 50% problems are from Arrays.", "Arrays are base for DSA. Without Arrays you cannot go forward in DSA.", "Syntax:\ndef two_sum(arr,t):\n seen={}\n for i, x in enumerate(arr):\n  if t-x in seen: return [seen[t-x], i]\n  seen[x]=i", "def two_sum(arr,t): seen={} # O(n) HashMap\nExample: arr=[2,7,11,15], t=9 -> [0,1] - 2+7=9", "seen={} -> see 2 -> need 7 not there -> store 2 -> see 7 -> 2 is there -> return [0,1].", "In Brute Force there are two loops - O(n^2) - we check every pair. In HashMap there is one loop - O(n) - for every value we check if needed value is in HashMap. Inside HashMap there is hash table, that is why searching is O(1). We exchanged Space for Time - Trade-off. In interviews they ask to go from Brute to Optimal.", "Time: Brute O(n^2) -> HashMap O(n) | Space: O(n)", "Fast, Interview No.1 pattern, Base for all DSA.", "Limitation: More space - HashMap, If we sort, original order is lost.", "Mistake: Starting with Brute O(n^2) and stopping there, Confusing index vs value in HashMap.", "Two Sum, Search, Max Subarray, Sorting."),
        ("DSA", "Linked List"): ("Linked List is Data Structure with Nodes connected like a chain. Every Node has two things - data + address of next Node. It is not continuous like Array - it can be anywhere, connected with next. In Array size is fixed, in Linked List size is dynamic - we can add anywhere. In Linked List Reverse, Detect Loop - Floyd Tortoise-Hare - Slow 1 step, Fast 2 steps - if they meet, loop is there, Middle Find, Merge - are all important problems. If you learn Linked List, Pointers and Dynamic Memory become clear.", "With Linked List, Pointers + Dynamic Memory become clear. In interviews Linked List questions are compulsory.", "Syntax:\nReverse: prev=None, curr=head\nwhile curr:\n nxt = curr.next\n curr.next = prev\n prev = curr\n curr = nxt", "Reverse: prev=None, curr=head\nExample: 1->2->3 becomes 3->2->1", "prev None, curr 1 -> 1.next=None -> prev 1, curr 2 -> 2.next=1 -> prev 2, curr 3 -> 3.next=2 -> head 3.", "In Linked List if we forget next, chain is cut. That is why in reverse we first save next in nxt. In Floyd, Slow 1, Fast 2 - if Fast is in loop, it will meet Slow - because Fast moves faster. In Linked List Search is O(n) - we have to see one by one from start. Insert at Head is O(1) - but in Array it is O(n).", "Time: Reverse O(n) | Space: O(1) | Search O(n)", "Dynamic size, Insert O(1) at head, No memory waste.", "Limitation: Search O(n), No random access - like arr[5], Extra memory - next pointer.", "Mistake: Overwriting next without saving - list cut, Not updating Head, Forgetting NULL check.", "Playlist, Browser history, Undo, LRU Cache."),
        ("DSA", "Stack & Queue"): ("Stack means LIFO - Last In First Out. Last put comes first. Example plates stack - plate put on top is taken first. Push means putting, Pop means taking. Queue means FIFO - First In First Out. First put comes first. Example Ticket Queue - who came first gets ticket first. Enqueue means putting, Dequeue means taking. With Stack - Undo, Bracket Check, Next Greater Element. With Queue - BFS, Level Order, Sliding Window.", "Stack & Queue are very easy, but used in many problems. In interviews, questions from Stack are easy.", "Syntax:\nStack: push(10), pop()->10\nQueue: enqueue(10), dequeue()->10\nPython: stack=[], stack.append(10), stack.pop()", "Stack: push(10), push(20), pop()\nOutput: 20 (Last in First out) - 20 came last, went first", "push 10 -> push 20 -> pop -> 20 comes (top).", "Inside Stack there is Array / Linked List. Top pointer tracks last element. Push means Top++, Pop means Top--. In Queue there are Front + Rear - two pointers. In Circular Queue when Rear goes to end it comes to start - space not wasted. With Stack we can also simulate Recursion - Function Call Stack is also Stack.", "Time: O(1) push/pop/enqueue/dequeue | Space: O(n)", "Simple, Fast O(1), Perfect for Undo/BFS.", "Limitation: In Stack we cannot directly see middle element, In Queue we cannot see last.", "Mistake: Using Queue logic in Stack, Pop in empty stack - underflow, Push in full stack - overflow.", "Undo, Bracket check, BFS, Printer Queue."),
        ("DSA", "Trees"): ("Tree is hierarchical Data Structure - like Branches from Root. Root means starting, Leaf means ending - node with no children. In Tree every Node has one Parent, can have many Children. In Binary Tree max 2 Children, in BST - Binary Search Tree - Left has smaller, Right has bigger - that is why Inorder gives sorted. In Tree Traversals - Inorder Left-Root-Right, Preorder Root-Left-Right, Postorder Left-Right-Root. BFS means Queue with Level by Level, DFS means Stack/Recursion with Deep. With Tree we represent File System, Org Chart, HTML DOM.", "If you learn Tree, Recursion becomes strong. In interviews many problems are from Tree.", "Syntax:\nInorder: Left -> Root -> Right\nPreorder: Root -> Left -> Right\nPostorder: Left -> Right -> Root", "Inorder: Left -> Root -> Right\nExample: BST [4,2,6] Inorder -> 2 4 6 (sorted)", "Root 4 -> Left 2 -> print 2 -> Root 4 -> Right 6 -> 2 4 6.", "In BST Search starts from Root - if needed value is smaller than Root go Left, if bigger go Right. In every step half data goes - that is why O(log n). In Tree Recursion means - Node + Left Subtree + Right Subtree - same problem smaller. Base Case means NULL node - should stop. Height means longest path from Root to Leaf.", "Time: Search O(log n) avg, O(n) worst | Space: O(h) height", "Sorted data, Fast search, Perfect for Hierarchical data.", "Limitation: In worst case it becomes like Linked List - Skewed Tree, Must balance - AVL, Red-Black.", "Mistake: Not knowing how to handle duplicate in BST, Forgetting Recursion base case - infinite, Confusing Inorder vs Preorder.", "File system, Org chart, HTML DOM, Database Index."),
        ("DSA", "Graphs"): ("Graph is Data Structure with Nodes + Edges. Nodes mean Cities, Edges mean Roads. Tree is a special Graph - no Cycle, Connected. In Graph Cycle can be there, Disconnect can also be there. To represent Graph, Adjacency List is best - for each Node, list of which Nodes it is connected to. BFS means Queue - Shortest Path - Level by Level. DFS means Stack/Recursion - Deep - Cycle Detection, Topological Sort. Dijkstra means Weighted Shortest Path - shortest route in Google Maps. With Graph - Friends Suggestion, Maps, Network.", "If you learn Graph, Maps, Social Networks become clear. In interviews Graph means advanced level.", "Syntax:\nBFS: Put start in Queue, mark visited, add neighbours\nDFS: Recursion - visit, DFS for neighbours", "BFS: Start A -> Queue [A] -> visit A -> neighbours B,C add -> visit B -> visit C\nOutput: A B C - Level order", "A visit -> B,C queue -> B visit -> D queue -> C visit -> ...", "In Graph if we do not mark visited, we fall in infinite loop in Cycle - going again and again to same nodes. In BFS Queue - node that came first is visited first - that is why Shortest Path. In DFS Stack - we go deep in one path. In Dijkstra Priority Queue - we take node with smallest distance first. In Adjacency Matrix memory is V*V - waste for big graph, in List it is only V+E.", "BFS/DFS: Time O(V+E) | Space O(V)", "Shortest path, Connections, Real world - Maps, Networks.", "Limitation: Complex, Debugging difficult, More representation - Matrix vs List.", "Mistake: Infinite loop without marking visited, Adjacency Matrix waste for big graph, Confusing Weighted vs Unweighted.", "Google Maps, Friends suggestion, Network, Flight routes."),
        ("DSA", "Sorting"): ("Sorting means putting data in order - small to big or big to small. Bubble Sort means comparing two neighbours and sending big to end - O(n^2) - slow, but easy. Merge Sort means Divide and Conquer - dividing array into two, sorting, joining - O(n log n) - stable - order of same values does not change. Quick Sort means picking Pivot, small left, big right - avg O(n log n), worst O(n^2) - in-place - no extra memory needed. Without Sorting we cannot search fast - Binary Search needs Sorted array.", "Sorting is base in DSA. In interviews Sorting algorithms + Time Complexity are compulsory.", "Syntax:\nQuick: pivot pick, small left, big right, repeat\nMerge: divide, sort, merge", "Quick: [3,1,2] pivot 3 -> [1,2] left, [] right -> [1,2,3]\nOutput: 1 2 3", "Pivot 3 -> 1,2 left -> sort left -> 1,2,3.", "In Merge Sort we divide array into half, again half, till one element. Then we join two sorted arrays while sorting - Merge. In Quick Sort we put Pivot in correct place - Partition. How we pick Pivot decides Quick Sort speed - Random Pivot is best. In Python sort() means Timsort - Merge + Insertion combined - O(n log n).", "Merge O(n log n) | Quick avg O(n log n), worst O(n^2) | Bubble O(n^2)", "Data organized, Search fast, Leaderboard, Analysis.", "Limitation: Bubble slow, Quick worst case slow, Merge needs extra memory.", "Mistake: In Quick worst pivot - first element pivot in sorted array, Forgetting extra space in Merge, Confusing Stable vs Unstable.", "Leaderboard, Search, E-commerce Sort by Price."),
        ("DSA", "DP"): ("DP means Dynamic Programming. Topic that scares everyone, but concept is very simple - Without solving same subproblem again and again, solve once and store it. Example Fibonacci - fib(5) needs fib(4) + fib(3), fib(4) needs fib(3) + fib(2) - fib(3) is calculated twice. In DP we calculate fib(3) once and store it, no need to calculate again. In DP two ways - Memoization means Recursion + Store, Tabulation means Table from bottom to top. With DP we can do Knapsack, LCS, Longest Palindrome. DP means Recursion + Memo.", "DP means Hard level in Interview. If DP comes, even FAANG becomes easy.", "Syntax:\ndp[0]=0, dp[1]=1\ndp[i]=dp[i-1]+dp[i-2]\n# Tabulation - bottom to top", "Fibonacci: dp[0]=0, dp[1]=1, dp[2]=1, dp[3]=2, dp[4]=3, dp[5]=5\nOutput: 5 - fib(5)=5", "dp[2]=dp[1]+dp[0]=1 -> dp[3]=1+1=2 -> dp[4]=2+1=3 -> dp[5]=3+2=5.", "In Recursion same calls come again and again - In Recursion Tree fib(3) twice, fib(2) three times. In DP we store those calls - Time goes from O(2^n) to O(n). For DP two properties are needed - Overlapping Subproblems - same problem should come again, Optimal Substructure - answer of big problem should come from small. Only if both are there we should use DP, otherwise Greedy / Divide and Conquer.", "Recursion O(2^n) -> DP O(n) | Space O(n) -> O(1) optimized", "Slow problem becomes fast, Hard problems become easy.", "Limitation: Table needs memory, If state is not defined correctly it becomes wrong, Difficult for beginners.", "Mistake: Wrong DP table size, Forgetting Base case, Using DP even without Overlapping, Confusing Recursion + Memo vs Tabulation.", "Fibonacci, Knapsack, LCS, Coin Change, Longest Palindrome."),
        ("DSA", "Greedy"): ("Greedy means picking best option visible now at every step. Without thinking about future, taking best in present. Example Activity Selection - sorting by End time, picking without overlapping gives max activities. Coin Change - starting from big coin, taking more coins gives min coins. Greedy is simple, fast - O(n log n) - but does not work everywhere. In Knapsack Greedy fails - there DP is needed. We should check with proof whether Greedy works or not.", "Greedy means solving easy problems fast. In interviews they ask Greedy vs DP difference.", "Syntax:\nActivity: Sort by end time, pick without overlapping\nCoin: Start from big coin, take more", "Activity: Sort by end time -> pick first -> next non-overlapping pick -> repeat\nOutput: Max activities", "Sort by end -> pick 1st -> 2nd overlap skip -> 3rd pick.", "In Greedy at every step we pick Local Best. In Activity, small End time means chance for more activities - that is why sort by end. In Coin, big coin means less coins - that is why from big. But in 0/1 Knapsack, even if we sort by Value/Weight, we cannot take half item - that is why Greedy fails - DP needed. If Greedy is correct, there should be proof - Exchange Argument.", "Time: O(n log n) sort + O(n) | Space: O(1)", "Simple, Fast, Optimal for some problems, Less code.", "Limitation: Does not work everywhere, Should not use without proof, Local best != Global best sometimes.", "Mistake: Thinking Greedy works everywhere - In Knapsack Greedy fails, DP needed, Using Greedy without sorting.", "Activity, Coin, Huffman, Fractional Knapsack, Meeting Rooms."),
    }
    if (skill, topic) in articles:
        intro, why, syntax, example, dry, deep, comp, adv, disadv, mistake, use = articles[(skill, topic)]
    else:
        intro = f"{topic} is a very important topic in {skill}."
        why = f"If you learn {topic}, you will become strong in {skill}."
        syntax = f"# {topic} in {skill}"
        example = f"print('{topic} - {skill}')"
        dry = f"Input -> Process {topic} -> Output."
        deep = f"You should understand what happens inside {topic}."
        comp = "Time: O(n) | Space: O(1)"
        adv = f"With {topic}, code becomes fast and clean."
        disadv = "Limitation: Without practice it will not be clear."
        mistake = "Mistake: Reading only theory without practice."
        use = f"In real projects, {topic} is used daily."
    html = ""
    html += f"<h2 style='color:#fef08a;margin-top:0;'>{topic} in {skill} - Complete Notes</h2>"
    html += f"<div class='diag'>Topic: {topic} | Skill: {skill} | Level: Beginner to Advanced | Full Detailed Notes</div>"
    html += f"<div class='cat'>1. Definition - Full Explanation</div><p style='color:white;line-height:2.0;font-size:15px;'>{intro}</p>"
    html += f"<div class='cat'>2. Why Learn This?</div><p style='color:white;line-height:1.9;'>{why}</p>"
    html += f"<div class='cat'>3. Syntax</div><div class='qbox' style='color:white;white-space:pre-wrap;'>{syntax}</div>"
    html += f"<div class='cat'>4. Example + Output</div><div class='qbox' style='color:white;white-space:pre-wrap;'>{example}</div>"
    html += f"<div class='cat'>5. Dry Run - Step by Step</div><div class='abox'>{dry}</div>"
    html += f"<div class='cat'>6. Deep Dive - What Happens Inside?</div><p style='color:white;line-height:1.9;'>{deep}</p>"
    html += f"<div class='cat'>7. Time & Space Complexity</div><div class='abox'>{comp}</div>"
    html += f"<div class='cat'>8. Advantages</div><p style='color:white;line-height:1.9;'>{adv}</p>"
    html += f"<div class='cat'>9. Disadvantages / Limitations</div><p style='color:white;line-height:1.9;'>{disadv}</p>"
    html += f"<div class='cat'>10. Common Mistakes - Do Not Do These!</div><p style='color:#fca5a5;line-height:1.9;'>{mistake}</p>"
    html += f"<div class='cat'>11. Real World Uses</div><p style='color:white;line-height:1.9;'>{use}</p>"
    html += f"<div class='cat'>12. Practice Questions</div><p style='color:white;'>1. Write 3 basic programs on {topic}<br>2. Write 2 medium problems on {topic}<br>3. Explain {topic} without seeing notes - in 2 mins<br>4. Write {topic} code in 5 mins - Time challenge<br>5. Give one real example of {topic}</p>"
    html += f"<div class='cat'>13. Interview Questions</div><p style='color:white;'>1. Explain {topic} with example?<br>2. What is Time Complexity of {topic}?<br>3. Write code for {topic} without library?<br>4. What is common mistake in {topic}?<br>5. Where did you use {topic} in real project?<br>6. Difference between {topic} and similar topic?</p>"
    return html
def get_interview_content(skill, topic=""):
    # All Skills - Interview Bank - 100% English, No external brand name
    bank = {
        ("C", "Pointers"): [
            ("Easy: What is a pointer?", "Pointer is a variable that stores address of another variable. Example int *p = &a."),
            ("Easy: Difference between *p and p?", "p is address, *p is value at that address."),
            ("Easy: What is NULL pointer?", "Pointer that points to nothing. If you dereference it, program crashes."),
            ("Medium: What is dangling pointer?", "Pointer pointing to memory that is already freed. Using it gives garbage or crash."),
            ("Medium: malloc vs calloc?", "malloc takes 1 arg size, memory not initialized. calloc takes 2 args n,size, memory initialized to 0."),
            ("Medium: What is pointer to pointer?", "Pointer that stores address of another pointer. int **pp = &p;"),
            ("Hard: What is memory leak?", "When you allocate memory and forget to free it, memory is lost till program ends."),
            ("Hard: Explain segmentation fault?", "When program tries to access memory it does not have permission for. Example dereferencing NULL."),
            ("Tricky: int *p; *p = 10; What happens?", "Undefined behaviour. p is uninitialized, it points to random address. May crash."),
            ("HR: Why are pointers difficult?", "Because you manage memory directly. One mistake can crash. But they give full control and speed."),
        ],
        ("C", "Arrays"): [
            ("Easy: What is array?", "Collection of same type values in continuous memory. Index starts from 0."),
            ("Medium: Why array access is O(1)?", "Because address is calculated directly with formula Base + index*size."),
            ("Medium: Array vs Pointer?", "Array name is constant pointer to first element. You can do arr+1 but not arr++."),
            ("Hard: What is out of bounds?", "Accessing arr[10] when size is 5. Gives garbage, may crash. C does not check bounds."),
            ("Tricky: How to find size of array?", "sizeof(arr)/sizeof(arr[0]). In function this does not work because array decays to pointer."),
        ],
        ("C", "Loops"): [
            ("Easy: What is loop?", "Loop repeats same work. for loop when count is known, while when condition based, do-while runs at least once."),
            ("Medium: for vs while?", "for is best when iterations are known. while is best when condition based."),
            ("Hard: What is infinite loop?", "Loop that never ends because condition never becomes false. Example forgetting i++."),
            ("Tricky: Why semicolon after for is dangerous?", "for(i=0;i<5;i++); - body becomes separate, loop runs empty."),
        ],
        ("DSA", "DP"): [
            ("Easy: What is DP?", "Dynamic Programming. Solve subproblem once, store it, reuse it. Recursion + Memo = DP."),
            ("Easy: Memoization vs Tabulation?", "Memoization = Top-down, Recursion + Cache. Tabulation = Bottom-up, Table from 0 to n."),
            ("Medium: When to use DP?", "When 2 conditions: Overlapping Subproblems + Optimal Substructure. Both must be there."),
            ("Medium: Fibonacci with DP?", "dp[0]=0, dp[1]=1, dp[i]=dp[i-1]+dp[i-2]. Recursion O(2^n) becomes DP O(n)."),
            ("Hard: DP vs Greedy?", "Greedy picks local best, may fail. DP checks all possibilities and picks global best. Knapsack Greedy fails, DP works."),
            ("Tricky: Can DP always be optimized to O(1) space?", "Not always. If dp[i] depends only on last 1-2 values, yes. If it depends on all previous, no."),
        ],
        ("DSA", "Arrays"): [
            ("Easy: What is Two Sum?", "Find two numbers that add to target. Brute O(n^2), HashMap O(n)."),
            ("Medium: Two Pointers technique?", "Use two pointers from both ends. Best for sorted array, pair sum, palindrome."),
            ("Medium: Sliding Window?", "Maintain a window and move it. Best for max subarray, longest substring."),
            ("Hard: How to optimize Brute to Optimal?", "First write brute, find repeated work, use HashMap or sorting to optimize."),
        ],
        ("Python", "Django"): [
            ("Easy: What is Django?", "Full web framework in Python. MVT - Model View Template. Admin, Auth, ORM are built-in."),
            ("Easy: Django vs Flask?", "Flask is micro, only core. Django is full, everything built-in. Small project - Flask, Big project - Django."),
            ("Medium: What is ORM?", "Object Relational Mapping. You write Python code, Django converts to SQL."),
            ("Medium: What are Migrations?", "makemigrations creates migration file, migrate applies it to DB."),
            ("Medium: What is MVT?", "Model = Database table, View = Logic, Template = HTML. Request goes URL -> View -> Model -> Template."),
            ("Hard: How to optimize Django queries?", "Use select_related for ForeignKey, prefetch_related for ManyToMany, avoid N+1 query problem."),
        ],
        ("Java", "OOP"): [
            ("Easy: What are 4 pillars of OOP?", "Encapsulation, Inheritance, Polymorphism, Abstraction."),
            ("Easy: Class vs Object?", "Class is blueprint, Object is real thing created from blueprint."),
            ("Medium: Overloading vs Overriding?", "Overloading = same name different params, compile time. Overriding = child rewrites parent method, runtime."),
            ("Hard: Why Java does not support multiple inheritance?", "To avoid Diamond Problem. It uses Interface instead - class can implement many interfaces."),
        ],
        ("SQL", "JOINS"): [
            ("Easy: What is JOIN?", "Combining 2 tables into one result using common column. ON tells how to join."),
            ("Easy: INNER vs LEFT?", "INNER = only matching in both. LEFT = all in left + matching in right, else NULL."),
            ("Medium: What is Cartesian Product?", "When you forget ON, every row joins with every row. 100*70=7000 rows. Wrong result."),
            ("Hard: JOIN vs Subquery?", "JOIN is generally faster, DB can optimize. Subquery is easier to read for complex logic."),
        ],
    }

    if (skill, topic) in bank:
        qa = bank[(skill, topic)]
    else:
        qa = [
            (f"Easy: What is {topic}?", f"{topic} is a core concept in {skill}. {topic} is used to solve real problems and write clean code."),
            (f"Easy: Why do we use {topic}?", f"We use {topic} to make code fast, clean and reusable. Without {topic}, {skill} projects become messy."),
            (f"Easy: Give one real example of {topic}?", f"In a real {skill} project, {topic} is used daily to build features faster."),
            (f"Medium: How does {topic} work inside?", f"Inside {topic}, input is taken, logic is applied, output is given. If you understand this flow, you can explain in interview."),
            (f"Medium: What is Time Complexity of {topic}?", f"Depends on implementation. Always try to go from Brute Force to Optimal. Explain trade-off between Time and Space."),
            (f"Medium: {topic} vs similar topic?", f"Compare {topic} with similar concept in {skill}. Tell difference in use case, speed, memory, and when to use which."),
            (f"Medium: Advantages of {topic}?", f"Advantages: Fast, Reusable, Clean code, Less bugs, Easy to test."),
            (f"Medium: Disadvantages of {topic}?", f"If used in wrong place, {topic} can make code slow or complex. Always check use case."),
            (f"Hard: Write code for {topic} without library?", f"Write from scratch without built-in functions. Interviewer checks if you know logic, not just library."),
            (f"Hard: How to optimize {topic}?", f"First write brute force, then find repeated work, then use better data structure to optimize."),
            (f"Hard: Explain {topic} to a 10 year old?", f"Use simple real life example. If you can explain simply, you really understand {topic}."),
            (f"Tricky: What is common mistake in {topic}?", f"Common mistake: Only reading theory, not practicing. Second: Copy-paste without understanding. Third: Not doing dry run."),
            (f"Tricky: Where did you use {topic} in real project?", f"Always prepare one project story: Problem -> Used {topic} -> Result. Interviewer loves real stories."),
            (f"HR: Why should we hire you for {skill}?", f"I know {skill} with {topic} clearly, I have built projects, I can write code and explain it. I learn fast."),
        ]

    html = ""
    html += f"<h2 style='color:#fef08a;margin-top:0;'>Interview Questions - {topic} in {skill}</h2>"
    html += f"<div class='diag'>Total Questions: {len(qa)} | Easy + Medium + Hard + HR + Tricky | {skill} - {topic}</div>"
    html += f"<div class='cat'>Interview Preparation - How to Answer?</div><p style='color:white;line-height:1.9;'>Rule: 1. Define in 1 line &nbsp; 2. Give Example &nbsp; 3. Tell Time Complexity &nbsp; 4. Tell Real Use. If you follow this, every answer becomes perfect.</p>"
    for i, (q, a) in enumerate(qa, 1):
        level = "Easy" if "Easy" in q else "Medium" if "Medium" in q else "Hard" if "Hard" in q else "Tricky / HR"
        html += f"<div class='cat'>Q{i}. {q}</div>"
        html += f"<p style='color:#a7f3d0;line-height:1.9;'><b>Level:</b> {level}<br><b>Answer:</b> {a}</p>"
        html += f"<p style='color:white;line-height:1.9;'><b>Tip:</b> Do not just say definition. Always add one example of {topic} and one real project use.</p>"
    html += f"<div class='cat'>Rapid Revision - 5 Minutes Before Interview</div><p style='color:white;'>1. Define {topic} in 10 seconds<br>2. Write code for {topic} without seeing<br>3. Tell Time Complexity<br>4. Tell 1 mistake + 1 real use<br>5. Tell {topic} vs similar topic difference</p>"
    html += f"<div class='cat'>HR Questions - For Every Topic</div><p style='color:white;'>1. Tell me about yourself?<br>2. Why {skill}?<br>3. What is your best project and why?<br>4. What will you do if you get stuck?<br>5. Where do you see yourself in 2 years?</p>"
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
            
            topic = st.session_state.get("selected_topic", "") 
            content = get_interview_content(skill, topic)
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
