import streamlit as st
import re

st.set_page_config(
    page_title="Quick Entry — Sheet Filler",
    page_icon="🪪",
    layout="wide",
)

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

FIELDS = [
    "Name",
    "Company",
    "Product type",
    "Quantity",
    "Location",
    "Timeline/Urgency",
    "Customisation",
]

def parse_email(text: str) -> dict:
    result = {}
    for field in FIELDS:
        # Case-insensitive match, also catches slight spelling variants (e.g. Customization vs Customisation)
        base = re.escape(field).replace("s", "[sz]")  # handle s/z variants
        pattern = rf"(?im)^\s*{base}\s*[:\-]\s*(.+)"
        match = re.search(pattern, text)
        result[field] = match.group(1).strip() if match else ""
    return result

# ── Initialise session state keys for all fields ───────────────────────────────
for f in FIELDS:
    if f"field_{f}" not in st.session_state:
        st.session_state[f"field_{f}"] = ""

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-block">
  <h1>🏭 ROTOSPEED — ROW BUILDER</h1>
  <p>Paste a customer reply → edit if needed → copy the whole row into Google Sheets.</p>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1.1], gap="large")

# ── Left: paste + parse ────────────────────────────────────────────────────────
with col_left:
    st.markdown('<span class="section-label">📧 Paste Customer Email</span>', unsafe_allow_html=True)
    email_text = st.text_area(
        label="email",
        label_visibility="collapsed",
        height=280,
        placeholder=(
            "Paste the customer reply here.\n\n"
            "Example:\n"
            "Name: Ahmad\n"
            "Company: ABC Sdn Bhd\n"
            "Product type: Water tank\n"
            "Quantity: 500\n"
            "Location: Selangor\n"
            "Timeline/Urgency: 6 weeks\n"
            "Customisation: Yes"
        ),
    )

    if st.button("⚡ Parse Email", use_container_width=True):
        if email_text.strip():
            parsed = parse_email(email_text)
            # ✅ Write directly into session_state keys — this is the fix
            for f in FIELDS:
                st.session_state[f"field_{f}"] = parsed.get(f, "")
        else:
            st.warning("Paste an email first.")

# ── Right: editable fields ─────────────────────────────────────────────────────
with col_right:
    st.markdown('<span class="section-label">✏️ Review & Edit Fields</span>', unsafe_allow_html=True)
    for f in FIELDS:
        st.text_input(label=f, key=f"field_{f}")

# ── Copy Row ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<span class="section-label">📋 Copy Row → Paste into Google Sheets</span>', unsafe_allow_html=True)

tab_row    = "\t".join(st.session_state.get(f"field_{f}", "") for f in FIELDS)
header_row = "\t".join(FIELDS)

c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown('<div class="copy-label">Header row (paste on row 1 — once only)</div>', unsafe_allow_html=True)
    st.text_area(label="headers", label_visibility="collapsed",
                 value=header_row, height=75)

with c2:
    st.markdown('<div class="copy-label">Data row (select all → Ctrl+C → paste into Sheet)</div>', unsafe_allow_html=True)
    st.text_area(label="data_row", label_visibility="collapsed",
                 value=tab_row, height=75)

st.markdown(
    '<div class="tip">💡 Click inside the <b>Data row</b> box → Ctrl+A → Ctrl+C → '
    'click the first empty cell in your Google Sheet → Ctrl+V. '
    'Each field lands in its own column automatically.</div>',
    unsafe_allow_html=True,
)

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#2a3040; font-family:IBM Plex Mono,monospace; font-size:0.68rem;'>"
    "Rotospeed Moulding · Internal Tool · No API Required"
    "</p>",
    unsafe_allow_html=True,
)