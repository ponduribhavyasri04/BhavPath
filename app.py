import streamlit as st
import random
import streamlit.components.v1 as components
st.set_page_config(page_title="BhavPath", page_icon="🚀", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.welcome-box {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 60px 20px; border-radius: 20px; text-align: center; color: white;}
.login-header {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 15px; text-align: center; color: white; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'completed' not in st.session_state: st.session_state.completed = []
if 'name' not in st.session_state: st.session_state.name = ""
if 'email' not in st.session_state: st.session_state.email = ""
if 'college' not in st.session_state: st.session_state.college = ""
if 'purpose' not in st.session_state: st.session_state.purpose = ""
if 'test_skill' not in st.session_state: st.session_state.test_skill = None
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'test_answers' not in st.session_state: st.session_state.test_answers = {}
if 'game_unlocked' not in st.session_state: st.session_state.game_unlocked = False
if 'game_score' not in st.session_state: st.session_state.game_score = 0
if 'collected_coins' not in st.session_state: st.session_state.collected_coins = []
if 'cert_skill' not in st.session_state: st.session_state.cert_skill = None
if 'cert_stage' not in st.session_state: st.session_state.cert_stage = "select"
if 'cert_questions' not in st.session_state: st.session_state.cert_questions = []
if 'cert_answers' not in st.session_state: st.session_state.cert_answers = {}
if 'cert_score' not in st.session_state: st.session_state.cert_score = 0

TOPICS = {
    "Python": ["Intro", "Variables", "Loops", "Functions", "Lists", "OOPS", "File Handling", "Final Boss"],
    "C": ["Intro", "Data Types", "Loops", "Functions", "Arrays", "Pointers", "Final Boss"],
    "C++": ["Intro", "OOP Basics", "Classes", "STL", "Final Boss"],
    "Java": ["Intro", "OOP", "Collections", "Threads", "Final Boss"],
    "SQL": ["Basics", "Joins", "Group By", "Having", "Window Functions", "Final Boss"],
    "DSA": ["Arrays", "Stack", "Queue", "Binary Search", "Linked List", "Final Boss"]
}

# ================= 1ST PAGE: WELCOME =================
if st.session_state.page == "welcome":
    st.markdown("""
    <div class="welcome-box">
        <div style="font-size:70px">🚀</div>
        <div style="font-size:60px; font-weight:900">BhavPath</div>
        <div style="font-size:28px; margin-top:10px">Welcome to your placement story</div>
        <div style="margin-top:10px; font-size:18px">Learn. Grind. Game. Get Placed.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>")
    c1,c2,c3 = st.columns(3)
    with c1: st.metric("6 Skills", "C, C++, Python, Java, SQL, DSA")
    with c2: st.metric("48 Modules", "GeeksForGeeks Style Content")
    with c3: st.metric("Game + Certificate", "Placement Ready")
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.page = "login"
            st.rerun()
    st.stop()

# ================= 2ND PAGE: LOGIN =================
if st.session_state.page == "login":
    st.markdown('<div class="login-header"><div style="font-size:35px; font-weight:800">🚀 BhavPath</div><div>Welcome to your placement story</div></div>', unsafe_allow_html=True)
    _, col, _ = st.columns([1,2,1])
    with col:
        with st.container(border=True):
            st.subheader("Login")
            name = st.text_input("Full Name", value=st.session_state.name, placeholder="Enter your name")
            email = st.text_input("Email", value=st.session_state.email, placeholder="yourname@college.com")
            college = st.text_input("College Name", value=st.session_state.college, placeholder="Rise College, Ongole")
            if st.button("Continue →", use_container_width=True, type="primary"):
                if name and email and college:
                    st.session_state.name = name; st.session_state.email = email; st.session_state.college = college
                    st.session_state.page = "purpose"; st.rerun()
                else: st.error("Please fill all fields")
            if st.button("Back"): st.session_state.page = "welcome"; st.rerun()
    st.stop()

# ================= 3RD PAGE: PURPOSE =================
if st.session_state.page == "purpose":
    st.markdown(f'<div class="login-header"><div style="font-size:30px; font-weight:800">🚀 BhavPath</div><div>Hi {st.session_state.name} - Select Your Purpose</div></div>', unsafe_allow_html=True)
    st.subheader("Why did you come to this link? Select Purpose:")

    r1_c1, r1_c2 = st.columns(2)
    with r1_c1:
        if st.button("📚 SKILL LEARNING\nLearn New Skills - GFG Full Content + Practice Code + Examples", use_container_width=True):
            st.session_state.purpose = "skill"; st.session_state.page = "main"; st.rerun()
        st.markdown("<br>")
        if st.button("📝 TEST ZONE\nSelect Skill C, C++, Python, Java, SQL, DSA - Take Test", use_container_width=True):
            st.session_state.purpose = "test"; st.session_state.page = "main"; st.rerun()
    with r1_c2:
        if st.button("📊 PLACEMENT PERCENTAGE CHECKING\nEnter B.Tech % + Skills Known → Get Company List Offering", use_container_width=True):
            st.session_state.purpose = "placement"; st.session_state.page = "main"; st.rerun()
        st.markdown("<br>")
        if st.button("📜 CERTIFICATE ZONE\nRandom AI Interview → Get Certificate", use_container_width=True):
            st.session_state.purpose = "certificate"; st.session_state.page = "main"; st.rerun()
    st.markdown("<br>")
    _, mid, _ = st.columns([1,2,1])
    with mid:
        if st.button("💼 INTERVIEW QUESTIONS\nTCS, Infosys, Wipro Q&A Practice", use_container_width=True):
            st.session_state.purpose = "interview"; st.session_state.page = "main"; st.rerun()
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"; st.rerun()
    st.stop()

# ================= COMMON SIDEBAR FOR 4TH PAGE =================
st.sidebar.markdown(f"### 🚀 BhavPath")
st.sidebar.write(f"Name: {st.session_state.name}")
st.sidebar.write(f"Email: {st.session_state.email}")
st.sidebar.write(f"College: {st.session_state.college}")
st.sidebar.write(f"Purpose: {st.session_state.purpose}")
st.sidebar.metric("XP", st.session_state.xp)
st.sidebar.metric("Game Score", st.session_state.game_score)
if st.sidebar.button("Change Purpose"): st.session_state.page = "purpose"; st.rerun()
if st.sidebar.button("Logout"): st.session_state.page = "welcome"; st.session_state.test_skill=None; st.session_state.game_unlocked=False; st.rerun()

# ================= 4TH PAGE: SKILL LEARNING - GFG CONTENT =================
if st.session_state.purpose == "skill":
    st.title("Skill Learning - GeeksForGeeks Style - Full Content")
    
    GFG_DATA = {
        "Loops": {
            "title": "Python Loops - for loop with step",
            "article": "Loop is used to execute a block of code repeatedly. Syntax: for i in range(start, stop, step): print(i). Important: range(0,10,3) starts at 0, goes till 9, with step 3. So it prints 0,3,6,9. This logic is used in BhavPath Game Zone and asked in interviews.",
            "example": "for i in range(0, 10, 3):\n    print(i)\n\n# Output:\n# 0\n# 3\n# 6\n# 9",
            "complexity": "Time: O(n/step) = O(n), Space: O(1)"
        }
    }
    
    left, middle, right = st.columns([1,2,1.2])
    with left:
        selected_topic = st.radio("Select Topic", list(TOPICS.keys()))
        selected_module = st.radio(f"Modules in {selected_topic}", TOPICS[selected_topic])
    with middle:
        st.markdown(f"## {selected_topic} - {selected_module}")
        if selected_module in GFG_DATA:
            data = GFG_DATA[selected_module]
            st.markdown(f"### {data['title']}")
            st.write(data['article'])
            st.divider()
            st.markdown("### Example Code With Output")
            st.code(data['example'], language="python")
            st.info(data['complexity'])
        else:
            st.write(f"**What is {selected_module}?**")
            st.write(f"{selected_module} is an important concept in {selected_topic}. It is frequently asked in placement interviews for Data Engineer and Software Engineer roles at TCS NQT, Infosys, Wipro.")
            st.write(f"**Why Important for Placements?** Companies ask questions on {selected_module}. Mastering this helps you get 7-15 LPA packages.")
            st.divider()
            st.markdown("### Example Code")
            st.code(f"# Example for {selected_module}\nfor i in range(0,10,3):\n    print(i) # Output: 0,3,6,9", language="python")
            st.info("Complexity: Time O(n), Space O(1)")
        
        key = f"{selected_topic}-{selected_module}"
        if key not in st.session_state.completed:
            if st.button(f"Mark {selected_module} as Completed +50 XP", type="primary"):
                st.session_state.completed.append(key); st.session_state.xp+=50; st.balloons()
        else: st.success("Already Completed")
    with right:
        st.markdown("### Practice - GFG Style")
        st.warning(f"Practice: Write code for {selected_module} - Print 0,3,6,9")
        practice_code = st.text_area("Your Code - Python Editor", "for i in range(0,10,3):\n    print(i)", height=200)
        if st.button("Run Code"):
            try:
                import io, sys
                old_stdout = sys.stdout; sys.stdout = buffer = io.StringIO()
                exec(practice_code); sys.stdout = old_stdout
                st.code(buffer.getvalue() or "No output")
            except Exception as e: st.error(e)
        st.divider()
        st.markdown("### Example Solutions")
        st.code("# Solution 1\nfor i in range(0,10,3):\n    print(i)\n\n# Solution 2\n# while loop\ni=0\nwhile i<10:\n    print(i)\n    i+=3", language="python")

# ================= 4TH PAGE: PLACEMENT PERCENTAGE CHECKING =================
elif st.session_state.purpose == "placement":
    st.title("Placement Percentage Checking - B.Tech %, Skills, Company List Offering")
    COMPANIES_DB = [
        {"name": "TCS NQT", "min_btech": 60, "skills": ["Python", "C", "SQL", "Aptitude"], "package": "3.5-7 LPA", "role": "Ninja / Digital"},
        {"name": "Infosys SP", "min_btech": 65, "skills": ["Python", "Java", "SQL", "OOPS"], "package": "5-9 LPA", "role": "Systems Engineer"},
        {"name": "Wipro Elite", "min_btech": 60, "skills": ["Java", "C", "SQL"], "package": "3.5-6.5 LPA", "role": "Project Engineer"},
        {"name": "Accenture", "min_btech": 65, "skills": ["Python", "Java", "Cloud"], "package": "4.5-6.5 LPA", "role": "ASE"},
        {"name": "Cognizant", "min_btech": 60, "skills": ["SQL", "Python", "Java"], "package": "4-7 LPA", "role": "Programmer Analyst"},
        {"name": "Data Engineer - Amazon", "min_btech": 70, "skills": ["Python", "SQL", "Spark", "Pandas"], "package": "10-15 LPA", "role": "Data Engineer"},
        {"name": "Data Engineer - Flipkart", "min_btech": 70, "skills": ["SQL", "Pandas", "ETL"], "package": "8-12 LPA", "role": "Data Engineer"},
    ]
    left,right = st.columns([1,2])
    with left:
        st.subheader("Enter Your Details")
        btech = st.number_input("B.Tech Percentage %", min_value=0, max_value=100, value=81)
        inter = st.number_input("Inter Percentage %", min_value=0, max_value=100, value=85)
        tenth = st.number_input("10th Percentage %", min_value=0, max_value=100, value=90)
        st.divider()
        st.subheader("Skills You Know")
        skill_python = st.checkbox("Python", value=True)
        skill_java = st.checkbox("Java")
        skill_c = st.checkbox("C / C++")
        skill_sql = st.checkbox("SQL", value=True)
        skill_pandas = st.checkbox("Pandas / Data Engineering")
        skill_aptitude = st.checkbox("Aptitude", value=True)
        my_skills = []
        if skill_python: my_skills.append("Python")
        if skill_java: my_skills.append("Java")
        if skill_c: my_skills.append("C")
        if skill_sql: my_skills.append("SQL")
        if skill_pandas: my_skills.append("Pandas")
        if skill_aptitude: my_skills.append("Aptitude")
        check_btn = st.button("Check My Companies List", type="primary", use_container_width=True)
    with right:
        if check_btn:
            eligible = []
            for comp in COMPANIES_DB:
                if btech >= comp["min_btech"]:
                    match_count = len(set(my_skills) & set(comp["skills"]))
                    comp["match"] = match_count
                    comp["match_percent"] = int((match_count / len(comp["skills"]))*100) if comp["skills"] else 0
                    eligible.append(comp)
            eligible = sorted(eligible, key=lambda x: x["match_percent"], reverse=True)
            st.success(f"You are eligible for {len(eligible)} companies out of {len(COMPANIES_DB)}")
            for comp in eligible:
                with st.container(border=True):
                    c1,c2,c3 = st.columns([2,1,1])
                    with c1:
                        st.markdown(f"### {comp['name']}")
                        st.write(f"Role: {comp['role']} | Package: {comp['package']}")
                        st.write(f"Required: {comp['min_btech']}% | Yours: {btech}% - Eligible")
                        st.write(f"Skills Needed: {', '.join(comp['skills'])}")
                    with c2: st.metric("Skill Match", f"{comp['match_percent']}%", f"{comp['match']}/{len(comp['skills'])}")
                    with c3:
                        if comp['match_percent']>=50: st.success("High Chance - Apply")
                        elif comp['match_percent']>=25: st.warning("Medium - Learn 1 skill")
                        else: st.error("Low - Upskill needed")
        else: st.info("Enter details on left and click Check")

# ================= 4TH PAGE: TEST + GAME ZONE - REAL PLAYABLE GAME =================
elif st.session_state.purpose == "test":
    TEST_BANK = {
        "C": [{"q": "What is output of for(i=0; i<10; i+=3) printf('%d ', i); ?", "o": ["0 3 6 9", "0 1 2 3", "3 6 9"], "a": "0 3 6 9"}],
        "C++": [{"q": "Which is OOP pillar in C++?", "o": ["Inheritance", "Loop", "Array"], "a": "Inheritance"}],
        "Python": [{"q": "What is output of range(0,10,3)?", "o": ["[0,3,6,9]", "[0,1,2,3]", "[3,6,9]"], "a": "[0,3,6,9]"}],
        "Java": [{"q": "Java is?", "o": ["Platform Independent", "Dependent"], "a": "Platform Independent"}],
        "SQL": [{"q": "Which function returns average B.Tech %?", "o": ["AVG(btech)", "SUM(btech)", "COUNT(btech)"], "a": "AVG(btech)"}],
        "DSA": [{"q": "Which data structure uses LIFO?", "o": ["Stack", "Queue", "Array"], "a": "Stack"}],
    }

    st.title("Test Zone + Game Zone - Skill Development")

    if not st.session_state.test_started and not st.session_state.game_unlocked:
        st.subheader("Step 1: Select Skill For Test - C, C++, Python, Java, SQL, DSA")
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("C Language", use_container_width=True): st.session_state.test_skill="C"
            if st.button("Python", use_container_width=True): st.session_state.test_skill="Python"
        with c2:
            if st.button("C++", use_container_width=True): st.session_state.test_skill="C++"
            if st.button("Java", use_container_width=True): st.session_state.test_skill="Java"
        with c3:
            if st.button("SQL", use_container_width=True): st.session_state.test_skill="SQL"
            if st.button("DSA", use_container_width=True): st.session_state.test_skill="DSA"
        if st.session_state.test_skill:
            st.info(f"Selected: {st.session_state.test_skill}")
            if st.button(f"Start {st.session_state.test_skill} Test →", type="primary", use_container_width=True):
                st.session_state.test_started=True; st.session_state.test_answers={}; st.rerun()

    elif st.session_state.test_started and not st.session_state.game_unlocked:
        skill = st.session_state.test_skill
        questions = TEST_BANK.get(skill, TEST_BANK["Python"])
        st.subheader(f"Test Running: {skill} - {len(questions)} Questions - Answer to Unlock Game Zone")
        for i,q in enumerate(questions):
            with st.container(border=True):
                st.markdown(f"**Q{i+1}. {q['q']}**")
                ans = st.radio(f"Select answer", q['o'], key=f"tq_{skill}_{i}", index=None)
                if ans: st.session_state.test_answers[i]=ans
        if st.button("Submit Test & Unlock Real Game Zone", type="primary", use_container_width=True):
            correct = sum(1 for idx,q in enumerate(questions) if st.session_state.test_answers.get(idx)==q['a'])
            st.session_state.xp+=correct*20
            st.session_state.game_unlocked=True
            st.session_state.test_started=False
            st.balloons()
            st.success(f"Score {correct}/{len(questions)} - Game Zone Unlocked!")
            st.rerun()

    else:
        skill = st.session_state.test_skill or "Python"
        st.success(f"Test Completed! Real Game Zone Unlocked - Skill: {skill}")

        game_html = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body { margin: 0; background: #1a1a2e; display: flex; justify-content: center; align-items: center; flex-direction: column; font-family: Arial; }
            #gameCanvas { border: 3px solid #667eea; border-radius: 15px; background: linear-gradient(180deg, #16213e 0%, #0f3460 100%); }
            #info { color: white; margin: 10px; text-align: center; }
            .controls { color: #aaa; font-size: 12px; margin-top: 5px; }
        </style>
        </head>
        <body>
            <div id="info">
                <div>Score: <span id="score">0</span> | Target: Collect <b style="color: #4ade80">0, 3, 6, 9</b> in order | Lives: <span id="lives">3</span></div>
                <div>Collected: <span id="collected">[]</span></div>
            </div>
            <canvas id="gameCanvas" width="600" height="400"></canvas>
            <div class="controls">CONTROLS: Arrow Keys / WASD to Move | Collect GREEN coins (0,3,6,9) | Avoid RED bombs</div>
            <div id="message" style="color: #fbbf24; font-weight: bold; margin-top: 10px; font-size: 18px;"></div>
        <script>
            const canvas = document.getElementById('gameCanvas');
            const ctx = canvas.getContext('2d');
            const scoreEl = document.getElementById('score');
            const livesEl = document.getElementById('lives');
            const collectedEl = document.getElementById('collected');
            const messageEl = document.getElementById('message');
            let player = { x: 300, y: 200, size: 20, speed: 5, color: '#667eea' };
            let keys = {}; let score = 0; let lives = 3; let collected = [];
            let targetSequence = [0,3,6,9]; let coins = []; let gameOver = false; let win = false;
            function spawnCoins() {
                coins = [];
                let correctVals = [0,3,6,9];
                correctVals.forEach(val => { coins.push({ x: Math.random()*550+25, y: Math.random()*350+25, value: val, isCorrect: true, size: 18, color: '#4ade80', collected: false }); });
                let wrongVals = [1,2,4,5,7,8];
                wrongVals.forEach(val => { coins.push({ x: Math.random()*550+25, y: Math.random()*350+25, value: val, isCorrect: false, size: 16, color: '#ef4444', collected: false }); });
            }
            function drawPlayer() {
                ctx.fillStyle = player.color; ctx.beginPath(); ctx.arc(player.x, player.y, player.size, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = 'white'; ctx.beginPath(); ctx.arc(player.x-5, player.y-5, 4, 0, Math.PI*2); ctx.arc(player.x+5, player.y-5, 4, 0, Math.PI*2); ctx.fill();
            }
            function drawCoins() {
                coins.forEach(coin => {
                    if(!coin.collected) {
                        ctx.fillStyle = coin.color; ctx.beginPath(); ctx.arc(coin.x, coin.y, coin.size, 0, Math.PI*2); ctx.fill();
                        ctx.strokeStyle = 'white'; ctx.lineWidth = 2; ctx.stroke();
                        ctx.fillStyle = 'white'; ctx.font = 'bold 14px Arial'; ctx.textAlign = 'center'; ctx.fillText(coin.value, coin.x, coin.y+5);
                    }
                });
            }
            function checkCollision() {
                coins.forEach(coin => {
                    if(!coin.collected) {
                        let dx = player.x - coin.x; let dy = player.y - coin.y; let dist = Math.sqrt(dx*dx + dy*dy);
                        if(dist < player.size + coin.size) {
                            coin.collected = true;
                            if(coin.isCorrect) {
                                if(collected.length < targetSequence.length && coin.value === targetSequence[collected.length]) {
                                    collected.push(coin.value); score += 25; messageEl.textContent = `Correct! Collected ${coin.value} - range(0,10,3) logic!`; messageEl.style.color = '#4ade80';
                                } else { messageEl.textContent = `Wrong order! Need ${targetSequence[collected.length]} but got ${coin.value}`; messageEl.style.color = '#ef4444'; lives--; }
                            } else { score = Math.max(0, score-10); lives--; messageEl.textContent = `BOMB! ${coin.value} is wrong! Lives -1`; messageEl.style.color = '#ef4444'; canvas.style.transform = 'translate(5px,5px)'; setTimeout(()=> canvas.style.transform='translate(0,0)', 100); }
                            updateUI(); checkWin();
                        }
                    }
                });
            }
            function updateUI() { scoreEl.textContent = score; livesEl.textContent = lives; collectedEl.textContent = '[' + collected.join(', ') + ']'; }
            function checkWin() {
                if(JSON.stringify(collected) === JSON.stringify(targetSequence)) { win = true; messageEl.textContent = 'WIN! You mastered range(0,10,3) = 0,3,6,9! +100 XP!'; messageEl.style.color = '#4ade80'; }
                if(lives <= 0 && !win) { gameOver = true; messageEl.textContent = 'Game Over! Lives over! Refresh to retry!'; messageEl.style.color = '#ef4444'; }
            }
            function update() {
                if(gameOver || win) return;
                if(keys['ArrowUp'] || keys['w'] || keys['W']) player.y -= player.speed;
                if(keys['ArrowDown'] || keys['s'] || keys['S']) player.y += player.speed;
                if(keys['ArrowLeft'] || keys['a'] || keys['A']) player.x -= player.speed;
                if(keys['ArrowRight'] || keys['d'] || keys['D']) player.x += player.speed;
                player.x = Math.max(player.size, Math.min(canvas.width-player.size, player.x));
                player.y = Math.max(player.size, Math.min(canvas.height-player.size, player.y));
                ctx.clearRect(0,0,canvas.width, canvas.height); drawCoins(); drawPlayer(); checkCollision(); requestAnimationFrame(update);
            }
            window.addEventListener('keydown', (e)=> { keys[e.key] = true; });
            window.addEventListener('keyup', (e)=> { keys[e.key] = false; });
            canvas.addEventListener('touchmove', (e)=>{ e.preventDefault(); let touch = e.touches[0]; let rect = canvas.getBoundingClientRect(); player.x = touch.clientX - rect.left; player.y = touch.clientY - rect.top; });
            spawnCoins(); update();
        </script>
        </body>
        </html>
        """
        components.html(game_html, height=550, width=650)
        st.divider()
        c1,c2,c3 = st.columns(3)
        with c1: st.success("GREEN: Collect 0,3,6,9 in order - +25 XP each - range(0,10,3) logic")
        with c2: st.error("RED: Avoid 1,2,4,5,7,8 - Bomb - -10 XP, -1 Life")
        with c3: st.info("CONTROLS: Arrow Keys / WASD / Touch Drag - Real playable game")
        if st.button("I Won Game - Claim +100 XP", type="primary"): st.session_state.xp+=100; st.session_state.game_score+=100; st.balloons(); st.success("Champion! +100 XP")
        if st.button("Go to Certificate Zone"): st.session_state.purpose="certificate"; st.session_state.cert_stage="select"; st.rerun()

# ================= 4TH PAGE: CERTIFICATE - AI INTERVIEW → CERTIFICATE =================
elif st.session_state.purpose == "certificate":
    AI_BANK = {
        "Python": ["Explain what is Python and why you chose it?", "What is difference between List and Tuple?", "Explain range(0,10,3) - What is output and why?", "What is OOPS in Python?", "How would you handle large dataset in Python?"],
        "General": ["Tell me about yourself and your college?", "Why should we hire you for Data Engineer role?", "Where do you see yourself in 5 years?", "Explain a project you did using your skills?"]
    }
    st.title("Certificate Zone - Random AI Interview → Certificate")
    if st.session_state.cert_stage == "select":
        st.subheader("Step 1: Select Skill for Certificate")
        if st.button("Python Certificate"): st.session_state.cert_skill="Python"
        if st.button("SQL Certificate"): st.session_state.cert_skill="SQL"
        if st.button("Java Certificate"): st.session_state.cert_skill="Java"
        if st.button("DSA Certificate"): st.session_state.cert_skill="DSA"
        if st.session_state.cert_skill:
            if st.button(f"Start AI Interview for {st.session_state.cert_skill} Certificate →", type="primary"):
                qs = random.sample(AI_BANK["Python"]+AI_BANK["General"], 5)
                st.session_state.cert_questions=qs; st.session_state.cert_stage="interview"; st.session_state.cert_answers={}; st.rerun()
    elif st.session_state.cert_stage == "interview":
        st.subheader(f"AI Interview Started - {st.session_state.cert_skill} - 5 Random Questions")
        for i,q in enumerate(st.session_state.cert_questions):
            st.write(f"Q{i+1}: {q}")
            ans = st.text_area(f"Your Answer Q{i+1}", key=f"cert_{i}", placeholder="Minimum 20 characters")
            if ans and len(ans)>10: st.session_state.cert_answers[i]=ans
        if len(st.session_state.cert_answers)>=3:
            if st.button("Submit Interview & Generate Certificate", type="primary"):
                score = min(100, 50 + len(st.session_state.cert_answers)*10 + sum(len(v) for v in st.session_state.cert_answers.values())//20)
                st.session_state.cert_score=score; st.session_state.cert_stage="result"; st.rerun()
        else: st.warning(f"Answer at least 3 questions - Currently {len(st.session_state.cert_answers)}/5")
    else:
        score = st.session_state.cert_score
        st.balloons()
        st.success(f"AI Interview Completed - Score: {score}%")
        if score>=60:
            st.markdown(f"""
            <div style="border:3px solid #667eea; padding:40px; border-radius:15px; text-align:center; background:white">
                <div style="font-size:50px">🏆</div>
                <div style="font-size:40px; font-weight:900; color:#667eea">BHAVPATH</div>
                <div style="letter-spacing:3px">CERTIFICATE OF EXCELLENCE</div>
                <div style="height:2px; background:linear-gradient(90deg,#667eea,#764ba2); margin:20px 0"></div>
                <div>Presented to</div>
                <div style="font-size:30px; font-weight:800">{st.session_state.name}</div>
                <div>{st.session_state.college} - {st.session_state.email}</div>
                <div style="margin:20px">For successfully completing <b>{st.session_state.cert_skill} Skill Assessment</b> with <b>AI Interview Score {score}%</b></div>
                <div style="background:#f8f9ff; padding:15px; border-radius:10px">Status: <b style="color:green">PLACEMENT READY - {st.session_state.cert_skill} EXPERT</b><br>Certificate ID: BP-{st.session_state.cert_skill}-{score}-{st.session_state.xp}</div>
            </div>
            """, unsafe_allow_html=True)
            st.download_button("Download Certificate", data=f"BHAVPATH CERTIFICATE\nName: {st.session_state.name}\nCollege: {st.session_state.college}\nEmail: {st.session_state.email}\nSkill: {st.session_state.cert_skill}\nScore: {score}%\nStatus: PLACEMENT READY", file_name=f"BhavPath_{st.session_state.cert_skill}_Certificate.txt", type="primary")
        else:
            st.error(f"Score {score}% - Minimum 60% needed - Retry")
        if st.button("New Certificate - Retry"): st.session_state.cert_stage="select"; st.session_state.xp+=100; st.rerun()

# ================= 4TH PAGE: INTERVIEW QUESTIONS =================
else:
    st.title("Interview Questions - TCS NQT, Infosys, Wipro")
    company = st.selectbox("Select Company", ["TCS NQT", "Infosys SP", "Wipro Elite", "Accenture"])
    st.code(f"Q1: What is output of range(0,10,3)?\nAns: 0,3,6,9 - range(start, stop, step)\n\nQ2: SQL - How to get average BTech %?\nAns: SELECT AVG(btech) FROM students;\n\nQ3: What is OOPS?\nAns: Object Oriented Programming - 4 pillars\n\nCompany: {company} - Focus on Python, SQL, Aptitude")
    ans = st.text_area("Your Answer Practice")
    if st.button("Submit Answer +50 XP"): st.session_state.xp+=50; st.success("Good!")
