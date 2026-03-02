import streamlit as st
import time, sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from auth import login_user

st.set_page_config(page_title="Login", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #2193b0, #6dd5ed);
    height:100vh;
}
.main > div {
    background: rgba(255,255,255,0.1);
    padding:3rem;
    border-radius:20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    max-width:450px;
    margin:auto;
    margin-top:8%;
}
.stTextInput > div > div > input {
    background: rgba(0,0,0,0.2);
    color:white;
    border-radius:12px;
    padding:12px;
    border:1px solid rgba(255,255,255,0.2);
}
.stTextInput > div > div > input:focus {
    border:1px solid #00f2fe;
    box-shadow:0 0 10px #00f2fe;
}
.stButton > button {
    background: linear-gradient(90deg,#2193b0,#6dd5ed);
    color:white;
    border-radius:12px;
    height:50px;
    font-weight:bold;
    width:100%;
    font-size:18px;
    transition:0.3s;
}
.stButton > button:hover {
    transform:scale(1.05);
    box-shadow:0 0 20px #2193b0,0 0 40px #6dd5ed;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>🔐 LOGIN</h1>", unsafe_allow_html=True)

email = st.text_input("📧 Email")
username = st.text_input("👤 Username")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    user = login_user(email,password)
    if user:
        st.success(f"Login Successful 🎉 Welcome {user}")
        st.session_state.logged_in=True
        st.session_state.username=user
        time.sleep(1)
        st.experimental_rerun()
    else:
        st.error("Invalid credentials ❌")