import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def render_home():
    with stylable_container(
        key="hero_container",
        css_styles="""
            {
                background: linear-gradient(135deg, #0f172a, #1e293b);
                border-radius: 12px;
                padding: 3rem 2rem;
                margin-bottom: 3rem;
                border: 1px solid #334155;
                border-left: 4px solid #7c3aed;
                font-family: 'Ubuntu Mono', monospace;
                position: relative;
                overflow: hidden;
            }
        """
    ):
        st.markdown("""
            <div style="position: absolute; top: 0; right: 0; width: 100%; height: 100%; background: radial-gradient(circle at 70% 30%, rgba(124, 58, 237, 0.1) 0%, transparent 70%); z-index: 0;"></div>
            <div style="position: relative; z-index: 1;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
                    <div style="width: 12px; height: 12px; border-radius: 50%; background: #7c3aed;"></div>
                    <h1 style="color: white; margin: 0; font-family: 'Space Mono', monospace; font-size: 2rem;">YARAAssist</h1>
                </div>
                <div style="color: #94a3b8; margin-bottom: 1.5rem;">
                    <p style="margin: 0; font-size: 1.1rem;">>_ Initialize YARA rule</p>
                </div>
                <div style="display: inline-block; background: rgba(124, 58, 237, 0.2); color: #7c3aed; padding: 0.5rem 1rem; border-radius: 6px; border-left: 3px solid #7c3aed; font-size: 0.9rem;">
                    STATUS: SYSTEM READY
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="margin-bottom: 2rem;">
            <h2 style="color: white; font-family: 'Space Mono', monospace; border-bottom: 2px solid #334155; padding-bottom: 0.5rem;">CORE CAPABILITIES</h2>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_feature_card(
            title="RULE ENGINE",
            content="Advanced pattern matching engine with support for strings, hex patterns, and regular expressions."
        )
        
        render_feature_card(
            title="CONDITION LOGIC",
            content="Flexible matching conditions with \"any\" or \"all\" operators for precise threat detection."
        )
    
    with col2:
        render_feature_card(
            title="METADATA INTEGRATION",
            content="Comprehensive rule metadata including author, description, and reference information."
        )
        
        render_feature_card(
            title="PRODUCTION OUTPUT",
            content="Enterprise-ready YARA rules formatted for immediate deployment in security infrastructure."
        )
    
    render_cta_section()

def render_feature_card(title, content):
    with stylable_container(
        key=f"feature_{title.replace(' ', '_')}",
        css_styles="""
            {
                background: linear-gradient(135deg, #1e293b, #0f172a);
                border-radius: 12px;
                padding: 1.5rem;
                border: 1px solid #334155;
                border-top: 3px solid #7c3aed;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
        """
    ):
        st.markdown(f"""
            <div class="feature-card">
                <h3 style="color: white; margin-top: 0; font-family: 'Space Mono', monospace;">{title}</h3>
                <div style="height: 2px; background: linear-gradient(to right, #7c3aed, transparent); margin: 0.5rem 0;"></div>
                <p style="color: #94a3b8; margin-bottom: 0;">
                    {content}
                </p>
            </div>
        """, unsafe_allow_html=True)

def render_cta_section():
    with stylable_container(
        key="cta_container",
        css_styles="""
            {
                background: linear-gradient(135deg, rgba(15, 23, 42, 0.7), rgba(30, 41, 59, 0.7));
                border-radius: 12px;
                padding: 2rem;
                border: 1px dashed #7c3aed;
                margin-top: 3rem;
                text-align: center;
                backdrop-filter: blur(5px);
            }
        """
    ):
        st.markdown("""
            <div style="margin-bottom: 1rem;">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                    <line x1="12" y1="9" x2="12" y2="13"></line>
                    <line x1="12" y1="17" x2="12.01" y2="17"></line>
                </svg>
            </div>
            <h3 style="color: white; font-family: 'Space Mono', monospace;">READY TO DEPLOY?</h3>
            <p style="color: #94a3b8; max-width: 600px; margin: 0 auto 1.5rem;">
                Navigate to the <span style="color: #7c3aed; font-weight: 500;">Generate</span> section to create your first YARA rule.
            </p>
        """, unsafe_allow_html=True)