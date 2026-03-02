import streamlit as st
import time, sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from auth import register_user

st.set_page_config(page_title="Register", layout="centered")

# Light mixed gradient background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
    height:100vh;
}
.main > div {
    background: rgba(255,255,255,0.15);
    border-radius:25px;
    padding:3rem;
    backdrop-filter: blur(20px);
    max-width:500px;
    margin:auto;
    margin-top:5%;
}
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05);
    color:#333;
    border-radius:12px;
    border:1px solid rgba(255,255,255,0.2);
    padding:12px;
}
.stTextInput > div > div > input:focus {
    border:1px solid #9b59b6;
    box-shadow:0 0 10px #9b59b6;
}
.stButton > button {
    background: linear-gradient(90deg,#fbc2eb,#a6c1ee);
    color:white;
    border-radius:12px;
    height:50px;
    width:100%;
    font-weight:700;
    font-size:18px;
    transition:0.3s;
}
.stButton > button:hover {
    transform:scale(1.05);
    box-shadow:0 0 20px #fbc2eb,0 0 40px #a6c1ee;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:#333;'>📝 REGISTER</h1>", unsafe_allow_html=True)

username = st.text_input("👤 Username")
email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")
confirm_password = st.text_input("🔑 Confirm Password", type="password")

if st.button("Register"):
    if not username or not email or not password:
        st.warning("All fields required ❌")
    elif password != confirm_password:
        st.warning("Passwords do not match ❌")
    elif len(password) < 6:
        st.warning("Password must be at least 6 characters ❌")
    else:
        success = register_user(username,email,password)
        if success:
            st.success("Account Created Successfully 🎉")
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.error("Email already exists ❌")