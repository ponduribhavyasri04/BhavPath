# app.py - BHAVPATH - FINAL - ONLY EASY ENGLISH - NO TELUGU
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io, textwrap

def get_font(s,b=False,i=False):
    try:
        if b: return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",s)
        if i: return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",s)
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
    except: return ImageFont.load_default()

def draw_pic(d, topic, x, y):
    if "List" in topic or "Array" in topic:
        for i in range(4):
            d.rectangle([(x+i*80,y),(x+i*80+70,y+50)],fill="#DBEAFE",outline="#6C5CE7",width=2)
            d.text((x+i*80+25,y+15),str(10*(i+1)),font=get_font(18,True),fill="#1E293B")
    elif "Linked" in topic:
        for i in range(3):
            cx=x+i*120
            d.ellipse([(cx,y),(cx+70,y+50)],fill="#FEF3C7",outline="#F59E0B",width=2)
            d.text((cx+12,y+15),"Data",font=get_font(14,True),fill="black")
            if i<2: d.line([(cx+70,y+25),(cx+110,y+25)],fill="#6C5CE7",width=3)
    elif "Stack" in topic:
        for i in range(3):
            d.rectangle([(x+20,y+i*30),(x+120,y+i*30+25)],fill="#D1FAE5",outline="#10B981",width=2)
            d.text((x+35,y+i*30+5),f"Item {3-i}",font=get_font(14),fill="black")
    else:
        d.rectangle([(x,y),(x+300,y+80)],fill="white",outline="#6C5CE7",width=2)
        d.rectangle([(x,y),(x+300,y+25)],fill="#0F172A")
        d.text((x+10,y+5),"id | name | salary",font=get_font(12,True),fill="white")
        d.text((x+10,y+30),"1 | Bhavya Ponduri | 50000",font=get_font(11),fill="black")

def make_pdf(title, data_list):
    W,H=900,1400; pages=[]
    for idx,item in enumerate(data_list):
        img=Image.new("RGB",(W,H),"#FFFFFF"); d=ImageDraw.Draw(img)
        d.rectangle([(10,10),(W-10,H-10)],outline="#A29BFE",width=2)
        d.rectangle([(20,20),(W-20,90)],fill="#0F172A")
        d.text((30,25),title[:40],font=get_font(20,True),fill="white")
        d.text((30,60),f"Ex: Bhavya Ponduri | BhavPath | P{idx+1}",font=get_font(11),fill="#A29BFE")
        y=105
        d.rectangle([(25,y),(W-25,y+48)],fill="#FFF3CD",width=1)
        d.text((35,y+10),f"{idx+1}. {item['topic'][:48]}",font=get_font(17,True),fill="#1E293B"); y+=62
        d.text((30,y),"EASY EXPLANATION:",font=get_font(14,True),fill="#6C5CE7"); y+=20
        for line in textwrap.wrap(item['concept'],width=68)[:4]:
            d.text((30,y),line,font=get_font(14),fill="#1E293B"); y+=18
        y+=8; d.text((30,y),"VISUAL PIC:",font=get_font(12,True),fill="#8B5CF6"); y+=18
        draw_pic(d,item['topic'],35,y); y+=90
        d.text((30,y),"CODE - Ex: Bhavya Ponduri:",font=get_font(13,True),fill="#0F172A"); y+=18
        d.rectangle([(28,y),(W-28,y+110)],fill="#F8FAFF",outline="#C7D2FE",width=1); y+=8
        for line in item['code'].split('\n')[:6]:
            d.text((40,y),line[:55],font=get_font(13,i=True),fill="#1E293B"); y+=18
        y+=115; d.text((30,y),"INTERVIEW / PYQ:",font=get_font(12,True),fill="#DC2626"); y+=18
        for line in textwrap.wrap(item['q'],width=68)[:2]:
            d.text((30,y),line,font=get_font(12),fill="#475569"); y+=16
        d.text((30,y+6),f"TIP: {item['tip'][:55]}",font=get_font(11,True),fill="#059669")
        d.text((W//2,H-15),f"Ex: Bhavya Ponduri | BhavPath | Light Watermark",font=get_font(10),fill="#E5E7EB",anchor="mm")
        pages.append(img)
    buf=io.BytesIO(); pages[0].save(buf,format="PDF",save_all=True,append_images=pages[1:]); return buf.getvalue()

CONCEPTS={
"Python":[
 {"topic":"Python Basics - Easy Start","concept":"Python is very easy language. Easy to learn. In TCS NQT they use Python for coding. It is high level language. Example: Bhavya Ponduri can start easily.","code":"name='Bhavya Ponduri'\nprint(f'Hello {name}')","q":"Why Python in placements? Python 2 vs 3? Asked TCS 2024.","tip":"Basics strong = 70% coding easy","video":"https://www.youtube.com/watch?v=_uQrJ0TkZlc","test":{"q":"Ex: Bhavya - How to print in Python?","opts":["print()","echo()","write()"],"ans":0,"exp":"We use print() in Python!"}},
 {"topic":"List - Boxes Picture","concept":"List is like a box. You can put items inside. You can change items. Items are in order. Example: Bhavya marks [58,75,82] - see boxes picture.","code":"marks=[58,75,82]\nmarks.append(90)\nprint(marks)","q":"List vs Tuple? How to reverse? Asked Wipro 2024.","tip":"Learn slicing [::-1] - TCS asks","video":"https://www.youtube.com/watch?v=5_5oE5lgrhw","test":{"q":"Append means what? Ex: Bhavya marks","opts":["Add at end","Add at start","Delete"],"ans":0,"exp":"Add at end!"}},
 {"topic":"Linked List Reverse - Circles Picture","concept":"Linked List has nodes. Each node has data + next pointer. Reverse is TOP question in TCS, Infosys. Use 3 pointers to reverse.","code":"prev=None\ncurr=head\nwhile curr:\n nxt=curr.next\n curr.next=prev","q":"Write reverse LL code? 100% asked!","tip":"See circles picture and learn reverse","video":"https://www.youtube.com/watch?v=8hly31xKli0","test":{"q":"LL reverse time complexity?","opts":["O(n)","O(n^2)","O(1)"],"ans":0,"exp":"O(n) - one loop only!"}},
 {"topic":"Stack - Plates Picture","concept":"Stack is like plates. Last plate you put, first you take. Called LIFO - Last In First Out. Push to add, Pop to remove. Used for brackets check.","code":"stack=[]\nstack.append('Bhavya')\nprint(stack.pop())","q":"Balanced brackets using stack? Wipro 2024 favourite.","tip":"Remember plates picture for stack","video":"https://www.youtube.com/watch?v=3y1kQ1K2A1k","test":{"q":"Stack is LIFO or FIFO?","opts":["LIFO","FIFO","Both"],"ans":0,"exp":"LIFO - Like plates!"}},
],
"SQL":[
 {"topic":"2nd Highest Salary - Table Picture","concept":"This question is asked in every company. Use MAX with subquery. See table picture with salary column. Take 2nd highest from table.","code":"SELECT MAX(salary) FROM emp\nWHERE salary < (SELECT MAX(salary) FROM emp);","q":"How to write 2nd highest? 3 methods? TCS Infosys 100% asked.","tip":"Remember by heart - will come in paper","video":"https://www.youtube.com/watch?v=5OdVJbNCSso","test":{"q":"2nd Highest uses what? Ex: Bhavya salary","opts":["MAX + Subquery","MIN","COUNT"],"ans":0,"exp":"MAX + Subquery!"}},
 {"topic":"JOINs - Venn Picture","concept":"JOIN means combine two tables. INNER means only common items. LEFT means all left table + common items. See Venn diagram picture - easy to understand.","code":"SELECT s.name, p.company FROM students s\nJOIN placements p ON s.id=p.sid;","q":"Difference INNER vs LEFT? Draw Venn? Infosys 2023.","tip":"Draw Venn diagram to understand JOINs","video":"https://www.youtube.com/watch?v=7S_tz1z_5bA","test":{"q":"INNER JOIN means?","opts":["Only common items","All left","All right"],"ans":0,"exp":"INNER means only common!"}},
],
"JavaScript":[
 {"topic":"JavaScript Basics - Browser Picture","concept":"JavaScript makes website active. It runs in browser. var, let, const difference is important. If Bhavya Ponduri makes website, JS is needed.","code":"let name='Bhavya Ponduri';\nconsole.log(name);","q":"What is JS? var vs let vs const? Cognizant asked.","tip":"JS basics is must for full stack","video":"https://www.youtube.com/watch?v=W6NZfCO5SIk","test":{"q":"let vs var difference?","opts":["Block vs Function scope","Same","No diff"],"ans":0,"exp":"let is block scope, var is function scope!"}},
 {"topic":"DOM - Live Picture","concept":"DOM is structure of website. See HTML like a tree. With JS you can change HTML. When button click, name changes on website.","code":"document.getElementById('name').innerText='Bhavya Placed!';","q":"What is DOM? How to change text on button click?","tip":"Make small project changing Bhavya name","video":"https://www.youtube.com/watch?v=PkZNo7MFNFg","test":{"q":"DOM full form?","opts":["Document Object Model","Data Object Model","Digital"],"ans":0,"exp":"Document Object Model!"}},
]
}

PYQ={
"TCS NQT":[
 {"topic":"TCS NQT 2024 - Second Largest Array","concept":"TCS 2024 asked: Find second largest in array. Example Bhavya marks. Easy logic: Remove duplicate, sort, take second last item.","code":"arr=[12,35,1,10,34,1]\narr=list(set(arr))\narr.sort()\nprint(arr[-2]) #34 - Answer","q":"PYQ TCS NQT 2024 - Second largest in array? Asked 2 times.","tip":"TCS asks array questions more - learn 3 methods","video":"https://www.youtube.com/watch?v=_uQrJ0TkZlc","test":{"q":"Second largest logic?","opts":["Remove duplicate + sort + take [-2]","Only sort","Only max"],"ans":0,"exp":"Remove duplicate + sort + take [-2]!"}},
 {"topic":"TCS NQT 2023 - String Reverse","concept":"TCS 2023 asked string reverse. Reverse Bhavya Ponduri name. Easy with slicing [::-1]. Very easy method.","code":"s='Bhavya Ponduri'\nprint(s[::-1]) # irudnoP ayvahB","q":"PYQ TCS 2023 - Reverse string without built-in?","tip":"Learn reverse with [::-1] and with loop both","video":"https://www.youtube.com/watch?v=5_5oE5lgrhw","test":{"q":"String reverse easy way?","opts":["[::-1]","reverse()","sort()"],"ans":0,"exp":"[::-1] is easy way!"}},
 {"topic":"TCS NQT 2022 - Prime Check","concept":"TCS 2022 asked prime number check. Check if number is prime or not. Simple loop logic to check prime.","code":"def is_prime(n):\n for i in range(2,n):\n if n%i==0: return False\n return True","q":"PYQ TCS 2022 - Prime number check? Most asked PYQ.","tip":"Prime logic by heart - will definitely come","video":"https://www.youtube.com/watch?v=8hly31xKli0","test":{"q":"7 is prime?","opts":["Yes","No","Maybe"],"ans":0,"exp":"Yes 7 is prime!"}},
],
"Infosys":[
 {"topic":"Infosys 2024 PYQ - OOP Class","concept":"Infosys 2024 asked OOP pillars. Class and object with real example Bhavya Ponduri. Class is blueprint, object is real thing.","code":"class Student:\n def __init__(self,name):\n self.name=name\ns=Student('Bhavya Ponduri')","q":"PYQ Infosys 2024 - What is OOP? Explain 4 pillars? 100% asked.","tip":"OOP 4 pillars 100% asked in Infosys","video":"https://www.youtube.com/watch?v=W6NZfCO5SIk","test":{"q":"OOP pillars how many?","opts":["4 pillars","2 pillars","6 pillars"],"ans":0,"exp":"4 pillars - E A I P!"}},
],
"Wipro":[
 {"topic":"Wipro 2024 PYQ - Balanced Brackets","concept":"Wipro 2024 asked balanced brackets using stack. Most asked PYQ in Wipro. Use stack - push opening brackets, pop closing.","code":"def is_balanced(s):\n stack=[]\n for c in s:\n if c in '({[': stack.append(c)\n return len(stack)==0","q":"PYQ Wipro 2024 - Balanced brackets using stack? Asked 3 times.","tip":"Stack brackets is Wipro favourite - learn it","video":"https://www.youtube.com/watch?v=3y1kQ1K2A1k","test":{"q":"Balanced brackets uses what?","opts":["Stack","Queue","Array"],"ans":0,"exp":"Stack is used!"}},
]
}

INTERVIEW={
"TCS":[
 {"topic":"TCS Interview - Self Introduction","concept":"First question in TCS interview is self introduction. Tell like Bhavya Ponduri: Name, branch, percentage, skills. Tell in 2 minutes only.","code":"My name is Bhavya Ponduri,\nCSE final year, 75%,\nSkills: Python, SQL, DSA,\nProject: BhavPath placement app","q":"Interview: Tell me about yourself? First question in TCS - 100% asked.","tip":"Tell in 2 mins - practice with Bhavya example","video":"https://www.youtube.com/watch?v=_uQrJ0TkZlc","test":{"q":"Self intro how long should be?","opts":["2 mins","10 mins","30 sec"],"ans":0,"exp":"2 mins is perfect!"}},
 {"topic":"TCS Interview - List vs Tuple","concept":"Technical question - List is changeable (mutable), Tuple is not changeable (immutable). Tell with Bhavya marks example. Easy to explain.","code":"List=[58,75,82] # Mutable - can change\nTuple=(58,75,82) # Immutable - cannot change\nList.append(90) # Works","q":"Interview: Difference between List and Tuple? 80% asked in TCS tech.","tip":"Tell with example - Bhavya marks example is easy","video":"https://www.youtube.com/watch?v=5_5oE5lgrhw","test":{"q":"List can change or not?","opts":["Yes Mutable - can change","No Immutable","Maybe"],"ans":0,"exp":"Yes List is mutable - can change!"}},
 {"topic":"TCS Interview - 2nd Highest Salary","concept":"SQL question - 2nd highest salary - Most asked in TCS tech interview. Simple logic: MAX + subquery to get 2nd highest.","code":"SELECT MAX(sal) FROM emp\nWHERE sal<(SELECT MAX(sal) FROM emp);","q":"Interview: Write query for 2nd highest salary? Top question in TCS SQL.","tip":"Learn 3 methods: subquery, LIMIT, window function","video":"https://www.youtube.com/watch?v=5OdVJbNCSso","test":{"q":"2nd highest query uses what?","opts":["MAX + subquery","Only MIN","Only COUNT"],"ans":0,"exp":"MAX + subquery!"}},
],
}

st.set_page_config(page_title="BhavPath - Only Easy English", page_icon="🚀", layout="wide")
st.markdown("""
<style>
.stApp{background:#0A0A0F!important;}
.orb{position:fixed; border-radius:50%; filter:blur(80px); opacity:0.6; animation:float 8s ease-in-out infinite;}
.orb1{width:600px; height:600px; background:radial-gradient(circle,#6C5CE7,#FF6B6B); top:-200px; left:-200px;}
.orb2{width:500px; height:500px; background:radial-gradient(circle,#48DBFB,#6C5CE7); top:20%; right:-150px; animation-delay:2s;}
.orb3{width:700px; height:700px; background:radial-gradient(circle,#FF6B6B,#FECA57); bottom:-300px; left:30%; animation-delay:4s;}
@keyframes float{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(30px,-30px) scale(1.1);}}
.glass{background:rgba(255,255,255,0.05)!important; backdrop-filter:blur(25px)!important; border:1px solid rgba(255,255,255,0.1)!important; border-radius:30px!important;}
.hero-title{font-size:85px!important; font-weight:800!important; background:linear-gradient(100deg,#fff 20%,#A29BFE 40%,#FF6B6B 70%,#48DBFB 90%)!important; -webkit-background-clip:text!important; -webkit-text-fill-color:transparent!important; line-height:0.9!important; animation:glow 3s ease-in-out infinite;}
@keyframes glow{0%,100%{filter:drop-shadow(0 0 20px rgba(162,155,254,0.5));}50%{filter:drop-shadow(0 0 40px rgba(255,107,107,0.8));}}
.typewriter{font-size:20px!important; color:#A29BFE!important; letter-spacing:4px!important; text-align:center; border-right:3px solid #6C5CE7; white-space:nowrap; overflow:hidden; animation:typing 3s steps(40,end),blink 0.8s infinite; width:fit-content; margin:0 auto;}
@keyframes typing{from{width:0;}to{width:100%;}}@keyframes blink{0%,50%{border-color:#6C5CE7;}51%,100%{border-color:transparent;}}
.badge{display:inline-block; padding:8px 18px; border-radius:100px; background:rgba(108,92,231,0.15); border:1px solid rgba(108,92,231,0.3); color:#A29BFE; font-size:12px; letter-spacing:2px; margin:5px;}
.stButton>button{background:linear-gradient(100deg,#FF6B6B 0%,#6C5CE7 50%,#48DBFB 100%)!important; border:none!important; border-radius:100px!important; padding:18px 40px!important; font-weight:800!important; color:white!important;}
label{color:#E2E8F0!important;}
</style>
<div class="orb orb1"></div><div class="orb orb2"></div><div class="orb orb3"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:50px 20px 20px 20px; position:relative; z-index:2;">
  <span class="badge">EX: BHAVYA PONDURI</span>
  <span class="badge">ONLY EASY ENGLISH</span>
  <h1 class="hero-title">BhavPath</h1>
  <div style="height:45px; margin:15px 0;"><div class="typewriter">ONLY EASY ENGLISH - NO TELUGU - SIMPLE WORDS</div></div>
  <p style="color:#94A3B8; max-width:700px; margin:10px auto;">Easy English • Visual Pics • Concept Videos • Concept Tests • Previous Papers • Interview Qs • Ex: Bhavya Ponduri</p>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="glass" style="padding:30px; position:relative; z-index:2;">', unsafe_allow_html=True)
    st.markdown("### Enter Details - Ex: Bhavya Ponduri Style - Easy English")
    with st.form("form"):
        c1,c2=st.columns([2,1])
        with c1:
            name=st.text_input("Full Name", value="Bhavya Ponduri", placeholder="Ex: Bhavya Ponduri")
            st.markdown('<p style="color:#A29BFE; font-size:13px; margin-top:-18px;">Ex: Bhavya Ponduri - Example like before</p>', unsafe_allow_html=True)
            company=st.selectbox("Select Company for PYQ + Interview Qs", ["TCS NQT","Infosys","Wipro"])
            course=st.selectbox("Select Course - Video + Test will come based on course", ["Python","SQL","JavaScript"])
        with c2:
            btech=st.slider("B.Tech %",40,100,58)
            backlogs=st.selectbox("Backlogs?",[0,1,2,"2+"])
            branch=st.selectbox("Branch?",["CSE","IT","ECE","AI/ML","Others"])
        submit=st.form_submit_button("LAUNCH MY BHAVPATH →")
    st.markdown('</div>', unsafe_allow_html=True)

if submit:
    st.markdown(f'<div class="glass" style="padding:20px; margin-top:25px; position:relative; z-index:2;"><h3 style="color:white;">Welcome Ex: {name} - {btech}% - {company} - {course}</h3><p style="color:#A29BFE;">Only Easy English • Visual Pics • Light Watermark #E5E7EB</p></div>', unsafe_allow_html=True)

    if btech<60: st.error(f"Ex: {name} - {btech}% LOW - Need 60%+")
    else:
        st.success(f"Ex: {name} - {btech}% Eligible for {company}!")

    tab1,tab2,tab3,tab4=st.tabs([f"{company} PYQ 3 Years", f"{company.split()[0]} Interview Qs", f"{course} Concepts Video+Test", f"All PDFs Easy English"])

    with tab1:
        st.markdown(f"### {company} Previous Year Papers - Easy English - Ex: {name}")
        for idx, pyq in enumerate(PYQ.get(company, PYQ["TCS NQT"])):
            with st.expander(f"PYQ {idx+1}: {pyq['topic']} - Ex: {name}", expanded=(idx==0)):
                c1,c2=st.columns([1.2,1])
                with c1:
                    st.markdown(f"**Easy Explanation:** {pyq['concept']}")
                    st.code(pyq['code'])
                    st.error(f"PYQ: {pyq['q']}")
                    st.success(f"TIP: {pyq['tip']}")
                with c2:
                    st.markdown(f"**Video About This Concept:** {pyq['topic']}")
                    st.video(pyq['video'])
                    st.markdown(f"**Test About This Concept:** {pyq['test']['q']}")
                    ans=st.radio(f"Select - Ex: {name}", pyq['test']['opts'], key=f"pyq_{company}_{idx}", horizontal=True)
                    if st.button(f"Check - PYQ {idx+1}", key=f"pyqbtn_{company}_{idx}"):
                        if ans==pyq['test']['opts'][pyq['test']['ans']]: st.balloons(); st.success(f"Correct Ex: {name}! {pyq['test']['exp']}")
                        else: st.error(f"Wrong Ex: {name}. Correct {pyq['test']['opts'][pyq['test']['ans']]}")

        pdf=make_pdf(f"{company} PYQ 3 Years Easy English", PYQ.get(company, PYQ["TCS NQT"]))
        st.download_button(f"Download {company} PYQ PDF - Easy English", pdf, f"Ex_{name}_{company}_PYQ_Easy.pdf", "application/pdf", use_container_width=True)

    with tab2:
        comp_key=company.split()[0]
        st.markdown(f"### {comp_key} Interview Qs - Only Easy English - Ex: {name}")
        for idx, iq in enumerate(INTERVIEW.get(comp_key, INTERVIEW["TCS"])):
            with st.expander(f"Interview Q{idx+1}: {iq['topic']} - Ex: {name}", expanded=(idx<2)):
                c1,c2=st.columns([1,1])
                with c1:
                    st.markdown(f"**Easy Explanation:** {iq['concept']}")
                    st.code(iq['code'])
                    st.error(f"Interview Q: {iq['q']}")
                with c2:
                    st.video(iq['video'])
                    ta=st.radio(f"{iq['test']['q']} - Ex: {name}", iq['test']['opts'], key=f"int_{comp_key}_{idx}", horizontal=True)
                    if st.button(f"Check - {iq['topic']}", key=f"intbtn_{comp_key}_{idx}"):
                        if ta==iq['test']['opts'][iq['test']['ans']]: st.success(f"Correct Ex: {name}! {iq['test']['exp']}")
                        else: st.error(f"Wrong. Correct {iq['test']['opts'][iq['test']['ans']]}")

        pdf=make_pdf(f"{comp_key} Interview Qs Easy English", INTERVIEW.get(comp_key, INTERVIEW["TCS"]))
        st.download_button(f"Download {comp_key} Interview PDF - Easy English", pdf, f"Ex_{name}_{comp_key}_Interview_Easy.pdf", "application/pdf", use_container_width=True)

    with tab3:
        st.markdown(f"### {course} Concept Wise - Video + Test About Particular Concept - Ex: {name}")
        for idx, concept in enumerate(CONCEPTS[course]):
            with st.expander(f"Concept {idx+1}: {concept['topic']} - Ex: {name}", expanded=(idx==0)):
                c1,c2=st.columns([1.3,1])
                with c1:
                    st.markdown(f"**Video About This Particular Concept:** {concept['topic']}")
                    st.markdown(f"**Easy Explanation:** {concept['concept']}")
                    st.video(concept['video'])
                    st.code(concept['code'])
                with c2:
                    st.markdown(f"**Online Test About This Particular Concept:** {concept['topic']}")
                    st.markdown(f"**Q: {concept['test']['q']}**")
                    ans=st.radio(f"Select - Ex: {name}", concept['test']['opts'], key=f"concept_{course}_{idx}", horizontal=False)
                    if st.button(f"Check Answer - {concept['topic']}", key=f"cbtn_{course}_{idx}"):
                        if ans==concept['test']['opts'][concept['test']['ans']]: st.balloons(); st.success(f"Correct Ex: {name}! {concept['test']['exp']}")
                        else: st.error(f"Wrong Ex: {name}. Correct {concept['test']['opts'][concept['test']['ans']]}")
                    single_pdf=make_pdf(f"{concept['topic']} Easy English", [concept])
                    st.download_button(f"Download {concept['topic']} PDF - Easy English + Pic", single_pdf, f"Ex_{name}_{concept['topic'][:12]}.pdf", "application/pdf", use_container_width=True, key=f"pdf_{course}_{idx}")

        full_course=make_pdf(f"{course} Full Easy English Visual", CONCEPTS[course])
        st.download_button(f"Download Full {course} PDF - Easy English + Visual Pics + Light Watermark #E5E7EB - Ex: Bhavya Ponduri", full_course, f"Ex_{name}_Full_{course}_Easy.pdf", "application/pdf", use_container_width=True)

    with tab4:
        st.markdown(f"### All PDFs - Easy English - Visual Pics - Light Watermark - Ex: {name}")
        col1,col2=st.columns(2)
        with col1:
            for crs in ["Python","SQL","JavaScript"]:
                pdf=make_pdf(f"{crs} Full Easy English Visual", CONCEPTS[crs])
                st.download_button(f"{crs} Full - Easy English - Pics - Ex: Bhavya Ponduri", pdf, f"Ex_{name}_{crs}_Full_Easy_Visual.pdf", "application/pdf", use_container_width=True, key=f"all_{crs}")
        with col2:
            for comp in ["TCS NQT","Infosys","Wipro"]:
                pdf=make_pdf(f"{comp} PYQ 3 Years", PYQ.get(comp, PYQ["TCS NQT"]))
                st.download_button(f"{comp} PYQ - 3 Years - Easy English", pdf, f"Ex_{name}_{comp}_PYQ.pdf", "application/pdf", use_container_width=True, key=f"allpyq_{comp}")
            pdf=make_pdf("TCS Interview Qs", INTERVIEW["TCS"])
            st.download_button(f"TCS Interview Qs - Easy English", pdf, f"Ex_{name}_TCS_Interview.pdf", "application/pdf", use_container_width=True, key="allint")

        all_data=[];
        for crs in CONCEPTS: all_data.extend(CONCEPTS[crs][:2])
        for comp in PYQ: all_data.extend(PYQ[comp][:1])
        mega=make_pdf("BhavPath MEGA Overall - All PYQ + Interview + Concepts Easy English Visual", all_data)
        st.download_button(f"MEGA PDF - Overall - Easy English + Visual Pics + Light Watermark - Ex: Bhavya Ponduri - SINGLE FILE", mega, f"Ex_{name}_BhavPath_MEGA_Overall.pdf", "application/pdf", use_container_width=True)

  
   
