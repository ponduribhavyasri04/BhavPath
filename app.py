import streamlit as st
import pandas as pd
import sys
from io import StringIO

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = "QIS College"
    st.session_state.selected_skill = "C"
    st.session_state.topic = "Intro"
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
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_detailed_content(skill, topic):
    txt = topic + " in " + skill + " - TCS, Infosys, Amazon asks this. Types Basic Intermediate Advanced. Real Ex Banking 1 lakh records. Memory 1000 Val1 1004 Val2. Code var=10, if greater, loop, solve func, FAANG optimized."
    return txt

def get_interview_content(skill):
    if skill == "C":
        return """
<div class='cat'>C Interview - Top 35 Questions - TCS, Infosys, Wipro, Amazon</div>
<div class='cat'>Category 1: Basics and Memory Q1-Q8</div>
<div class='qbox'><b>Q1. What is pointer? Explain pointer to pointer, null, dangling, wild with code and diagram.</b></div><div class='abox'><b>Answer:</b> Pointer stores address. int a=10; int *p=&a; p=1000. Pointer to pointer int **pp=&p; Null int *p=NULL safe. Dangling free(p); p still points freed crash set p=NULL. Wild int *p; uninitialized garbage. Diagram a at 1000=10, p at 2000=1000, pp at 3000=2000. Code printf value. 90 percent asked.</div>
<div class='qbox'><b>Q2. Explain memory layout of C program? Stack, Heap, Data, Text? Where malloc goes?</b></div><div class='abox'><b>Answer:</b> Text code, Data global static, Stack local variables function calls LIFO auto free, Heap dynamic malloc manual free. Example int g=10 Data, int *p=malloc(4) Heap, int a=5 Stack. Stack overflow recursion without base. Malloc goes to Heap.</div>
<div class='qbox'><b>Q3. malloc vs calloc vs realloc vs free? Difference? Write code for 1 lakh ints.</b></div><div class='abox'><b>Answer:</b> malloc 400000 1 arg size uninitialized fast, calloc 100000,4 2 args zero init safe slow, realloc resize existing, free release. Code int *p = malloc 100000 sizeof int; if p NULL handle; free p; p NULL; Without free memory leak system slows. Banking uses calloc zero init.</div>
<div class='qbox'><b>Q4. Structure vs Union vs Structure padding? Size calculation?</b></div><div class='abox'><b>Answer:</b> Structure sum plus padding alignment struct char a int b size not 5 but 8 due 4-byte alignment. Union shares same memory size = max member only one active. Use struct for employee full data, union for value can be int OR float. Wipro asks padding.</div>
<div class='qbox'><b>Q5. Storage classes auto static extern register? Scope lifetime default?</b></div><div class='abox'><b>Answer:</b> auto local auto free garbage scope function lifetime function. static keeps value between calls stays till program default 0. extern global across files default 0. register request CPU register fast loop counters. static int count=0; count++ remembers calls counting.</div>
<div class='qbox'><b>Q6. Call by value vs reference? Write swap program?</b></div><div class='abox'><b>Answer:</b> Value copies original not changed void func int x x=20; Reference passes address original changes void func int *x *x=20;. Swap needs reference void swap int *a int *b int t=*a; *a=*b; *b=t;. Large array pass by reference saves memory.</div>
<div class='qbox'><b>Q7. String vs char array? Why backslash 0? What if forget?</b></div><div class='abox'><b>Answer:</b> char arr 5 elements not string no backslash 0. char str Hello auto backslash 0. String functions strlen strcpy need backslash 0 to know end. If forget printf prints garbage till random backslash 0 buffer overflow.</div>
<div class='qbox'><b>Q8. Memory leak, segmentation fault, dangling? Prevention Tools?</b></div><div class='abox'><b>Answer:</b> Leak malloc without free loop 1000 times free 1. Segfault accessing not owned NULL dereference dangling out of bounds arr 10 size 5 stack overflow. Prevention every malloc free NULL check bounds check init pointers. Tool valgrind.</div>
<div class='cat'>Category 2: Advanced C Q9-Q18</div>
<div class='qbox'><b>Q9. Recursion, stack overflow, tail recursion? Factorial iterative vs recursive?</b></div><div class='abox'><b>Answer:</b> Function calling itself each call pushes stack frame. Factorial recursive if n==0 return 1 else n*fact n-1 O n stack. Iterative loop O 1. Stack overflow no base condition infinite. Tail recursion last statement optimize to loop.</div>
<div class='qbox'><b>Q10. File handling r w a r+ w+ a+ rb wb? Count lines code?</b></div><div class='abox'><b>Answer:</b> r read existing fail if not exist, w write create truncate, a append, r+ read+write existing, w+ create, a+ append+read, b binary. Code FILE *fp=fopen data.txt r; int count=0; char ch; while ch=fgetc fp !=EOF if ch newline count++; fclose fp;</div>
<div class='qbox'><b>Q11. Preprocessor macros include define ifdef? Macro vs function?</b></div><div class='abox'><b>Answer:</b> Preprocessor before compilation include copy header define MAX 100 replacement ifdef conditional. Macro vs function macro no type check fast replacement but side effects define SQUARE x x*x SQUARE 2+3 = 2+3*2+3=11 wrong function type safe. Use inline instead.</div>
<div class='qbox'><b>Q12. Array vs Linked List vs Stack vs Queue? When use? Time complexity?</b></div><div class='abox'><b>Answer:</b> Array continuous O1 access On insert middle use fast search employee ID. Linked List nodes scattered On access O1 insert use frequent insert delete browser history. Stack LIFO push pop browser back undo recursion. Queue FIFO enqueue dequeue printer BFS.</div>
<div class='qbox'><b>Q13. Linked list types Singly Doubly Circular? Reverse singly code?</b></div><div class='abox'><b>Answer:</b> Singly next only Head 10 20 NULL, Doubly next prev 10 20 30, Circular last first. Reverse iterative prev NULL curr Head while curr next=curr.next curr.next=prev prev=curr curr=next Head=prev O n O1.</div>
<div class='qbox'><b>Q14. Binary search vs linear search? Code? Condition sorted?</b></div><div class='abox'><b>Answer:</b> Linear On unsorted check each. Binary Olog n sorted only low=0 high=n-1 mid= low+high /2 if arr mid==target return else adjust. 1 lakh sorted find 85 percent 17 steps not 1 lakh.</div>
<div class='qbox'><b>Q15. Sorting Bubble Selection Insertion Quick Merge? Time complexity? Stable?</b></div><div class='abox'><b>Answer:</b> Bubble On2 swap adjacent Selection On2 min find Insertion On2 best On sorted Quick On log n avg On2 worst in-place fast Merge On log n always stable On space. Stable keeps order equal marks.</div>
<div class='qbox'><b>Q16. Bit manipulation and or xor not shift? Check even odd using bit?</b></div><div class='abox'><b>Answer:</b> AND OR XOR NOT shift left *2 right /2. Check even if n and 1 ==0 even else odd last bit 0 even 1 odd. Count set bits while n count+= n and 1 n shift right.</div>
<div class='qbox'><b>Q17. Output questions: 5/2 vs 5.0/2? sizeof int vs sizeof int*? a++ ++a a-- order?</b></div><div class='abox'><b>Answer:</b> 5/2 integer 2, 5.0/2 float 2.5. sizeof int 4 sizeof int* 8 64-bit. a++ ++a a-- order undefined depends compiler right to left but sequence point tricky.</div>
<div class='cat'>Category 3: Coding Problems Q18-Q35</div>
<div class='qbox'><b>Q18. Reverse string without library, palindrome, anagram?</b></div><div class='abox'><b>Answer:</b> Reverse two pointers i=0 j=len-1 swap till i less j. Palindrome reverse compare or two pointers. Anagram sort both compare or frequency array 26 count.</div>
<div class='qbox'><b>Q19. Second largest without sorting? Missing number?</b></div><div class='abox'><b>Answer:</b> Second largest first max second second_max one pass if x greater than max second=max max=x else if x greater than second and x !=max second=x On. Missing number 1 to n size n-1 sum expected n n+1 /2 - actual On.</div>
<div class='qbox'><b>Q20-Q35: Prime Armstrong Fibonacci factorial, count vowels consonants words remove duplicates, transpose matrix multiplication spiral, stack using array queue using two stacks infix to postfix, linked list insertion deletion middle loop detection merge, binary tree height BST search etc. 15 plus coding patterns.</b></div><div class='abox'>Practice all on code runner right side. Vowels sum 1 for c in aeiou, words spaces+1, duplicates frequency array, transpose rows to cols matrix i j = matrix j i, multiplication triple loop On3, spiral top right bottom left shrink boundaries, stack array top=-1 push top++ arr top = x pop arr top--, queue two stacks enqueue stack1 dequeue if stack2 empty pop all stack1 to stack2 pop stack2, insertion newNode next=Head Head=newNode O1, middle slow fast slow 1 fast 2 when fast null slow middle, merge compare link, tree height 1+max left right, BST left less than root less than right O log n. All Top 35 coding for TCS.</div>
"""
    if skill == "Java":
        return """
<div class='cat'>Java Interview - Top 40 Questions - TCS, Infosys, Amazon, Google, Product Companies</div>
<div class='cat'>Category 1: Core Java Basics Q1-Q10</div>
<div class='qbox'><b>Q1. Why Java platform independent? JVM JRE JDK bytecode WORA? C++ vs Java?</b></div><div class='abox'><b>Answer:</b> Java compiles to bytecode class not machine code JVM runs any OS Windows Linux Mac WORA. JDK=JRE plus dev tools javac JRE=JVM plus libraries. JDK for dev JRE for running only. C++ needs recompile per OS platform dependent. C++ manual memory Java auto GC. C++ multiple inheritance Java single via interface.</div>
<div class='qbox'><b>Q2. OOP 4 Pillars real example code? Encapsulation Inheritance Polymorphism Abstraction? Is-a vs Has-a?</b></div><div class='abox'><b>Answer:</b> Encapsulation private data public getter setter bank balance private validation. Inheritance Dog extends Animal reuses is-a Dog is Animal. Polymorphism same method different behavior overloading compile time add int add double overriding runtime Dog sound bark vs Animal generic. Abstraction abstract class interface hides Car engine hidden you drive. Has-a Car has Engine composition. Student has Placement.</div>
<div class='qbox'><b>Q3. String vs StringBuilder vs StringBuffer? Why String immutable? String pool? == vs equals?</b></div><div class='abox'><b>Answer:</b> String immutable every concat creates new object 10000 loops 10000 objects waste. StringBuilder mutable fast not synchronized use loops building resume. StringBuffer mutable synchronized thread-safe slower. String pool heap stores literals String s1=Java s2=Java same reference s1==s2 true new String Java new object heap s1==s2 false but s1.equals s2 true content. == reference equals content. Pool saves memory.</div>
<div class='qbox'><b>Q4. ArrayList vs LinkedList vs Vector vs CopyOnWriteArrayList? When use? Time complexity internal working?</b></div><div class='abox'><b>Answer:</b> ArrayList dynamic array O1 get On insert middle shift array resize 1.5x use for reading searching TCS employee list. LinkedList doubly nodes On get O1 insert use frequent insert delete. Vector synchronized legacy slow. CopyOnWriteArrayList thread-safe copy on write read heavy. Internally ArrayList Object array. Code ArrayList String list=new ArrayList; list.add TCS;</div>
<div class='qbox'><b>Q5. HashMap vs HashTable vs ConcurrentHashMap vs TreeMap vs LinkedHashMap? How HashMap works internally? hashCode bucket collision load factor treeify?</b></div><div class='abox'><b>Answer:</b> HashMap key-value non-synchronized null allowed one null key many null values O1 avg. HashTable synchronized null not allowed legacy. ConcurrentHashMap thread-safe segment locking Java 8 CAS. TreeMap sorted by key Olog n Red-Black tree. LinkedHashMap insertion order. Internal key.hashCode to bucket index hash and n-1 if collision linked list after 8 elements treeify tree. Load factor 0.75 resize double. Example put Bhav 90 hash 123 index 5 store get same hash O1 avg On worst all same bucket. Amazon Google 100 percent.</div>
<div class='qbox'><b>Q6. Exception handling? Checked vs unchecked? try catch finally throw vs throws? Custom exception? How finally works even after return?</b></div><div class='abox'><b>Answer:</b> try risky catch handle finally always executes even after return used to close DB connection file. throw you throw exception throw new Exception Not eligible throws method declares may throw void apply throws Exception. Checked compile time IOException must handle unchecked runtime NullPointer. Custom exception extends Exception. Finally executes after return because return value saved then finally then actual return if finally has return overrides try return.</div>
<div class='qbox'><b>Q7. Multithreading? How to create thread extends Thread vs implements Runnable? start vs run? sleep vs wait vs yield? Synchronization? Deadlock?</b></div><div class='abox'><b>Answer:</b> Multiple threads parallel. Create extends Thread or implements Runnable second better multiple inheritance. Start creates new thread calls run run direct no new thread same thread. Sleep pauses timed wait releases lock waits for notify yield hints scheduler. Synchronization synchronized prevents two threads accessing same bank account same time Without sync balance 1000 two threads withdraw 500 both see 1000 final 500 instead of 0 race condition. Deadlock two threads waiting each other lock Thread1 lock A waiting B Thread2 lock B waiting A avoid lock ordering.</div>
<div class='qbox'><b>Q8. Overloading vs Overriding? Rules? Can overload main? Override static? covariant return? Override annotation?</b></div><div class='abox'><b>Answer:</b> Overloading same class same name different params number type order compile time add int add double can overload main but JVM calls only original main String args. Overriding child redefines parent runtime same signature Dog sound bark vs Animal generic rules access modifier cannot be more restrictive return type covariant child type allowed private static final cannot override static hides not override. Use Override annotation compile time check.</div>
<div class='qbox'><b>Q9. Interface vs Abstract class? When use? Java 8 default methods? Multiple inheritance? Functional interface? Marker interface?</b></div><div class='abox'><b>Answer:</b> Abstract class abstract plus concrete methods variables constructor single inheritance extends is-a Dog is Animal. Interface only abstract methods Java 8 default static methods multiple implements can-do Flyable. Use abstract when is-a relation interface when can-do capability. Functional interface single abstract method lambda Runnable. Marker interface no methods Serializable Cloneable tells JVM special handling. Spring uses interfaces.</div>
<div class='qbox'><b>Q10. Collections hierarchy? List Set Map Queue Deque? Comparable vs Comparator? Fail-fast vs Fail-safe? How sort custom objects?</b></div><div class='abox'><b>Answer:</b> Collection interface List ordered duplicate Set unique Map key-value not Collection. List ArrayList LinkedList Set HashSet LinkedHashSet TreeSet sorted Map HashMap etc Queue PriorityQueue Deque ArrayDeque. Comparable natural ordering compareTo inside class Comparator external custom compare. Fail-fast throws ConcurrentModificationException when modifying while iterating ArrayList Fail-safe works on copy CopyOnWriteArrayList. Sort custom Student by avg implement Comparable or Comparator Collections.sort list a,b -> a.avg-b.avg.</div>
<div class='cat'>Category 2: Advanced Java and Frameworks Q11-Q25</div>
<div class='qbox'><b>Q11. JDBC Steps? Driver types? Statement vs PreparedStatement vs CallableStatement? How prevent SQL injection?</b></div><div class='abox'><b>Answer:</b> JDBC Java Database Connectivity Steps Load driver Class.forName com.mysql.cj.jdbc.Driver Connection con=DriverManager.getConnection url user pass Statement st=con.createStatement ResultSet rs=st.executeQuery SELECT * FROM students while rs.next process con.close. Types Type1 JDBC-ODBC bridge Type2 Native Type3 Network Type4 Thin pure Java mostly used. Statement static SQL PreparedStatement precompiled parameterized faster prevents SQL injection SELECT * FROM users WHERE name=? setString prevents OR 1=1 injection. CallableStatement calls stored procedures.</div>
<div class='qbox'><b>Q12. Spring, Spring Boot? Dependency Injection? IoC? Annotations? How create REST API? Microservices?</b></div><div class='abox'><b>Answer:</b> Spring framework DI IoC Inversion of Control you dont create object Spring creates injects Autowired UserService service instead of new. Benefits loose coupling easy testing. Spring Boot makes microservices easy auto-configuration embedded Tomcat. Annotations SpringBootApplication RestController Service Repository GetMapping PostMapping. Create REST API for BhavPath RestController class StudentController GetMapping students List Student getAll. Microservices small independent services communicate via REST. TCS Infosys uses Spring Boot.</div>
<div class='qbox'><b>Q13. Garbage collection? Types? How works? Mark and sweep? Generations Young Old Permanent? Can force GC? finalize?</b></div><div class='abox'><b>Answer:</b> JVM auto deletes unused objects Suggest System.gc not force Works mark and sweep marks reachable from GC roots sweeps unreachable Generations Young Eden Survivor Old long-lived Permanent metadata Java 8 Metaspace Types Serial Parallel CMS G1 Benefit no memory leak like C finalize called by GC before delete deprecated.</div>
<div class='qbox'><b>Q14. Final finally finalize? final variable method class? What is immutable class? How create?</b></div><div class='abox'><b>Answer:</b> final variable cannot change constant final int MAX=100 method cannot override class cannot extend String is final finally block always executes for closing resources even after return if finally has return overrides try return finalize method called by GC before deleting Immutable class cannot change after creation String immutable steps final class private final fields no setters constructor sets getter returns copy if mutable Use security thread-safe.</div>
<div class='qbox'><b>Q15. Singleton pattern? Write thread-safe singleton? Double-checked locking? Enum singleton? Where used?</b></div><div class='abox'><b>Answer:</b> Only one object exists like DB connection config logger Basic private static Singleton instance private constructor public static Singleton getInstance if instance==null instance=new Singleton return instance. Thread-safe synchronized method slow or double-checked locking if instance==null synchronized Singleton class if instance==null instance=new Singleton. Best enum singleton enum Singleton INSTANCE thread-safe serialization safe Amazon asks design patterns.</div>
<div class='qbox'><b>Q16-Q25: Java 8 features lambda streams functional interface default methods Optional Date Time API Serialization Cloning deep vs shallow equals hashCode contract memory areas heap stack method area class loader etc.</b></div><div class='abox'>Lambda anonymous a,b -> a+b Streams filter map reduce for placement data students.stream filter s avg greater than 75 collect Optional avoids NullPointer Optional.ofNullable name orElse Default Serialization converts object to bytes implements Serializable for saving file network Cloning shallow copies reference deep copies full object equals hashCode contract if equals true hashCode must same else HashMap fails Memory heap objects stack local vars references method area class metadata Class loader loads class Practice code runner right side.</div>
<div class='cat'>Category 3: Coding Questions Java Q26-Q40</div>
<div class='qbox'><b>Q26. Reverse string palindrome anagram count words first non-repeating? Write code without library?</b></div><div class='abox'><b>Answer:</b> Reverse new StringBuilder str reverse or two pointers Palindrome str.equals reverse Anagram sort char arrays Arrays.sort or frequency array 26 count Count words split by space First non-repeating frequency map then traverse Code Map Character Integer map=new HashMap; for char c str.toCharArray map.put c map.getOrDefault c 0 plus 1; TCS coding.</div>
<div class='qbox'><b>Q27. Two sum three sum find duplicate missing second largest without sorting?</b></div><div class='abox'><b>Answer:</b> Two sum HashMap On seen map if target-num in map return Three sum sort plus two pointers On2 Duplicate Floyd cycle or HashSet Missing sum expected n n+1 /2 - sum actual or XOR Second largest single pass max second_max Practice on right side runner.</div>
<div class='qbox'><b>Q28. Linked list reverse detect loop middle merge two sorted lists? Stack using array queue using two stacks?</b></div><div class='abox'><b>Answer:</b> Reverse iterative prev null curr head while curr next=curr.next curr.next=prev prev=curr curr=next head=prev Loop Floyd slow fast meet Middle slow fast when fast null slow middle Merge two sorted compare heads link smaller Stack array top=-1 push plus plus top arr top = x pop arr top-- Queue using two stacks enqueue push stack1 dequeue if stack2 empty pop all stack1 to stack2 pop stack2.</div>
<div class='qbox'><b>Q29-Q40: Binary search quick sort merge sort tree traversals inorder preorder postorder BFS DFS binary tree height BST validation DP fibonacci knapsack LCS etc.</b></div><div class='abox'>All Top 50 coding questions pattern for product based companies Binary search O log n sorted Sorting quick O n log n avg merge always O n log n stable Tree inorder Left Root Right BST sorted preorder copy postorder delete BFS queue level shortest DFS recursion deep path Height 1 plus max left right BST left less than root less than right validate LCA BST if both less than root go left both greater than root go right else root is LCA DP fibonacci memoization cache vs tabulation array Knapsack max value weight limit LCS dp i j if text1 i-1 == text2 j-1 dp i j = dp i-1 j-1 plus 1 else max dp i-1 j dp i j-1 etc Practice all on code runner.</div>
"""
    if skill == "Python":
        return """
<div class='cat'>Python Interview - Top 35 Questions - TCS, Infosys, Amazon, Data Science, Django</div>
<div class='cat'>Category 1: Core Python Q1-Q12</div>
<div class='qbox'><b>Q1. List vs Tuple vs Set vs Dict vs Frozenset? Mutable vs immutable? Hashable? Time complexity? When use?</b></div><div class='abox'><b>Answer:</b> List mutable ordered duplicate 1 2 2 O1 access On search index allow use scores 85 90. Tuple immutable ordered 1 2 faster hashable can be dict key 1 2 QIS use fixed coordinates. Set unordered unique 1 2 O1 search no duplicate use unique skills. Dict key-value Python 90 O1 key must be hashable immutable. Frozenset immutable set hashable can be dict key. List for dynamic tuple for fixed set for unique dict for mapping.</div>
<div class='qbox'><b>Q2. args vs kwargs? How to use? Write function that accepts any number of args? What is unpacking?</b></div><div class='abox'><b>Answer:</b> args tuple positional unlimited def add args sum args call add 1 2 3. kwargs dict keyword def func kwargs for k v in kwargs.items call func name Bhav college QIS. Unpacking list to args my_list 1 2 3 add *my_list. Dict to kwargs my_dict name Bhav func **my_dict. Use when dont know how many args placement function receives. Very common Django.</div>
<div class='qbox'><b>Q3. Decorator, Generator, Iterator, GIL? Write decorator for logging? Generator for large file?</b></div><div class='abox'><b>Answer:</b> Decorator wraps function adds behavior without modifying login_required def my_func. Code def my_decorator func def wrapper print Before func print After return wrapper. Generator yields one by one saves memory def gen yield 1 yield 2 for large file 1GB not load all for line in open file yield line. Iterator iter next. GIL only one thread executes Python bytecode at a time CPU-bound threading not faster but IO-bound ok use multiprocessing for CPU.</div>
<div class='qbox'><b>Q4. OOP in Python? self, init, inheritance, multiple inheritance, super, overloading overriding? What is MRO?</b></div><div class='abox'><b>Answer:</b> self current object like this Java. init constructor def init self name self.name=name. Inheritance class Student Person. Multiple inheritance class C A B MRO Method Resolution Order order search parent C A B object uses C3 linearization super calls parent. Overloading Python doesn't support same name different params last defined wins use args to simulate overriding child redefines parent. Code super init calls parent. TCS Digital asks.</div>
<div class='qbox'><b>Q5. Shallow copy vs deep copy? What is copy module? What happens if list contains mutable objects?</b></div><div class='abox'><b>Answer:</b> Shallow copy copies reference top level only list2=list1.copy or list1 inner mutable still shared list1 1 2 list2=list1.copy list1 0 0 =99 list2 also 99 because inner list shared. Deep copy copies full recursively import copy copy.deepcopy list1 list2 independent. Use deepcopy when nested mutable. Important for placement data copying.</div>
<div class='qbox'><b>Q6. Lambda, map, filter, reduce, list comprehension? Which faster? Write examples?</b></div><div class='abox'><b>Answer:</b> Lambda anonymous lambda x x+10. Map applies function to each list map lambda x x*2 1 2 3 -> 2 4 6. Filter filters map filter lambda x x greater than 2 1 2 3 -> 3. Reduce reduces to single from functools import reduce reduce lambda a b a+b 1 2 3 ->6. List comprehension x*x for x in range 5 if x percent 2 ==0 faster than map filter Pythonic. For placement scores squares = s*s for s in scores.</div>
<div class='qbox'><b>Q7. Exception handling try except else finally? Custom exception? What is else block?</b></div><div class='abox'><b>Answer:</b> try risky except handles else executes if no exception finally always executes close file. Code try x=10/0 except ZeroDivisionError print Divide by zero else print No error finally print Always. Custom exception class MyError Exception pass raise MyError Not eligible. Use for validation.</div>
<div class='qbox'><b>Q8. File handling? With open? r w a r+? How to read large file without loading fully?</b></div><div class='abox'><b>Answer:</b> With open auto close with open data.txt r as f data=f.read. r read existing w write create truncate a append r+ read+write b binary. Large file don't read all at once use for line in file process line or generator yield line saves memory 1GB file not load fully. TCS asks file handling.</div>
<div class='qbox'><b>Q9. What is Django vs Flask vs FastAPI? REST API? ORM? How to create API? What is middleware?</b></div><div class='abox'><b>Answer:</b> Flask micro simple small API Django full batteries ORM admin auth FastAPI modern fast async automatic docs. For BhavPath small API Flask enough full website Django high performance FastAPI. REST API HTTP GET POST PUT DELETE JSON GET api students returns name Bhav. ORM Object Relational Mapping Student.objects.filter avg greater than 75 instead of SQL. Middleware processes request before view like authentication logging. TCS uses Django.</div>
<div class='qbox'><b>Q10-Q12: Pandas vs Python list? NumPy vs list? Why NumPy faster? Vectorization? DataFrame operations? GIL impact on multithreading vs multiprocessing?</b></div><div class='abox'>Pandas DataFrame for tabular placement data pd.DataFrame faster operations vectorized C. NumPy array 10x faster than Python list because C array contiguous type same no type checking. Vectorization operation on whole array without loop np.array 1 2 3 *2 -> 2 4 6 fast. GIL only one thread executes Python bytecode CPU-bound threading not faster use multiprocessing Process for CPU parallelism. IO-bound threading ok. Data science uses Pandas NumPy.</div>
<div class='cat'>Category 2: Advanced and Coding Q13-Q35</div>
<div class='qbox'><b>Q13. Reverse string, palindrome, anagram, count vowels, first non-repeating, remove duplicates without set? Write code.</b></div><div class='abox'><b>Answer:</b> Reverse str slicing or two pointers. Palindrome str==str slicing. Anagram sorted str1==sorted str2 or Counter. Count vowels sum 1 for c in str if c in aeiou. First non-repeating frequency dict then traverse. Remove duplicates without set preserve order result empty list result.append x for x in arr if x not in result On2 or use dict.fromkeys On. All TCS coding round.</div>
<div class='qbox'><b>Q14. Two sum, three sum, find duplicate, missing number, second largest, rotate array? On solutions?</b></div><div class='abox'><b>Answer:</b> Two sum HashMap seen if target-num in seen return. Three sum sort plus two pointers On2. Duplicate Floyd or set. Missing sum expected n n+1 /2 - actual or XOR. Second largest single pass. Rotate array k times arr -k plus arr :-k On or reverse thrice. Practice on right side runner.</div>
<div class='qbox'><b>Q15-Q35: Linked list reverse middle loop detection, stack queue using list, binary search, quick sort merge sort, tree traversals BFS DFS, binary tree height, BST, DP fibonacci knapsack LCS, binary search etc. 20 plus Top coding patterns for product companies.</b></div><div class='abox'>All Top 30 coding patterns Linked list reverse iterative prev curr next middle slow fast slow 1 fast 2 when fast null slow middle loop Floyd slow fast meet stack list append pop queue deque popleft or two stacks binary search O log n sorted low high mid sorting quick O n log n avg merge always O n log n stable tree inorder Left Root Right BST sorted preorder copy postorder delete BFS queue level shortest DFS recursion deep height 1 plus max left right BST left less than root less than right DP fibonacci memoization cache vs tabulation array knapsack max value weight limit LCS longest common subsequence dynamic programming etc Practice all on code runner right side Amazon Google level questions.</div>
"""
    if skill == "SQL":
        return """
<div class='cat'>SQL Interview - Top 35 Questions - TCS, Infosys, Amazon, Data Engineering</div>
<div class='cat'>Category 1: Basics Q1-Q12</div>
<div class='qbox'><b>Q1. WHERE vs HAVING? Can we use aggregate in WHERE? Write example with GROUP BY?</b></div><div class='abox'><b>Answer:</b> WHERE filters rows before GROUP BY SELECT * FROM students WHERE avg greater than 75. HAVING filters groups after GROUP BY SELECT college COUNT FROM students GROUP BY college HAVING COUNT greater than 50. WHERE cannot use aggregate COUNT AVG because rows not grouped yet HAVING can. Example BhavPath Find colleges with more than 50 students avg greater than 75 SELECT college COUNT FROM students WHERE avg greater than 75 GROUP BY college HAVING COUNT greater than 50. TCS SQL round 100 percent.</div>
<div class='qbox'><b>Q2. Explain all JOINs with Venn diagram? INNER, LEFT, RIGHT, FULL, CROSS, SELF? Write query for BhavPath to find not placed students?</b></div><div class='abox'><b>Answer:</b> INNER only matching both students who have placement. LEFT all left plus matching right all students even if no placement NULL. RIGHT opposite. FULL both sides all. CROSS cartesian 5 students x 3 companies=15 rows. SELF join same table manager employee. Query not placed SELECT s.name FROM students s LEFT JOIN placements p ON s.id=p.student_id WHERE p.student_id IS NULL. Diagram two circles overlapping=INNER left circle full=LEFT. Important.</div>
<div class='qbox'><b>Q3. What is index? Clustered vs Non-clustered? Unique vs Composite? When index slows? Write CREATE INDEX?</b></div><div class='abox'><b>Answer:</b> Index speeds search On to O log n like book index B-Tree. Clustered rearranges physical data one per table PK. Non-clustered separate copy many per table. Unique enforces uniqueness email composite multiple columns college avg. Index slows insert update because index also updated. CREATE INDEX idx_avg ON students avg; CREATE UNIQUE INDEX idx_email ON students email; For BhavPath avg search fast 1 lakh rows 1 sec to 0.01 sec. Amazon asks.</div>
<div class='qbox'><b>Q4. Normalization? 1NF, 2NF, 3NF, BCNF? Denormalization? Why normalize? Example BhavPath?</b></div><div class='abox'><b>Answer:</b> Removes redundancy saves storage. 1NF atomic no array in cell no multi-value. 2NF no partial dependency student table id course course_fee fee depends only on course not id split into student and course tables. 3NF no transitive student college college_city city depends on college not student split college table. BCNF stricter. Denormalization adds redundancy for performance reporting. BhavPath students and colleges separate normalized.</div>
<div class='qbox'><b>Q5. Subquery vs JOIN vs CTE vs Window? Which faster? Correlated vs non-correlated? Write query avg greater than overall avg?</b></div><div class='abox'><b>Answer:</b> Subquery inside query SELECT * FROM students WHERE avg greater than SELECT AVG avg FROM students. JOIN combines tables usually faster optimizer uses index subquery per row correlated slow. CTE Common Table Expression WITH avg_cte AS SELECT AVG avg as avg FROM students SELECT * FROM students avg_cte WHERE students.avg greater than avg_cte.avg readable. Window functions ROW_NUMBER etc. Correlated subquery depends on outer query SELECT * FROM students s1 WHERE avg greater than SELECT AVG avg FROM students s2 WHERE s2.college=s1.college per college avg. Non-correlated independent. Use JOIN generally faster.</div>
<div class='qbox'><b>Q6. What is primary key, foreign key, unique key, composite key, candidate key? Difference?</b></div><div class='abox'><b>Answer:</b> Primary key unique not null one per table id foreign key references other table student college_id references college id unique key unique can be null one or many composite key multiple columns together unique student_id subject_id candidate key all possible PKs email id both candidate one becomes primary. PK enforces entity integrity FK referential integrity.</div>
<div class='qbox'><b>Q7. What is ACID? Atomicity, Consistency, Isolation, Durability? Transaction? COMMIT ROLLBACK SAVEPOINT? Isolation levels?</b></div><div class='abox'><b>Answer:</b> ACID for banking transaction Atomicity all or nothing transfer 500 from A to B both debit credit or none Consistency valid state Isolation concurrent transactions don't interfere Durability once committed persists even crash Transaction BEGIN COMMIT makes permanent ROLLBACK undo SAVEPOINT partial rollback Isolation levels Read Uncommitted dirty read Read Committed no dirty Repeatable Read no non-repeatable Serializable no phantom. Use for placement fee payment.</div>
<div class='qbox'><b>Q8. Window functions? ROW_NUMBER vs RANK vs DENSE_RANK vs LEAD LAG? Write query top 3 students per college?</b></div><div class='abox'><b>Answer:</b> ROW_NUMBER unique sequential 1 2 3 4 even same avg RANK same avg same rank gaps 1 1 3 DENSE_RANK same rank no gaps 1 1 2 LEAD next row LAG previous row Top 3 per college SELECT * FROM SELECT name college avg ROW_NUMBER OVER PARTITION BY college ORDER BY avg DESC as rn FROM students WHERE rn less than =3. PARTITION BY college groups. Very important for Amazon data roles.</div>
<div class='qbox'><b>Q9. GROUP BY vs DISTINCT vs ORDER BY? Can use GROUP BY without aggregate? Having without GROUP BY?</b></div><div class='abox'><b>Answer:</b> GROUP BY groups rows aggregate COUNT SUM AVG SELECT college COUNT FROM students GROUP BY college. DISTINCT removes duplicate rows SELECT DISTINCT college FROM students. ORDER BY sorts SELECT * FROM students ORDER BY avg DESC. GROUP BY without aggregate possible but useless MySQL allows. HAVING without GROUP BY treats whole table as one group SELECT COUNT FROM students HAVING COUNT greater than 5. ORDER BY after GROUP BY HAVING.</div>
<div class='qbox'><b>Q10. Stored Procedure vs Function vs Trigger vs View? Write example?</b></div><div class='abox'><b>Answer:</b> Procedure can have IN OUT params no return mandatory can have transactions CALL procedure. Function must return single value SELECT function. Trigger auto executes on INSERT UPDATE DELETE BEFORE AFTER CREATE TRIGGER before_insert BEFORE INSERT ON students FOR EACH ROW SET NEW.created_at=NOW. View virtual table SELECT * FROM view simplifies security CREATE VIEW high_avg AS SELECT * FROM students WHERE avg greater than 75. Procedure for complex logic placement eligibility.</div>
<div class='qbox'><b>Q11-Q12: UNION vs UNION ALL vs INTERSECT vs EXCEPT? Difference? NULL handling? COUNT star vs COUNT col vs COUNT DISTINCT col?</b></div><div class='abox'>UNION combines removes duplicate UNION ALL keeps duplicate faster INTERSECT common rows EXCEPT first minus second MySQL no INTERSECT use IN. NULL unknown comparison NULL=NULL false use IS NULL. COUNT star counts all rows including NULL COUNT col counts non-NULL of that column COUNT DISTINCT col counts unique non-NULL. Important for data analysis.</div>
<div class='cat'>Category 2: Advanced and Coding SQL Q13-Q35</div>
<div class='qbox'><b>Q13. Write query to find second highest salary avg without LIMIT? With LIMIT? Nth highest?</b></div><div class='abox'><b>Answer:</b> Without LIMIT SELECT MAX avg FROM students WHERE avg less than SELECT MAX avg FROM students. With LIMIT SELECT DISTINCT avg FROM students ORDER BY avg DESC LIMIT 1 OFFSET 1 MySQL. Nth highest SELECT DISTINCT avg FROM students ORDER BY avg DESC LIMIT 1 OFFSET N-1 or window SELECT * FROM SELECT avg DENSE_RANK OVER ORDER BY avg DESC as r FROM students WHERE r=N. Top asked TCS.</div>
<div class='qbox'><b>Q14. Write query to find duplicate records? Delete duplicates? Find not placed students?</b></div><div class='abox'><b>Answer:</b> Duplicate SELECT email COUNT FROM students GROUP BY email HAVING COUNT greater than 1. Delete duplicates keep min id DELETE FROM students WHERE id NOT IN SELECT MIN id FROM students GROUP BY email. Not placed LEFT JOIN SELECT s.name FROM students s LEFT JOIN placements p ON s.id=p.student_id WHERE p.student_id IS NULL. Or NOT IN SELECT name FROM students WHERE id NOT IN SELECT student_id FROM placements.</div>
<div class='qbox'><b>Q15. Write query for department wise highest salary, college wise topper, etc?</b></div><div class='abox'><b>Answer:</b> College wise topper SELECT college name avg FROM SELECT college name avg RANK OVER PARTITION BY college ORDER BY avg DESC as rnk FROM students WHERE rnk=1. Or correlated SELECT * FROM students s1 WHERE avg = SELECT MAX avg FROM students s2 WHERE s2.college=s1.college. Use window functions modern approach.</div>
<div class='qbox'><b>Q16-Q35: Self join manager employee, find managers with more than 5 reportees, cumulative sum, running total, moving average, pivot rows to columns, unpivot, recursive CTE for hierarchy, etc. 20 plus advanced queries for data engineering roles.</b></div><div class='abox'>Self join SELECT e.name as employee m.name as manager FROM employees e JOIN employees m ON e.manager_id=m.id. Managers with greater than 5 reportees SELECT manager_id COUNT FROM employees GROUP BY manager_id HAVING COUNT greater than 5. Cumulative sum SELECT id avg SUM avg OVER ORDER BY id as running_total. Moving avg AVG avg OVER ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW. Pivot CASE WHEN college=QIS THEN avg END. Recursive CTE for employee hierarchy. Practice all on right side Python Pandas simulates SQL.</div>
"""
    if skill == "DSA":
        return """
<div class='cat'>DSA Interview - Top 50 Questions - Must for Amazon, Google, Microsoft, Product Companies - Patterns Wise</div>
<div class='cat'>Pattern 1: Array and Hashing Q1-Q10</div>
<div class='qbox'><b>Q1. Two Sum, Three Sum, Four Sum, Subarray sum equals K? On HashMap? Two pointers? Explain all variants with code.</b></div><div class='abox'><b>Answer:</b> Two Sum On HashMap seen if target-num in seen return. Example 2 7 11 15 target 9 -> 0 1. Three Sum sort On2 two pointers left right sum==0 store if sum less than 0 left++ else right-- skip duplicates. Four Sum similar On3. Subarray sum K prefix sum hashmap count prefixSum-K exists. Pattern HashMap for O1 look up. Most asked Amazon.</div>
<div class='qbox'><b>Q2. Contains duplicate, duplicate II, find duplicate number Floyd, first missing positive? On O1 space?</b></div><div class='abox'><b>Answer:</b> Contains duplicate set len set vs list. Duplicate II k distance HashMap store last index check i-map num less than =k. Find duplicate Floyd cycle detection array as linked list 1..n duplicate creates cycle slow fast meet then find entrance. First missing positive On O1 space place each number at its index arr i should be i+1 swap. Example 3 4 -1 1 -> 1 -1 3 4 first missing 2.</div>
<div class='qbox'><b>Q3. Product of array except self On without division? Prefix suffix? Maximum subarray Kadane? Maximum product subarray?</b></div><div class='abox'><b>Answer:</b> Product except self On without division prefix i=product 0..i-1 suffix i=product i+1..n-1 result=prefix*suffix. Example 1 2 3 4 prefix 1 1 2 6 suffix 24 12 4 1 result 24 12 8 6. Kadane max subarray currentSum=max num currentSum+num maxSum=max maxSum currentSum On. Max product track max and min because negative negative positive.</div>
<div class='qbox'><b>Q4. Best time to buy sell stock I II III? At most one transaction, multiple, at most two? DP? Explain?</b></div><div class='abox'><b>Answer:</b> I one transaction minPrice track maxProfit=max maxProfit price-minPrice On. II multiple transactions sum all positive differences if price i greater than price i-1 profit+=difference. III at most two transactions DP four variables buy1 sell1 buy2 sell2. Pattern DP for stock problems. Amazon asks.</div>
<div class='qbox'><b>Q5. Rotate array by K, rotate image 90 degrees, spiral matrix, set matrix zeroes? O1 space tricks?</b></div><div class='abox'><b>Answer:</b> Rotate array K arr -K plus arr :-K On or reverse thrice reverse whole reverse first K reverse rest O1 space. Rotate image 90 clockwise transpose then reverse each row. Spiral matrix boundaries top bottom left right shrink. Set matrix zeroes O1 space use first row col as marker. Tricks for O1 space.</div>
<div class='qbox'><b>Q6-Q10: Merge intervals, insert interval, non-overlapping intervals, meeting rooms I II, longest consecutive sequence On set, etc.</b></div><div class='abox'>Merge intervals sort by start merge overlapping if current.start less than =prev.end prev.end=max prev.end curr.end. Insert interval similar. Non-overlapping remove minimum intervals sort by end greedy. Meeting rooms I check overlap sort start II min rooms priority queue end times. Longest consecutive set On for num in set if num-1 not in set start sequence count while num+1 in set. Patterns for intervals.</div>
<div class='cat'>Pattern 2: Two Pointers, Sliding Window, Binary Search Q11-Q20</div>
<div class='qbox'><b>Q11. Valid palindrome, palindrome II at most one deletion, container with most water, trapping rain water? Two pointers pattern?</b></div><div class='abox'><b>Answer:</b> Valid palindrome two pointers left right while left less than right if s left != s right false else left++ right-- On. Palindrome II at most one deletion when mismatch try skip left or skip right check palindrome. Container with most water left right area= right-left * min height left height right move smaller height On. Trapping rain water left max right max two pointers or prefix max. Two pointers pattern for palindrome area.</div>
<div class='qbox'><b>Q12. Longest substring without repeating characters, minimum window substring, longest repeating character replacement? Sliding window pattern?</b></div><div class='abox'><b>Answer:</b> Sliding window left right plus set map. Longest without repeating right expands set add if duplicate left shrink until no duplicate maxLen=max maxLen right-left+1 On. Minimum window substring need all chars of t map count need formed. Longest repeating replacement max count of same char in window windowSize-maxCount less than =k valid else shrink left. Pattern sliding window for substring.</div>
<div class='qbox'><b>Q13. Binary search, search in rotated sorted array, find minimum in rotated, search 2D matrix? Binary search pattern?</b></div><div class='abox'><b>Answer:</b> Binary search sorted O log n low high mid. Rotated sorted array 4 5 6 7 0 1 2 one side sorted check if left sorted if target in left sorted search left else right. Find minimum rotated if arr mid greater than arr right min in right else left. Search 2D matrix treat as 1D binary search mid cols mid percent cols. Pattern binary search for sorted rotated.</div>
<div class='qbox'><b>Q14-Q20: Koko eating bananas, ship packages, median of two sorted arrays O log min m n hard, etc.</b></div><div class='abox'>Binary search on answer pattern. Koko bananas min speed to eat all in h hours binary search speed 1..maxPile check hours sum ceil pile speed less than =h. Ship packages min capacity to ship in D days binary search capacity maxWeight..sumWeights check days needed. Median two sorted arrays O log min m n partition left max less than = right min hard pattern. Practice binary search on answer.</div>
<div class='cat'>Pattern 3: Linked List, Stack, Queue Q21-Q30</div>
<div class='qbox'><b>Q21. Reverse linked list iterative recursive, reverse between, reverse K group? How to reverse?</b></div><div class='abox'><b>Answer:</b> Reverse iterative prev=None curr=Head while curr next=curr.next curr.next=prev prev=curr curr=next Head=prev On O1 space. Recursive reverse rest head.next.next=head head.next=None. Reverse between left right dummy node prev before left reverse sublist. K group reverse each K nodes if less than K remain as is. Pattern reverse linked list must know.</div>
<div class='qbox'><b>Q22. Detect cycle Floyd, find cycle start, find duplicate Floyd, happy number? Floyd pattern?</b></div><div class='abox'><b>Answer:</b> Floyd tortoise hare slow 1 fast 2 if meet cycle. Find start move one to head both 1 step meet at start proof. Find duplicate array as linked list nums as next pointer duplicate creates cycle. Happy number sum squares digits if cycle not happy if 1 happy use set or Floyd. Pattern Floyd for cycle detection.</div>
<div class='qbox'><b>Q23. Merge two sorted lists, merge K sorted lists heap, reorder list, remove Nth from end? Two pointers?</b></div><div class='abox'><b>Answer:</b> Merge two sorted dummy compare heads link smaller On. Merge K lists heap min-heap push first nodes pop smallest push its next On log K. Reorder list find middle slow fast reverse second half merge alternate. Remove Nth from end two pointers first moves N steps then both move when first null second is before target. Pattern merge two pointers.</div>
<div class='qbox'><b>Q24. Valid parentheses, min stack O1 getMin, daily temperatures, next greater element? Stack pattern?</b></div><div class='abox'><b>Answer:</b> Valid parentheses stack push opening if closing check top matching pop else false. Min stack two stacks one data one min if new less than = min push min stack. Daily temperatures stack indices monotonic decreasing if current temp greater than stack top temp while pop answer pop = currentIndex-popIndex. Next greater similar. Pattern stack for parentheses next greater.</div>
<div class='qbox'><b>Q25-Q30: Implement queue using two stacks, stack using two queues, LRU cache doubly linked list plus hashmap, etc.</b></div><div class='abox'>Queue using two stacks enqueue push stack1 dequeue if stack2 empty pop all stack1 to stack2 pop stack2. Stack using two queues push to queue1 pop all but last to queue2 swap. LRU cache doubly linked list most recent at head hashmap key to node get move to head put if exists move to head else add head if capacity exceeded remove tail. O1 get put. Design questions Amazon.</div>
<div class='cat'>Pattern 4: Tree, Graph, DP Q31-Q50</div>
<div class='qbox'><b>Q31. Tree traversals inorder preorder postorder level order iterative recursive? What is BST? Validate BST? Lowest common ancestor BST?</b></div><div class='abox'><b>Answer:</b> Inorder Left Root Right BST sorted Preorder Root Left Right copy tree Postorder Left Right Root delete tree Level order BFS queue. Iterative inorder stack push left until null pop print go right. BST left less than root less than right. Validate BST inorder sorted or recursion min max range if node.val less than = min or greater than = max false. LCA BST if both less than root go left both greater than root go right else root is LCA. Pattern tree must know.</div>
<div class='qbox'><b>Q32. Maximum depth, diameter, balanced tree, same tree, subtree? Tree DP?</b></div><div class='abox'><b>Answer:</b> Max depth recursive 1 plus max leftDepth rightDepth On. Diameter longest path between any two nodes max of leftDepth plus rightDepth and leftDiameter rightDiameter. Balanced height diff less than =1 for all nodes check height returns -1 if not balanced. Same tree both null true one null false val same and left same right same. Subtree check same tree for each node of main tree. Pattern tree DP bottom up.</div>
<div class='qbox'><b>Q33. BFS DFS, number of islands, clone graph, course schedule topological sort? Graph patterns?</b></div><div class='abox'><b>Answer:</b> BFS queue level by level shortest path unweighted DFS recursion stack deep path. Number of islands grid DFS BFS mark visited count islands O mn. Clone graph hashmap old to new DFS BFS. Course schedule detect cycle topological sort Kahn's BFS indegree 0 queue or DFS cycle detection. Graph patterns BFS DFS topological sort must know.</div>
<div class='qbox'><b>Q34. Dijkstra shortest path, Bellman Ford, Floyd Warshall, Kruskal MST? Shortest path patterns?</b></div><div class='abox'><b>Answer:</b> Dijkstra O E log V non-negative weights priority queue distance array. Bellman Ford O V E handles negative weights detects negative cycle. Floyd Warshall O V3 all pairs. Kruskal MST minimum spanning tree sort edges union-find. Dijkstra for QIS to companies shortest route. Pattern shortest path.</div>
<div class='qbox'><b>Q35-Q50: DP Fibonacci, climbing stairs, house robber, coin change, knapsack 0/1, longest common subsequence, longest increasing subsequence O n log n, edit distance, word break, etc. 15 plus DP patterns must for Google.</b></div><div class='abox'>DP patterns Fibonacci memoization top-down cache dict if n in memo return else tabulation bottom-up dp array On. Climbing stairs dp n = dp n-1 plus dp n-2 like fibonacci. House robber dp i = max dp i-1 dp i-2 plus nums i cannot rob adjacent. Coin change min coins dp amount = min dp amount dp amount-coin plus 1 O amount coins. Knapsack 0/1 max value weight limit dp i w = max dp i-1 w dp i-1 w-weight i plus value i. LCS dp i j if text1 i-1 == text2 j-1 dp i j = dp i-1 j-1 plus 1 else max dp i-1 j dp i j-1. LIS O n log n patience sorting tails array binary search. Edit distance insert delete replace. Word break dp i =True if dp j and s j:i in dict. Must practice 100 plus DP for Google.</div>
"""
    return """
<div class='cat'>C++ Interview - Top 35 Questions - TCS, Infosys, Product Based, Game Development</div>
<div class='cat'>Category 1: Core C++ Q1-Q15</div>
<div class='qbox'><b>Q1. C vs C++? Why C++ better for OOP? Procedural vs OOP? Why superset? Header file?</b></div><div class='abox'><b>Answer:</b> C procedural functions no OOP manual memory malloc free printf scanf not type safe no reference no overloading. C++ procedural plus OOP classes objects inheritance polymorphism STL new delete type safe cin cout type safe reference overloading namespace. C++ better for large projects reusable classes Student Placement. C for OS embedded drivers C++ for games banking browsers. Header file contains declarations include iostream etc.</div>
<div class='qbox'><b>Q2. OOP 4 Pillars code? Encapsulation Inheritance types Polymorphism compile time vs runtime Abstraction? Is-a vs Has-a?</b></div><div class='abox'><b>Answer:</b> Encapsulation class Student private int marks public int getMarks hides data. Inheritance types single class B public A multiple class C public A public B multilevel A B C hierarchical A B A C hybrid. Polymorphism compile time overloading same name different params add int add double and runtime overriding virtual function class Animal virtual void sound class Dog public Animal void sound override cout bark vtable. Abstraction pure virtual virtual void apply =0 abstract class cannot instantiate. Is-a Dog is Animal inheritance Has-a Car has Engine composition.</div>
<div class='qbox'><b>Q3. STL containers vector list deque set map unordered_map stack queue priority_queue time complexity? When use?</b></div><div class='abox'><b>Answer:</b> STL Standard Template Library ready-made containers algorithms iterators. vector dynamic array O1 random access On insert middle contiguous use random access. list doubly linked list On access O1 insert doubly use frequent insert delete. deque double ended O1 both ends. set unique sorted O log n Red-Black tree unordered_set hash O1 avg unique. map key-value sorted O log n unordered_map hash O1 avg key-value. stack LIFO queue FIFO priority_queue max heap O log n. Code vector int v v.push_back 10 sort v.begin v.end map string int m m TCS =90 Saves time coding round.</div>
<div class='qbox'><b>Q4. Pointer vs reference vs smart pointer? this pointer? Dangling? Memory leak?</b></div><div class='abox'><b>Answer:</b> Pointer stores address can be null can reassign int *p=&a; Reference alias cannot be null must be initialized cannot reassign int &r=a; Smart pointer auto delete unique_ptr one owner cannot copy unique_ptr int p=make_unique int 10; shared_ptr multiple owners ref count shared_ptr int p1=make_shared int 10; shared_ptr int p2=p1; count 2 when 0 auto delete weak_ptr breaks cycle. This pointer points to current object this marks. Dangling pointer points freed memory free p p dangling set p NULL. Memory leak malloc without free. Modern C++ prefers smart pointers.</div>
<div class='qbox'><b>Q5. Constructor destructor copy constructor assignment operator move constructor move assignment? Rule of 3 5 0? Shallow vs deep copy?</b></div><div class='abox'><b>Answer:</b> Constructor initializes object Student default Student string name parameterized destructor ~Student cleanup called when object dies. Copy constructor Student const Student and other copies other to new object assignment operator Student and operator= const Student and other copies to existing object move constructor Student Student and and other steals resources other move assignment. Rule of 3 if you define destructor copy constructor copy assignment you need all three Rule of 5 adds move Rule of 0 define none let compiler generate. Shallow copy copies pointer address both point same memory double free deep copy copies actual data new memory.</div>
<div class='qbox'><b>Q6-Q15: Virtual function vtable pure virtual abstract class interface overloading vs overriding static vs dynamic binding diamond problem virtual inheritance namespace templates function vs class exception handling etc.</b></div><div class='abox'>Virtual function runtime polymorphism base pointer points derived calls derived method vtable stores function pointers. Pure virtual =0 abstract class cannot instantiate must override. Interface abstract class with only pure virtual. Overloading compile time same name different params overriding runtime virtual. Static binding compile time overloading dynamic binding runtime virtual. Diamond problem D inherits B and C both inherit A two copies of A ambiguous virtual inheritance class B virtual public A solves one copy. Namespace avoids name collision namespace BhavPath. Templates generic template typename T T add T a T b return a+b works int float function template class template vector T. Exception try catch throw. Practice all.</div>
<div class='cat'>Category 2: Coding C++ Q16-Q35</div>
<div class='qbox'><b>Q16. Reverse string palindrome anagram first non-repeating without library? Use STL?</b></div><div class='abox'><b>Answer:</b> Reverse two pointers i=0 j=len-1 swap or std reverse str.begin str.end. Palindrome reverse compare or two pointers. Anagram sort both sort s1.begin s1.end compare or frequency map. First non-repeating frequency map unordered_map char int then traverse. Code string s=BhavPath reverse s.begin s.end. Use STL for speed coding round.</div>
<div class='qbox'><b>Q17. Two sum three sum find duplicate missing second largest without sorting? Use unordered_map?</b></div><div class='abox'><b>Answer:</b> Two sum unordered_map seen if target-num in seen return. Three sum sort plus two pointers On2. Duplicate set or Floyd. Missing sum expected - actual. Second largest single pass. Use unordered_map O1 avg for fast. Practice on right side runner.</div>
<div class='qbox'><b>Q18-Q35: Linked list reverse middle loop detection merge two sorted stack queue implementation using array STL binary search quick sort merge sort tree traversals inorder preorder postorder BFS DFS binary tree height BST validation DP fibonacci knapsack LCS LIS etc. 18 plus coding patterns product based.</b></div><div class='abox'>All coding patterns same as DSA but C++ STL implementation Linked list struct Node int val Node* next; reverse iterative prev curr next. Stack vector push_back pop_back or std stack queue std queue. Binary search std binary_search. Sorting sort quick sort introsort O n log n avg. Tree Node left right. BFS queue Node* DFS recursion. Height 1 plus max left right. BST validation min max range. DP fibonacci memoization map vs tabulation array knapsack 0/1 dp i w = max dp i-1 w dp i-1 w-weight i plus value i LCS dp i j if same dp i-1 j-1 plus 1 else max dp i-1 j dp i j-1 LIS O n log n tails binary search lower_bound. Practice all on code runner right side C++ logic in Python for now later compile C++.</div>
"""

def get_default_code(skill):
    codes = {
        "C": "# C Interview - Pointer Example\n# Python practice for C concepts\na=10\np=id(a)\nprint(f\"a={a} address={p}\")\nprint(f\"*p (value at address) = {a}\")\narr=[10,20,30,40]\nprint(f\"Array: {arr}\")\ns=list(\"BhavPath\")\ni,j=0,len(s)-1\nwhile i<j:\n    s[i],s[j]=s[j],s[i]\n    i+=1; j-=1\nprint(f\"Reversed: {''.join(s)}\")",
        "Java": "# Java Interview - OOP Example\nclass Animal:\n    def sound(self):\n        print(\"Animal sound\")\nclass Dog(Animal):\n    def sound(self):\n        print(\"Dog barks - Bow Bow\")\ndog=Dog()\ndog.sound()\narray_list=[\"TCS\", \"Infosys\", \"Amazon\"]\nprint(f\"ArrayList: {array_list}\")\narray_list.append(\"Google\")\nprint(f\"After add: {array_list}\")\ndef two_sum(arr, target):\n    seen={}\n    for i,num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\nprint(f\"Two Sum [2,7,11,15] target 9: {two_sum([2,7,11,15], 9)}\")",
        "Python": "# Python - List vs Tuple vs Set vs Dict\nmy_list=[1,2,2,3]\nmy_tuple=(1,2,3)\nmy_set={1,2,3}\nmy_dict={\"Python\":90, \"Java\":85}\nprint(f\"List: {my_list}\")\nprint(f\"Tuple: {my_tuple}\")\nprint(f\"Set: {my_set}\")\nprint(f\"Dict: {my_dict}\")\ndef placement_func(*args, **kwargs):\n    print(f\"args: {args}\")\n    print(f\"kwargs: {kwargs}\")\nplacement_func(\"Python\", \"Java\", name=\"Bhav\", college=\"QIS\")\ns=\"BhavPath\"\nfrom collections import Counter\nfreq=Counter(s)\nfor c in s:\n    if freq[c]==1:\n        print(f\"First non-repeating: {c}\")\n        break\ndef two_sum(arr, target):\n    seen={}\n    for i,num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\nprint(f\"Two Sum: {two_sum([2,7,11,15], 9)}\")",
        "SQL": "# SQL Interview - Pandas style\nimport pandas as pd\nstudents=pd.DataFrame({\"id\":[1,2,3,4,5],\"name\":[\"Bhav\",\"Rahul\",\"Priya\",\"Arjun\",\"Sneha\"],\"avg\":[85,72,90,65,88]})\nprint(students)\nprint(\"\\nWHERE avg>75:\")\nprint(students[students[\"avg\"]>75])\nprint(\"\\nSecond highest avg without LIMIT:\")\nmax_avg=students[\"avg\"].max()\nsecond_max=students[students[\"avg\"]<max_avg][\"avg\"].max()\nprint(second_max)\nplacements=pd.DataFrame({\"student_id\":[1,3,5],\"company\":[\"TCS\",\"Amazon\",\"Infosys\"]})\nmerged=pd.merge(students, placements, left_on=\"id\", right_on=\"student_id\", how=\"left\")\nprint(\"\\nLEFT JOIN not placed (company is NULL):\")\nprint(merged[merged[\"company\"].isna()][[\"name\",\"avg\"]])",
        "DSA": "# DSA - Top patterns\ndef two_sum(arr, target):\n    seen={}\n    for i, num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\narr=[2,7,11,15]\ntarget=9\nprint(f\"Two Sum: {two_sum(arr, target)}\")\ndef binary_search(arr, target):\n    low,high=0,len(arr)-1\n    while low<=high:\n        mid=(low+high)//2\n        if arr[mid]==target:\n            return mid\n        elif arr[mid]<target:\n            low=mid+1\n        else:\n            high=mid-1\n    return -1\nsorted_arr=[10,20,30,40,50,60,70,80,90,100]\nprint(f\"Binary Search find 70: index {binary_search(sorted_arr, 70)}\")\ndef max_subarray(arr):\n    curr=max_sum=arr[0]\n    for num in arr[1:]:\n        curr=max(num, curr+num)\n        max_sum=max(max_sum, curr)\n    return max_sum\nprint(f\"Max subarray [-2,1,-3,4,-1,2,1,-5,4]: {max_subarray([-2,1,-3,4,-1,2,1,-5,4])}\")\nclass Node:\n    def __init__(self, val):\n        self.val=val\n        self.next=None\nhead=Node(10)\nhead.next=Node(20)\nhead.next.next=Node(30)\ncurr=head\nprint(\"Original:\", end=\" \")\nwhile curr:\n    print(curr.val, end=\"->\")\n    curr=curr.next\nprint(\"NULL\")\nprev=None\ncurr=head\nwhile curr:\n    nxt=curr.next\n    curr.next=prev\n    prev=curr\n    curr=nxt\nhead=prev\ncurr=head\nprint(\"Reversed:\", end=\" \")\nwhile curr:\n    print(curr.val, end=\"->\")\n    curr=curr.next\nprint(\"NULL\")",
        "C++": "# C++ STL Simulation\nvector=[]\nvector.append(10)\nvector.append(20)\nprint(f\"Vector: {vector}\")\nmap_dict={\"TCS\":90,\"Infosys\":85}\nprint(f\"Map: {map_dict}\")\nmy_set=set([10,20,10])\nprint(f\"Set: {my_set}\")\nclass Student:\n    def __init__(self, name, avg):\n        self.name=name\n        self.avg=avg\n    def display(self):\n        print(f\"Student: {self.name}, Avg: {self.avg}%\")\ns1=Student(\"Bhav\",85)\ns1.display()\ndef two_sum(arr, target):\n    seen={}\n    for i,num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\nprint(f\"Two Sum: {two_sum([2,7,11,15], 9)}\")\narr=[64,34,25,12,22,11,90]\nprint(f\"Before sort: {arr}\")\narr.sort()\nprint(f\"After sort: {arr}\")"
    }
    return codes.get(skill, codes["C"])

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
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA</p></div></div>""", unsafe_allow_html=True)
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
            st.markdown(f"<div class='detail-box'><h2 style='color:#fef08a;margin-top:0;'>{st.session_state.topic} in {skill}</h2><div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div>", unsafe_allow_html=True)
            st.markdown("---", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:#00ff88;'>Try {skill} Code - Practice and Run</h3>", unsafe_allow_html=True)
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
    st.markdown("""<div class='center' style='padding-top:14vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Interview Zone</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;font-size:18px;'>Crack TCS, Infosys, Amazon, Google - Interview + Code Practice - Top 50 Questions Each Skill</p></div></div>""", unsafe_allow_html=True)
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
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1><p style='color:#a78bfa;'>Top 35-50 Questions Each Skill - Theory plus Coding plus Output Based - With Code Runner</p></div>", unsafe_allow_html=True)
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
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} Interview + Code Practice - Top 50 Qs</h1></div>", unsafe_allow_html=True)
    _,c,_=st.columns([0.05,3,0.05])
    with c:
        col1, col2 = st.columns([1.3, 1])
        with col1:
            content=get_interview_content(skill)
            st.markdown(f"<div class='detail-box'><h3 style='color:#fef08a;margin-top:0;'>Interview Questions - {skill} - Category Wise</h3><div style='color:white;line-height:1.8;font-size:13px;'>{content}</div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='detail-box'><h3 style='color:#00ff88;margin-top:0;'>Code Practice - {skill} - Run Here</h3><p style='color:#a78bfa;font-size:12px;'>Left side questions chadivi, right side code practice chey - Interview + Code in one page</p>", unsafe_allow_html=True)
            default_code=get_default_code(skill)
            code_key=f"iv_code_{skill}"
            if code_key not in st.session_state:
                st.session_state[code_key]=default_code
            code_input=st.text_area("Editor", value=st.session_state[code_key], height=400, key=f"editor_{skill}", label_visibility="collapsed")
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
