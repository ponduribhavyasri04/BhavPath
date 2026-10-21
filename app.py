import streamlit as st
from datetime import date
st.set_page_config(page_title="BhavPath Final", layout="wide", page_icon="🚀")
st.markdown("""
<style>
.stApp{background:#F8FAFC !important}
.white-card{background:#FFF !important;border-radius:12px;padding:14px;border:1px solid #E2E8F0}
.white-card b{color:#000 !important;font-weight:700 !important}
.blue-card{background:#2563EB !important;border-radius:12px;padding:14px}
.blue-card *{color:#FFF !important;font-weight:700 !important}
.bullet-card{background:#FFF !important;border-radius:12px;padding:16px;border:2px solid #E2E8F0}
.bullet-card *{color:#000 !important;font-weight:700 !important}
.info-card{background:#FFF !important;border:2px solid #2563EB !important;border-left:8px solid #2563EB !important;border-radius:10px;padding:16px;margin-bottom:14px}
.info-card b{color:#0F2C61 !important;font-weight:900 !important;font-size:16px !important}
.info-card span{color:#000 !important;font-size:15px !important;font-weight:600 !important;line-height:1.6 !important}
.summary-card{background:#F8FAFC !important;border:2px solid #CBD5E1 !important;border-radius:10px;padding:14px}
.summary-card *{color:#000 !important;font-weight:600 !important}
.ad-card{background:linear-gradient(135deg,#667EEA 0%,#764BA2 100%) !important;border-radius:12px;padding:12px}
.ad-card *{color:#FFF !important}
.cert-card{background:linear-gradient(135deg,#FFF8E1 0%,#FFE082 100%) !important;border:3px solid #FFB300 !important;border-radius:16px;padding:20px;text-align:center}
.practice-card{background:#FFFBEB !important;border:2px solid #F59E0B;border-radius:10px;padding:14px;margin-bottom:10px}
.practice-card *{color:#000 !important;font-weight:800 !important;font-size:15px !important}
.locked-card{background:#E2E8F0 !important;border-radius:8px;padding:10px}
.locked-card *{color:#000 !important}
.stButton>button{background:#2563EB !important;border-radius:8px;font-weight:bold !important;border:none !important}
.stButton>button *{color:#FFF !important}
div[data-testid="stRadio"] label p{color:#000 !important;font-weight:700 !important}
div[data-testid="stCodeBlock"]{background:#1E293B !important;border-radius:10px !important}
div[data-testid="stCodeBlock"] *{color:#E2E8F0 !important}
div[data-testid="stTextArea"] textarea{background:#1E293B !important;color:#FFF !important;border:2px solid #334155 !important}
div[data-testid="stTextArea"] label p{color:#000 !important;font-weight:800 !important}
div[data-testid="stSelectbox"] label p{color:#000 !important;font-weight:900 !important}
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state:
    st.session_state.logged=False
    st.session_state.user={"btech":81,"name":"Bhav","college":"Rise College, Ongole"}
    st.session_state.xp=820
    st.session_state.selected_topic="Python"
    st.session_state.completed={}
    st.session_state.current_mod=0
    st.session_state.cert_unlocked=False
    st.session_state.final_boss_won=False
    st.session_state.purpose_done=False
    st.session_state.page_view="list"

def make_modules(lang):
    base=[
        {"name":"Introduction","about":f"About Introduction in {lang} - {lang} is easy language. Created for beginners. BTech 81 percent easy. College projects TCS NQT use. Easy syntax. Full content info chaala.","content":f"{lang} easy syntax - Beginners best - No complex","code":"print('Hello Bhav')" if lang=="Python" else "#include <stdio.h>\nint main(){printf(\"Hello Bhav\");return 0;}" if lang=="C" else "#include <iostream>\nusing namespace std;\nint main(){cout<<\"Hello Bhav\"<<endl;return 0;}" if lang=="C++" else "public class Main{public static void main(String[] args){System.out.println(\"Hello Bhav\");}}" if lang=="Java" else "CREATE DATABASE bhavpath_db;","task":"Print Hello","practice":[
            {"pq":f"{lang} creator who","opts":["Creator correct","Other wrong"],"ans":"Creator correct","code":"print('creator')" if lang=="Python" else "code","task":"Print creator"},
            {"pq":f"Print Bhav 81 in {lang}","opts":["Correct syntax","Wrong syntax"],"ans":"Correct syntax","code":"print('Bhav 81')" if lang=="Python" else "code","task":"Print Bhav"},
            {"pq":"Output Hello","opts":["Hello Correct","Error Wrong"],"ans":"Hello Correct","code":"print('Hello')","task":"Hello"}]},
        {"name":"Variables","about":f"About Variables in {lang} - Data store container. {lang} specific type handling. BTech 81 example. Swap example. Multiple assignments. Full rich content info.","content":f"Variables in {lang} - Data store - Type handling - Swap","code":"btech=81\nname='Bhav'\nprint(name,btech)\na=81\nb=75\na,b=b,a\nprint(a,b)" if lang=="Python" else "#include <stdio.h>\nint main(){int btech=81;char name[]=\"Bhav\";printf(\"%s %d\",name,btech);int a=81,b=75,temp;temp=a;a=b;b=temp;return 0;}" if lang=="C" else "#include <iostream>\n#include <string>\nusing namespace std;\nint main(){int btech=81;string name=\"Bhav\";cout<<name<<btech<<endl;int a=81,b=75;swap(a,b);return 0;}" if lang=="C++" else "public class Main{public static void main(String[] args){int btech=81;String name=\"Bhav\";System.out.println(name+btech);int a=81,b=75,temp;temp=a;a=b;b=temp;}}" if lang=="Java" else "DECLARE @btech INT=81;SELECT @btech;","task":"Variables","practice":[
            {"pq":f"{lang} declare","opts":["Correct type","Wrong type"],"ans":"Correct type","code":"code","task":"Declare"},
            {"pq":f"{lang} swap 81 75","opts":["Swap correct","Swap wrong"],"ans":"Swap correct","code":"code","task":"Swap"},
            {"pq":"Multiple same 81","opts":["x=y=z=81 Correct","Wrong"],"ans":"x=y=z=81 Correct","code":"x=y=z=81","task":"Multiple"}]},
        {"name":"Operators","about":"About Operators - Arithmetic plus minus multiply divide mod power floor Comparison equal not equal greater less greater equal less equal for 60 percent eligibility Logical and or not Assignment. No percent symbol to avoid syntax error. Full content rich.","content":"Operators Arithmetic Comparison Logical Assignment - For eligibility check greater equal 60","code":"btech=81\nprint(btech>=60)\nprint(btech % 2)\nprint(10+20)","task":"Check greater equal 60","practice":[
            {"pq":"81 greater equal 60","opts":["True eligible Correct","False Wrong"],"ans":"True eligible Correct","code":"print(81>=60)","task":"Check True"},
            {"pq":"81 mod 2 odd","opts":["1 Odd Correct","0 Even Wrong"],"ans":"1 Odd Correct","code":"print(81%2)","task":"Odd"},
            {"pq":"10 plus 20","opts":["30 Correct","20 Wrong"],"ans":"30 Correct","code":"print(10+20)","task":"Plus"}]},
        {"name":"Loops","about":"About Loops - Same work repeat for loop fixed range 0 10 3 gives 0 3 6 9 coins Final Boss 4 coins Important range 1 11 gives 1 to 10 sum 55 Table 81 while loop condition true break continue. Rich content.","content":"for i in range 0 10 3 gives 0 3 6 9 coins Final Boss 4 coins range 1 11 sum 55","code":"# Final Boss coins 0 3 6 9\nfor i in range(0,10,3):\n    print(i)\nprint('4 coins Boss Slayed')\ntotal=0\nfor i in range(1,11):\n    total+=i\nprint(total)","task":"Collect 0 3 6 9","practice":[
            {"pq":"range 0 10 3 Final Boss","opts":["0 3 6 9 Correct","0 1 2 Wrong"],"ans":"0 3 6 9 Correct","code":"for i in range(0,10,3):\n    print(i)","task":"0 3 6 9"},
            {"pq":"Sum 1 to 10 55","opts":["range 1 11 sum 55 Correct","range 1 10 Wrong"],"ans":"range 1 11 sum 55 Correct","code":"total=0\nfor i in range(1,11):\n    total+=i\nprint(total)","task":"Sum 55"},
            {"pq":"Print Bhav 3 times","opts":["range 3 Correct","range 1 Wrong"],"ans":"range 3 Correct","code":"for i in range(3):\n    print('Bhav')","task":"Print 3"}]},
        {"name":"Identifiers","about":"Identifiers variable names Rules letter underscore start number start not allowed space hyphen not allowed special not allowed case sensitive Valid my_var underscore name btech1 my_btech 81 Invalid 1var my minus var.","content":"Rules letter underscore start Valid my_var underscore name btech1 Invalid 1var my minus var","code":"my_btech=81\n_name='Bhav'\nprint(my_btech)","task":"Identifier","practice":[
            {"pq":"Valid identifier","opts":["my_btech Valid","1btech Invalid"],"ans":"my_btech Valid","code":"my_btech=81","task":"Valid"},
            {"pq":"Invalid hyphen","opts":["my minus var Invalid","my underscore Valid"],"ans":"my minus var Invalid","code":"my_var=81","task":"Invalid"},
            {"pq":"Create 3 valid","opts":["btech name college Correct","Wrong"],"ans":"btech name college Correct","code":"btech=81\nname='Bhav'","task":"3 valid"}]},
    ]
    full=[]
    names=["Introduction","Basic Input Output","Identifiers","Keywords","Variables","Data Types","Operators","Conditional Statements","Loops","Pandas"]
    for i in range(10):
        if i < len(base):
            full.append(base[i])
        else:
            t=base[0]
            n=dict(t)
            n["name"]=names[i]
            n["about"]=f"About {names[i]} in {lang} - {t['about']} - {lang} specific rich content BTech 81 percent TCS NQT 8 LPA important"
            n["content"]=f"{names[i]} in {lang} - {t['content']}"
            full.append(n)
    return full

TOPICS={
    "Python":{"title":"Python - 10 Modules","desc":"Easy plus Data Science","modules":make_modules("Python")},
    "C":{"title":"C - 10 Modules","desc":"Dennis Ritchie 1972","modules":make_modules("C")},
    "C++":{"title":"C++ - 10 Modules","desc":"Bjarne Stroustrup 1985","modules":make_modules("C++")},
    "Java":{"title":"Java - 10 Modules","desc":"James Gosling 1995","modules":make_modules("Java")},
    "SQL":{"title":"SQL - 10 Modules","desc":"Database TCS must 8 LPA","modules":make_modules("SQL")},
}
def cert_html(name,college,btech,topic,xp,date_str):
    return f"""<div class="cert-card"><div style="font-size:22px;font-weight:900;color:#0F2C61">CERTIFICATE</div><div style="border:2px solid #FFB300;border-radius:12px;padding:12px;background:white;margin-top:8px"><div style="font-size:18px;font-weight:900;color:#2563EB">{name}</div><div style="font-size:11px;color:#000">from {college} with {btech} percent</div><div style="font-size:14px;font-weight:800;color:#0F2C61;margin-top:6px">{topic}</div><div style="display:flex;justify-content:space-around;margin-top:8px;font-size:10px"><div><b>XP:</b> {xp}</div><div><b>Date:</b> {date_str}</div><div><b>Grade:</b> A+</div></div></div></div>"""

if not st.session_state.logged:
    st.title("BhavPath - Login")
    email=st.text_input("Email",placeholder="bhav@gmail.com")
    college=st.text_input("College",placeholder="Rise College, Ongole")
    if st.button("Login and Continue"):
        if email and "@" in email and college:
            st.session_state.user={"email":email,"college":college,"btech":81,"name":email.split("@")[0]}
            st.session_state.logged=True
            st.session_state.purpose_done=False
            st.rerun()
elif not st.session_state.purpose_done:
    st.title("One More Step")
    btech=st.slider("BTech percent",0,100,81)
    if st.button(f"Browse Topics with {btech} percent"):
        st.session_state.user["btech"]=btech
        st.session_state.purpose_done=True
        st.rerun()
else:
    st.markdown(f'<div class="blue-card"><b>BhavPath | {st.session_state.user["college"]} | {st.session_state.user["btech"]} percent | {st.session_state.xp} XP | {st.session_state.selected_topic}</b></div>', unsafe_allow_html=True)
    done=len([k for k,v in st.session_state.completed.items() if v])
    st.progress(min(done/8,1.0))
    col_b1,col_b2=st.columns([1,3])
    with col_b1:
        if st.button("Back Change percent", use_container_width=True):
            st.session_state.purpose_done=False
            st.rerun()
    with col_b2:
        if st.button("Back to All Topics List Malli", use_container_width=True):
            st.session_state.page_view="list"
            st.rerun()
    st.divider()
    if st.session_state.page_view=="list":
        col_topics,col_content=st.columns([1,3])
        with col_topics:
            st.subheader("Skills - List Page Only")
            st.markdown('<div class="white-card"><b>List Page varake - Ikkada matrame Open buttons</b></div>', unsafe_allow_html=True)
            for tname in TOPICS.keys():
                is_sel=st.session_state.selected_topic==tname
                if is_sel:
                    st.markdown(f'<div class="blue-card"><b>{tname} SELECTED</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="white-card"><b>{tname}</b><br>{TOPICS[tname]["desc"]}</div>', unsafe_allow_html=True)
                if st.button(f"Open {tname}",key=f"open_{tname}", use_container_width=True):
                    st.session_state.selected_topic=tname
                    st.session_state.current_mod=0
                    st.session_state.page_view="list"
                    st.rerun()
        with col_content:
            t=TOPICS[st.session_state.selected_topic]
            st.subheader(f"{t['title']} - {len(t['modules'])} Modules")
            for i,mod in enumerate(t["modules"]):
                is_done=st.session_state.completed.get(f"{st.session_state.selected_topic}_{i}")
                tick="✅" if is_done else "•"
                if st.button(f"{tick} {i+1}. {mod['name']} -> Open Detail",key=f"nextpage_{st.session_state.selected_topic}_{i}",use_container_width=True):
                    st.session_state.current_mod=i
                    st.session_state.page_view="detail"
                    st.rerun()
    else:
        if st.session_state.cert_unlocked and st.session_state.final_boss_won:
            col_nav,col_content,col_side=st.columns([0.6,2.4,0.8])
        else:
            col_nav,col_content=st.columns([0.7,3.0])
        with col_nav:
            t=TOPICS[st.session_state.selected_topic]
            st.subheader("Navigation - Detail Only")
            st.markdown(f'<div class="blue-card"><b>Current: {st.session_state.selected_topic}</b><br>Detail page lo Open C Java list ledu - Page varake</div>', unsafe_allow_html=True)
            for i,mod in enumerate(t["modules"]):
                is_done=st.session_state.completed.get(f"{st.session_state.selected_topic}_{i}")
                is_cur=i==st.session_state.current_mod
                tick="✅" if is_done else "•"
                if is_cur:
                    st.markdown(f'<div class="blue-card"><b>{tick} {i+1}. {mod["name"]} - Current</b></div>', unsafe_allow_html=True)
                else:
                    if st.button(f"{tick} {i+1}. {mod['name']}",key=f"detail_nav_{i}",use_container_width=True):
                        st.session_state.current_mod=i
                        st.rerun()
            if st.button("Back to All Topics List", use_container_width=True):
                st.session_state.page_view="list"
                st.rerun()
        with col_content:
            t=TOPICS[st.session_state.selected_topic]
            mod=t["modules"][st.session_state.current_mod]
            if st.button(f"Back to {t['title']} List",key="back_to_list",use_container_width=True):
                st.session_state.page_view="list"
                st.rerun()
            st.divider()
            st.subheader(f"{t['title']} - Module {st.session_state.current_mod+1}: {mod['name']}")
            st.markdown(f'<div class="blue-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]} - {t["title"]}</b></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-card"><div><b>About {mod["name"]} - {t["title"]} - Black Clear:</b></div><div style="margin-top:10px;"><span>{mod["about"]}</span></div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="summary-card"><b>Summary:</b> <span>{mod["content"]} - {t["title"]} specific {st.session_state.user["btech"]} percent</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bullet-card"><b>Code - {t["title"]} Specific - Language Wise Fixed</b></div>', unsafe_allow_html=True)
            lang_map={"Python":"python","C":"c","C++":"cpp","Java":"java","SQL":"sql"}
            st.code(mod["code"],language=lang_map.get(st.session_state.selected_topic,"python"))
            st.divider()
            st.subheader("Code Space - Middle Big Area")
            code_input=st.text_area("Your Code - Big Area 250:",value=mod["code"],height=250,key=f"code_mid_{st.session_state.current_mod}")
            if st.button("Run Code - Middle",key=f"run_mid_{st.session_state.current_mod}",use_container_width=True):
                st.success(f"Output: {mod['task']} done")
                st.code(code_input,language=lang_map.get(st.session_state.selected_topic,"python"))
            st.divider()
            st.subheader("Practice - Select plus Run")
            p_list=mod.get("practice",[])
            pq_options=[f"{i+1}. {p['pq']}" for i,p in enumerate(p_list)]
            if pq_options:
                sel=st.selectbox("Select Practice Question - Select chesi run:",pq_options,key=f"select_pq_{st.session_state.current_mod}")
                idx=pq_options.index(sel)
                pq=p_list[idx]
                st.markdown(f'<div class="practice-card"><b>{pq["pq"]} - Q{idx+1}</b><br><span>{pq["task"]}</span></div>', unsafe_allow_html=True)
                st.code(pq["code"],language=lang_map.get(st.session_state.selected_topic,"python"))
                choice=st.radio(f"Select Answer Q{idx+1}:",pq["opts"],key=f"quiz_{st.session_state.current_mod}_{idx}")
                c1,c2=st.columns([1,1])
                with c1:
                    if st.button(f"Check Answer Q{idx+1}",key=f"check_{st.session_state.current_mod}_{idx}",use_container_width=True):
                        if choice==pq["ans"]:
                            st.success("Correct plus 20 XP")
                            st.session_state.xp+=20
                            st.balloons()
                        else:
                            st.error(f"Wrong Correct: {pq['ans']}")
                with c2:
                    if st.button(f"Run Practice Q{idx+1}",key=f"run_pq_{st.session_state.current_mod}_{idx}",use_container_width=True):
                        st.success(f"Practice Q{idx+1} Run")
                        st.code(pq["code"],language=lang_map.get(st.session_state.selected_topic,"python"))
                pq_code=st.text_area(f"Your Code Q{idx+1} Edit and Run:",value=pq["code"],height=180,key=f"pq_code_{st.session_state.current_mod}_{idx}")
                if st.button(f"Run Your Code Q{idx+1}",key=f"run_your_{st.session_state.current_mod}_{idx}",use_container_width=True):
                    st.success(f"Your Code Q{idx+1} Run")
                    st.code(pq_code,language=lang_map.get(st.session_state.selected_topic,"python"))
            st.divider()
            col_prev,col_done,col_next=st.columns([1,1,1])
            with col_prev:
                if st.session_state.current_mod>0:
                    if st.button("Prev",use_container_width=True):
                        st.session_state.current_mod-=1
                        st.rerun()
            with col_done:
                key=f"{st.session_state.selected_topic}_{st.session_state.current_mod}"
                if st.session_state.completed.get(key):
                    st.success("Done")
                else:
                    if st.button("Mark Done plus 50 XP",key=f"done_{key}",use_container_width=True):
                        st.session_state.completed[key]=True
                        st.session_state.xp+=50
                        st.balloons()
                        st.rerun()
            with col_next:
                if st.session_state.current_mod<len(t["modules"])-1:
                    if st.button("Next",use_container_width=True):
                        st.session_state.current_mod+=1
                        st.rerun()
            st.divider()
            st.subheader("FINAL BOSS")
            if done>=3:
                st.markdown(f'<div class="blue-card"><b>UNLOCKED {done} modules</b></div>', unsafe_allow_html=True)
                step=st.slider("for i 0 10 i plus equal - Collect 0 3 6 9",1,5,3,key="game")
                if st.button("PLAY FINAL BOSS",key="play_game",use_container_width=True):
                    coins=[0,3,6,9]
                    path=list(range(0,10,step))
                    coll=len([x for x in path if x in coins])
                    st.write(f"Path {path} | {coll}/4")
                    if coll==4:
                        st.balloons()
                        st.success("SLAYED plus 200 XP Certificate side lo")
                        st.session_state.xp+=200
                        st.session_state.final_boss_won=True
                        st.session_state.cert_unlocked=True
                        st.rerun()
                    else:
                        st.error(f"Need i plus equal 3 Got {coll}/4")
            else:
                st.markdown(f'<div class="locked-card"><b>Locked Complete {3-done} more</b></div>', unsafe_allow_html=True)
        if st.session_state.cert_unlocked and st.session_state.final_boss_won:
            with col_side:
                today=date.today().strftime("%d-%m-%Y")
                html=cert_html(st.session_state.user["name"],st.session_state.user["college"],st.session_state.user["btech"],st.session_state.selected_topic,st.session_state.xp,today)
                st.markdown(html,unsafe_allow_html=True)
                txt=f"Certificate - {st.session_state.user['name']} - {st.session_state.user['college']} - {st.session_state.user['btech']} percent - {st.session_state.selected_topic} - XP {st.session_state.xp}"
                st.download_button(label="Download Certificate",data=txt,file_name=f"Certificate_{st.session_state.selected_topic}.txt",mime="text/plain",use_container_width=True)
