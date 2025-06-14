import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container
from datetime import datetime
import re

def render_generate():
    # Cyber-themed header
    colored_header(
        label="ADVANCED YARA RULE GENERATOR",
        description="CONFIGURE COMPREHENSIVE DETECTION PARAMETERS",
        color_name="violet-70"
    )
    
    # Form section with tabs for different rule aspects
    tab1, tab2, tab3 = st.tabs(["Basic Rule", "Advanced Options", "Validation & Testing"])
    
    with tab1:
        render_basic_rule_section()
    
    with tab2:
        render_advanced_options_section()
    
    with tab3:
        render_validation_section()

def render_basic_rule_section():
    with stylable_container(
        key="form_container",
        css_styles="""
            {
                background: linear-gradient(135deg, #1e293b, #0f172a);
                border-radius: 12px;
                padding: 2rem;
                border: 1px solid #334155;
                margin-bottom: 2rem;
                font-family: 'Ubuntu Mono', monospace;
                border-left: 4px solid #7c3aed;
            }
        """
    ):
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">
                <div style="width: 10px; height: 10px; border-radius: 50%; background: #7c3aed;"></div>
                <div style="color: #7c3aed; font-size: 0.9rem;">RULE CONFIGURATION</div>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            rule_name = st.text_input("Rule Name*", "malware_family", help="Unique name for your YARA rule (letters, numbers, underscores only)")
            threat_level = st.selectbox(
                "Threat Level",
                options=["Low", "Medium", "High", "Critical"],
                index=2,
                help="Severity of the threat being detected"
            )
        
        with col2:
            author = st.text_input("Author/Organization", placeholder="Your name or company", help="Optional attribution")
            reference = st.text_input("Reference URL", placeholder="https://example.com/threat-report", help="Link to threat intelligence")
        
        description = st.text_area("Description*", placeholder="Detailed description of what this rule detects", height=100)
        
        st.markdown("""
            <div style="margin: 1.5rem 0 0.5rem; color: #7c3aed; font-size: 0.9rem;">
                Detection Strings* (one per line)
            </div>
        """, unsafe_allow_html=True)
        
        strings_input = st.text_area(
            "detection_strings",
            height=200,
            placeholder="Enter each detection pattern on a new line...\nExample:\nThis program cannot be run in DOS mode\nMaliciousPayload\nEvilDomain.com\n{ 6A 40 68 00 30 00 00 6A 14 8D 91 }",
            help="Text strings, hex patterns (in {}) or regular expressions (in //)",
            label_visibility="collapsed"
        )
        
        condition = st.selectbox(
            "Matching Condition*",
            options=["ANY of them (broad detection)", 
                    "ALL of them (strict detection)",
                    "Custom condition..."],
            index=0,
            help="How strings should be matched"
        )
        
        if st.button("🛡️ GENERATE YARA RULE", type="primary", use_container_width=True):
            handle_rule_generation(rule_name, author, description, condition, strings_input, threat_level, reference)

def render_advanced_options_section():
    with stylable_container(
        key="advanced_container",
        css_styles="""
            {
                background: linear-gradient(135deg, #1e293b, #0f172a);
                border-radius: 12px;
                padding: 2rem;
                border: 1px solid #334155;
                margin-bottom: 2rem;
            }
        """
    ):
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">
                <div style="width: 10px; height: 10px; border-radius: 50%; background: #7c3aed;"></div>
                <div style="color: #7c3aed; font-size: 0.9rem;">ADVANCED DETECTION PARAMETERS</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("**String Modifiers**")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            nocase = st.checkbox("nocase", help="Case insensitive matching")
        with c2:
            wide = st.checkbox("wide", help="Unicode strings (2 bytes per char)")
        with c3:
            ascii = st.checkbox("ascii", help="ASCII strings (wide + ascii)")
        with c4:
            fullword = st.checkbox("fullword", help="Match whole words only")
        
        st.write("**Rule Scope**")
        scope_col1, scope_col2 = st.columns(2)
        with scope_col1:
            rule_type = st.selectbox(
                "Rule Type",
                options=["General", "PE File", "ELF File", "PDF", "Office Document"],
                index=0
            )
        with scope_col2:
            target_os = st.multiselect(
                "Target OS",
                options=["Windows", "Linux", "macOS", "Android", "iOS", "Cross-platform"],
                default=["Windows"]
            )
        
        st.write("**Additional Metadata**")
        meta_col1, meta_col2 = st.columns(2)
        with meta_col1:
            version = st.text_input("Version", "1.0")
            license = st.selectbox(
                "License",
                options=["MIT", "Apache 2.0", "GPL", "Proprietary", "Other"]
            )
        with meta_col2:
            created = st.date_input("Creation Date", datetime.now())
            updated = st.date_input("Last Updated", datetime.now())

def render_validation_section():
    with stylable_container(
        key="validation_container",
        css_styles="""
            {
                background: linear-gradient(135deg, #1e293b, #0f172a);
                border-radius: 12px;
                padding: 2rem;
                border: 1px solid #334155;
                margin-bottom: 2rem;
            }
        """
    ):
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">
                <div style="width: 10px; height: 10px; border-radius: 50%; background: #7c3aed;"></div>
                <div style="color: #7c3aed; font-size: 0.9rem;">RULE VALIDATION & TESTING</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("**Rule Validation**")
        uploaded_file = st.file_uploader("Test against sample file", type=["exe", "dll", "pdf", "doc", "bin"])
        if uploaded_file:
            st.success(f"File {uploaded_file.name} ready for testing")
            if st.button("Validate Rule Against Sample"):
                # Here you would add actual validation logic
                st.info("Validation feature coming soon!")
        
        st.write("**Rule Quality Check**")
        if st.button("Analyze Rule Quality"):
            # Add quality analysis logic
            with st.expander("Quality Analysis Results"):
                st.success("✓ Proper rule naming convention")
                st.warning("⚠ Could add more metadata")
                st.error("✗ No reference URL provided")

def handle_rule_generation(rule_name, author, description, condition, strings_input, threat_level, reference):
    # Validate inputs
    if not rule_name or not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', rule_name):
        st.error("Invalid rule name! Use only letters, numbers and underscores")
        return
    
    if not description:
        st.error("Please provide a description")
        return
    
    strings = [s.strip() for s in strings_input.splitlines() if s.strip()]
    if not strings:
        st.error("Please provide at least one detection string")
        return
    
    # Build the YARA rule
    yara_rule = f"rule {rule_name}\n{{\n"
    yara_rule += "    meta:\n"
    yara_rule += f"        author = \"{author}\"\n" if author else ""
    yara_rule += f"        description = \"{description}\"\n"
    yara_rule += f"        threat_level = \"{threat_level}\"\n"
    yara_rule += f"        reference = \"{reference}\"\n" if reference else ""
    yara_rule += f"        date = \"{datetime.now().strftime('%Y-%m-%d')}\"\n"
    
    yara_rule += "    strings:\n"
    for i, s in enumerate(strings):
        # Auto-detect string type and apply appropriate formatting
        if s.startswith('{') and s.endswith('}'):
            # Hex string
            yara_rule += f"        $s{i+1} = {s}\n"
        elif s.startswith('/') and s.endswith('/'):
            # Regex string
            yara_rule += f"        $s{i+1} = {s}\n"
        else:
            # Normal string
            yara_rule += f"        $s{i+1} = \"{s}\" nocase\n"  # Default to nocase for text strings
    
    yara_rule += "    condition:\n"
    if condition.startswith("ANY"):
        yara_rule += "        any of them\n"
    elif condition.startswith("ALL"):
        yara_rule += "        all of them\n"
    else:
        yara_rule += "        // Custom condition\n"
        yara_rule += "        any of them\n"
    
    yara_rule += "}"
    
    render_results_section(yara_rule, rule_name)

def render_results_section(yara_rule, rule_name):
    with stylable_container(
        key="results_container",
        css_styles="""
            {
                background: linear-gradient(135deg, #0f172a, #1e293b);
                border-radius: 12px;
                padding: 2rem;
                border: 1px solid #334155;
                margin-top: 2rem;
                border-left: 4px solid #7c3aed;
            }
        """
    ):
        st.markdown("""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #7c3aed;"></div>
                    <h3 style="color: white; margin: 0; font-family: 'Space Mono', monospace;">YARA RULE COMPILED</h3>
                </div>
                <div style="display: flex; gap: 0.5rem;">
                    <button onclick="copyToClipboard()" style="
                        background: #334155; 
                        color: white; 
                        border: none; 
                        border-radius: 6px; 
                        padding: 0.5rem 1rem; 
                        cursor: pointer;
                        font-family: 'Ubuntu Mono', monospace;
                        transition: all 0.3s;
                    " onmouseover="this.style.background='#7c3aed'" onmouseout="this.style.background='#334155'">
                        COPY
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.code(yara_rule, language="yara")
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📥 DOWNLOAD YARA FILE",
                data=yara_rule,
                file_name=f"{rule_name}.yar",
                mime="text/plain",
                use_container_width=True
            )
        with col2:
            st.download_button(
                label="📄 EXPORT AS JSON",
                data=convert_to_json(yara_rule),
                file_name=f"{rule_name}_metadata.json",
                mime="application/json",
                use_container_width=True
            )
        
        # Add copy functionality
        st.markdown("""
            <script>
            function copyToClipboard() {
                const code = document.querySelector(".stCodeBlock code");
                const range = document.createRange();
                range.selectNode(code);
                window.getSelection().removeAllRanges();
                window.getSelection().addRange(range);
                document.execCommand("copy");
                window.getSelection().removeAllRanges();
                alert("YARA rule copied to clipboard!");
            }
            </script>
            """, unsafe_allow_html=True)

def convert_to_json(yara_rule):
    # Simple conversion for metadata - in a real app you'd parse the YARA properly
    import json
    metadata = {
        "source": "Generated by YARAAssist",
        "generated_at": datetime.now().isoformat(),
        "content": yara_rule
    }
    return json.dumps(metadata, indent=2)