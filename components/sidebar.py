import streamlit as st

def render_sidebar():
    with st.sidebar:
        # Custom CSS for sidebar
        st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <div style="position: relative; display: inline-block;">
                    <div class="cyber-pulse" style="
                        position: absolute;
                        width: 60px;
                        height: 60px;
                        background: rgba(124, 58, 237, 0.1);
                        border-radius: 50%;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        z-index: 0;
                    "></div>
                    <h1 style="
                        font-size: 1.75rem; 
                        color: white; 
                        margin-bottom: 0.5rem;
                        position: relative;
                        z-index: 1;
                        font-family: 'Space Mono', monospace;
                    ">
                        <span style="color: #7c3aed; text-shadow: 0 0 8px rgba(124, 58, 237, 0.4);">YARA</span>Assist
                    </h1>
                </div>
                <p style="color: #64748b; font-size: 0.85rem; margin-top: 0.5rem; font-family: 'Ubuntu Mono', monospace;">
                    :: YARA RULEs GENERATOR ::
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Sidebar menu with radio buttons
        selected_page = st.radio(
            "Menu",
            options=["🏠 Home", "⚡ Generate"],
            label_visibility="collapsed",
            index=0
        )
        
        #  My Card 
        st.markdown("""
            <div class="author-card">
                <div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 0.5rem;">
                    <div style="
                        width: 80px;
                        height: 80px;
                        border-radius: 50%;
                        background: linear-gradient(135deg, #7c3aed, #4f46e5);
                        display: grid;
                        place-items: center;
                        margin-bottom: 1rem;
                        overflow: hidden;
                        border: 2px solid #7c3aed;
                    ">
                        <img src="https://avatar.iran.liara.run/public/41" 
                             style="
                                 width: 100%;
                                 height: 100%;
                                 object-fit: cover;
                                 object-position: center;
                                 display: block;
                             " 
                             onerror="this.src='data:image/svg+xml;charset=UTF-8,<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 100 100\"><rect width=\"100\" height=\"100\" fill=\"%234f46e5\"/><text x=\"50\" y=\"60\" font-size=\"40\" fill=\"white\" text-anchor=\"middle\" dominant-baseline=\"middle\">AA</text></svg>'">
                    </div>
                    <h4 style="
                        margin: 0; 
                        color: white; 
                        font-family: 'Space Mono', monospace;
                        font-size: 1rem;
                    ">
                        ABDELRAHMAN ALADWANI
                    </h4>
                    <div style="
                        background: rgba(124, 58, 237, 0.1);
                        color: #7c3aed;
                        padding: 0.25rem 0.75rem;
                        border-radius: 999px;
                        font-size: 0.75rem;
                        font-weight: 600;
                        margin: 0.5rem 0;
                        font-family: 'Ubuntu Mono', monospace;
                    ">
                        System Administrator
                    </div>
                    <a href="https://www.linkedin.com/in/abdelrahman-aladwani-a95063285/" 
                       target="_blank" 
                       style="
                           color: #7c3aed; 
                           text-decoration: none; 
                           display: inline-flex;
                           align-items: center;
                           gap: 0.5rem;
                           font-size: 0.85rem;
                           margin-top: 0.5rem;
                           transition: all 0.3s;
                       " 
                       onmouseover="this.style.color='#a78bfa'" 
                       onmouseout="this.style.color='#7c3aed'">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                        </svg>
                        CONNECT
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        return selected_page