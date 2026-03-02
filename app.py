import streamlit as st

st.set_page_config(page_title="Toonify App", layout="centered")

# ---------- ANIMATED BACKGROUND ----------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #141e30, #243b55, #0f2027, #2c5364);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.block-container {
    padding-top: 2rem;
}

/* Glass Card */
.main-card {
    max-width: 700px;
    margin: auto;
    margin-top: 40px;
    padding: 35px;
    border-radius: 15px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    color: white;
}

h1, h2, h3 {
    text-align: center;
    color: white;
}

.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    border: none;
}

.stButton>button:hover {
    background-color: #1e40af;
}

</style>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------- SIDEBAR ----------
menu = ["Home", "Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# -------- HOME PAGE --------
if choice == "Home":

    st.title("🎨 Welcome to Toonify App")

    st.write("""
    Toonify App is an AI-powered image transformation platform 
    that converts normal photos into cartoon-style artworks.
    """)

    st.divider()

    # Section 1
    st.header("🎨 AI Cartoon Transformation")
    st.image("https://images.unsplash.com/photo-1611605698335-8b1569810432", use_container_width=True)
    st.write("Transform normal photos into creative cartoon versions using AI filters.")

    st.divider()

    # Section 2
    st.header("🚀 Modern & Clean Interface")
    st.image("https://images.unsplash.com/photo-1558655146-d09347e92766", use_container_width=True)
    st.write("Professional UI with smooth navigation and user-friendly design.")

    st.divider()

    # Section 3
    st.header("🔐 Secure Authentication")
    st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3", use_container_width=True)
    st.write("Session-based login system ensures user privacy and safety.")

    st.divider()

    # Section 4
    st.header("🖼 Easy Image Upload")
    st.image("https://images.unsplash.com/photo-1581090700227-4c4f50d86f6f", use_container_width=True)
    st.write("Upload JPG or PNG images easily and preview instantly.")

    st.success("👉 Use the sidebar to Login or Register and start your creative journey!")

# -------- REGISTER --------
elif choice == "Register":

    st.title("Create Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password == confirm_password and name != "":
            st.success("Registration Successful!")
        else:
            st.error("Passwords do not match")

# -------- LOGIN --------
elif choice == "Login":

    if not st.session_state.logged_in:

        st.title("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username and password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Enter username and password")

    else:
        st.success(f"Welcome, {st.session_state.username} 👋")

        st.subheader("Upload Your Image")

        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            st.image(uploaded_file, use_container_width=True)
            st.success("Image uploaded successfully!")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)