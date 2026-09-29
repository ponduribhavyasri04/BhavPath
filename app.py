# app.py - BHAVPATH - LONG LASTING - NO EXTERNAL LINKS - JUST BHAVYA PONDURI - STABLE 2026-2030
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import textwrap

# --- STABLE FONT - NEVER BREAKS ---
def get_font(s,b=False):
    try:
        # Linux Streamlit Cloud fonts
        path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(path, s)
    except:
        return ImageFont.load_default()

# --- PDF - WATERMARK JUST BHAVPATH - BHAVYA PONDURI - LONG LASTING ---
def make_pdf():
    W,H = 900, 1100
    img = Image.new("RGB", (W,H), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([(10,10),(W-10,H-10)], outline="#A29BFE", width=2)
    d.rectangle([(20,20),(W-20,85)], fill="#0F172A")
    d.text((25,30), "BhavPath - Bhavya Ponduri", font=get_font(18,True), fill="white")
    d.text((25,60), "Ex: Bhavya Ponduri | 58% | CSE | TCS Target", font=get_font(11), fill="#A29BFE")
    y=110
    d.text((30,y), "Welcome Bhavya Ponduri!", font=get_font(16,True), fill="#1E293B"); y+=35
    txt = "Hi Bhavya Ponduri! 58% CSE. Your placement roadmap ready. Capgemini 55% eligible, TCS 60% with projects. Simple English excellent content. Long lasting code - never breaks."
    for line in textwrap.wrap(txt, width=72):
        d.text((30,y), line, font=get_font(12), fill="black"); y+=18
    y+=15
    d.text((30,y), "Placement Road:", font=get_font(13,True), fill="#6C5CE7"); y+=22
    roads = ["1. Python Basics - print('Hello Bhavya Ponduri')","2. DSA - List boxes [58,75,82], Stack plates LIFO, Linked List chain","3. SQL - 2nd highest salary, JOINs - Table picture","4. PYQ - TCS NQT 2022 2023 2024 same repeat","5. Interview - My name is Bhavya Ponduri, CSE 58%","6. Goal - TCS Job - Bhavya Ponduri success"]
    for r in roads:
        d.text((30,y), r, font=get_font(11), fill="#1E293B"); y+=18
    y+=20
    d.text((30,y), "Eligible Companies - 58%:", font=get_font(13,True), fill="#0F172A"); y+=22
    for c in ["Capgemini 55% - Eligible","TCS NQT 60% - Eligible with Projects","Wipro 60% - Eligible","Infosys 65% - Need 65%"]:
        d.text((30,y), f"- {c}", font=get_font(11), fill="#475569"); y+=18
    # WATERMARK - JUST BHAVPATH - BHAVYA PONDURI - LONG LASTING - NO OTHER INFO
    d.text((W//2, H-15), "BhavPath - Bhavya Ponduri", font=get_font(10), fill="#E5E7EB", anchor="mm")
    buf = io.BytesIO()
    img.save(buf, format="PDF")
    return buf.getvalue()

# --- ANIMATED VIDEOS - PURE CSS - NO EXTERNAL LINKS - LONG LASTING - NEVER BREAKS ---
def animated_videos():
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0F172A,#1E293B); padding:22px; border-radius:18px; border:1px solid #6C5CE7; text-align:center; margin-bottom:18px;">
      <p style="color:#A29BFE; font-size:10px; letter-spacing:3px; margin:0;">ANIMATED VIDEO - OUR OWN - LONG LASTING - NO EXTERNAL LINK</p>
      <h4 style="color:white; margin:10px 0 5px 0;">List - Boxes - Bhavya Ponduri Marks [58,75,82]</h4>
      <div style="display:flex; gap:12px; justify-content:center; margin:18px 0;">
        <div style="background:#6C5CE7; color:white; padding:14px 20px; border-radius:14px; font-weight:800; font-size:18px; animation: bounce 1s infinite;">58<br><span style="font-size:10px;">[0]</span></div>
        <div style="background:#FF6B6B; color:white; padding:14px 20px; border-radius:14px; font-weight:800; font-size:18px; animation: bounce 1s infinite 0.2s;">75<br><span style="font-size:10px;">[1]</span></div>
        <div style="background:#48DBFB; color:white; padding:14px 20px; border-radius:14px; font-weight:800; font-size:18px; animation: bounce 1s infinite 0.4s;">82<br><span style="font-size:10px;">[2]</span></div>
      </div>
      <div style="background:rgba(255,255,255,0.05); padding:12px; border-radius:12px; text-align:left;">
        <p style="color:#E5E7EB; font-size:13px; margin:0;"><b style="color:#A29BFE;">Simple English:</b> List is collection of boxes. Order fixed. You can add, remove, change. Example Bhavya Ponduri marks are [58,75,82]. Index [0]=58 means first box.</p>
      </div>
      <div style="background:rgba(254,202,87,0.1); padding:12px; border-radius:12px; text-align:left; margin-top:10px;">
        <p style="color:#FECA57; font-size:13px; margin:0;"><b>Telugu:</b> List ante dabba lanti di. Bhavya Ponduri marks 58,75,82. [0] ante modati dabba. Append ante kothadi add cheyadam. Chala easy ga ardham avuthundi!</p>
      </div>
      <p style="color:#64748B; font-size:10px; margin-top:12px;">BhavPath - Bhavya Ponduri | Long lasting CSS animation</p>
    </div>

    <div style="background:linear-gradient(135deg,#0F172A,#1E293B); padding:22px; border-radius:18px; border:1px solid #FF6B6B; text-align:center; margin-bottom:18px;">
      <p style="color:#FF6B6B; font-size:10px; letter-spacing:3px;">ANIMATED VIDEO - STACK - LIFO</p>
      <h4 style="color:white; margin:10px 0;">Stack - Plates - Bhavya Ponduri</h4>
      <div style="display:flex; flex-direction:column-reverse; align-items:center; gap:8px; margin:18px 0;">
        <div style="width:160px; padding:12px; background:#6C5CE7; border-radius:10px; color:white; font-weight:700; animation: pop 1.5s infinite;">Bottom - Bhavya</div>
        <div style="width:160px; padding:12px; background:#FF6B6B; border-radius:10px; color:white; font-weight:700; animation: pop 1.5s infinite 0.5s;">Middle - Ponduri</div>
        <div style="width:160px; padding:12px; background:#48DBFB; border-radius:10px; color:white; font-weight:700; border:2px dashed white; animation: pop 1.5s infinite 1s;">Top - Pop() Here</div>
      </div>
      <div style="background:rgba(255,255,255,0.05); padding:12px; border-radius:12px; text-align:left;">
        <p style="color:#E5E7EB; font-size:13px; margin:0;"><b style="color:#A29BFE;">Simple English:</b> Stack is Last In First Out - LIFO. Last plate you put is first you take. Push = add, Pop = remove top.</p>
      </div>
      <div style="background:rgba(254,202,87,0.1); padding:12px; border-radius:12px; text-align:left; margin-top:10px;">
        <p style="color:#FECA57; font-size:13px; margin:0;"><b>Telugu:</b> Stack ante plates okadani meedha okati pettadam. Meedha pettina plate ne mundhu teestham. Danine LIFO antaru. Push ante pettadam, Pop ante teeyadam.</p>
      </div>
      <p style="color:#64748B; font-size:10px; margin-top:12px;">BhavPath - Bhavya Ponduri</p>
    </div>

    <div style="background:linear-gradient(135deg,#0F172A,#1E293B); padding:22px; border-radius:18px; border:1px solid #48DBFB; text-align:center;">
      <p style="color:#48DBFB; font-size:10px; letter-spacing:3px;">ANIMATED VIDEO - SQL - TABLE PICTURE</p>
      <h4 style="color:white; margin:10px 0;">SQL - 2nd Highest Salary - Most Asked in TCS</h4>
      <div style="background:#1E293B; padding:12px; border-radius:12px; margin:15px 0; font-family:monospace; color:#A29BFE; font-size:12px; text-align:left;">SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp);<br>-- Bhavya Ponduri Example</div>
      <div style="background:rgba(255,255,255,0.05); padding:12px; border-radius:12px; text-align:left;">
        <p style="color:#E5E7EB; font-size:13px; margin:0;"><b style="color:#A29BFE;">Simple English:</b> Find second highest salary from employee table. Use MAX inside MAX. Top question in TCS NQT and Infosys - 100% asked every year.</p>
      </div>
      <div style="background:rgba(254,202,87,0.1); padding:12px; border-radius:12px; text-align:left; margin-top:10px;">
        <p style="color:#FECA57; font-size:13px; margin:0;"><b>Telugu:</b> Employee table lo second highest salary kanukkovadam. Modati highest theesesaka migilina vatillo highest teesukunte second highest vasthundi. TCS lo prathi sari adugutharu - chala important!</p>
      </div>
      <p style="color:#64748B; font-size:10px; margin-top:12px;">BhavPath - Bhavya Ponduri</p>
    </div>

    <style>
    @keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
    @keyframes pop{0%{transform:scale(0.85)}50%{transform:scale(1.08)}100%{transform:scale(1)}}
    </style>
    """, unsafe_allow_html=True)

# --- APP CONFIG - LONG LASTING ---
st.set_page_config(page_title="BhavPath - Bhavya Ponduri", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.stApp{background:#070711!important;}
.orb{position:fixed; border-radius:50%; filter:blur(90px); opacity:0.45; pointer-events:none;}
.orb1{width:500px; height:500px; background:radial-gradient(circle,#6C5CE7,#FF6B6B); top:-150px; left:-150px;}
.orb2{width:400px; height:400px; background:radial-gradient(circle,#48DBFB,#6C5CE7); top:25%; right:-100px;}
.glass{background:rgba(255,255,255,0.04)!important; backdrop-filter:blur(18px)!important; border:1px solid rgba(255,255,255,0.08)!important; border-radius:20px!important;}
.hero{font-size:75px!important; font-weight:800!important; background:linear-gradient(100deg,#fff 30%,#A29BFE 70%)!important; -webkit-background-clip:text!important; -webkit-text-fill-color:transparent!important; margin:0!important;}
.stButton>button{background:linear-gradient(100deg,#6C5CE7,#FF6B6B)!important; border:none!important; border-radius:100px!important; padding:14px 28px!important; font-weight:800!important; color:white!important; width:100%!important; font-size:16px!important; transition:0.3s!important;}
.stButton>button:hover{transform:scale(1.02)!important;}
</style>
<div class="orb orb1"></div><div class="orb orb2"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:35px 20px 5px 20px; position:relative; z-index:2;">
  <h1 class="hero">BhavPath</h1>
  <p style="color:#A29BFE; font-size:14px; letter-spacing:3px; margin-top:5px;">Ex: Bhavya Ponduri</p>
  <p style="color:#64748B; font-size:11px;">Long Lasting • Neat • No Addition Info • Animated • Simple English • Telugu Video</p>
</div>
""", unsafe_allow_html=True)

# --- MAIN - JUST BHAVYA PONDURI - NO LAUNCH FOR - LONG LASTING ---
st.markdown('<div class="glass" style="padding:22px; margin:20px; position:relative; z-index:2; text-align:center;">', unsafe_allow_html=True)
st.markdown("#### Example: Bhavya Ponduri - 58% - CSE - TCS Target")
st.caption("Long lasting code - no external links - stable - 2026 to 2030 work avuthundi")
go = st.button("🚀 Launch →")
st.markdown('</div>', unsafe_allow_html=True)

if go:
    st.balloons()
    st.markdown('<div class="glass" style="padding:20px; margin:20px; position:relative; z-index:2;"><h2 style="color:white; margin:0;">Welcome Bhavya Ponduri! 🎉</h2><p style="color:#A29BFE; margin:5px 0 0 0;">58% | CSE | BhavPath - Bhavya Ponduri | Long lasting journey starts</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="glass" style="padding:20px; margin:0 20px; position:relative; z-index:2;">', unsafe_allow_html=True)
    st.markdown("### ✅ Eligible Companies for Bhavya Ponduri - 58%")
    st.success("Capgemini - 55% - Eligible ✅ - Bhavya Ponduri")
    st.success("TCS NQT - 60% - Eligible with Projects ✅ - Long lasting")
    st.success("Wipro - 60% - Eligible with Projects ✅")
    st.warning("Infosys - 65% - Need 65% - Try strong projects Bhavya")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass" style="padding:20px; margin:20px; position:relative; z-index:2;">', unsafe_allow_html=True)
    st.markdown("### 🗺️ Placement Road for Bhavya Ponduri - Excellent Simple English - Long Lasting")
    st.markdown("""
    **Excellent Simple English - Long lasting content for Bhavya Ponduri:**

    - **Step 1 - Python Basics:** Python is easy language. Like ABC. `print("Hello Bhavya Ponduri")` - very simple - long lasting skill.
    - **Step 2 - DSA:** List is boxes [58,75,82], Stack is plates LIFO, Linked List is chain - easy with animated pics - never change.
    - **Step 3 - SQL:** Find 2nd highest salary, JOINs - Most asked in TCS - table picture with animation - long lasting question.
    - **Step 4 - PYQ:** TCS NQT 2022, 2023, 2024 - Same questions repeat - practice daily - long lasting prep.
    - **Step 5 - Interview:** Self intro - My name is Bhavya Ponduri, CSE 58%, I love coding - List vs Tuple - simple words - long lasting.
    - **Final Goal:** TCS Job - Like Bhavya Ponduri success story - Long lasting career!
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass" style="padding:20px; margin:20px; position:relative; z-index:2;">', unsafe_allow_html=True)
    st.markdown("### 🎬 Animated Videos - Our Own - Not Others - Telugu Explanation - Long Lasting")
    animated_videos()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass" style="padding:20px; margin:20px; position:relative; z-index:2; text-align:center;">', unsafe_allow_html=True)
    st.markdown("#### 📄 Download PDF - Long Lasting - Just BhavPath - Bhavya Ponduri")
    st.download_button("📥 Download PDF - BhavPath - Bhavya Ponduri - Click Here", make_pdf(), "BhavPath-Bhavya_Ponduri-LongLasting.pdf", "application/pdf", use_container_width=True)
    st.markdown('<p style="color:#E5E7EB; font-size:10px; margin-top:12px; letter-spacing:2px;">BhavPath - Bhavya Ponduri</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.success("Done Bhavya! Long lasting code ready - No external links - Just BhavPath - Bhavya Ponduri watermark - Never breaks till 2030!")
