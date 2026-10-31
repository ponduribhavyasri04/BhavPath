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
.code{background:#0f0f0f;border:1px solid #333;border-radius:8px;padding:12px;margin:10px 0;color:#00ff88;font-family:monospace;font-size:13px;white-space:pre-wrap}
.test-card{background:linear-gradient(135deg,#0d1a3a,#1a0a2a);border:2px solid #0d4aff;border-radius:15px;padding:20px;margin:15px 0;}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_current_week():
    today = datetime.date.today()
    return today.isocalendar()[1]  # Week number 1-52

def get_test_questions_pool():
    pool = {
        "C": [
            {"q": "What is size of int in C (64-bit)?", "options": ["2 bytes", "4 bytes", "8 bytes", "16 bytes"], "ans": 1, "exp": "int is 4 bytes in 64-bit compiler. Pointer is 8 bytes."},
            {"q": "What is pointer? What does int *p store?", "options": ["Value of variable", "Address of variable", "Garbage value", "NULL always"], "ans": 1, "exp": "Pointer stores address of variable. int *p=&a stores address of a."},
            {"q": "Which is correct for malloc?", "options": ["malloc(4) returns zero init", "malloc needs 2 args", "malloc returns void* need cast", "malloc 1 arg size uninitialized"], "ans": 3, "exp": "malloc takes 1 arg size, returns uninitialized memory. calloc zero init."},
            {"q": "What is dangling pointer?", "options": ["Points to NULL", "Points to freed memory", "Points to garbage random", "Points to stack"], "ans": 1, "exp": "Dangling points to freed memory. After free(p), p becomes dangling. Set p=NULL."},
            {"q": "Array vs Linked List - Which has O(1) random access?", "options": ["Linked List", "Array", "Both", "None"], "ans": 1, "exp": "Array has O(1) random access via index. Linked List O(n) access needs traversal."},
            {"q": "What is output? int a=5/2; printf(\"%d\",a);", "options": ["2.5", "2", "3", "Error"], "ans": 1, "exp": "5/2 integer division gives 2, not 2.5. 5.0/2 gives 2.5 float."},
            {"q": "Which storage class keeps value between function calls?", "options": ["auto", "register", "static", "extern"], "ans": 2, "exp": "static keeps value between calls. static int count=0 remembers."},
            {"q": "What is segmentation fault?", "options": ["Memory leak", "Accessing not owned memory", "Stack overflow", "Infinite loop"], "ans": 1, "exp": "Segfault is accessing memory you don't own - NULL dereference, dangling, out of bounds."},
            {"q": "How to reverse string without library?", "options": ["Use strrev()", "Two pointers i=0 j=len-1 swap", "Use recursion only", "Not possible"], "ans": 1, "exp": "Two pointers i=0 j=len-1 swap till i<j. O(n) time O(1) space."},
            {"q": "What is structure padding? struct {char a; int b;} size?", "options": ["5 bytes", "6 bytes", "8 bytes", "4 bytes"], "ans": 2, "exp": "char 1 + padding 3 + int 4 = 8 due to 4-byte alignment. Wipro asks."},
            {"q": "Which loop ensures at least one execution?", "options": ["for", "while", "do-while", "None"], "ans": 2, "exp": "do-while checks condition after body, ensures at least one execution."},
            {"q": "Binary search time complexity?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "ans": 1, "exp": "Binary search O(log n) needs sorted array. Linear O(n)."},
            {"q": "Quick Sort worst case?", "options": ["O(n log n)", "O(n^2)", "O(n)", "O(log n)"], "ans": 1, "exp": "Quick Sort worst O(n^2) when pivot is smallest/largest always. Avg O(n log n)."},
            {"q": "What does free(p) do?", "options": ["Deletes pointer", "Releases memory pointed by p", "Sets p to NULL", "Nothing"], "ans": 1, "exp": "free releases memory. Pointer p still exists dangling. Set p=NULL after free."},
            {"q": "Which is correct for string? char str[] = \"Hello\"; What is last char?", "options": ["o", "NULL", "\\0", "o with \\0 after"], "ans": 3, "exp": "String automatically ends with \\0. Hello has H e l l o \\0. strlen 5 but array size 6."},
        ],
        "Python": [
            {"q": "List vs Tuple - Which is mutable?", "options": ["List mutable Tuple immutable", "Both mutable", "Both immutable", "List immutable"], "ans": 0, "exp": "List mutable can change. Tuple immutable cannot change, faster, hashable."},
            {"q": "What is output? my_list=[1,2,2,3] len(set(my_list))?", "options": ["4", "3", "2", "1"], "ans": 1, "exp": "set removes duplicates. [1,2,2,3] -> {1,2,3} len 3."},
            {"q": "What are args and kwargs?", "options": ["args tuple kwargs dict", "args dict kwargs tuple", "Both list", "Both dict"], "ans": 0, "exp": "args is tuple for positional unlimited, kwargs dict for keyword."},
            {"q": "What is decorator in Python?", "options": ["Wraps function adds behavior", "Deletes function", "Creates class", "Loop"], "ans": 0, "exp": "Decorator wraps function adds behavior without modifying. @login_required example."},
            {"q": "What is GIL in Python?", "options": ["Global Interpreter Lock - one thread executes bytecode", "Garbage collector", "Global variable", "Loop"], "ans": 0, "exp": "GIL only one thread executes Python bytecode at a time. CPU-bound threading not faster."},
            {"q": "Which is faster? List comprehension or for loop with append?", "options": ["For loop", "List comprehension faster", "Same speed", "While loop"], "ans": 1, "exp": "List comprehension faster because loop runs in C, not Python bytecode."},
            {"q": "What is output? [x*x for x in range(5) if x%2==0]?", "options": ["[0,1,4,9,16]", "[0,4,16]", "[0,2,4]", "[1,9]"], "ans": 1, "exp": "x%2==0 gives 0,2,4 squares 0,4,16."},
            {"q": "Shallow copy vs deep copy?", "options": ["Shallow copies reference only, deep copies full", "Both same", "Shallow deep", "Deep reference"], "ans": 0, "exp": "Shallow copies top level only inner mutable shared. Deep copy copies full recursively."},
            {"q": "What does with open() do?", "options": ["Auto closes file", "Deletes file", "Creates file only", "Nothing"], "ans": 0, "exp": "with open auto closes file even after exception. Best practice."},
            {"q": "Which is correct for Two Sum O(n)?", "options": ["Brute force O(n^2)", "HashMap O(n) seen dict", "Sort O(n log n)", "Binary search"], "ans": 1, "exp": "Two Sum HashMap O(n) time O(n) space. seen dict stores value->index, check target-val in seen."},
            {"q": "What is output? s=\"BhavPath\" s[::-1]?", "options": ["BhavPath", "htaPvahB", "PathBhav", "Error"], "ans": 1, "exp": "s[::-1] reverses string. BhavPath -> htaPvahB."},
            {"q": "First non-repeating char in BhavPath?", "options": ["B", "h", "a", "P"], "ans": 0, "exp": "B appears once, h appears once? Actually B first non-repeating. Counter needed."},
            {"q": "What is lambda?", "options": ["Anonymous function lambda x: x+10", "Named function", "Class", "Loop"], "ans": 0, "exp": "Lambda is anonymous function. lambda x: x+10 adds 10."},
            {"q": "Django vs Flask?", "options": ["Flask micro Django full batteries", "Both same", "Django micro", "Flask full"], "ans": 0, "exp": "Flask micro simple small API, Django full framework with ORM admin auth."},
            {"q": "What is output? bool([]) bool([0])?", "options": ["True True", "False True", "True False", "False False"], "ans": 1, "exp": "Empty list bool False, non-empty list even with 0 True."},
        ],
        "Java": [
            {"q": "Why Java platform independent?", "options": ["Compiles to bytecode runs on JVM any OS", "Compiles to machine code", "Needs recompile per OS", "Not independent"], "ans": 0, "exp": "Java bytecode runs on JVM any OS WORA. C++ needs recompile."},
            {"q": "String vs StringBuilder? Which faster for loop 10000 concat?", "options": ["String faster", "StringBuilder faster", "Same", "StringBuffer fastest"], "ans": 1, "exp": "String immutable creates 10000 objects waste. StringBuilder mutable 1 object faster."},
            {"q": "ArrayList vs LinkedList - O(1) random access?", "options": ["ArrayList O(1) get", "LinkedList O(1) get", "Both O(1)", "None"], "ans": 0, "exp": "ArrayList dynamic array O(1) get. LinkedList O(n) get needs traversal."},
            {"q": "How HashMap works internally?", "options": ["hashCode to bucket index", "Linear search", "Binary search", "Sort"], "ans": 0, "exp": "HashMap hashCode to bucket index hash & n-1. Collision linked list after 8 tree."},
            {"q": "What is == vs equals in Java?", "options": ["== reference equals content", "Both same", "== content equals reference", "None"], "ans": 0, "exp": "== checks reference same object, equals checks content same. String pool example."},
            {"q": "What is overloading vs overriding?", "options": ["Overloading compile time same name diff params, overriding runtime child redefines parent", "Both same", "Overloading runtime", "Overriding compile"], "ans": 0, "exp": "Overloading same class diff params compile time. Overriding child redefines parent runtime."},
            {"q": "Interface vs Abstract class?", "options": ["Abstract can have concrete + abstract methods single inheritance, Interface only abstract multiple implements", "Both same", "Interface single", "Abstract multiple"], "ans": 0, "exp": "Abstract class abstract+concrete single extends. Interface only abstract Java8 default multiple implements."},
            {"q": "What is exception handling? finally always executes?", "options": ["Yes finally always executes even after return", "No never", "Only if exception", "Only if no exception"], "ans": 0, "exp": "finally always executes even after return, used to close DB connection."},
            {"q": "What is multithreading? How to create thread?", "options": ["extends Thread or implements Runnable", "Only extends Thread", "Only Runnable", "Not possible"], "ans": 0, "exp": "Create by extends Thread or implements Runnable second better."},
            {"q": "What is singleton pattern?", "options": ["Only one object exists like DB connection", "Many objects", "No objects", "Abstract"], "ans": 0, "exp": "Singleton only one object exists like DB connection config. Private constructor static instance."},
            {"q": "JDBC steps order?", "options": ["Load driver -> Connection -> Statement -> ResultSet -> Close", "Connection -> Load", "Statement -> Connection", "Random"], "ans": 0, "exp": "JDBC Load driver Class.forName, Connection DriverManager.getConnection, Statement createStatement, ResultSet executeQuery, close."},
            {"q": "What is final finally finalize?", "options": ["final variable cannot change, finally always executes, finalize called by GC", "All same", "final method", "finalize variable"], "ans": 0, "exp": "final variable cannot change method cannot override class cannot extend, finally always executes, finalize GC before delete."},
            {"q": "What is Collections? List vs Set vs Map?", "options": ["List ordered duplicate, Set unique, Map key-value", "All same", "List unique", "Set ordered duplicate"], "ans": 0, "exp": "List ordered duplicate allows index, Set unique no duplicate, Map key-value."},
            {"q": "What is Spring Boot? DI?", "options": ["Dependency Injection Spring creates object injects", "Manual new object", "No injection", "Spring not used"], "ans": 0, "exp": "DI IoC Spring creates injects Autowired instead of new. Loose coupling."},
            {"q": "What is garbage collection? Mark and sweep?", "options": ["JVM auto deletes unused objects mark reachable sweep unreachable", "Manual free", "No GC", "C style"], "ans": 0, "exp": "GC auto deletes unused objects mark and sweep. Generations Young Old."},
        ],
        "SQL": [
            {"q": "WHERE vs HAVING difference?", "options": ["WHERE filters rows before GROUP BY, HAVING filters groups after", "Both same", "WHERE after HAVING before", "No difference"], "ans": 0, "exp": "WHERE filters rows before GROUP BY cannot use aggregate, HAVING filters groups after can use COUNT."},
            {"q": "Which JOIN returns only matching rows both tables?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "ans": 0, "exp": "INNER only matching both. LEFT all left + matching right. RIGHT opposite. FULL both all."},
            {"q": "What is index? Why use?", "options": ["Speeds search O(n) to O(log n) B-Tree", "Slows search", "No use", "Deletes data"], "ans": 0, "exp": "Index speeds search O(n) to O(log n) like book index B-Tree. Without index full scan 1 sec with index 0.01 sec."},
            {"q": "What is normalization? 1NF?", "options": ["Atomic values no array in cell", "Non-atomic", "Duplicate", "None"], "ans": 0, "exp": "1NF atomic no array in cell. 2NF no partial dependency. 3NF no transitive."},
            {"q": "Subquery vs JOIN which faster generally?", "options": ["JOIN faster optimizer uses index", "Subquery faster", "Same", "Subquery always"], "ans": 0, "exp": "JOIN generally faster optimizer uses index subquery per row correlated slow."},
            {"q": "What is primary key?", "options": ["Unique not null one per table", "Can be duplicate", "Can be null", "Many per table"], "ans": 0, "exp": "Primary key unique not null one per table id. Foreign key references other table."},
            {"q": "What is ACID? Atomicity?", "options": ["All or nothing transaction", "Partial", "No guarantee", "Only one"], "ans": 0, "exp": "ACID Atomicity all or nothing, Consistency valid state, Isolation concurrent don't interfere, Durability persists."},
            {"q": "ROW_NUMBER vs RANK vs DENSE_RANK?", "options": ["ROW_NUMBER unique 1 2 3 4, RANK same rank gaps 1 1 3, DENSE_RANK no gaps 1 1 2", "All same", "ROW_NUMBER gaps", "RANK unique"], "ans": 0, "exp": "ROW_NUMBER unique sequential, RANK same rank gaps, DENSE_RANK same rank no gaps."},
            {"q": "Write query second highest salary without LIMIT?", "options": ["SELECT MAX(salary) WHERE salary < (SELECT MAX(salary))", "SELECT MIN", "SELECT COUNT", "SELECT *"], "ans": 0, "exp": "Second highest without LIMIT SELECT MAX salary WHERE salary < (SELECT MAX salary). With LIMIT LIMIT 1 OFFSET 1."},
            {"q": "How to find duplicate emails?", "options": ["SELECT email COUNT GROUP BY email HAVING COUNT>1", "SELECT DISTINCT", "SELECT WHERE", "SELECT ORDER BY"], "ans": 0, "exp": "Duplicate SELECT email COUNT FROM students GROUP BY email HAVING COUNT>1."},
            {"q": "LEFT JOIN to find not placed students query?", "options": ["SELECT s.name FROM students s LEFT JOIN placements p ON s.id=p.student_id WHERE p.student_id IS NULL", "INNER JOIN", "RIGHT JOIN", "CROSS JOIN"], "ans": 0, "exp": "Not placed LEFT JOIN WHERE p.student_id IS NULL. INNER only matching would not show not placed."},
            {"q": "UNION vs UNION ALL?", "options": ["UNION removes duplicate UNION ALL keeps duplicate faster", "Both same", "UNION ALL removes", "UNION keeps"], "ans": 0, "exp": "UNION combines removes duplicate, UNION ALL keeps duplicate faster."},
            {"q": "What is NULL? NULL=NULL?", "options": ["Unknown NULL=NULL false use IS NULL", "True", "False always", "Error"], "ans": 0, "exp": "NULL unknown NULL=NULL false. Use IS NULL. COUNT(*) counts all COUNT(col) counts non-NULL."},
            {"q": "Stored Procedure vs Function?", "options": ["Procedure can have IN OUT no return mandatory transactions, Function must return single value", "Both same", "Function no return", "Procedure must return"], "ans": 0, "exp": "Procedure IN OUT params no return mandatory can have transactions CALL. Function must return single value SELECT."},
            {"q": "What is window function? PARTITION BY?", "options": ["ROW_NUMBER OVER PARTITION BY college ORDER BY avg DESC groups", "No grouping", "Only ORDER BY", "No window"], "ans": 0, "exp": "Window functions ROW_NUMBER OVER PARTITION BY college ORDER BY avg DESC. Top 3 per college WHERE rn<=3."},
        ],
        "DSA": [
            {"q": "Two Sum O(n) solution uses?", "options": ["HashMap seen dict", "Brute O(n^2)", "Sort", "Binary search"], "ans": 0, "exp": "Two Sum HashMap O(n) time O(n) space. seen stores value->index check target-val in seen."},
            {"q": "Reverse Linked List iterative time?", "options": ["O(n) time O(1) space", "O(n^2)", "O(log n)", "O(1)"], "ans": 0, "exp": "Reverse iterative prev=None curr=Head while curr next=curr.next curr.next=prev prev=curr curr=next Head=prev O(n) time O(1) space."},
            {"q": "Detect loop in Linked List uses?", "options": ["Floyd tortoise hare slow 1 fast 2", "Linear search", "Binary search", "HashMap only"], "ans": 0, "exp": "Floyd tortoise hare slow 1 fast 2 if meet loop exists. Find start move one to head both 1 step meet at start."},
            {"q": "Stack vs Queue?", "options": ["Stack LIFO push pop Queue FIFO enqueue dequeue", "Both LIFO", "Both FIFO", "Stack FIFO"], "ans": 0, "exp": "Stack LIFO Last In First Out browser back undo recursion. Queue FIFO First In First Out printer BFS."},
            {"q": "Tree inorder traversal order?", "options": ["Left Root Right - BST sorted", "Root Left Right", "Left Right Root", "Right Left Root"], "ans": 0, "exp": "Inorder Left Root Right BST sorted order. Preorder Root Left Right copy tree. Postorder Left Right Root delete tree."},
            {"q": "BFS vs DFS? BFS uses?", "options": ["Queue level by level shortest path", "Stack", "Recursion only", "No queue"], "ans": 0, "exp": "BFS uses queue level by level shortest path unweighted. DFS uses stack recursion deep path."},
            {"q": "Quick Sort vs Merge Sort? Quick Sort worst?", "options": ["Quick worst O(n^2) avg O(n log n) in-place, Merge always O(n log n) stable O(n) extra", "Both same", "Quick always O(n log n)", "Merge O(n^2)"], "ans": 0, "exp": "Quick Sort avg O(n log n) worst O(n^2) in-place fast. Merge Sort always O(n log n) stable O(n) extra space."},
            {"q": "Binary search needs?", "options": ["Sorted array O(log n)", "Unsorted", "Random", "Linked List"], "ans": 0, "exp": "Binary search needs sorted array O(log n). low=0 high=n-1 mid=(low+high)//2. 1 lakh elements 17 steps."},
            {"q": "Dynamic Programming Fibonacci memoization vs tabulation?", "options": ["Memo top-down cache dict, Tabulation bottom-up dp array", "Both same", "Memo bottom-up", "Tabulation top-down"], "ans": 0, "exp": "DP memoization top-down cache dict if n in memo return, tabulation bottom-up dp array dp[0]=0 dp[1]=1 for i 2..n dp[i]=dp[i-1]+dp[i-2] O(n)."},
            {"q": "What is Kadane's algorithm for?", "options": ["Maximum subarray sum O(n)", "Minimum subarray", "Sort", "Search"], "ans": 0, "exp": "Kadane max subarray currentSum=max(num, currentSum+num) maxSum=max(maxSum, currentSum) O(n)."},
            {"q": "What is valid parentheses check uses?", "options": ["Stack push opening if closing check top matching pop", "Queue", "Array", "No stack"], "ans": 0, "exp": "Valid parentheses stack push opening if closing check top matching pop else false. O(n)."},
            {"q": "What is LRU cache implementation?", "options": ["Doubly linked list + HashMap O(1) get put", "Array only", "Single linked list", "Stack"], "ans": 0, "exp": "LRU doubly linked list most recent at head HashMap key to node get move to head put add head if capacity exceeded remove tail O(1)."},
            {"q": "What is Dijkstra algorithm for?", "options": ["Shortest path non-negative weights O(E log V) priority queue", "Longest path", "Negative weights", "No weights"], "ans": 0, "exp": "Dijkstra shortest path non-negative weights O(E log V) priority queue distance array. Bellman Ford handles negative."},
            {"q": "What is knapsack 0/1 DP formula?", "options": ["dp[i][w]=max(dp[i-1][w], dp[i-1][w-weight[i]]+value[i])", "dp[i][w]=dp[i-1][w]+weight", "dp[i][w]=value", "No DP"], "ans": 0, "exp": "Knapsack 0/1 max value weight limit dp[i][w]=max(dp[i-1][w], dp[i-1][w-weight[i]]+value[i]) O(n*W)."},
            {"q": "What is LCS Longest Common Subsequence DP?", "options": ["dp[i][j]=dp[i-1][j-1]+1 if same else max(dp[i-1][j], dp[i][j-1])", "dp[i][j]=i+j", "dp[i][j]=0", "No DP"], "ans": 0, "exp": "LCS dp[i][j] if text1[i-1]==text2[j-1] dp[i][j]=dp[i-1][j-1]+1 else max(dp[i-1][j], dp[i][j-1]) O(mn)."},
        ]
    }
    return pool

def get_weekly_random_questions(skill, num_q=10):
    pool = get_test_questions_pool()
    all_q = pool.get(skill, pool["Python"])
    week = get_current_week()
    # Seed with week number so questions change weekly but same within week
    random.seed(week + hash(skill) % 1000)
    selected = random.sample(all_q, min(num_q, len(all_q)))
    # Shuffle options also randomly but keep answer correct
    for q in selected:
        # Create list of (option, is_correct)
        opts = q["options"]
        correct_opt = opts[q["ans"]]
        random.shuffle(opts)
        new_ans = opts.index(correct_opt)
        q["options"] = opts
        q["ans"] = new_ans
    random.seed()  # Reset seed
    return selected

def get_detailed_content(skill, topic):
    html = ""
    html += "<h2 style='color:#fef08a;margin-top:0;'>" + topic + " in " + skill + "</h2>"
    html += "<div class='diag'><b>Quick Diagram: " + topic + " Memory</b><br>Addr 1000: Val1=10 | Addr 1004: Val2=20 | Addr 1008: Val3=30 | Addr 1012: Val4=40<br>Flow: Start -> Init i=0 -> Check i < n? -> Yes -> Execute -> i++ -> Loop -> No -> Exit</div>"
    html += "<div class='cat'>Introduction to " + topic + "</div>"
    html += "<p><b>What is " + topic + "?</b> " + topic + " is fundamental concept in " + skill + " that allows you to handle data efficiently. It is backbone of problem solving in competitive programming and technical interviews.</p>"
    html += "<p><b>Why Learn " + topic + "?</b> Every major company like TCS, Infosys, Wipro, Amazon, Google asks at least 2-3 questions from " + topic + ". In BhavPath project, " + topic + " handles 1 lakh records. Without proper understanding, task that should take 0.01 seconds may take 1 hour.</p>"
    html += "<div class='cat'>Detailed Explanation</div>"
    html += "<p><b>Definition:</b> " + topic + " in " + skill + " is defined as technique that provides structured way to store, access, manipulate, iterate over data. It abstracts low-level memory details.</p>"
    html += "<p><b>Working Principle:</b> When you declare variable or collection for " + topic + ", memory allocated in RAM. Array of 4 ints takes 16 bytes contiguous. Base address stored, access via index: Address = Base + (index * size). Gives O(1) random access. For loops, counter i maintained in stack, condition checked, body executes, counter increments.</p>"
    html += "<div class='cat'>Types of " + topic + "</div>"
    html += "<div class='qbox'><b>1. Basic " + topic + ":</b> Simple syntax, easy for beginners. TCS easy level. Example for i in range 5 print i. Time O(n) Space O(1).</div>"
    html += "<div class='qbox'><b>2. Intermediate " + topic + ":</b> Nested loops, combination with conditions and functions. Medium-level TCS NQT. Example For i in range(n): For j in range(m): print(i,j). Time O(n^2).</div>"
    html += "<div class='qbox'><b>3. Advanced / Optimized " + topic + ":</b> Designed for large data 10^6 elements. Uses list comprehension, generators, sliding window, hashing. Optimized to O(n log n) or O(n). Used in Amazon Google. Example [x*x for x in range(n) if x%2==0] faster.</div>"
    html += "<div class='cat'>Code Examples - 5 Levels</div>"
    html += "<div class='qbox'><b>Level 1 Beginner:</b><br>var = 10<br>print var<br>Output 10</div>"
    html += "<div class='qbox'><b>Level 2 With Condition:</b><br>if var > 5:<br>&nbsp;&nbsp;print Greater<br>else:<br>&nbsp;&nbsp;print Smaller</div>"
    html += "<div class='qbox'><b>Level 3 With Loop:</b><br>for i in range 0 5:<br>&nbsp;&nbsp;print i<br>Output 0 1 2 3 4</div>"
    html += "<div class='qbox'><b>Level 4 Placement Level:</b><br>def find_max arr:<br>&nbsp;&nbsp;max_val = arr 0<br>&nbsp;&nbsp;for x in arr:<br>&nbsp;&nbsp;&nbsp;&nbsp;if x > max_val:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_val = x<br>&nbsp;&nbsp;return max_val<br>Time O(n)</div>"
    html += "<div class='qbox'><b>Level 5 FAANG Optimized O(n) HashMap:</b><br>def two_sum arr target:<br>&nbsp;&nbsp;seen = dict<br>&nbsp;&nbsp;for i val in enumerate arr:<br>&nbsp;&nbsp;&nbsp;&nbsp;if target - val in seen:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return [seen[target-val], i]<br>&nbsp;&nbsp;&nbsp;&nbsp;seen[val] = i<br>&nbsp;&nbsp;return -1</div>"
    html += "<div class='cat'>Common Mistakes</div><p>1 Off-by-one range(n) gives 0 to n-1 not n 2 Infinite loop while True without break 3 Not init variable garbage value 4 Wrong indentation in Python 5 Using = instead of == 6 Ignoring empty list edge case</p>"
    html += "<div class='cat'>Advantages and Use Cases</div><p>Advantages Fast reusable saves lines memory efficient. Use Cases Banking 1 lakh accounts E-commerce listing Social media feed Student management in BhavPath</p>"
    html += "<div class='cat'>Placement Importance</div><p>TCS asks 2 questions on this topic Infosys coding includes this Amazon Google DSA heavily uses this. Mastering gives 20 percent closer to placement.</p>"
    html += "<div class='cat'>Top 10 Interview Questions on " + topic + "</div><p>1 What is " + topic + "? 2 Difference between similar concepts? 3 Internal working memory diagram? 4 Write code without built-in? 5 Optimize for 10^6? 6 Where used in project? 7 Advantages disadvantages? 8 What if fails? 9 Multi-threaded behavior? 10 Design system using " + topic + "?</p>"
    return html

def get_interview_content(skill):
    html = ""
    html += "<div class='cat'>Top Interview Questions - " + skill + " - Detailed with Diagrams</div>"
    html += "<div class='diag'>Quick Diagram: Stack - Local vars | Heap - Objects malloc | Code - Text segment</div>"
    if skill == "C":
        html += "<div class='qbox'><b>Q1. What is pointer? Why use pointer? Explain pointer to pointer with diagram.</b></div><div class='abox'><b>Answer:</b> Pointer stores address. int a=10 at addr 1000. int *p = &a p stores 1000 at 2000. *p is value at address =10. Why use? 1 Dynamic memory malloc 2 Pass large data without copy 3 Build Linked List. Code int a=10; int *p=&a; printf percent d *p prints 10. Diagram a 1000=10 p 2000=1000 pp 3000=2000. Always init as NULL to avoid wild. TCS asks 90 percent times.</div>"
        html += "<div class='qbox'><b>Q2. Array vs Pointer? Explain size difference?</b></div><div class='abox'><b>Answer:</b> Array continuous fixed size int arr 5 =20 bytes sizeof arr 20. Pointer 8 bytes stores address dynamic. Array name constant p++ allowed arr++ error. Example int arr 5; int *p=arr; p++ ok arr++ error. Memory diagram Array 10 20 30 contiguous Linked List Head 10->20->30->NULL scattered.</div>"
        html += "<div class='qbox'><b>Q3. What is dangling pointer? How to avoid?</b></div><div class='abox'><b>Answer:</b> Pointer pointing to freed memory. int *p=malloc 4; free p; Now p dangling using *p crashes segmentation fault. Solution After free set p=NULL. Code free p; p=NULL; if p not equal NULL safe. Prevents crash. Amazon asks.</div>"
        html += "<div class='qbox'><b>Q4. malloc vs calloc vs realloc vs free?</b></div><div class='abox'><b>Answer:</b> malloc 1 arg size uninitialized garbage fast. calloc 2 args count size zero init safe slow. realloc resize existing block. free release memory. Use calloc when need zero init banking 1 lakh accounts zero safe. Code int *p = malloc 100000 * sizeof int; if p==NULL handle; free p; p=NULL; Without free memory leak.</div>"
        html += "<div class='qbox'><b>Q5. Structure vs Union vs padding?</b></div><div class='abox'><b>Answer:</b> Structure all members separate memory sum plus padding for alignment. struct char a int b size not 5 but 8 due 4-byte alignment padding. Union shares same memory size = max member only one active. Use struct for employee full data name age salary, union for value can be int OR float.</div>"
        html += "<div class='qbox'><b>Q6. Storage classes auto static extern register?</b></div><div class='abox'><b>Answer:</b> auto local default garbage scope function lifetime function auto free. static keeps value between calls stays till program ends default 0 scope function lifetime program. extern global across files default 0. register request CPU register fast for loop counters. Example static int count=0; count++ remembers counting function calls.</div>"
        html += "<div class='qbox'><b>Q7. Call by value vs Call by reference? Write swap?</b></div><div class='abox'><b>Answer:</b> Value copies original not changed void func int x x=20 original 10 stays 10. Reference passes address original changes void func int *x *x=20 original becomes 20. Swap needs reference void swap int *a int *b int t=*a; *a=*b; *b=t; Large array pass by reference saves memory copying.</div>"
        html += "<div class='qbox'><b>Q8. String vs char array? Why need backslash 0?</b></div><div class='abox'><b>Answer:</b> char arr 5 Hello not string no backslash 0. char str Hello auto backslash 0 at end char str 6. String functions strlen strcpy need backslash 0 to know end. If forget printf prints garbage till random backslash 0 buffer overflow.</div>"
        html += "<div class='qbox'><b>Q9. Memory leak, segmentation fault, dangling? Prevention?</b></div><div class='abox'><b>Answer:</b> Leak malloc without free loop 1000 times free 1 memory grows. Segfault accessing not owned memory NULL dereference dangling out of bounds arr 10 size 5 stack overflow. Prevention every malloc free NULL check bounds check init pointers. Tool valgrind detects leaks.</div>"
        html += "<div class='qbox'><b>Q10. Null pointer vs Void pointer vs Wild pointer?</b></div><div class='abox'><b>Answer:</b> NULL int *p=NULL points nothing safe to check if p==NULL. Void void *p can point any type need cast int *p = (int*)p. Wild uninitialized int *p points random garbage dangerous. Always init pointer.</div>"
    else:
        html += "<div class='qbox'><b>Q1. List vs Tuple vs Set vs Dict? Explain with diagram and time complexity?</b></div><div class='abox'><b>Answer:</b> List mutable ordered duplicate 1 2 2 O1 access On search use scores 85 90. Tuple immutable ordered 1 2 faster hashable can be dict key use fixed coordinates. Set unordered unique 1 2 O1 search no duplicate use unique skills. Dict key-value a 1 O1 key must be hashable immutable. Frozenset immutable set hashable can be dict key. List for dynamic tuple for fixed set for unique dict for mapping.</div>"
        html += "<div class='qbox'><b>Q2. args vs kwargs? How to use? Unpacking?</b></div><div class='abox'><b>Answer:</b> args tuple positional unlimited def add args sum args call add 1 2 3. kwargs dict keyword def func kwargs for k v in kwargs.items call func name Bhav college QIS. Unpacking list to args my_list 1 2 3 add *my_list. Dict to kwargs my_dict name Bhav func **my_dict. Use when dont know how many args placement function receives. Very common in Django.</div>"
        html += "<div class='qbox'><b>Q3. Decorator Generator Iterator GIL? Write decorator for logging?</b></div><div class='abox'><b>Answer:</b> Decorator wraps function adds behavior without modifying login_required. Code def my_decorator func def wrapper print Before func print After return wrapper. Generator yields one by one saves memory def gen yield 1 yield 2 for large file 1GB not load all for line in open file yield line. Iterator iter next. GIL only one thread executes Python bytecode at a time CPU-bound threading not faster but IO-bound ok use multiprocessing for CPU.</div>"
        html += "<div class='qbox'><b>Q4. OOP in Python? self init inheritance MRO?</b></div><div class='abox'><b>Answer:</b> self current object like this Java. init constructor def init self name self.name=name. Inheritance class Student Person. Multiple inheritance class C A B MRO Method Resolution Order order search parent C A B object uses C3 linearization super calls parent. Overloading Python doesn't support same name different params last defined wins use args to simulate overriding child redefines parent. Code super init calls parent. TCS Digital asks.</div>"
        html += "<div class='qbox'><b>Q5. Reverse string palindrome anagram count vowels first non-repeating remove duplicates?</b></div><div class='abox'><b>Answer:</b> Reverse str slicing or two pointers. Palindrome str==str slicing. Anagram sorted str1==sorted str2 or Counter. Count vowels sum 1 for c in str if c in aeiou. First non-repeating frequency dict then traverse. Remove duplicates without set preserve order result empty result.append x for x in arr if x not in result On2 or dict.fromkeys On. All TCS coding round.</div>"
    return html

def get_default_code(skill):
    if skill == "C":
        return "# Practice - Pointer and Array\na=10\np=id(a)\nprint(a, p)\narr=[10,20,30,40]\nprint(arr)\ns=list(\"BhavPath\")\ni,j=0,len(s)-1\nwhile i<j:\n    s[i],s[j]=s[j],s[i]\n    i+=1; j-=1\nprint(''.join(s))\narr=[10,20,5,30,25]\nmax1=max2=-1\nfor x in arr:\n    if x>max1:\n        max2=max1\n        max1=x\n    elif x>max2 and x!=max1:\n        max2=x\nprint(\"Second largest\", max2)"
    return "# Practice - List vs Dict and Two Sum\nmy_list=[1,2,2,3]\nprint(my_list)\ns=\"BhavPath\"\nfrom collections import Counter\nfreq=Counter(s)\nfor c in s:\n    if freq[c]==1:\n        print(\"First non-repeating\", c)\n        break\ndef two_sum(arr, target):\n    seen={}\n    for i,num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\nprint(two_sum([2,7,11,15], 9))"

# Pages routing
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
        df=pd.DataFrame([["Google/Amazon","75%+"],["TCS Digital","70%+"],["Wipro","65%+"]], columns=["Company","Eligibility"])
        st.dataframe(df, use_container_width=True)
        st.bar_chart(pd.DataFrame({"Score":[tenth,inter,btech]}, index=["10th","Inter","BTech"]))
        st.progress(int(avg))
        if st.button("Home"):
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
            st.markdown("<div class='detail-box'><h3 style='color:#00ff88;margin-top:0;'>Code Practice - Run Here</h3><p style='color:#a78bfa;font-size:12px;'>Left side Q/A chadivi right side code practice chey</p>", unsafe_allow_html=True)
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
    week = get_current_week()
    st.markdown(f"<div class='center'><h1 style='color:white;'>Test Zone - Weekly Random Tests</h1><p style='color:#a78bfa;'>Week {week} - Questions change every Monday - Random shuffle each time</p></div>", unsafe_allow_html=True)
    _,col,_=st.columns([0.3,2,0.3])
    with col:
        st.write("")
        st.markdown("<div class='test-card'><h3 style='color:#fef08a;margin:0;'>How Test Zone Works - Random & Weekly Changing</h3><p style='color:#c7f0ff;margin-top:10px;'>1. <b>Random Tests:</b> Each time you start test, 10 questions randomly selected from pool of 15 per skill - No repeat same order<br>2. <b>Weekly Changing:</b> Every Monday week number changes, questions shuffle with new seed - You get new set every week<br>3. <b>Skill Wise:</b> C, Java, Python, SQL, DSA separate tests - Choose your skill<br>4. <b>Instant Score:</b> After submit, see score, correct answers, explanation for each question<br>5. <b>Leaderboard Ready:</b> Practice daily to improve placement readiness</p></div>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='center'><h3 style='color:white;'>Select Skill for Test - Random 10 Questions</h3></div>", unsafe_allow_html=True)
        st.write("")
        r1_c1, r1_c2, r1_c3 = st.columns(3)
        with r1_c1:
            if st.button("C Test - Random", use_container_width=True):
                st.session_state.test_skill="C"
                st.session_state.test_questions=get_weekly_random_questions("C", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r1_c2:
            if st.button("Java Test - Random", use_container_width=True):
                st.session_state.test_skill="Java"
                st.session_state.test_questions=get_weekly_random_questions("Java", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r1_c3:
            if st.button("Python Test - Random", use_container_width=True):
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
            if st.button("SQL Test - Random", use_container_width=True):
                st.session_state.test_skill="SQL"
                st.session_state.test_questions=get_weekly_random_questions("SQL", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r2_c2:
            if st.button("DSA Test - Random", use_container_width=True):
                st.session_state.test_skill="DSA"
                st.session_state.test_questions=get_weekly_random_questions("DSA", 10)
                st.session_state.test_answers={}
                st.session_state.test_submitted=False
                st.session_state.test_week=week
                st.session_state.page="test_attempt"
                st.rerun()
        with r2_c3:
            if st.button("Mixed Test - Random All Skills", use_container_width=True):
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
        if st.button("Back to Purpose", use_container_width=True):
            st.session_state.page="purpose"
            st.rerun()

elif st.session_state.page == "test_attempt":
    skill = st.session_state.test_skill
    questions = st.session_state.test_questions
    week = st.session_state.test_week
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Test - Week {week} - Random 10 Questions</h1><p style='color:#a78bfa;'>Questions shuffle every week - Options also shuffled randomly</p></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        if not st.session_state.test_submitted:
            st.markdown("<div class='detail-box'>", unsafe_allow_html=True)
            for idx, q in enumerate(questions):
                st.markdown(f"<div class='qbox'><b>Q{idx+1}. {q['q']}</b></div>", unsafe_allow_html=True)
                # Radio for options
                key = f"test_q_{idx}"
                options = q["options"]
                # Use index in session state
                selected = st.radio(f"Select for Q{idx+1}", options, key=key, index=None, label_visibility="collapsed")
                if selected is not None:
                    # Find index of selected
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
                    st.session_state.page="test_welcome"
                    st.rerun()
        else:
            # Show results
            score = 0
            for idx, q in enumerate(questions):
                user_ans = st.session_state.test_answers.get(idx, -1)
                if user_ans == q["ans"]:
                    score += 1
            st.markdown(f"<div class='center'><h2 style='color:#00ff88;'>Your Score: {score} / {len(questions)} - {score*10} %</h2><p style='color:#a78bfa;'>Week {week} Test Completed - Next week new questions will come automatically</p></div>", unsafe_allow_html=True)
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
                if st.button("Retake - New Random Questions", use_container_width=True, type="primary"):
                    st.session_state.test_questions=get_weekly_random_questions(skill, 10)
                    st.session_state.test_answers={}
                    st.session_state.test_submitted=False
                    st.rerun()
            with c2:
                if st.button("Change Skill", use_container_width=True):
                    st.session_state.page="test_welcome"
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
