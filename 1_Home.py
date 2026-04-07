import streamlit as st



st.set_page_config(
    page_title="Quick Entry — Sheet Filler",
    page_icon="🪪",
    initial_sidebar_state="expanded",
    layout="centered",
)

# 2. Centered Welcome Text
st.markdown("<h1 style='text-align: center;'>🪪 Welcome to Quick Entry — Sheet Filler</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8898aa;'>Data Parser Internal Tool</p>", unsafe_allow_html=True)

st.markdown("---")

# 3. Instructions
st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <h3>How to use this tool:</h3>
    <p>1. Look at the <b>Sidebar</b> on the left.</p>
    <p>2. Click on the specific form you need (e.g., <b>Commercial</b>, <b>HRO</b>).</p>
    <p>3. Paste your customer's information into the box to instantly format the data for Google Sheets.</p>
</div>
""", unsafe_allow_html=True)

# An eye-catching hint box
st.markdown("""
<div style="
    background-color: rgba(28, 131, 225, 0.1); 
    border: 1px solid rgba(28, 131, 225, 0.2);
    color: #83c9ff; 
    padding: 1rem; 
    border-radius: 0.5rem; 
    text-align: center; 
    margin-top: 1rem;">
    👈 <strong>Select a pipeline from the menu on the left to get started.</strong>
</div>
""", unsafe_allow_html=True)