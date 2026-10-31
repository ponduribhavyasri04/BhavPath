import streamlit as st
import pandas as pd
import io
import sys
from io import StringIO

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state: 
    st.session_state.page="welcome"
    st.session_state.college="QIS College"
    st.session_state.selected_skill="C"
    st.session_state.topic="Intro"
    st.session_state.pdata=None

st.markdown("""
<style>
[data-testid="stHeader"]{display:none}
.stApp{background:#05000a}
.bg-blue{position:fixed;width:800px;height:800px;background:radial-gradient(circle,#0d4aff 0%,#0d4aff00 70%);top:-100px;left:-100px;filter:blur(20px)}
.bg-pink{position:fixed;width:900px;height:900px;background:radial-gradient(circle,#ff006a 0%,#ff006a00 70%);bottom:-200px;right:-200px;filter:blur(30px);opacity:.9}
.glass{position:relative;z-index:10;padding:22px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.center{text-align:center;position:relative;z-index:10}
.detail-box{position:relative;z-index:10;max-height:85vh;overflow-y:auto;padding:25px;border-radius:18px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px)}
.qbox{background:rgba(13,74,255,0.1);border-left:4px solid #0d4aff;padding:12px 15px;margin:12px 0;border-radius:8px}
.abox{background:rgba(0,255,136,0.08);border-left:4px solid #00ff88;padding:12px 15px;margin:8px 0 18px 0;border-radius:8px}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_detailed_content(skill, topic):
    return f"{topic} in {skill} - TCS, Infosys, Amazon asks this. Types Basic Intermediate Advanced. Real Ex Banking 1 lakh records. Memory 1000 Val1 1004 Val2. Code var=10, if>5, loop, solve func, FAANG optimized."

def get_interview_content(skill):
    data = {
    "C": """
<div class='qbox'><b>Q1. What is pointer? int *p=&a;</b></div><div class='abox'>Pointer stores address. Why? Dynamic memory malloc, pass large data, Linked List. Code: int a=10; int *p=&a; printf("%d", *p); ->10. TCS 90% asks.</div>
<div class='qbox'><b>Q2. Array vs Pointer?</b></div><div class='abox'>Array continuous fixed size 20 bytes, pointer 8 bytes stores address. Array name constant. p++ ok, arr++ error.</div>
<div class='qbox'><b>Q3. Dangling pointer? free(p); p=NULL;</b></div><div class='abox'>Pointer pointing to freed memory. Set NULL after free to avoid crash.</div>
<div class='qbox'><b>Q4. malloc vs calloc?</b></div><div class='abox'>malloc 1 arg garbage, calloc 2 args zero init. Use calloc for safety.</div>
<div class='qbox'><b>Q5. Structure vs Union?</b></div><div class='abox'>Structure sum size, Union max size shared memory. TCS Wipro asks.</div>
<div class='qbox'><b>Q6. Storage classes auto static extern register?</b></div><div class='abox'>auto local, static keeps value between calls, extern global across files, register CPU.</div>
<div class='qbox'><b>Q7. Call by value vs reference?</b></div><div class='abox'>Value copies, original not changed. Reference passes address, original changes. swap needs reference.</div>
<div class='qbox'><b>Q8. String vs char array?</b></div><div class='abox'>char arr[5]={'H','e'} no \\0, char str[]="Hello" has \\0. String funcs need \\0.</div>
<div class='qbox'><b>Q9. Memory leak?</b></div><div class='abox'>malloc without free - system slows. Every malloc must have free.</div>
<div class='qbox'><b>Q10. Null vs Void vs Wild pointer?</b></div><div class='abox'>NULL points nothing safe, Void can point any type need cast, Wild uninitialized garbage.</div>
<div class='qbox'><b>Q11. Recursion stack overflow? factorial base condition</b></div><div class='abox'>Function calling itself each call pushes stack. No base condition crash.</div>
<div class='qbox'><b>Q12. File modes r w a r+ w+ a+?</b></div><div class='abox'>r read existing, w write create truncate, a append, r+ read+write, w+ create, a+ append+read.</div>
<div class='qbox'><b>Q13. Linked List vs Array?</b></div><div class='abox'>Array O(1) access O(n) insert middle, Linked List O(n) access O(1) insert. Use array for search, linked list for insert/delete.</div>
<div class='qbox'><b>Q14. Segmentation fault causes?</b></div><div class='abox'>NULL dereference, dangling pointer, array out of bounds arr[10] size 5, stack overflow.</div>
<div class='qbox'><b>Q15. Reverse string without library?</b></div><div class='abox'>Two pointers i=0 j=len-1 swap till i<j. O(n) time O(1) space. TCS coding round.</div>
""",
    "Java": """
<div class='qbox'><b>Q1. OOP 4 Pillars? Encapsulation Inheritance Polymorphism Abstraction</b></div><div class='abox'>Encapsulation private data + getter setter, Inheritance Dog extends Animal, Polymorphism overloading/overriding, Abstraction abstract/interface. Code: class Dog extends Animal{void sound(){System.out.println("bark");}}</div>
<div class='qbox'><b>Q2. ArrayList vs LinkedList?</b></div><div class='abox'>ArrayList dynamic array O(1) get O(n) insert middle, LinkedList nodes O(n) get O(1) insert. ArrayList for reading.</div>
<div class='qbox'><b>Q3. HashMap working? hashCode->bucket collision list/tree O(1) avg</b></div><div class='abox'>hash & (n-1) -> index. Collision linked list after 8 tree. Load factor 0.75. Amazon Google 100%.</div>
<div class='qbox'><b>Q4. String vs StringBuilder vs StringBuffer?</b></div><div class='abox'>String immutable many objects, StringBuilder mutable fast not sync, StringBuffer sync thread-safe slower. Loop 10000 concat StringBuilder 100x faster.</div>
<div class='qbox'><b>Q5. Exception try catch finally throw vs throws?</b></div><div class='abox'>try risky, catch handle, finally always close DB. throw you throw new Exception, throws method declares may throw.</div>
<div class='qbox'><b>Q6. Multithreading? extends Thread implements Runnable start() not run() synchronized?</b></div><div class='abox'>Multiple threads parallel. synchronized prevents two threads accessing same bank account same time balance issue.</div>
<div class='qbox'><b>Q7. Overloading vs Overriding?</b></div><div class='abox'>Overloading same class same name different params compile time add(int) add(double). Overriding child redefines parent runtime.</div>
<div class='qbox'><b>Q8. Interface vs Abstract class?</b></div><div class='abox'>Abstract abstract+concrete methods variables constructor single extends. Interface abstract only multiple implements no constructor. is-a vs can-do.</div>
<div class='qbox'><b>Q9. List Set Map differences?</b></div><div class='abox'>List ordered duplicate ArrayList, Set unordered unique HashSet O(1) TreeSet sorted, Map key-value HashMap TreeMap.</div>
<div class='qbox'><b>Q10. JDBC steps? Load driver Connection Statement ResultSet close</b></div><div class='abox'>Class.forName, DriverManager.getConnection, createStatement, executeQuery SELECT * FROM students, close. PreparedStatement prevents SQL injection.</div>
<div class='qbox'><b>Q11. Spring Boot DI? @Autowired</b></div><div class='abox'>You dont create object Spring creates injects. Loose coupling easy testing. @SpringBootApplication @RestController @Service.</div>
<div class='qbox'><b>Q12. Garbage collection mark and sweep Young Old?</b></div><div class='abox'>JVM auto deletes unused objects. Suggest System.gc(). Mark reachable sweep unreachable.</div>
<div class='qbox'><b>Q13. final finally finalize?</b></div><div class='abox'>final variable cannot change method cannot override class cannot extend, finally always executes, finalize GC before delete.</div>
<div class='qbox'><b>Q14. JVM JRE JDK platform independent bytecode?</b></div><div class='abox'>Java compiles to bytecode .class JVM runs any OS. JDK=JRE+tools javac, JRE=JVM+libraries. Write once run anywhere.</div>
<div class='qbox'><b>Q15. Singleton pattern single object DB connection?</b></div><div class='abox'>private static instance, private constructor, public static getInstance if null create return. Thread-safe synchronized.</div>
""",
    "Python": """
<div class='qbox'><b>Q1. List vs Tuple vs Set vs Dict? O(1) access</b></div><div class='abox'>List mutable [1,2,2], Tuple immutable (1,2) hashable, Set unique {1,2} O(1) search, Dict {"a":1} O(1). Use list scores, set unique skills, dict student->%.</div>
<div class='qbox'><b>Q2. *args **kwargs?</b></div><div class='abox'>*args tuple positional def add(*args): sum(args) add(1,2,3). **kwargs dict keyword def func(**kwargs): for k,v items func(name="Bhav").</div>
<div class='qbox'><b>Q3. Decorator Generator GIL?</b></div><div class='abox'>Decorator @login_required wraps adds behavior, Generator yield saves memory large file 1GB not load all, GIL one thread executes bytecode CPU-bound threading not faster IO-bound ok multiprocessing for CPU.</div>
<div class='qbox'><b>Q4. OOP self __init__ inheritance?</b></div><div class='abox'>self current object like this, __init__ constructor def __init__(self,name): self.name=name, super().__init__() parent call, multiple inheritance Python supports.</div>
<div class='qbox'><b>Q5. Django vs Flask REST API?</b></div><div class='abox'>Flask micro simple small API, Django full batteries ORM admin. REST GET POST PUT DELETE JSON GET /api/students returns [{"name":"Bhav"}].</div>
<div class='qbox'><b>Q6-Q15: Pandas DataFrame vs List NumPy 10x faster vectorization, lambda map filter, shallow deep copy reference vs full, file with open auto close, exception try except, etc.</b></div><div class='abox'>Pandas for placement data pd.DataFrame, NumPy C fast, lambda anonymous lambda x:x+10, map filter apply list, shallow copies reference deep full import copy, with open.</div>
""",
    "SQL": """
<div class='qbox'><b>Q1. WHERE vs HAVING? WHERE rows before GROUP BY HAVING groups after</b></div><div class='abox'>WHERE avg>75 SELECT * FROM students WHERE avg>75. HAVING COUNT>50 SELECT college COUNT(*) GROUP BY college HAVING COUNT>50. WHERE cannot use aggregate COUNT HAVING can.</div>
<div class='qbox'><b>Q2. JOINs INNER LEFT RIGHT FULL CROSS? Two circles diagram</b></div><div class='abox'>INNER only matching both, LEFT all left+matching right all students even if no placement NULL, RIGHT opposite, FULL both all, CROSS cartesian 5x3=15. LEFT JOIN to find not placed.</div>
<div class='qbox'><b>Q3. Indexing Clustered vs Non-clustered? O(n) to O(log n) book index</b></div><div class='abox'>Clustered rearranges physical data one per table PK, Non-clustered separate copy many per table. Without index search 1 lakh 1 sec with index 0.01 sec CREATE INDEX idx_avg ON students(avg) but insert slow.</div>
<div class='qbox'><b>Q4. Normalization 1NF 2NF 3NF BCNF? Remove redundancy</b></div><div class='abox'>1NF atomic no array in cell, 2NF no partial dependency student table id course course_fee fee depends only on course not id split, 3NF no transitive student->college->city split, BCNF stricter saves storage but joins needed.</div>
<div class='qbox'><b>Q5. Subquery vs JOIN which faster? SELECT * WHERE avg>(SELECT AVG...)</b></div><div class='abox'>Subquery inside query, JOIN combines tables Usually JOIN faster optimizer uses index subquery per row correlated slow. Use JOIN SELECT s.name FROM students s JOIN placements p ON s.id=p.student_id WHERE p.company='TCS'.</div>
<div class='qbox'><b>Q6-Q15: Window functions ROW_NUMBER RANK DENSE_RANK top 3 per college, GROUP BY vs DISTINCT, Procedure vs Function OUT param vs return, ACID Atomicity Consistency Isolation Durability banking transaction, Primary vs Foreign key etc.</b></div><div class='abox'>ROW_NUMBER unique rank, RANK same marks same rank gaps, DENSE_RANK no gaps. Procedure OUT param no return mandatory Function must return. Primary unique not null foreign references other table.</div>
""",
    "DSA": """
<div class='qbox'><b>Q1. Two Sum O(n) HashMap arr=[2,7,11,15] target=9 -> [0,1]</b></div><div class='abox'>seen={}; for i,num in enumerate(arr): if target-num in seen: return [seen[target-num], i]; seen[num]=i O(n) time O(n) space TCS Amazon 100%.</div>
<div class='qbox'><b>Q2. Reverse Linked List iterative prev=None curr=Head? Head->10->20->30->NULL to NULL<-10<-20<-30</b></div><div class='abox'>while curr: next=curr.next; curr.next=prev; prev=curr; curr=next; Head=prev O(n) time O(1) space iterative O(n) space recursive.</div>
<div class='qbox'><b>Q3. Detect loop Floyd tortoise hare slow 1 fast 2 if meet loop?</b></div><div class='abox'>slow=head fast=head while fast and fast.next slow=slow.next fast=fast.next.next if slow==fast loop exists. Find start move one to head both 1 step meet at start.</div>
<div class='qbox'><b>Q4. Stack vs Queue push pop top vs enqueue dequeue? Browser back button vs printer queue?</b></div><div class='abox'>Stack LIFO Last In First Out recursion stack undo, Queue FIFO First In First Out BFS. Stack list append pop, Queue deque popleft or two stacks. Queue using 2 stacks Amazon asks.</div>
<div class='qbox'><b>Q5. Tree traversals inorder Left Root Right sorted, preorder Root Left Right copy, postorder Left Right Root delete?</b></div><div class='abox'>inorder(node): if node: inorder(left) print(val) inorder(right) iterative uses stack BST sorted order.</div>
<div class='qbox'><b>Q6. BFS vs DFS queue level by level shortest path vs stack recursion deep?</b></div><div class='abox'>BFS queue level shortest path unweighted, DFS stack/recursion deep path exists topological sort. BFS shortest placement path DFS maze. O(V+E).</div>
<div class='qbox'><b>Q7. Quick Sort vs Merge Sort O(n log n) avg O(n^2) worst vs always O(n log n) stable?</b></div><div class='abox'>Quick pivot partition in-place O(1) space fast practice, Merge divide conquer stable O(n) extra space. Quick array Merge linked list stable sort keep original order equal marks.</div>
<div class='qbox'><b>Q8. DP Fibonacci memoization top-down cache vs tabulation bottom-up array O(n) vs O(2^n)?</b></div><div class='abox'>DP overlapping subproblems fib(n)=fib(n-1)+fib(n-2) naive O(2^n) repeats. Memoization if n in memo return, Tabulation dp[0]=0 dp[1]=1 for i 2..n dp[i]=dp[i-1]+dp[i-2] O(n). Use knapsack LCS.</div>
<div class='qbox'><b>Q9. Binary Search O(log n) sorted array low high mid?</b></div><div class='abox'>low=0 high=n-1 while low<=high mid=(low+high)//2 if arr[mid]==target return mid elif arr[mid]<target low=mid+1 else high=mid-1. 1 lakh students sorted find 85% 17 steps not 1 lakh.</div>
<div class='qbox'><b>Q10-Q15: Greedy coin change 93=50+20+20+2+1, Dijkstra O(E log V) shortest path QIS to companies, Trie autocomplete prefix Py->Python, Heap top K highest package, etc.</b></div><div class='abox'>Practice 100+ DSA for Amazon Google Use BhavPath DSA section.</div>
""",
    "C++": """
<div class='qbox'><b>Q1. C vs C++? C procedural printf scanf manual, C++ procedural+OOP classes STL cin cout type safe new delete superset?</b></div><div class='abox'>C++ better for large projects reusable classes Student Placement. C OS embedded, C++ games banking.</div>
<div class='qbox'><b>Q2. OOP 4 Pillars code? private public : public virtual =0?</b></div><div class='abox'>Encapsulation class Student{private int marks; public getMarks();}; Inheritance class TCSStudent: public Student{}; Polymorphism virtual void sound(){} override bark; Abstraction pure virtual virtual void apply()=0;</div>
<div class='qbox'><b>Q3. STL vector map set? vector<int> v push_back v[0], map<string,int> m m["TCS"]=90 O(log n), set<int> s insert unique sorted sort(v.begin(), v.end())?</b></div><div class='abox'>Ready-made containers saves time coding round not write own sorting TCS asks STL.</div>
<div class='qbox'><b>Q4. Smart pointers unique_ptr one owner cannot copy, shared_ptr multiple ref count 2 when 0 delete, weak_ptr breaks cycle auto delete?</b></div><div class='abox'>Raw pointer manual delete leak. unique_ptr make_unique, shared_ptr make_shared, weak_ptr. Modern C++ prefers smart pointers avoid leak BhavPath project.</div>
<div class='qbox'><b>Q5-Q15: Inheritance single multiple multilevel hierarchical, Polymorphism overloading compile time vs overriding runtime virtual table vtable function pointers, Templates generic template<typename T> T add(T a,T b){return a+b;} int float etc.</b></div><div class='abox'>Practice C++ TCS Wipro product based Build project classes placement system.</div>
"""
    }
    return data.get(skill, data["C"])

def get_default_code(skill):
    codes = {
        "C": "# C Interview - Pointer Example (Python practice)\na=10\np=id(a)\nprint(f\"a={a} address={p}\")\nprint(f\"*p (value at address) = {a}\")\n\narr=[10,20,30,40]\nprint(f\"Array: {arr}\")\nprint(f\"Pointer to first: arr[0]={arr[0]}\")\n\nsize=5\nmalloc_arr=[0]*size\nprint(f\"malloc {size} ints: {malloc_arr}\")",
        "Java": "# Java Interview - OOP Example\nclass Animal:\n    def sound(self):\n        print(\"Animal sound\")\nclass Dog(Animal):\n    def sound(self):\n        print(\"Dog barks - Bow Bow\")\ndog=Dog()\ndog.sound()\n\narray_list=[\"TCS\", \"Infosys\", \"Amazon\"]\nprint(f\"ArrayList: {array_list}\")\narray_list.append(\"Google\")\nprint(f\"After add: {array_list}\")\n\nhash_map={\"TCS\": 90, \"Infosys\": 85}\nprint(f\"HashMap: {hash_map}\")",
        "Python": "# Python - List vs Tuple vs Set vs Dict\nmy_list=[1,2,2,3]\nmy_tuple=(1,2,3)\nmy_set={1,2,3}\nmy_dict={\"Python\":90, \"Java\":85}\nprint(f\"List: {my_list}\")\nprint(f\"Tuple: {my_tuple}\")\nprint(f\"Set: {my_set}\")\nprint(f\"Dict: {my_dict}\")\n\ndef placement_func(*args, **kwargs):\n    print(f\"args: {args}\")\n    print(f\"kwargs: {kwargs}\")\nplacement_func(\"Python\", \"Java\", name=\"Bhav\", college=\"QIS\")\nsquares=[x*x for x in range(1,6)]\nprint(f\"Squares: {squares}\")",
        "SQL": "# SQL Interview - Pandas style\nimport pandas as pd\nstudents=pd.DataFrame({\"id\":[1,2,3,4,5],\"name\":[\"Bhav\",\"Rahul\",\"Priya\",\"Arjun\",\"Sneha\"],\"avg\":[85,72,90,65,88]})\nprint(students)\nprint(\"\\nWHERE avg>75:\")\nprint(students[students[\"avg\"]>75])\nplacements=pd.DataFrame({\"student_id\":[1,3,5],\"company\":[\"TCS\",\"Amazon\",\"Infosys\"]})\nmerged=pd.merge(students, placements, left_on=\"id\", right_on=\"student_id\", how=\"left\")\nprint(\"\\nLEFT JOIN:\")\nprint(merged[[\"name\",\"avg\",\"company\"]])",
        "DSA": "# DSA - Two Sum O(n) - TCS Amazon 100%\ndef two_sum(arr, target):\n    seen={}\n    for i, num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\narr=[2,7,11,15]\ntarget=9\nprint(f\"Array: {arr}, Target: {target}\")\nprint(f\"Two Sum: {two_sum(arr, target)}\")\n\nclass Node:\n    def __init__(self, val):\n        self.val=val\n        self.next=None\nhead=Node(10)\nhead.next=Node(20)\nhead.next.next=Node(30)\ncurr=head\nprint(\"Original:\", end=\" \")\nwhile curr:\n    print(curr.val, end=\"->\")\n    curr=curr.next\nprint(\"NULL\")\nprev=None\ncurr=head\nwhile curr:\n    nxt=curr.next\n    curr.next=prev\n    prev=curr\n    curr=nxt\nhead=prev\ncurr=head\nprint(\"Reversed:\", end=\" \")\nwhile curr:\n    print(curr.val, end=\"->\")\n    curr=curr.next\nprint(\"NULL\")",
        "C++": "# C++ STL Simulation\nvector=[]\nvector.append(10)\nvector.append(20)\nprint(f\"Vector: {vector}\")\nmap_dict={\"TCS\":90,\"Infosys\":85}\nprint(f\"Map: {map_dict}\")\nmy_set=set([10,20,10])\nprint(f\"Set: {my_set}\")\n\nclass Student:\n    def __init__(self, name, avg):\n        self.name=name\n        self.avg=avg\n    def display(self):\n        print(f\"Student: {self.name}, Avg: {self.avg}%\")\ns1=Student(\"Bhav\",85)\ns1.display()\nclass PlacedStudent(Student):\n    def __init__(self, name, avg, company):\n        super().__init__(name, avg)\n        self.company=company\n    def display(self):\n        print(f\"Placed: {self.name} in {self.company} with {self.avg}%\")\ns2=PlacedStudent(\"Bhav\",85,\"TCS\")\ns2.display()"
    }
    return codes.get(skill, codes["C"])

if st.session_state.page == "welcome":
    st.markdown("""<div class='center' style='padding-top:22vh'><h1 style='color:#c7f0ff;font-size:78px;font-weight:900;'>Welcome to BhavPath</h1><div class='glass' style='display:inline-block;margin-top:20px;padding:28px 50px;'><h2 style='margin:0;font-size:34px;background:linear-gradient(90deg,#fef08a,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>What is Your Placement Story..??</h2></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.4,1,1.4])
    with c:
        st.write(""); st.write("")
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
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
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
                st.session_state.topic="Basics"
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
        st.write(""); st.write("")
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
            st.markdown(f"<div class='detail-box'><h2 style='color:#fef08a;margin-top:0;'>{st.session_state.topic} in {skill}</h2><div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div>", unsafe_allow_html=True)
            st.markdown("---", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:#00ff88;'>Try {skill} Code - Practice & Run</h3>", unsafe_allow_html=True)
            default_code=get_default_code(skill)
            code_input=st.text_area("Code Editor", value=default_code, height=200, key=f"code_skill_{skill}_{st.session_state.topic}")
            if st.button("Run Code", key=f"run_skill_{skill}_{st.session_state.topic}", type="primary"):
                try:
                    old_stdout=sys.stdout
                    sys.stdout=mystdout=StringIO()
                    exec(code_input, {"pd": pd})
                    sys.stdout=old_stdout
                    output=mystdout.getvalue()
                    st.success(f"Output:\n{output}")
                except Exception as e:
                    st.error(f"Error: {e}")
            st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "interview_welcome":
    st.markdown("""<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;font-size:18px;'>Crack TCS, Infosys, Amazon, Google - Interview + Code Practice</p></div></div>""", unsafe_allow_html=True)
    _,c,_=st.columns([1.3,1,1.3])
    with c:
        st.write(""); st.write("")
        if st.button("Start Interview Prep", use_container_width=True, type="primary"):
            st.session_state.page="interview_skills"
            st.rerun()
        if st.button("Back"):
            st.session_state.page="purpose"
            st.rerun()

elif st.session_state.page == "interview_skills":
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1><p style='color:#a78bfa;'>Interview Questions + Code Practice & Run</p></div>", unsafe_allow_html=True)
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
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview + Code Practice</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.05,3,0.05])
    with c:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            content=get_interview_content(skill)
            st.markdown(f"<div class='detail-box'><h3 style='color:#fef08a;margin-top:0;'>Interview Questions - {skill}</h3><div style='color:white;line-height:1.8;font-size:13px;'>{content}</div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='detail-box'><h3 style='color:#00ff88;margin-top:0;'>Code Practice - {skill} - Run Here</h3><p style='color:#a78bfa;font-size:12px;'>Ikkada code rasi Run cheyavachu - Interview + Code in one page</p>", unsafe_allow_html=True)
            default_code=get_default_code(skill)
            code_key=f"iv_code_{skill}"
            if code_key not in st.session_state:
                st.session_state[code_key]=default_code
            code_input=st.text_area("Editor", value=st.session_state[code_key], height=380, key=f"editor_{skill}", label_visibility="collapsed")
            c_run, c_reset = st.columns(2)
            with c_run:
                if st.button("Run Code", key=f"run_iv_{skill}", type="primary", use_container_width=True):
                    st.session_state[code_key]=code_input
                    try:
                        old_stdout=sys.stdout
                        sys.stdout=mystdout=StringIO()
                        exec(code_input, {"pd": pd})
                        sys.stdout=old_stdout
                        output=mystdout.getvalue()
                        st.session_state[f"output_{skill}"]=output
                        st.session_state[f"error_{skill}"]=None
                    except Exception as e:
                        st.session_state[f"output_{skill}"]=None
                        st.session_state[f"error_{skill}"]=str(e)
            with c_reset:
                if st.button("Reset", key=f"reset_{skill}", use_container_width=True):
                    st.session_state[code_key]=default_code
                    st.session_state[f"output_{skill}"]=None
                    st.session_state[f"error_{skill}"]=None
                    st.rerun()
            if f"output_{skill}" in st.session_state and st.session_state[f"output_{skill}"]:
                st.success(f"Output:\n{st.session_state[f'output_{skill}']}")
            if f"error_{skill}" in st.session_state and st.session_state[f"error_{skill}"]:
                st.error(f"Error: {st.session_state[f'error_{skill}']}")
            st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("Back to Skills"):
            st.session_state.page="interview_skills"
            st.rerun()

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon</h1></div>", unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.page="purpose"
        st.rerun()
            
