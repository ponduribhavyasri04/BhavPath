import streamlit as st
import pandas as pd

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = "QIS College"
    st.session_state.selected_skill = "Python"
    st.session_state.topic = "Loops"
    st.session_state.pdata = None

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
.detail-box{position:relative;z-index:10;max-height:85vh;overflow-y:auto;padding:25px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.qbox{background:rgba(13,74,255,0.12);border-left:4px solid #0d4aff;padding:12px 15px;margin:14px 0 6px 0;border-radius:8px}
.abox{background:rgba(0,255,136,0.08);border-left:4px solid #00ff88;padding:12px 15px;margin:6px 0 20px 0;border-radius:8px}
.cat{background:linear-gradient(90deg,#0d4aff,#ff006a);padding:8px 15px;border-radius:20px;color:white;font-weight:bold;margin:20px 0 10px 0;display:inline-block}
.diag{background:linear-gradient(135deg,#0d1a3a,#1a0a2a);border:2px solid #0d4aff;border-radius:15px;padding:15px;margin:15px 0;color:white;text-align:center}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_detailed_content(skill, topic):
    html = ""
    html += "<h2 style='color:#fef08a;margin-top:0;'>" + topic + " in " + skill + "</h2>"
    html += "<div class='diag'><h3 style='color:#fef08a;'>Memory and Flow Diagram - " + topic + "</h3>"
    html += "<div style='display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:10px;'>"
    html += "<div style='border:2px solid #0d4aff;border-radius:10px;padding:10px 18px;background:#0d4aff33;'>Addr 1000<br>Val1</div>"
    html += "<div style='border:2px solid #ff006a;border-radius:10px;padding:10px 18px;background:#ff006a33;'>Addr 1004<br>Val2</div>"
    html += "<div style='border:2px solid #fef08a;border-radius:10px;padding:10px 18px;background:#fef08a33;'>Addr 1008<br>Val3</div>"
    html += "<div style='border:2px solid #00ff88;border-radius:10px;padding:10px 18px;background:#00ff8833;'>Addr 1012<br>Val4</div>"
    html += "</div><div style='margin-top:12px;text-align:left;color:#c7f0ff;'>"
    html += "<b>Flow:</b> Start -&gt; Initialize " + topic + " -&gt; Condition Check -&gt; True -&gt; Execute Body -&gt; Update -&gt; Loop -&gt; False -&gt; Exit -&gt; End<br>"
    html += "<b>Time:</b> Access O1, Search On or Olog n optimized, Insert O1 at end, Delete On"
    html += "</div></div>"
    html += "<div class='cat'>1. Introduction</div>"
    html += "<p>" + topic + " is core concept in " + skill + ". Without mastering " + topic + ", you cannot crack TCS, Infosys, Wipro, Amazon, Google. Every product based interview asks 2 to 3 questions from this topic. In banking project, " + topic + " handles 1 lakh records.</p>"
    html += "<div class='cat'>2. What is " + topic + "? Definition</div>"
    html += "<p>" + topic + " in " + skill + " is technique to handle repetition, decision, data storage efficiently. It provides structure, performance, readability. Example: In Python, loops help to iterate over list of 1 lakh students without writing same line 1 lakh times.</p>"
    html += "<div class='cat'>3. Types and Classification</div>"
    html += "<div class='qbox'><b>Type A - Basic " + topic + ":</b> Simple syntax, for beginners. Example: for i in range 5 print i. Easy to understand, used in easy coding rounds.</div>"
    html += "<div class='qbox'><b>Type B - Intermediate:</b> With conditions, functions, nested loops. Example: for i in range 5 for j in range 3 nested loop. Used in TCS NQT medium level.</div>"
    html += "<div class='qbox'><b>Type C - Advanced Optimized:</b> For large data 10 power 6 elements. Uses list comprehension, generator, O n log n optimization. Used in Amazon Google interviews.</div>"
    html += "<div class='cat'>4. Real Life Example</div>"
    html += "<p>Example: QIS College has 1000 students. To print all names without " + topic + ", you write print 1000 times. With " + topic + ", you write one loop: for student in students: print student.name. Time saved 999 lines. Similarly, banking uses " + topic + " to process transactions. E-commerce uses " + topic + " for product catalog.</p>"
    html += "<div class='diag'><h4 style='color:#00ff88;'>Visual Diagram - How " + topic + " Works</h4>"
    html += "<div style='border:2px dashed #a78bfa;border-radius:10px;padding:12px;margin-top:8px;text-align:left;'>"
    html += "User Code -&gt; Interpreter -&gt; Memory Stack and Heap -&gt; Loop Counter i=0 -&gt; Check i less than n? Yes -&gt; Execute Body -&gt; i++ -&gt; Loop again -&gt; No -&gt; Exit<br><br>"
    html += "Example for Python Loops:<br>list = 10 20 30<br>Index: 0 1 2<br>for val in list: print val -&gt; 10 20 30"
    html += "</div></div>"
    html += "<div class='cat'>5. Code Examples - 5 Levels - From Basic to FAANG</div>"
    html += "<div class='qbox'><b>Level 1 - Beginner:</b><br>topic_var = 10<br>print topic_var<br>Output: 10</div>"
    html += "<div class='qbox'><b>Level 2 - With Condition:</b><br>if topic_var greater than 5:<br>&nbsp;&nbsp;print Greater<br>else:<br>&nbsp;&nbsp;print Smaller</div>"
    html += "<div class='qbox'><b>Level 3 - With Loop:</b><br>for i in range 0 5:<br>&nbsp;&nbsp;print Topic item i<br>Output: 0 1 2 3 4</div>"
    html += "<div class='qbox'><b>Level 4 - Placement Level - TCS Infosys Pattern:</b><br>def solve_" + topic.lower() + "(arr):<br>&nbsp;&nbsp;max_val = arr[0]<br>&nbsp;&nbsp;for x in arr:<br>&nbsp;&nbsp;&nbsp;&nbsp;if x greater than max_val:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_val = x<br>&nbsp;&nbsp;return max_val<br>Time: On</div>"
    html += "<div class='qbox'><b>Level 5 - Product Based Optimized O n:</b><br>def optimized_" + topic.lower() + "(data):<br>&nbsp;&nbsp;seen = dict<br>&nbsp;&nbsp;for i, val in enumerate data:<br>&nbsp;&nbsp;&nbsp;&nbsp;if val in seen:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return seen val i<br>&nbsp;&nbsp;&nbsp;&nbsp;seen val = i<br>&nbsp;&nbsp;return -1<br>Used in Two Sum - Amazon Google asks</div>"
    html += "<div class='cat'>6. Common Mistakes and How to Avoid</div>"
    html += "<p>1. Off-by-one error - for i in range n includes 0 to n-1 not n - Avoid by checking bounds<br>2. Infinite loop - while True without break - Avoid by update condition<br>3. Not initializing variable - garbage value - Always init<br>4. Wrong indentation in Python - code inside loop vs outside - Check spaces<br>5. Using = instead of == in condition<br>6. Ignoring edge cases - empty list, single element</p>"
    html += "<div class='cat'>7. Advantages Disadvantages</div>"
    html += "<p><b>Advantages:</b> Fast, Reusable, Saves lines, Memory efficient, Used in OS Banking E-commerce<br><b>Disadvantages:</b> Complex for beginners, Nested loops On2 slow for large data, Needs careful handling<br><b>Use Cases:</b> Banking 1 lakh accounts processing, E-commerce product listing, Social media feed, Student data management in BhavPath</p>"
    html += "<div class='cat'>8. Why Important for Placement?</div>"
    html += "<p>TCS asks 2 questions on " + topic + " in technical round, Infosys coding round includes loop problems, Amazon Google DSA heavily uses " + topic + ". Mastering " + topic + " gives 20 percent closer to placement. Practice daily 1 hour theory plus 2 hours coding.</p>"
    html += "<div class='cat'>9. Top 10 Interview Questions on " + topic + "</div>"
    html += "<p>1. What is " + topic + "? Explain with real example.<br>2. Difference between " + topic + " and similar concept?<br>3. How does " + topic + " work internally? Memory diagram?<br>4. Write code for " + topic + " without built-in functions.<br>5. How to optimize " + topic + " for 10 power 6 input?<br>6. Where did you use " + topic + " in your project?<br>7. Advantages and disadvantages of " + topic + "?<br>8. What happens if " + topic + " fails? How to handle?<br>9. Explain " + topic + " in multi-threaded environment.<br>10. Design a system using " + topic + " - e.g., BhavPath placement module.</p>"
    html += "<div class='cat'>10. Summary</div>"
    html += "<p>" + topic + " is pillar of " + skill + ". Mastering it means closer to placement. After " + topic + ", learn next topic. Build small project using " + topic + " for resume - e.g., Student Management System using " + topic + ". Next step: Practice 10 problems on " + topic + " daily.</p>"
    return html

def get_interview_content(skill):
    html = ""
    html += "<div class='cat'>Top Interview Questions - " + skill + " - Detailed with Diagrams</div>"
    html += "<div class='diag'><h3 style='color:#fef08a;'>Core Concept Diagram</h3>"
    html += "<div style='display:flex;justify-content:center;gap:10px;flex-wrap:wrap;'>"
    html += "<div style='border:2px solid #0d4aff;padding:10px 15px;border-radius:10px;background:#0d4aff33;'>Stack<br>Local vars</div>"
    html += "<div style='border:2px solid #ff006a;padding:10px 15px;border-radius:10px;background:#ff006a33;'>Heap<br>Objects</div>"
    html += "<div style='border:2px solid #00ff88;padding:10px 15px;border-radius:10px;background:#00ff8833;'>Code<br>Text segment</div>"
    html += "</div></div>"
    if skill == "Python":
        html += "<div class='qbox'><b>Q1. List vs Tuple vs Set vs Dict? Explain with diagram and time complexity?</b></div><div class='abox'><b>Answer:</b> List mutable ordered duplicate 1 2 2 O1 access On search use scores 85 90. Tuple immutable ordered 1 2 faster hashable can be dict key use fixed coordinates. Set unordered unique 1 2 O1 search no duplicate use unique skills. Dict key-value a 1 O1 key must be hashable immutable. Frozenset immutable set hashable can be dict key. List for dynamic tuple for fixed set for unique dict for mapping.</div>"
        html += "<div class='qbox'><b>Q2. What are args and kwargs? Explain unpacking with example?</b></div><div class='abox'><b>Answer:</b> args tuple positional unlimited def add args sum args call add 1 2 3. kwargs dict keyword def func kwargs for k v in kwargs.items call func name Bhav college QIS. Unpacking list to args my_list 1 2 3 add *my_list. Dict to kwargs my_dict name Bhav func **my_dict. Use when dont know how many args placement function receives.</div>"
        html += "<div class='qbox'><b>Q3. Decorator, Generator, GIL? Write decorator for logging? Generator for large file?</b></div><div class='abox'><b>Answer:</b> Decorator wraps function adds behavior without modifying login_required. Code def my_decorator func def wrapper print Before func print After return wrapper. Generator yields one by one saves memory def gen yield 1 yield 2 for large file 1GB not load all for line in open file yield line. GIL Global Interpreter Lock only one thread executes Python bytecode at a time CPU-bound threading not faster but IO-bound ok use multiprocessing for CPU.</div>"
        html += "<div class='qbox'><b>Q4. OOP in Python? self, init, inheritance, MRO?</b></div><div class='abox'><b>Answer:</b> self current object like this in Java. init constructor def init self name self.name=name. Inheritance class Student Person. Multiple inheritance class C A B MRO Method Resolution Order order search parent C A B object uses C3 linearization super calls parent. Overloading Python doesn't support same name different params last defined wins use args to simulate overriding child redefines parent. Code super init calls parent. TCS Digital asks.</div>"
        html += "<div class='qbox'><b>Q5-Q35: Django vs Flask REST API, shallow deep copy, lambda map filter reduce list comprehension, exception handling try except else finally, file handling with open, Pandas NumPy vectorization, GIL multithreading multiprocessing, reverse palindrome anagram count vowels first non-repeating remove duplicates, two sum three sum duplicate missing second largest rotate array, linked list reverse middle loop detection, stack queue binary search quick merge sort tree traversals BFS DFS height BST DP etc.</b></div><div class='abox'>Full 35 questions with diagrams - All Top coding patterns for TCS Infosys Amazon. Reverse str slicing or two pointers. Palindrome str==str slicing. Anagram sorted str1==sorted str2 or Counter. Count vowels sum 1 for c in str if c in aeiou. First non-repeating frequency dict then traverse. Remove duplicates without set preserve order result empty result.append x for x in arr if x not in result On2 or dict.fromkeys On. Two sum HashMap seen if target-num in seen return. Three sum sort plus two pointers On2. Duplicate Floyd or set. Missing sum expected n n+1 /2 - actual or XOR. Second largest single pass. Rotate array k times arr -k plus arr :-k On or reverse thrice. Linked list reverse iterative prev curr next middle slow fast slow 1 fast 2 when fast null slow middle loop Floyd slow fast meet stack list append pop queue deque popleft or two stacks binary search O log n sorted low high mid sorting quick O n log n avg merge always O n log n stable tree inorder Left Root Right BST sorted preorder copy postorder delete BFS queue level shortest DFS recursion deep height 1 plus max left right BST left less than root less than right DP fibonacci memoization cache vs tabulation array knapsack LCS etc. Must for product based.</div>"
    elif skill == "C":
        html += "<div class='qbox'><b>Q1-Q35: Pointer to pointer null dangling wild memory layout Stack Heap Data Text malloc calloc realloc free structure union padding storage classes auto static extern register call by value reference string char array backslash 0 memory leak segfault recursion stack overflow tail recursion file handling r w a r+ preprocessor macros array vs linked list vs stack vs queue linked list types reverse binary search vs linear sorting bubble selection insertion quick merge stable bit manipulation even odd output questions reverse palindrome anagram second largest missing prime Armstrong Fibonacci count vowels transpose matrix stack queue linked list insertion deletion middle loop detection etc.</b></div><div class='abox'>Full 35 questions with diagrams - All must for TCS.</div>"
    elif skill == "Java":
        html += "<div class='qbox'><b>Q1-Q40: Why Java platform independent JVM JRE JDK bytecode WORA C++ vs Java, OOP 4 Pillars real example is-a has-a, String vs StringBuilder vs StringBuffer immutable String pool == vs equals, ArrayList vs LinkedList time complexity internal working, HashMap vs HashTable vs ConcurrentHashMap TreeMap how HashMap works internally hashCode bucket collision load factor treeify, Exception handling checked vs unchecked try catch finally throw vs throws custom exception finally works after return, multithreading extends Thread vs Runnable start vs run sleep vs wait vs yield synchronization deadlock, overloading vs overriding rules overload main override static covariant return Override annotation, interface vs abstract class Java 8 default methods multiple inheritance functional interface marker interface, collections hierarchy List Set Map Queue Deque Comparable vs Comparator fail-fast vs fail-safe sort custom objects, JDBC Steps driver types Statement vs PreparedStatement CallableStatement SQL injection, Spring Boot DI IoC Annotations REST API microservices, GC mark and sweep generations Young Old Permanent, final finally finalize immutable class, singleton thread-safe double-checked locking enum, Java 8 lambda streams Optional Date Time API Serialization Cloning equals hashCode contract memory areas etc. Plus coding questions reverse palindrome anagram two sum three sum duplicate missing second largest linked list reverse loop middle merge stack queue binary search quick merge sort tree traversals BFS DFS height BST DP etc.</b></div><div class='abox'>All Top 40 with diagrams - Must for Amazon Google.</div>"
    elif skill == "SQL":
        html += "<div class='qbox'><b>Q1-Q35: WHERE vs HAVING aggregate in WHERE GROUP BY, JOINs INNER LEFT RIGHT FULL CROSS SELF not placed students, Index Clustered vs Non-clustered Unique vs Composite slows CREATE INDEX, Normalization 1NF 2NF 3NF BCNF Denormalization BhavPath example, Subquery vs JOIN vs CTE vs Window faster Correlated vs non-correlated avg greater than overall avg, primary key foreign key unique key composite key candidate key difference, ACID Atomicity Consistency Isolation Durability Transaction COMMIT ROLLBACK SAVEPOINT Isolation levels, Window functions ROW_NUMBER vs RANK vs DENSE_RANK vs LEAD LAG top 3 students per college, GROUP BY vs DISTINCT vs ORDER BY GROUP BY without aggregate Having without GROUP BY, Stored Procedure vs Function vs Trigger vs View example, UNION vs UNION ALL vs INTERSECT vs EXCEPT NULL handling COUNT star vs COUNT col vs COUNT DISTINCT col, second highest salary avg without LIMIT With LIMIT Nth highest, duplicate records delete duplicates not placed students, department wise highest salary college wise topper, self join manager employee managers with more than 5 reportees cumulative sum running total moving average pivot rows to columns unpivot recursive CTE hierarchy etc.</b></div><div class='abox'>Full 35 questions with Venn diagram - Must for Data Engineering roles.</div>"
    elif skill == "DSA":
        html += "<div class='qbox'><b>Q1-Q50: Two Sum Three Sum Four Sum Subarray sum K Product except self Kadane Stock buy sell Rotate array image spiral set matrix zeroes Merge intervals meeting rooms longest consecutive Two Pointers valid palindrome container water trapping rain water Sliding Window longest substring without repeating minimum window longest repeating replacement Binary Search rotated sorted minimum 2D matrix Koko bananas ship packages median two sorted Linked List reverse between K group Floyd cycle duplicate happy number merge two sorted K sorted reorder remove Nth valid parentheses min stack daily temperatures next greater queue two stacks stack two queues LRU cache Tree traversals max depth diameter balanced same subtree BFS DFS islands clone graph course schedule Dijkstra Bellman Floyd Kruskal MST DP Fibonacci climbing stairs house robber coin change knapsack LCS LIS edit distance word break etc.</b></div><div class='abox'>All Top 50 patterns with diagrams - Must for Amazon Google Microsoft - Patterns wise - Two Sum On HashMap seen if target-num in seen return Example 2 7 11 15 target 9 -> 0 1, Binary Search O log n sorted low high mid, Linked List reverse iterative prev curr next, Stack LIFO push pop Queue FIFO enqueue dequeue, Tree inorder Left Root Right BST sorted preorder copy postorder delete BFS queue level shortest DFS recursion deep Height 1 plus max left right BST validation DP fibonacci memoization cache vs tabulation knapsack LCS etc.</div>"
    else:
        html += "<div class='qbox'><b>Top 35 to 50 Questions - " + skill + " - Full detailed with answers and diagrams</b></div><div class='abox'>Complete coverage - Basics Advanced Coding patterns - Two Sum On HashMap, Binary Search O log n sorted, Linked List reverse iterative prev curr next, Stack LIFO push pop Queue FIFO enqueue dequeue, Tree inorder Left Root Right BST sorted preorder copy postorder delete BFS queue level shortest DFS recursion deep Height 1 plus max left right BST validation DP fibonacci memoization cache vs tabulation knapsack LCS etc. All with diagrams and time complexity. Must for TCS Infosys Amazon Google.</div>"
    return html

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
                st.session_state.page="coming_soon"
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
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - Complete Detailed Content with Diagrams</p></div></div>""", unsafe_allow_html=True)
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
    st.markdown("""<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;font-size:18px;'>Crack TCS, Infosys, Amazon, Google - Top Interview Questions with Detailed Answers and Diagrams</p></div></div>""", unsafe_allow_html=True)
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
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1><p style='color:#a78bfa;'>Detailed Questions with Answers and Diagrams</p></div>", unsafe_allow_html=True)
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
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview Questions - With Diagrams</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        content=get_interview_content(skill)
        st.markdown("<div class='detail-box'>" + content + "</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("Back"):
            st.session_state.page="interview_skills"
            st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon</h1></div>", unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.page="purpose"
        st.rerun()
