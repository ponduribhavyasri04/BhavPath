
import streamlit as st
import pandas as pd
import random
import datetime

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = "QIS College"
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
    html = ""
    html += "<h2 style='color:#fef08a;margin-top:0;'>" + topic + " in " + skill + "</h2>"
    html += "<div class='diag'><b>Quick Diagram: " + topic + " Memory</b><br>Addr 1000: Val1=10 | Addr 1004: Val2=20 | Addr 1008: Val3=30 | Addr 1012: Val4=40<br>Flow: Start -> Init i=0 -> Check i < n? -> Yes -> Execute -> i++ -> Loop -> No -> Exit</div>"
    html += "<div class='cat'>Introduction to " + topic + "</div>"
    html += "<p><b>What is " + topic + "?</b> " + topic + " is fundamental concept in " + skill + " that allows you to handle data efficiently. It is backbone of problem solving.</p>"
    html += "<p><b>Why Learn " + topic + "?</b> Every major company like TCS, Infosys, Wipro, Amazon, Google asks at least 2-3 questions from " + topic + ". In BhavPath project, " + topic + " handles 1 lakh records.</p>"
    html += "<div class='cat'>Detailed Explanation</div>"
    html += "<p><b>Definition:</b> " + topic + " in " + skill + " is defined as technique that provides structured way to store, access, manipulate, iterate over data.</p>"
    html += "<p><b>Working Principle:</b> When you declare variable or collection for " + topic + ", memory allocated in RAM. Array of 4 ints takes 16 bytes contiguous. Base address stored, access via index: Address = Base + (index * size). Gives O(1) random access.</p>"
    html += "<div class='cat'>Types of " + topic + "</div>"
    html += "<div class='qbox'><b>1. Basic " + topic + ":</b> Simple syntax, easy for beginners. TCS easy level. Example for i in range 5 print i. Time O(n) Space O(1).</div>"
    html += "<div class='qbox'><b>2. Intermediate " + topic + ":</b> Nested loops, combination with conditions and functions. Medium-level TCS NQT. Example For i in range(n): For j in range(m): print(i,j). Time O(n^2).</div>"
    html += "<div class='qbox'><b>3. Advanced / Optimized " + topic + ":</b> Designed for large data 10^6 elements. Uses list comprehension, generators, sliding window, hashing. Optimized to O(n log n) or O(n). Used in Amazon Google.</div>"
    html += "<div class='cat'>Code Examples - 5 Levels</div>"
    html += "<div class='qbox'><b>Level 1 Beginner:</b><br>var = 10<br>print var<br>Output 10</div>"
    html += "<div class='qbox'><b>Level 4 Placement Level:</b><br>def find_max arr:<br>&nbsp;&nbsp;max_val = arr 0<br>&nbsp;&nbsp;for x in arr:<br>&nbsp;&nbsp;&nbsp;&nbsp;if x > max_val:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_val = x<br>&nbsp;&nbsp;return max_val<br>Time O(n)</div>"
    html += "<div class='qbox'><b>Level 5 FAANG Optimized O(n) HashMap:</b><br>def two_sum arr target:<br>&nbsp;&nbsp;seen = dict<br>&nbsp;&nbsp;for i val in enumerate arr:<br>&nbsp;&nbsp;&nbsp;&nbsp;if target - val in seen:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return [seen[target-val], i]<br>&nbsp;&nbsp;&nbsp;&nbsp;seen[val] = i<br>&nbsp;&nbsp;return -1</div>"
    return html

def get_interview_content(skill):
    html = ""
    html += "<div class='cat'>Top Interview Questions - " + skill + "</div>"
    html += "<div class='diag'>Quick Diagram: Stack - Local vars | Heap - Objects malloc | Code - Text segment</div>"
    if skill == "C":
        html += "<div class='qbox'><b>Q1. What is pointer? Why use pointer? Explain pointer to pointer with diagram.</b></div><div class='abox'><b>Answer:</b> Pointer stores address. int a=10 at addr 1000. int *p = &a p stores 1000 at 2000. *p is value at address =10. Why use? 1 Dynamic memory malloc 2 Pass large data without copy 3 Build Linked List. Code int a=10; int *p=&a; printf percent d *p prints 10. Diagram a 1000=10 p 2000=1000 pp 3000=2000. Always init as NULL to avoid wild. TCS asks 90 percent times.</div>"
        html += "<div class='qbox'><b>Q2. Array vs Pointer? Explain size difference?</b></div><div class='abox'><b>Answer:</b> Array continuous fixed size int arr 5 =20 bytes sizeof arr 20. Pointer stores address of first element. Array name is constant pointer cannot be reassigned.</div>"
    elif skill == "Python":
        html += "<div class='qbox'><b>Q1. List vs Tuple?</b></div><div class='abox'><b>Answer:</b> List mutable, Tuple immutable.</div>"
        html += "<div class='qbox'><b>Q2. What is GIL?</b></div><div class='abox'><b>Answer:</b> Global Interpreter Lock - only one thread executes bytecode at a time.</div>"
    elif skill == "Java":
        html += "<div class='qbox'><b>Q1. Why Java platform independent?</b></div><div class='abox'><b>Answer:</b> Compiles to bytecode, runs on JVM any OS.</div>"
        html += "<div class='qbox'><b>Q2. == vs equals?</b></div><div class='abox'><b>Answer:</b> == reference, equals content.</div>"
    elif skill == "SQL":
        html += "<div class='qbox'><b>Q1. WHERE vs HAVING?</b></div><div class='abox'><b>Answer:</b> WHERE filters rows before GROUP BY, HAVING filters groups after.</div>"
        html += "<div class='qbox'><b>Q2. INNER vs LEFT JOIN?</b></div><div class='abox'><b>Answer:</b> INNER only matching, LEFT left full + matching.</div>"
    else:
        html += "<div class='qbox'><b>Q1. Two Sum O(n)?</b></div><div class='abox'><b>Answer:</b> HashMap seen dict, O(n) time.</div>"
        html += "<div class='qbox'><b>Q2. Stack vs Queue?</b></div><div class='abox'><b>Answer:</b> Stack LIFO, Queue FIFO.</div>"
    return html

TOPICS_MAP = {
    "C": ["Loops", "Arrays", "Pointers", "Strings", "Functions", "Structures"],
    "Python": ["Loops", "Lists", "Functions", "Strings", "Dictionaries"],
    "Java": ["OOP", "Strings", "Collections"],
    "SQL": ["Joins", "GROUP BY"],
    "DSA": ["Arrays", "Linked List", "Stack & Queue", "Trees"]
}

# ---------- WELCOME ----------
if st.session_state.page == "welcome":
    st.markdown("<div class='center'><h1 style='font-size:55px;'>BhavPath 🚀</h1><p>Your Placement Journey - Learn, Practice, Get Placed</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='glass center'>", unsafe_allow_html=True)
    st.session_state.college = st.selectbox("Select College", ["QIS College", "Other College"])
    if st.button("Start Learning ➜", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- HOME ----------
elif st.session_state.page == "home":
    st.markdown(f"<div class='center'><h1>BhavPath - {st.session_state.college}</h1></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📚 Technical Skills", use_container_width=True):
            st.session_state.page = "skills"
            st.rerun()
    with c2:
        if st.button("🧪 Test Zone", use_container_width=True):
            st.session_state.page = "test"
            st.rerun()
    with c3:
        if st.button("🔮 Prediction", use_container_width=True):
            st.session_state.page = "prediction"
            st.rerun()

# ---------- SKILLS ----------
elif st.session_state.page == "skills":
    c1, c2 = st.columns([1, 5])
    with c1:
        if st.button("⬅ Back", key="skills_back"):
            st.session_state.page = "home"
            st.rerun()
    with c2:
        st.markdown("### 📚 Technical Skills")
    st.session_state.selected_skill = st.selectbox("Select Skill", ["C", "Python", "Java", "SQL", "DSA"])
    topics = TOPICS_MAP.get(st.session_state.selected_skill, ["Loops"])
    st.session_state.topic = st.selectbox("Select Topic", topics)
    if st.button("View Details", use_container_width=True):
        st.session_state.page = "detail"
        st.rerun()
    st.markdown(get_interview_content(st.session_state.selected_skill), unsafe_allow_html=True)

# ---------- DETAIL ----------
elif st.session_state.page == "detail":
    c1, c2 = st.columns([1, 5])
    with c1:
        if st.button("⬅ Back", key="detail_back"):
            st.session_state.page = "skills"
            st.rerun()
    with c2:
        st.markdown(f"### {st.session_state.topic} - {st.session_state.selected_skill}")
    st.markdown(f"<div class='detail-box'>{get_detailed_content(st.session_state.selected_skill, st.session_state.topic)}</div>", unsafe_allow_html=True)

# ---------- TEST ----------
elif st.session_state.page == "test":
    st.markdown("### 🧪 Test Zone")
    st.session_state.test_skill = st.selectbox("Select Skill for Test", ["C", "Python", "Java", "SQL", "DSA"])
    if st.button("Start Weekly Test"):
        st.session_state.test_questions = get_weekly_random_questions(st.session_state.test_skill, 10)
        st.session_state.test_answers = {}
        st.session_state.test_submitted = False
        st.rerun()
    if st.session_state.test_questions:
        for i, q in enumerate(st.session_state.test_questions):
            st.markdown(f"<div class='qbox'><b>Q{i+1}. {q['q']}</b></div>", unsafe_allow_html=True)
            st.session_state.test_answers[i] = st.radio(f"Select - Q{i+1}", q["options"], key=f"test_q_{i}", index=None)
        if st.button("Submit Test", use_container_width=True):
            st.session_state.test_submitted = True
            st.rerun()
    if st.session_state.test_submitted and st.session_state.test_questions:
        score = 0
        for i, q in enumerate(st.session_state.test_questions):
            chosen = st.session_state.test_answers.get(i)
            if chosen is not None and q["options"].index(chosen) == q["ans"]:
                score += 1
            st.markdown(f"<div class='abox'><b>Q{i+1}:</b> {q['q']}<br><b>Correct:</b> {q['options'][q['ans']]}<br><b>Exp:</b> {q['exp']}</div>", unsafe_allow_html=True)
        st.success(f"Your Score: {score} / {len(st.session_state.test_questions)}")

# ---------- PREDICTION - OKKATE CHANGE IKKADA ----------
elif st.session_state.page == "prediction":
    st.markdown("### 🔮 Prediction")
    cgpa = st.slider("CGPA", 5.0, 10.0, 7.5)
    tenth = st.slider("10th %", 40, 100, 85)
    inter = st.slider("Inter %", 40, 100, 85)
    btech = st.slider("BTech %", 40, 100, 80)
    skills = st.multiselect("Skills Known", ["C", "Python", "Java", "SQL", "DSA"], default=["Python"])
    if st.button("Predict", use_container_width=True):
        avg_marks = (tenth + inter + btech) / 3
        skill_score = len(skills) * 8
        chance = int((cgpa / 10) * 40 + (avg_marks / 100) * 40 + skill_score)
        chance = min(chance, 98)
        st.session_state.pred_chance = chance
        st.session_state.pred_skills = skills
        st.session_state.pred_tenth = tenth
        st.session_state.pred_inter = inter
        st.session_state.pred_btech = btech
    if 'pred_chance' in st.session_state:
        chance = st.session_state.pred_chance
        st.markdown(f"### Company List - {chance}%")
        df_comp = pd.DataFrame(
            [("Google / Amazon", "75%+"), ("TCS Digital", "70%+"), ("Wipro", "65%+")],
            columns=["Company", "Eligibility"]
        )
        st.dataframe(df_comp, use_container_width=True, hide_index=True)
        df_chart = pd.DataFrame(
            {"Subject": ["10th", "BTech", "Inter"], "Marks": [st.session_state.pred_tenth, st.session_state.pred_btech, st.session_state.pred_inter]}
        )
        st.bar_chart(df_chart.set_index("Subject"))
        if chance >= 80:
            st.success("High chance - Keep practicing mock interviews")
        elif chance >= 60:
            st.info("Medium chance - Focus on DSA + 1 project")
        else:
            st.info("Need improvement - Start with C + Python basics daily")
    # KINDHA - BACK + HOME PAKKA PAKKANA - IDHE OKKATE CHANGE
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Back", use_container_width=True, key="pred_back_bottom"):
            st.session_state.page = "home"
            st.rerun()
    with c2:
        if st.button("🏠 Home", use_container_width=True, key="pred_home_bottom"):
            st.session_state.page = "welcome"
            st.rerun()
