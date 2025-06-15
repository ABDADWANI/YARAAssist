import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container
from datetime import datetime
import re
import json
import yaml


def render_generate():
    render_header()
    render_documentation()

    tab1, tab2, tab3 = st.tabs(["Rule Construction", "Rule Analysis", "Threat Intelligence"])

    with tab1:
        render_rule_builder()

    with tab2:
        render_rule_analysis()

    with tab3:
        render_threat_loader()


def render_header():
    colored_header(
        label="YARA RULE LABORATORY",
        description="Professional Malware Detection Tool",
        color_name="violet-70"
    )


def render_documentation():
    with st.expander("Documentation", expanded=False):
        cols = st.columns(3)
        cols[0].markdown(render_doc_block("Basic Syntax", [
            "rule [name]", "meta:", "strings:", "condition:"]
        ), unsafe_allow_html=True)

        cols[1].markdown(render_doc_block("Pattern Types", [
            "Text: \"string\"", "Hex: { DE AD BE EF }", "Regex: /pattern/i"]
        ), unsafe_allow_html=True)

        cols[2].markdown(render_example_block(), unsafe_allow_html=True)


def render_doc_block(title, items):
    list_items = ''.join([f'<li><code>{item}</code></li>' for item in items])
    return f"""
        <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 12px;'>
            <span style='font-weight: 600;'>{title}</span>
        </div>
        <ul style='margin-top: 0; padding-left: 1.2rem;'>{list_items}</ul>
    """


def render_example_block():
    return """
        <div style='font-weight: 600; margin-bottom: 12px;'>Examples</div>
        <pre style='background: #1e293b; padding: 8px; border-radius: 4px; font-size: 0.85rem;'>
rule example {
    meta:
        author = "Analyst"
    strings:
        $text = "malware"
        $hex = { 01 02 03 }
    condition:
        any of them
}
        </pre>
    """


def render_rule_builder():
    with stylable_container(key="form_container", css_styles="""{
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid #334155;
        margin-bottom: 2rem;
        font-family: 'Ubuntu Mono', monospace;
        border-left: 4px solid #7c3aed;
    }"""):
        rule_name = st.text_input("Rule Identifier*", "malware_rule")
        col1, col2 = st.columns(2)
        author = col1.text_input("Author", placeholder="Analyst name")
        threat_level = col1.selectbox("Threat Severity", ["Low", "Medium", "High", "Critical"], index=2)
        description = col2.text_input("Description", placeholder="Detection purpose")
        reference = col2.text_input("Reference", placeholder="CVE or URL")

        pattern_type = st.radio("Signature Type:", ["Text String", "Hex Pattern", "Regular Expression"], horizontal=True)
        strings_input = st.text_area("Patterns (one per line)", height=150)

        c1, c2, c3, c4 = st.columns(4)
        modifiers = {
            'nocase': c1.checkbox("Case Insensitive"),
            'wide': c2.checkbox("Unicode"),
            'ascii': c3.checkbox("ASCII"),
            'fullword': c4.checkbox("Full Word")
        }

        condition = st.selectbox("Detection Logic", ["Any pattern matches (broad)", "All patterns match (strict)", "Custom condition..."], index=0)

        if st.button("Generate Detection Rule", use_container_width=True):
            generate_rule(rule_name, author, description, strings_input, condition, threat_level, reference, modifiers, pattern_type)


def generate_rule(name, author, desc, patterns, condition, level, ref, mods, ptype):
    if not name or not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
        st.error("Invalid rule name! Use only letters, numbers and underscores")
        return

    lines = [s.strip() for s in patterns.splitlines() if s.strip()]
    if not lines:
        st.error("Please provide at least one detection string")
        return

    rule = [f"rule {name} {{", "    meta:"]
    if author: rule.append(f"        author = \"{author}\"")
    if desc: rule.append(f"        description = \"{desc}\"")
    if ref: rule.append(f"        reference = \"{ref}\"")
    rule.append(f"        threat_level = \"{level}\"")
    rule.append(f"        date = \"{datetime.now().strftime('%Y-%m-%d')}\"")

    rule.append("    strings:")
    for i, val in enumerate(lines):
        ident = "$str" if "Text" in ptype else "$hex" if "Hex" in ptype else "$re"
        line = f"        {ident}{i+1} = {'\"'+val+'\"' if 'Text' in ptype else val}"
        mod_line = " ".join(k for k, v in mods.items() if v)
        if mod_line:
            line += f" {mod_line}"
        rule.append(line)

    rule.append("    condition:")
    rule.append("        any of them" if "any" in condition.lower() else "        all of them")
    rule.append("}")

    display_rule_output("\n".join(rule), name)


def display_rule_output(rule_text, rule_name):
    with stylable_container(key="results_container", css_styles="""{
        background: linear-gradient(135deg, #0f172a, #1e293b);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid #334155;
        margin-top: 2rem;
    }"""):
        st.code(rule_text, language="yara")
        col1, col2, col3 = st.columns(3)
        col1.download_button("Download .yar", rule_text, f"{rule_name}.yar", "text/plain")
        col2.download_button("Export as JSON", json.dumps({"rule": rule_text}), f"{rule_name}.json", "application/json")
        col3.download_button("Export as YAML", yaml.dump({"rule": rule_text}), f"{rule_name}.yaml", "text/yaml")


def render_rule_analysis():
    uploaded = st.file_uploader("Upload YARA rule for evaluation", type=[".yar", ".yara"])
    if uploaded:
        code = uploaded.read().decode()
        st.success("Rule uploaded successfully!")
        st.expander("View Rule").code(code, language="yara")
        run_static_analysis(code)


def run_static_analysis(code):
    info = {
        "Rule Name": re.search(r"rule\\s+([^\\s{]+)", code),
        "String Count": len(re.findall(r"\\$\\w+\\s*=", code)),
        "Condition Type": "any" if "any of them" in code else "all" if "all of them" in code else "custom",
        "Has Metadata": bool(re.search(r"meta:\\s*\\n", code))
    }
    for k, v in info.items():
        st.write(f"- **{k}:** {v.group(1) if hasattr(v, 'group') else v}")


def render_threat_loader():
    threats = {
        "Emotet": ["Emotet", "{ 8B 45 08 50 FF 15 }", "/emotet.*dll/i"],
        "Ryuk": ["Ryuk", "{ 55 8B EC 83 EC 20 }", "/\\.ryuk/i"],
        "Mirai": ["Mirai", "{ 68 00 00 00 00 68 00 00 00 00 }", "/botnet.*scan/i"],
        "WannaCry": ["WannaCry", "{ E8 00 00 00 00 59 83 F9 }", "/wncry.*\\.exe/i"]
    }

    choice = st.selectbox("Select malware family", list(threats.keys()) + ["Custom"])
    if choice != "Custom":
        st.session_state.strings_input = "\n".join(threats[choice])
        st.success(f"Loaded {choice} patterns! Switch to Rule Construction tab.")
