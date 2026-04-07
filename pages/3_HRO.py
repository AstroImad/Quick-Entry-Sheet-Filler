import streamlit as st
from core_logic import render_sheet_filler

st.set_page_config(
    page_title="HRO — Sheet Filler", 
    page_icon="🪪", 
    initial_sidebar_state="expanded",
    layout="wide")

st.markdown("HRO Data")

HRO_FILEDS = [
    "Name",
    "Company",
    "Product type",
    "Quantity",
    "Location",
    "Timeline/Urgency",
    "Customisation",
]

render_sheet_filler(
    title="Quick Entry: HRO Form",
    subtitle="Paste a customer reply → edit if needed → copy the whole row into Google Sheets.",
    fields=HRO_FILEDS,
    namespace="HRO" # UNIQUE NAMESPACE
)