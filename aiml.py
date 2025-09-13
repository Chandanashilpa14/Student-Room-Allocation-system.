
import streamlit as st

# Page configuration
st.set_page_config(page_title="Student Room Allocator", page_icon="🏫", layout="centered")

# Add title and intro
st.markdown("<h1 style='text-align: center; color: white;'> Student Room Allocation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Please enter your details below to find your assigned exam room.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input fields in a form
with st.form("room_form", clear_on_submit=False):

    name = st.text_input("👤 Name")
    roll_no = st.number_input("🔢 Roll Number", min_value=1, step=1)

    submit = st.form_submit_button("Check Room")

# Logic (rule-based ) on form submission
if submit:
    if not name:
        st.warning("⚠️ Please enter your name.")
    else:
        if 1 <= roll_no <6:
            room = 10
            st.success(f"✅ Hello **{name}**, your roll number `{roll_no}` is assigned to **Room 10**.")
        elif 10 <= roll_no <50:
            room = 30
            st.success(f"✅ Hello **{name}**, your roll number `{roll_no}` is assigned to **Room 30**.")
        else:
            st.error(f"❌ Sorry **{name}**, your roll number `{roll_no}` does not have a room assigned.")
