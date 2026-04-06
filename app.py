import streamlit as st
import re

# ─────────────────────────────────────────────
#  Customised CSS
# ─────────────────────────────────────────────

def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;600&display=swap');

    html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
    .stApp { background-color: #0f1117; color: #e8e8e8; }

    .header-block {
        background: linear-gradient(135deg, #1a1f2e 0%, #0f1117 100%);
        border: 1px solid #2a3040;
        border-left: 4px solid #f0a500;
        padding: 1.2rem 1.8rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }
    .header-block h1 {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.2rem;
        color: #f0a500;
        margin: 0 0 0.2rem 0;
    }
    .header-block p { color: #8898aa; font-size: 0.83rem; margin: 0; }

    .section-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.12em;
        color: #f0a500;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
        display: block;
    }
    .copy-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        color: #f0a500;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }
    .tip {
        background: #111827;
        border-radius: 6px;
        padding: 0.7rem 1rem;
        font-size: 0.78rem;
        color: #6b7890;
        font-family: 'IBM Plex Mono', monospace;
        margin-top: 0.8rem;
    }
    .stTextArea textarea {
        background: #1a1f2e !important;
        color: #e8e8e8 !important;
        border: 1px solid #2a3040 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.82rem !important;
        border-radius: 6px !important;
    }
    .stTextInput input {
        background: #1a1f2e !important;
        color: #e8e8e8 !important;
        border: 1px solid #2a3040 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.85rem !important;
        border-radius: 6px !important;
    }
    .stButton > button {
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.82rem !important;
        border-radius: 4px !important;
        background: #f0a500 !important;
        color: #0f1117 !important;
        border: none !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] { display: none; }
    hr { border-color: #1e2536 !important; }
    label { color: #aab4c8 !important; font-size: 0.8rem !important; }
    </style>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Text parser function
# ─────────────────────────────────────────────
def parse_text(text: str) -> dict:
    result = {}
    for field in FIELDS:
        base = re.escape(field).replace("s", "[sz]")
        pattern = rf"(?im)^\s*{base}\s*[:\-]\s*(.+)"
        match = re.search(pattern, text)
        result[field] = match.group(1).strip() if match else ""
    return result

def render_sheet_filler(title: str, subtitle: str, fields: list, namespace: str):
    """Main reusable UI component."""
    inject_custom_css()

    # Initialize session state keys
    for f in fields:
        key = f"field_{f}"
        if key not in st.session_state:
            st.session_state[f"field_{f}_{namespace}"] = ""

    # Header
    st.markdown(f"""
    <div class="header-block">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.1], gap="large")

    # Left: paste + parse
    with col_left:
        st.markdown('<span class="section-label">📧 Paste Customer Details</span>', unsafe_allow_html=True)
        user_text = st.text_area(
            label="email",
            label_visibility="collapsed",
            height=280,
            key=f"textarea_{namespace}"
        )

        if st.button("⚡ Parse Text", use_container_width=True, key=f"parse_{namespace}"):
            if user_text.strip():
                parsed = parse_text(user_text)
                for f in fields:
                    st.session_state[f"field_{f}_{namespace}"] = parsed.get(f, "")
            else:
                st.warning("Paste some text first.")

    # Right: editable fields
    with col_right:
        st.markdown('<span class="section-label">✏️ Edit & Copy</span>', unsafe_allow_html=True)
        for f in FIELDS:
            st.text_input(label=f, key=f"field_{f}_{namespace}")

    # Copy Row
    st.markdown("---")
    st.markdown('<span class="section-label">📋 Copy Row → Paste into Google Sheets</span>', unsafe_allow_html=True)

    tab_row    = "\t".join(st.session_state.get(f"field_{f}_{namespace}", "") for f in fields)
    header_row = "\t".join(fields)

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown('<div class="copy-label">Header row (paste on row 1 — once only)</div>', unsafe_allow_html=True)
        # 💡 UX UPGRADE: Changed to st.code for the auto-copy button!
        st.code(header_row, language="text")

    with c2:
        st.markdown('<div class="copy-label">Data row (click to copy)</div>', unsafe_allow_html=True)
        # 💡 UX UPGRADE: Changed to st.code for the auto-copy button!
        st.code(tab_row, language="text")

    st.markdown(
        '<div class="tip">💡 Hover over the box above and click the <b>Copy</b> icon in the top right → '
        'click the first empty cell in your Google Sheet → Ctrl+V. '
        'Each field lands in its own column automatically.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:#2a3040; font-family:IBM Plex Mono,monospace; font-size:0.68rem;'>"
        "Quick Entry — Sheet Filler · Internal Tool · No API Required"
        "</p>",
        unsafe_allow_html=True,
    )