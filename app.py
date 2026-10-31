import matplotlib.pyplot as plt
import io

def create_memory_image(topic, skill):
    # Creates real pic diagram instead of +---+
    fig, ax = plt.subplots(figsize=(8, 2.5))
    fig.patch.set_facecolor('#05000a')
    ax.set_facecolor('#05000a')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2)
    ax.axis('off')
    
    # Addresses
    addrs = [1000, 1004, 1008, 1012]
    vals = ["Val1","Val2","Val3","Val4"]
    colors = ['#0d4aff', '#ff006a', '#fef08a', '#00f5ff']
    
    for i in range(4):
        x = i*2.5 + 0.2
        # Box
        rect = plt.Rectangle((x, 0.5), 2, 1.2, fill=False, edgecolor=colors[i], linewidth=2)
        ax.add_patch(rect)
        ax.text(x+1, 1.8, f"Addr: {addrs[i]}", color='white', ha='center', fontsize=9, weight='bold')
        ax.text(x+1, 1.0, vals[i], color='white', ha='center', fontsize=14, weight='bold')
    
    # Pointer arrow
    ax.annotate('pointer (ptr)', xy=(3.5, 0.5), xytext=(3.5, -0.2),
                arrowprops=dict(facecolor='#ff006a', shrink=0.05, width=2, headwidth=8),
                color='#ff006a', ha='center', fontsize=12, weight='bold')
    
    ax.set_title(f'{skill} - {topic} - Memory Layout Diagram', color='white', fontsize=14, pad=20)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return buf

def create_architecture_image(skill, topic):
    fig, ax = plt.subplots(figsize=(8, 1.5))
    fig.patch.set_facecolor('#05000a')
    ax.set_facecolor('#05000a')
    ax.axis('off')
    
    steps = [f'User Code\n({topic})', 'Compiler\n/ Interpreter', 'Memory\n(Stack+Heap)', 'Output']
    for i, step in enumerate(steps):
        x = i*2.8 + 0.5
        rect = plt.Rectangle((x, 0.3), 2, 0.8, fill=True, facecolor='#1a1a3a', edgecolor='#0d4aff', linewidth=2)
        ax.add_patch(rect)
        ax.text(x+1, 0.7, step, color='white', ha='center', va='center', fontsize=8, weight='bold')
        if i < 3:
            ax.annotate('', xy=(x+2.1, 0.7), xytext=(x+2.5, 0.7),
                        arrowprops=dict(arrowstyle='->', color='#ff006a', lw=2))
    
    ax.set_title(f'{skill} - {topic} Architecture', color='white', fontsize=12)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 1.5)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return buf

# ===== SKILL DETAIL PAGE LO - PIC DIAGRAMS =====
elif st.session_state.page == "skill_detail":
    skill=st.session_state.selected_skill
    st.markdown(f"<div class='center'><h1 style='color:white;'>{skill} - Full Detailed Learning</h1></div>", unsafe_allow_html=True)
    all_topics={"C":["Intro","Data Types","Loops","Functions","Pointers","Arrays","Structures","File Handling"],"C++":["Basics","OOP","STL","Pointers","Inheritance","Polymorphism","Templates","Projects"],"Java":["Basics","OOP","Collections","Exception","Multithreading","JDBC","Spring","Projects"],"Python":["Basics","Loops","Functions","OOP","Libraries","File Handling","Django","Projects"],"SQL":["SELECT","JOINS","GROUP BY","Subqueries","Indexing","Normalization","Procedures","Projects"],"DSA":["Arrays","Linked List","Stack & Queue","Trees","Graphs","Sorting","DP","Greedy"]}
    topics_list=all_topics.get(skill, all_topics["C"])
    _,c,_=st.columns([0.1,3,0.1])
    with c:
        col1,col2=st.columns([1,2.5])
        with col1:
            st.markdown(f"<div class='glass'><h3 style='color:white;margin:0;'>📚 {skill} Topics</h3></div>", unsafe_allow_html=True)
            st.write("")
            for i,t in enumerate(topics_list,1):
                if st.button(f"{i}. {t}", key=f"{skill}{i}", use_container_width=True, type="primary" if st.session_state.topic==t else "secondary"):
                    st.session_state.topic=t; st.rerun()
            if st.button("← Back"): st.session_state.page="tech_skills"; st.rerun()
        with col2:
            # DIAGRAMS AS PICS - NOT TEXT
            st.markdown(f"<div class='detail-box'>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#fef08a;'>📘 {st.session_state.topic} in {skill}</h2>", unsafe_allow_html=True)
            
            # Architecture pic
            arch_img = create_architecture_image(skill, st.session_state.topic)
            st.image(arch_img, caption=f"{skill} {st.session_state.topic} Architecture Flow")
            
            # Memory pic
            mem_img = create_memory_image(st.session_state.topic, skill)
            st.image(mem_img, caption=f"{st.session_state.topic} Memory Layout - Address 1000,1004,1008,1012")
            
            # Content after pics
            content = get_detailed_content(skill, st.session_state.topic)
            st.markdown(f"<div style='color:white;white-space:pre-wrap;line-height:1.8;font-size:14px;'>{content}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
