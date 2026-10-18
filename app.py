# ===== SPECIFIC TOPIC - MODULES LIST - BULLET GREEN UNDERLINE =====
with col_content:
    t = TOPICS[st.session_state.selected_topic]
    st.subheader(f"📖 {t['title']} - For {st.session_state.user['btech']}%")

    # SPECIFIC TOPIC - LIST LO YEM VUNTAYO
    st.markdown(f'<div class="white-card"><b>📋 {t["title"]} - Specific Topic Modules:</b></div>', unsafe_allow_html=True)
    
    for i, mod in enumerate(t["modules"]):
        is_sel = st.session_state.current_mod == i
        is_done = st.session_state.completed.get(f"{st.session_state.selected_topic}_{i}")
        tick = "✅" if is_done else "•"
        
        if is_sel:
            st.markdown(f'<div style="background:#2563EB; color:white; border-radius:8px; padding:8px; margin-bottom:6px;"><b>{tick} {i+1}. {mod["name"]} - Selected ✅</b></div>', unsafe_allow_html=True)
        else:
            if st.button(f"{tick} {i+1}. {mod['name']}", key=f"specific_{st.session_state.selected_topic}_{i}", use_container_width=True):
                st.session_state.current_mod = i
                st.rerun()

    st.divider()
    st.write("👇 **Selected Module Content - Kinda:**")

    # CONTENT
    mod = t["modules"][st.session_state.current_mod]
    st.markdown(f'<div class="white-card"><b>Module {st.session_state.current_mod+1}: {mod["name"]}</b><br><br>{mod["content"]}<br><br>For {st.session_state.user["btech"]}% profile - Helps in TCS NQT!</div>', unsafe_allow_html=True)
    st.code(mod["code"], language="python" if st.session_state.selected_topic in ["Python","Data Engineering"] else "cpp")
    
    # Buttons same...
    col_prev, col_done, col_next = st.columns([1,1,1])
    with col_prev:
        if st.session_state.current_mod > 0:
            if st.button("← Prev"): st.session_state.current_mod -=1; st.rerun()
    with col_done:
        key = f"{st.session_state.selected_topic}_{st.session_state.current_mod}"
        if st.session_state.completed.get(key): st.success("✅ Done")
        else:
            if st.button(f"Mark Done +50 XP", key=f"done_{key}"):
                st.session_state.completed[key]=True; st.session_state.xp+=50; st.balloons(); st.rerun()
    with col_next:
        if st.session_state.current_mod < len(t["modules"])-1:
            if st.button("Next →"): st.session_state.current_mod+=1; st.rerun()
