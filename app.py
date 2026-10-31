import streamlit as st
import pandas as pd

st.set_page_config(page_title="BhavPath", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.college = "QIS College"
    st.session_state.selected_skill = "C"
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
.qbox{background:rgba(13,74,255,0.14);border-left:4px solid #0d4aff;padding:14px 16px;margin:18px 0 6px 0;border-radius:8px}
.abox{background:rgba(0,255,136,0.09);border-left:4px solid #00ff88;padding:14px 16px;margin:6px 0 22px 0;border-radius:8px}
.cat{background:linear-gradient(90deg,#0d4aff,#ff006a);padding:8px 16px;border-radius:20px;color:white;font-weight:bold;margin:22px 0 12px 0;display:inline-block}
.diag{background:linear-gradient(135deg,#0d1a3a,#1a0a2a);border:1px solid #0d4aff;border-radius:10px;padding:10px;margin:12px 0;color:white;text-align:center;font-size:13px}
.code{background:#0f0f0f;border:1px solid #333;border-radius:8px;padding:12px;margin:10px 0;color:#00ff88;font-family:monospace;font-size:13px;white-space:pre-wrap}
</style>
<div class="bg-blue"></div><div class="bg-pink"></div>
""", unsafe_allow_html=True)

def get_detailed_content(skill, topic):
    html = ""
    html += "<h2 style='color:#fef08a;margin-top:0;'>" + topic + " in " + skill + "</h2>"
    
    # Small compact diagram - less space
    html += "<div class='diag'><b>Quick Diagram: " + topic + " Memory</b><br>"
    html += "Addr 1000: Val1=10 | Addr 1004: Val2=20 | Addr 1008: Val3=30 | Addr 1012: Val4=40<br>"
    html += "Flow: Start -> Init i=0 -> Check i < n? -> Yes -> Execute -> i++ -> Loop -> No -> Exit</div>"

    html += "<div class='cat'>Introduction to " + topic + "</div>"
    html += "<p><b>What is " + topic + "?</b> " + topic + " is a fundamental programming concept in " + skill + " that allows you to handle data efficiently. It is the backbone of problem solving in competitive programming and technical interviews.</p>"
    html += "<p><b>Why Learn " + topic + "?</b> Every major company like TCS, Infosys, Wipro, Amazon, Google asks at least 2-3 questions from " + topic + ". In real-world projects like BhavPath, " + topic + " is used to manage over 1 lakh student records. Without proper understanding of " + topic + ", a task that should take 0.01 seconds may take 1 hour. Mastering " + topic + " improves your logic, reduces code length, and optimizes performance.</p>"
    html += "<p><b>Where is it Used?</b> 1. Banking systems for processing transactions 2. E-commerce platforms for product catalog management 3. Social media feeds for content display 4. Operating systems for process management 5. BhavPath placement module for student data filtering.</p>"

    html += "<div class='cat'>Detailed Explanation</div>"
    html += "<p><b>Definition:</b> " + topic + " in " + skill + " is defined as a technique or construct that provides a structured way to store, access, manipulate, and iterate over data. It abstracts low-level memory details and provides high-level usability.</p>"
    html += "<p><b>Working Principle:</b> When you declare a variable or collection for " + topic + ", memory is allocated in RAM. For example, an array of 4 integers takes 4 * 4 = 16 bytes of contiguous memory. The base address is stored, and access is done via index calculation: Address of element = Base Address + (index * size_of_element). This gives O(1) random access. For loops, a counter variable i is maintained in stack, condition is checked, body executes, and counter increments. This continues until condition becomes false.</p>"
    html += "<p><b>Internal Working:</b> At compiler level, loops are converted to conditional jump instructions (JMP, JE, JNE in assembly). The CPU maintains a program counter. For each iteration, it checks condition, jumps to body if true, else jumps to exit. Understanding this helps you write efficient code and avoid infinite loops.</p>"

    html += "<div class='cat'>Types of " + topic + "</div>"
    html += "<div class='qbox'><b>1. Basic " + topic + ":</b> Simple syntax, easy for beginners. Used in easy-level coding rounds. Example: For loop that prints numbers from 0 to 4. Time Complexity O(n), Space O(1). Used when task is straightforward and input size is small (less than 1000).</div>"
    html += "<div class='qbox'><b>2. Intermediate " + topic + ":</b> Involves nested loops, combination with conditions and functions. Used in medium-level TCS NQT, Infosys SP. Example: Nested for loop to print pattern, or loop with function call inside. Time Complexity often O(n^2) due to nesting. Requires careful optimization to avoid Time Limit Exceeded (TLE). Example: For i in range(n): For j in range(m): print(i,j)</div>"
    html += "<div class='qbox'><b>3. Advanced / Optimized " + topic + ":</b> Designed for large data (10^6 elements). Uses advanced techniques like list comprehension, generators, sliding window, two pointers, hashing. Time Complexity optimized to O(n log n) or O(n). Space Complexity often O(1) or O(n). Used in Amazon, Google, Microsoft product-based interviews. Example: [x*x for x in range(n) if x % 2 == 0] is faster than normal loop with condition due to C-level optimization in Python. Another example: Using HashMap to find Two Sum in O(n) instead of O(n^2) brute force.</div>"
    html += "<div class='qbox'><b>4. Special Variants:</b> Includes while loop, do-while loop, for-each loop, infinite loop with break. While loop is used when number of iterations is not known beforehand (e.g., reading file until EOF). Do-while ensures at least one execution. For-each (for x in arr) is more readable and avoids off-by-one errors.</div>"

    html += "<div class='cat'>Properties and Characteristics</div>"
    html += "<p><b>1. Time Complexity:</b><br>Access: O(1) for array, O(n) for linked list<br>Search: O(n) linear, O(log n) binary if sorted<br>Insertion: O(1) at end, O(n) at middle due to shifting<br>Deletion: O(1) at end, O(n) at middle<br><b>2. Space Complexity:</b> O(1) extra if in-place, O(n) if auxiliary array used<br><b>3. Stability:</b> Some algorithms maintain relative order of equal elements (stable like Merge Sort), others don't (Quick Sort)<br><b>4. In-place:</b> Some work without extra space (Bubble Sort in-place), others need extra space (Merge Sort needs O(n) extra)</p>"

    html += "<div class='cat'>Code Examples - From Basic to Advanced - With Explanation</div>"
    html += "<p><b>Example 1: Basic Declaration and Access (Beginner Level)</b></p>"
    html += "<div class='code'># Basic Example\nvar = 10\nprint(var)  # Output: 10\n# Explanation: Variable var stores 10 in memory at some address. print reads from that address.</div>"
    html += "<p><b>Example 2: With Conditional Logic (Intermediate)</b></p>"
    html += "<div class='code'># With Condition\nvar = 10\nif var > 5:\n    print(\"Greater than 5\")  # This executes\nelse:\n    print(\"Smaller\")\n# Explanation: if checks condition, if true executes first block else second. Condition evaluation O(1).</div>"
    html += "<p><b>Example 3: With Loop - Iteration (Intermediate)</b></p>"
    html += "<div class='code'># Loop Example\nfor i in range(0, 5):\n    print(i)\n# Output: 0 1 2 3 4\n# Explanation: range(0,5) generates 0 to 4. Loop variable i takes each value. Body executes 5 times. Time O(n) where n=5.</div>"
    html += "<p><b>Example 4: Placement Level - Find Maximum in Array (TCS, Infosys Pattern) - Time O(n)</b></p>"
    html += "<div class='code'>def find_max(arr):\n    # Initialize max with first element\n    max_val = arr[0]\n    # Traverse array from second element\n    for x in arr:\n        if x > max_val:\n            max_val = x  # Update max if current larger\n    return max_val\n\narr = [10, 20, 5, 30, 25]\nprint(find_max(arr))  # Output: 30\n# Explanation: Single pass O(n) time, O(1) space. Best for placement coding round. Edge case: empty array check needed.</div>"
    html += "<p><b>Example 5: Product-Based Optimized - Two Sum Problem (Amazon, Google) - Time O(n) with HashMap</b></p>"
    html += "<div class='code'>def two_sum(arr, target):\n    # HashMap stores value -> index\n    seen = {}\n    for i, val in enumerate(arr):\n        # Check if complement exists\n        complement = target - val\n        if complement in seen:\n            return [seen[complement], i]  # Found pair\n        seen[val] = i  # Store current\n    return -1\n\narr = [2, 7, 11, 15]\ntarget = 9\nprint(two_sum(arr, target))  # Output: [0, 1] because 2+7=9\n# Explanation: O(n) time using HashMap O(1) lookup, O(n) space. Brute force O(n^2) would be too slow for 1 lakh elements. This is optimized for FAANG.</div>"
    html += "<p><b>Example 6: Advanced - List Comprehension (Pythonic and Faster)</b></p>"
    html += "<div class='code'># Normal loop\nsquares = []\nfor x in range(10):\n    if x % 2 == 0:\n        squares.append(x*x)\n\n# Optimized list comprehension - Faster (C-level loop)\nsquares_opt = [x*x for x in range(10) if x % 2 == 0]\nprint(squares_opt)  # [0, 4, 16, 36, 64]\n# Explanation: List comprehension is faster because loop runs in C, not Python bytecode. Time O(n), Space O(n). Recommended for Python interviews.</div>"

    html += "<div class='cat'>Common Mistakes and How to Avoid Them</div>"
    html += "<p><b>1. Off-by-One Error:</b> Using range(n) gives 0 to n-1, not 1 to n. Many beginners write for i in range(1, n) expecting n iterations but get n-1. Always verify start and end. Solution: Use range(0, n) for n iterations, or range(1, n+1) if you need 1 to n.<br><b>2. Infinite Loop:</b> while True without break or update condition causes program to hang. Example while i < 5: print(i) without i++ . Solution: Always ensure loop variable updates and termination condition reachable.<br><b>3. Not Initializing Variable:</b> Using variable without initialization leads to garbage value in C, NameError in Python. Solution: Always initialize max_val = arr[0] before loop, not random value.<br><b>4. Wrong Indentation (Python):</b> Code inside loop vs outside loop confusion due to spaces. Example print inside loop prints 5 times, outside prints once. Solution: Use consistent 4 spaces, check indentation carefully.<br><b>5. Using = Instead of ==:</b> if x = 5 assigns 5 instead of comparing. In Python, SyntaxError, in C, logical bug. Solution: Use == for comparison, = for assignment.<br><b>6. Ignoring Edge Cases:</b> Empty array, single element, negative numbers, duplicate values. Always test with [] [5] [5,5,5] [-1, -2, 3]. Solution: Add if not arr: return None check at start.</p>"

    html += "<div class='cat'>Advantages, Disadvantages, and Use Cases</div>"
    html += "<p><b>Advantages:</b><br>1. Fast Access: O(1) random access for arrays<br>2. Reusable: Write once, use for any size input<br>3. Saves Code: 2 lines of loop replace 1000 lines of repetitive code<br>4. Memory Efficient: In-place algorithms use O(1) extra space<br>5. Foundation for Advanced Topics: Mastering loops and arrays is prerequisite for Trees, Graphs, DP<br><b>Disadvantages:</b><br>1. Complexity for Beginners: Nested loops O(n^2) can be confusing<br>2. Performance Issues: Wrong algorithm choice leads to TLE (Time Limit Exceeded) for large inputs<br>3. Requires Careful Handling: Pointer errors in C, indentation errors in Python cause bugs<br><b>Real-World Use Cases:</b><br>1. Banking Systems: Process 1 lakh customer accounts, calculate interest for each using loop<br>2. E-commerce: Display product catalog, filter products by price using loop with condition<br>3. Social Media: Iterate over feed, show posts, like counts<br>4. Operating Systems: Schedule processes, manage memory blocks<br>5. BhavPath Placement Module: Filter students with avg > 75, generate company list based on percentage, sort students by performance</p>"

    html += "<div class='cat'>Why is " + topic + " Important for Placements?</div>"
    html += "<p><b>Placement Statistics:</b><br>TCS NQT: 2-3 questions directly from " + topic + " in technical round, 1 coding question uses " + topic + " logic<br>Infosys SP: Coding round includes array and loop manipulation<br>Wipro Elite: Output-based questions on loops and conditionals<br>Amazon: 100% of DSA rounds include array and HashMap optimization using " + topic + " concepts<br>Google: DP, Graph problems built on top of " + topic + " mastery<br><b>Salary Impact:</b> Students who master " + topic + " and similar core topics get 7-12 LPA packages in product-based companies, vs 3.5 LPA for those who skip fundamentals. Mastering " + topic + " gives you 20% closer to placement. Recommendation: Practice 1 hour theory + 2 hours coding daily on " + topic + ".</p>"

    html += "<div class='cat'>Top 10 Interview Questions on " + topic + " - Must Prepare</div>"
    html += "<p>1. What is " + topic + "? Explain with real-life example and code.<br>2. What is difference between " + topic + " and similar concept (e.g., for vs while, array vs linked list)?<br>3. How does " + topic + " work internally? Explain with memory diagram and time complexity.<br>4. Write code for " + topic + " without using built-in functions (e.g., reverse array without reverse()).<br>5. How to optimize " + topic + " for large input (10^6 elements)? Explain O(n) vs O(n^2).<br>6. Where did you use " + topic + " in your final year project? Explain architecture.<br>7. What are advantages and disadvantages of " + topic + "? When would you avoid it?<br>8. What happens if " + topic + " fails? How to handle edge cases like empty input?<br>9. Explain " + topic + " in multi-threaded environment. Is it thread-safe?<br>10. Design a system using " + topic + " - e.g., Design BhavPath placement module that filters students based on percentage using " + topic + ".</p>"

    html += "<div class='cat'>Practice Problems - From Easy to Hard</div>"
    html += "<p><b>Easy:</b> 1. Print numbers 1 to 10 using loop 2. Find sum of array elements 3. Check if number is even or odd<br><b>Medium:</b> 1. Find second largest element without sorting 2. Reverse array without extra space 3. Remove duplicates from sorted array<br><b>Hard:</b> 1. Two Sum with O(n) HashMap 2. Maximum subarray sum (Kadane's Algorithm) O(n) 3. Trapping rain water problem O(n) with two pointers<br>Solve these 10 problems to master " + topic + " completely.</p>"

    html += "<div class='cat'>Summary and Next Steps</div>"
    html += "<p><b>Summary:</b> " + topic + " is pillar of " + skill + ". It is not just syntax, but a way of thinking to solve problems efficiently. Mastering " + topic + " means you can handle any data manipulation task. It is prerequisite for advanced topics like Trees, Graphs, Dynamic Programming.<br><b>Next Steps:</b><br>1. Practice 10 problems daily on " + topic + " from easy to hard<br>2. Build a small project using " + topic + " for resume - e.g., Student Management System using " + topic + " to filter and sort students<br>3. Learn next topic in " + skill + " after mastering this<br>4. Revise time complexities: Access O(1), Search O(n) or O(log n), Insertion O(1) or O(n)<br>5. Prepare explanation with diagram for interview - Interviewers love diagrams and complexity analysis</p>"

    return html

def get_interview_content(skill):
    html = ""
    html += "<div class='cat'>Top Interview Questions - " + skill + " - Detailed with Diagrams</div>"
    html += "<div class='diag'>Quick Diagram: Stack - Local vars | Heap - Objects malloc | Code - Text segment</div>"

    if skill == "C":
        html += "<div class='qbox'><b>Q1. What is pointer? Why use pointer? Explain pointer to pointer with diagram and code.</b></div><div class='abox'><b>Answer:</b> Pointer stores address. int a=10 at addr 1000. int *p = &a p stores 1000 at 2000. *p is value at address =10. Why use? 1 Dynamic memory malloc 2 Pass large data without copy 3 Build Linked List. Code int a=10; int *p=&a; printf percent d *p prints 10. Diagram a 1000=10 p 2000=1000 pp 3000=2000. Always init as NULL to avoid wild. TCS asks 90 percent times.</div>"
        html += "<div class='qbox'><b>Q2. Array vs Pointer? Explain size difference with code?</b></div><div class='abox'><b>Answer:</b> Array continuous fixed size int arr 5 =20 bytes sizeof arr 20. Pointer 8 bytes stores address dynamic. Array name constant p++ allowed arr++ error. Example int arr 5; int *p=arr; p++ ok arr++ error. Memory diagram Array 10 20 30 contiguous Linked List Head 10->20->30->NULL scattered. Infosys coding round asks.</div>"
        html += "<div class='qbox'><b>Q3. What is dangling pointer? How to avoid? Write code?</b></div><div class='abox'><b>Answer:</b> Pointer pointing to freed memory. int *p=malloc 4; free p; Now p dangling using *p crashes segmentation fault. Solution After free set p=NULL. Code free p; p=NULL; if p not equal NULL safe. Prevents crash. Amazon asks dangling pointer in interviews.</div>"
        html += "<div class='qbox'><b>Q4. malloc vs calloc vs realloc vs free? Difference? Write code for 1 lakh ints?</b></div><div class='abox'><b>Answer:</b> malloc 1 arg size uninitialized garbage fast. calloc 2 args count size zero init safe slow. realloc resize existing block. free release memory. Use calloc when need zero init banking 1 lakh accounts zero safe. Code int *p = malloc 100000 * sizeof int; if p==NULL handle; free p; p=NULL; Without free memory leak system slows.</div>"
        html += "<div class='qbox'><b>Q5. Structure vs Union vs Structure padding? Explain size calculation?</b></div><div class='abox'><b>Answer:</b> Structure all members separate memory sum plus padding for alignment. struct char a int b size not 5 but 8 due 4-byte alignment padding. Union shares same memory size = max member only one active. Use struct for employee full data name age salary, union for value can be int OR float. Wipro asks padding. Example struct size 8 union size 4.</div>"
        html += "<div class='qbox'><b>Q6. Storage classes auto static extern register? Explain scope lifetime default?</b></div><div class='abox'><b>Answer:</b> auto local default garbage scope function lifetime function auto free. static keeps value between calls stays till program ends default 0 scope function lifetime program. extern global across files default 0. register request CPU register fast for loop counters. Example static int count=0; count++ remembers counting function calls. TCS NQT asks.</div>"
        html += "<div class='qbox'><b>Q7. Call by value vs Call by reference? Write swap program both ways?</b></div><div class='abox'><b>Answer:</b> Value copies original not changed void func int x x=20 original 10 stays 10. Reference passes address original changes void func int *x *x=20 original becomes 20. Swap needs reference void swap int *a int *b int t=*a; *a=*b; *b=t; Large array pass by reference saves memory copying.</div>"
        html += "<div class='qbox'><b>Q8. String vs char array? Why need backslash 0? What if forget?</b></div><div class='abox'><b>Answer:</b> char arr 5 Hello not string no backslash 0. char str Hello auto backslash 0 at end char str 6. String functions strlen strcpy need backslash 0 to know end. If forget printf prints garbage till random backslash 0 buffer overflow security issue. Code char str 6 = Hello strlen 5. Diagram Hello H e l l o backslash0.</div>"
        html += "<div class='qbox'><b>Q9. Memory leak, segmentation fault, dangling? How to prevent? Tools?</b></div><div class='abox'><b>Answer:</b> Leak malloc without free loop 1000 times free 1 memory grows. Segfault accessing not owned memory NULL dereference dangling out of bounds arr 10 size 5 stack overflow. Prevention every malloc free NULL check bounds check init pointers. Tool valgrind detects leaks. Product companies like Google care about leak.</div>"
        html += "<div class='qbox'><b>Q10. Null pointer vs Void pointer vs Wild pointer? Difference with code?</b></div><div class='abox'><b>Answer:</b> NULL int *p=NULL points nothing safe to check if p==NULL. Void void *p can point any type need cast int *p = (int*)p. Wild uninitialized int *p points random garbage dangerous. Always init pointer. Example int *p=NULL safe int *q; wild dangerous. TCS Digital asks.</div>"
        html += "<div class='qbox'><b>Q11. Recursion, stack overflow, tail recursion? Write factorial iterative vs recursive?</b></div><div class='abox'><b>Answer:</b> Function calling itself each call pushes stack frame. Factorial recursive if n==0 return 1 else n*fact n-1 On stack space. Iterative for loop O1 space. Stack overflow if no base condition infinite recursion crash. Tail recursion recursive call is last statement compiler can optimize to loop. Use recursion for tree graph but iterative for large n.</div>"
        html += "<div class='qbox'><b>Q12. File handling? Explain r w a r+ w+ a+ rb wb? Write code count lines?</b></div><div class='abox'><b>Answer:</b> r read existing fail if not exist, w write create truncate, a append, r+ read+write existing, w+ read+write create, a+ append+read, b binary. Code FILE *fp=fopen data.txt r; int count=0; char ch; while ch=fgetc fp !=EOF if ch newline count++; fclose fp; TCS asks file handling.</div>"
        html += "<div class='qbox'><b>Q13. Array vs Linked List vs Stack vs Queue? When to use which? Time complexity?</b></div><div class='abox'><b>Answer:</b> Array continuous O1 access On insert middle use fast search employee ID. Linked List nodes scattered via pointers On access O1 insert use frequent insert delete browser history. Stack LIFO push pop top browser back button recursion undo. Queue FIFO enqueue dequeue printer queue BFS. Diagram Array 10 20 30 contiguous Linked List Head 10->20->30->NULL scattered.</div>"
        html += "<div class='qbox'><b>Q14. Linked list types Singly Doubly Circular? Write code reverse singly?</b></div><div class='abox'><b>Answer:</b> Singly next only Head 10 20 NULL, Doubly next+prev 10 less than greater than 20 less than greater than 30, Circular last first. Reverse iterative prev=NULL curr=Head while curr next=curr.next curr.next=prev prev=curr curr=next Head=prev On time O1 space. Very important placement Q.</div>"
        html += "<div class='qbox'><b>Q15. Binary search vs linear search? Write code? Condition sorted?</b></div><div class='abox'><b>Answer:</b> Linear On unsorted check each. Binary Olog n sorted only low=0 high=n-1 mid= low+high /2 if arr mid==target return else adjust. 1 lakh sorted find 85 percent 17 steps not 1 lakh. Code iterative and recursive. All companies ask.</div>"
        html += "<div class='qbox'><b>Q16. Sorting Bubble Selection Insertion Quick Merge? Time complexity? Which stable?</b></div><div class='abox'><b>Answer:</b> Bubble On2 swap adjacent Selection On2 min find Insertion On2 best On sorted Quick O n log n avg On2 worst pivot in-place fast Merge O n log n always stable O n extra space. Stable keeps order equal marks. Quick array Merge linked list. For placement scores merge stable.</div>"
        html += "<div class='qbox'><b>Q17. Bit manipulation and or xor not shift left right? Check even odd using bit?</b></div><div class='abox'><b>Answer:</b> AND OR XOR NOT shift left *2 shift right /2. Check even if n and 1 ==0 even else odd because last bit 0 even 1 odd. Count set bits while n count+= n and 1 n shift right. Fast O1. Product companies ask bit manipulation. Code if n and 1 ==0 even else odd.</div>"
        html += "<div class='qbox'><b>Q18. Output questions: 5/2 vs 5.0/2? sizeof int vs sizeof int*? a++ ++a a-- order?</b></div><div class='abox'><b>Answer:</b> 5/2 integer division 2, 5.0/2 float 2.5. sizeof int 4 sizeof int* 8 64-bit. a++ ++a a-- order undefined in C depends compiler evaluation order right to left but sequence point tricky. Important for TCS NQT output questions.</div>"
        html += "<div class='qbox'><b>Q19. Reverse string without library, palindrome, anagram?</b></div><div class='abox'><b>Answer:</b> Reverse two pointers i=0 j=len-1 swap till i less than j. Palindrome reverse and compare or two pointers. Anagram sort both strings compare or frequency array 26 letters count. Code char str BhavPath int i=0 j=strlen-1 while i less than j char t=str i; str i=str j; str j=t; i++; j--; On time O1 space. TCS coding round 100 percent asks.</div>"
        html += "<div class='qbox'><b>Q20. Second largest without sorting? Missing number? Write code?</b></div><div class='abox'><b>Answer:</b> Second largest first largest max second second_max traverse one pass if x greater than max second=max max=x else if x greater than second and x !=max second=x On. Missing number 1 to n array size n-1 sum expected n n+1 /2 minus sum actual On. XOR method also. TCS coding round 100 percent. Code single pass.</div>"
    else:
        html += "<div class='qbox'><b>Q1. List vs Tuple vs Set vs Dict? Explain with diagram and time complexity? When use?</b></div><div class='abox'><b>Answer:</b> List mutable ordered duplicate 1 2 2 O1 access On search use scores 85 90. Tuple immutable ordered 1 2 faster hashable can be dict key use fixed coordinates. Set unordered unique 1 2 O1 search no duplicate use unique skills. Dict key-value a 1 O1 key must be hashable immutable. Frozenset immutable set hashable can be dict key. List for dynamic tuple for fixed set for unique dict for mapping.</div>"
        html += "<div class='qbox'><b>Q2. args vs kwargs? How to use? Unpacking?</b></div><div class='abox'><b>Answer:</b> args tuple positional unlimited def add args sum args call add 1 2 3. kwargs dict keyword def func kwargs for k v in kwargs.items call func name Bhav college QIS. Unpacking list to args my_list 1 2 3 add *my_list. Dict to kwargs my_dict name Bhav func **my_dict. Use when dont know how many args placement function receives. Very common in Django.</div>"
        html += "<div class='qbox'><b>Q3. Decorator Generator Iterator GIL? Write decorator for logging? Generator for large file?</b></div><div class='abox'><b>Answer:</b> Decorator wraps function adds behavior without modifying login_required. Code def my_decorator func def wrapper print Before func print After return wrapper. Generator yields one by one saves memory def gen yield 1 yield 2 for large file 1GB not load all for line in open file yield line. Iterator iter next. GIL only one thread executes Python bytecode at a time CPU-bound threading not faster but IO-bound ok use multiprocessing for CPU.</div>"
        html += "<div class='qbox'><b>Q4. OOP in Python? self init inheritance multiple inheritance super overloading overriding? What is MRO?</b></div><div class='abox'><b>Answer:</b> self current object like this Java. init constructor def init self name self.name=name. Inheritance class Student Person. Multiple inheritance class C A B MRO Method Resolution Order order search parent C A B object uses C3 linearization super calls parent. Overloading Python doesn't support same name different params last defined wins use args to simulate overriding child redefines parent. Code super init calls parent. TCS Digital asks.</div>"
        html += "<div class='qbox'><b>Q5. Shallow copy vs deep copy? What is copy module?</b></div><div class='abox'><b>Answer:</b> Shallow copy copies reference top level only list2=list1.copy or list1 inner mutable still shared list1 1 2 list2=list1.copy list1 0 0 =99 list2 also 99 because inner list shared. Deep copy copies full recursively import copy copy.deepcopy list1 list2 independent. Use deepcopy when nested mutable. Important for placement data copying.</div>"
        html += "<div class='qbox'><b>Q6. Lambda map filter reduce list comprehension? Which faster?</b></div><div class='abox'><b>Answer:</b> Lambda anonymous lambda x x+10. Map applies function to each list map lambda x x*2 1 2 3 ->2 4 6. Filter filters map filter lambda x x greater than 2 1 2 3 ->3. Reduce reduces to single from functools import reduce reduce lambda a b a+b 1 2 3 ->6. List comprehension x*x for x in range 5 if x percent 2==0 faster than map filter Pythonic.</div>"
        html += "<div class='qbox'><b>Q7. Exception handling try except else finally? Custom exception?</b></div><div class='abox'><b>Answer:</b> try risky except handles else executes if no exception finally always executes close file. Code try x=10/0 except ZeroDivisionError print Divide by zero else print No error finally print Always. Custom exception class MyError Exception pass raise MyError Not eligible. Use for validation.</div>"
        html += "<div class='qbox'><b>Q8. File handling With open r w a r+ How to read large file without loading fully?</b></div><div class='abox'><b>Answer:</b> With open auto close with open data.txt r as f data=f.read. r read existing w write create truncate a append r+ read+write b binary. Large file don't read all at once use for line in file process line or generator yield line saves memory 1GB file not load fully. TCS asks file handling.</div>"
        html += "<div class='qbox'><b>Q9. Django vs Flask vs FastAPI REST API ORM middleware?</b></div><div class='abox'><b>Answer:</b> Flask micro simple small API Django full batteries ORM admin auth FastAPI modern fast async automatic docs. For BhavPath small API Flask enough full website Django high performance FastAPI. REST API HTTP GET POST PUT DELETE JSON GET api students returns name Bhav. ORM Student.objects.filter avg greater than 75 instead of SQL. Middleware processes request before view like authentication logging. TCS uses Django.</div>"
        html += "<div class='qbox'><b>Q10. Reverse string palindrome anagram count vowels first non-repeating remove duplicates without set?</b></div><div class='abox'><b>Answer:</b> Reverse str slicing or two pointers. Palindrome str==str slicing. Anagram sorted str1==sorted str2 or Counter. Count vowels sum 1 for c in str if c in aeiou. First non-repeating frequency dict then traverse. Remove duplicates without set preserve order result empty result.append x for x in arr if x not in result On2 or dict.fromkeys On. All TCS coding round.</div>"
    return html

def get_default_code(skill):
    if skill == "C":
        return "# Practice - Pointer and Array\n# Python practice for C concepts\na=10\np=id(a)\nprint(a, p)\narr=[10,20,30,40]\nprint(arr)\n# Reverse\ns=list(\"BhavPath\")\ni,j=0,len(s)-1\nwhile i<j:\n    s[i],s[j]=s[j],s[i]\n    i+=1; j-=1\nprint(''.join(s))\n# Second largest\narr=[10,20,5,30,25]\nmax1=max2=-1\nfor x in arr:\n    if x>max1:\n        max2=max1\n        max1=x\n    elif x>max2 and x!=max1:\n        max2=x\nprint(\"Second largest\", max2)"
    return "# Practice - List vs Dict and Two Sum\nmy_list=[1,2,2,3]\nmy_tuple=(1,2,3)\nmy_set={1,2,3}\nmy_dict={\"Python\":90}\nprint(my_list, my_tuple, my_set, my_dict)\n# First non-repeating\ns=\"BhavPath\"\nfrom collections import Counter\nfreq=Counter(s)\nfor c in s:\n    if freq[c]==1:\n        print(\"First non-repeating\", c)\n        break\n# Two sum On\ndef two_sum(arr, target):\n    seen={}\n    for i,num in enumerate(arr):\n        if target-num in seen:\n            return [seen[target-num], i]\n        seen[num]=i\n    return -1\nprint(two_sum([2,7,11,15], 9))"

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
    st.markdown("""<div class='center' style='padding-top:16vh'><h1 style='color:white;font-size:58px;font-weight:900;'>Welcoming to<br><span style='background:linear-gradient(90deg,#0d4aff,#ff006a,#fef08a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>BhavPath Technical Skills</span></h1><div class='glass' style='display:inline-block;margin-top:25px;'><p style='color:#c7f0ff;'>C, C++, Java, Python, SQL, DSA - Full Detailed Content with Diagrams - More Content Less Diagram Space</p></div></div>""", unsafe_allow_html=True)
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
    st.markdown("<div class='center'><h1 style='color:white;'>Select Interview Skill</h1><p style='color:#a78bfa;'>Each Question Separate Q Box + Answer Box + Diagram</p></div>", unsafe_allow_html=True)
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

else:
    st.markdown("<div class='center'><h1 style='color:white;'>Coming Soon</h1></div>", unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.page="purpose"
        st.rerun()
