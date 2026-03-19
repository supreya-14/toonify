import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Toonify AI", layout="wide")

# ---------- SESSION STATE ----------
if "brightness" not in st.session_state:
    st.session_state.brightness = 1.0
if "contrast" not in st.session_state:
    st.session_state.contrast = 1.0
if "saturation" not in st.session_state:
    st.session_state.saturation = 1.0

# --------- NEW SESSION STATES FOR NAVIGATION ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "last_active" not in st.session_state:
    st.session_state.last_active = time.time()

# --------- SESSION TIMEOUT (10 min) ----------
if time.time() - st.session_state.last_active > 600:
    st.session_state.logged_in = False
    st.warning("⚠ Session expired. Please refresh the app.")
    st.stop()

st.session_state.last_active = time.time()

def reset_controls():
    st.session_state.brightness = 1.0
    st.session_state.contrast = 1.0
    st.session_state.saturation = 1.0

# ---------- SIDEBAR NAVIGATION ----------
st.sidebar.title("🎨 Toonify Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Dashboard", "Image Transform", "Logout"]
)

st.session_state.page = page

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#5f2c82,#6a11cb,#8e2de2);
color:white;
}

section[data-testid="stSidebar"]{
background: linear-gradient(180deg,#5f2c82,#6a11cb,#8e2de2);
color:white;
}

section[data-testid="stSidebar"] *{
color:white;
}

.welcome{
text-align:center;
font-size:34px;
font-weight:700;
color:#ffd6ff;
}

.subtext{
text-align:center;
font-size:18px;
max-width:900px;
margin:auto;
color:#f3d9ff;
line-height:1.6;
margin-bottom:20px;
}

.title{
font-size:70px;
font-weight:900;
text-align:center;
}

h2,h3{
color:#ffd6ff;
}

.feature-card{
background: linear-gradient(145deg,#7b2ff7,#9b4dff);
padding:30px;
border-radius:20px;
margin:10px;
box-shadow:0px 10px 20px rgba(0,0,0,0.3);
text-align:center;
}

.stRadio > div{
display:grid;
grid-template-columns:1fr 1fr;
gap:10px;
}

.stRadio label{
background:rgba(255,255,255,0.1);
padding:10px;
border-radius:10px;
text-align:center;
}

.upload-box{
background:rgba(255,255,255,0.08);
padding:60px;
border-radius:25px;
text-align:center;
border:1px solid rgba(255,255,255,0.2);
}

.stSlider > div > div > div > div{
background:linear-gradient(90deg,#7b2ff7,#9b4dff);
}

.stSlider [role="slider"]{
background:#ffffff;
border:3px solid #7b2ff7;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HOME PAGE
# ============================================================
if st.session_state.page == "Home":

    st.markdown("""
    <div class="welcome">
    🎨✨ Welcome to Toonify ✨🖼️
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtext">
    Turn your photos into stunning AI cartoon art with Toonify. Upload any image and instantly transform it into creative styles like cartoon, sketch, pop art, and vintage effects.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 class="title">
    📸➡️🎨 Turn your photos into stunning AI cartoon art ✨
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("## Powerful Features")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
        🎨 <h3>Multiple Art Styles</h3>
        Cartoon, pencil sketch, vintage and more.
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
        ⚡ <h3>Instant Processing</h3>
        Transform images instantly with AI.
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
        🎛 <h3>Quality Controls</h3>
        Adjust brightness, contrast and saturation.
        </div>
        """,unsafe_allow_html=True)

    c4,c5,c6 = st.columns(3)

    with c4:
        st.markdown("""
        <div class="feature-card">
        🤖 <h3>AI Powered Filters</h3>
        Advanced computer vision algorithms create artistic styles.
        </div>
        """,unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="feature-card">
        🖼 <h3>Side-by-Side Preview</h3>
        Compare original and styled images instantly.
        </div>
        """,unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div class="feature-card">
        ⬇ <h3>Easy Download</h3>
        Download your AI artwork instantly.
        </div>
        """,unsafe_allow_html=True)

    st.markdown("## 🖼 Example Cartoon Transformations")

    g1,g2,g3 = st.columns(3)

    with g1:
        st.image("https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d",caption="Original Photo",use_container_width=True)

    with g2:
        st.image("https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e",caption="Cartoon Style",use_container_width=True)

    with g3:
        st.image("https://images.unsplash.com/photo-1506794778202-cad84cf45f1d",caption="Vintage Effect",use_container_width=True)

    st.markdown("## 🚀 How Toonify Works")

    s1,s2,s3 = st.columns(3)

    with s1:
        st.markdown("### 1️⃣ Upload Image")
        st.write("Upload your image using the uploader.")

    with s2:
        st.markdown("### 2️⃣ Choose Style")
        st.write("Select artistic filters like cartoon, vintage or sketch.")

    with s3:
        st.markdown("### 3️⃣ Download")
        st.write("Download your AI generated cartoon instantly.")

# ============================================================
# DASHBOARD PAGE
# ============================================================
elif st.session_state.page == "Dashboard":

    st.title("📊 Dashboard")

    st.info("Welcome to Toonify Dashboard")

    col1,col2,col3 = st.columns(3)

    col1.metric("Images Processed", "120")
    col2.metric("Active Users", "25")
    col3.metric("Styles Available", "8")  # updated for 3 new filters

    st.success("System running normally 🚀")

    st.markdown("## 📈 Platform Analytics")

    a1,a2 = st.columns(2)

    with a1:
        st.bar_chart({
            "Cartoon":[50],
            "Sketch":[30],
            "Pop Art":[25],
            "Vintage":[15],
            "AI Anime":[20],
            "Watercolor":[18],
            "Comic Book":[22]
        })

    with a2:
        st.line_chart({
            "Images":[10,20,15,30,25,40,35]
        })

    st.markdown("## 🖼 Recent Transformations")

    r1,r2,r3 = st.columns(3)

    with r1:
        st.image("https://images.unsplash.com/photo-1544005313-94ddf0286df2")

    with r2:
        st.image("https://images.unsplash.com/photo-1500648767791-00dcc994a43e")

    with r3:
        st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330")

    st.markdown("## ℹ About Toonify")

    st.write("""
    Toonify AI converts normal photos into artistic cartoon styles using computer vision.
    Users can upload photos, apply filters, adjust quality, preview results and download artwork.
    """)

# ============================================================
# IMAGE TRANSFORM PAGE
# ============================================================
elif st.session_state.page == "Image Transform":

    left,right = st.columns([1,2])

    with left:

        st.subheader("🎨 Art Styles")

        style = st.radio(
            "",
            [
                "Cartoon",
                "Pencil Sketch (Color)",
                "Vintage",
                "Pop Art",
                "🤖 AI Anime Style",
                "🎨 Watercolor Painting",
                "🖌 Comic Book Effect"
            ]
        )

        st.subheader("🎛 Quality Controls")

        brightness = st.slider("Brightness",0.5,2.0,st.session_state.brightness,key="brightness")
        contrast = st.slider("Contrast",0.5,2.0,st.session_state.contrast,key="contrast")
        saturation = st.slider("Saturation",0.5,2.0,st.session_state.saturation,key="saturation")

        st.button("🔄 Reset Controls", on_click=reset_controls)

    with right:

        st.subheader("📤 Upload Your Photo")

        st.markdown("""
        <div class="upload-box">
        <h1>📤</h1>
        <h3>Drag & Drop Your Image</h3>
        <p>JPG • PNG • JPEG</p>
        </div>
        """,unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])

    if uploaded_file is not None:

        try:

            image = Image.open(uploaded_file).convert("RGB")

            image = ImageEnhance.Brightness(image).enhance(brightness)
            image = ImageEnhance.Contrast(image).enhance(contrast)
            image = ImageEnhance.Color(image).enhance(saturation)

            img = np.array(image)

            if style == "Cartoon":

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blur = cv2.medianBlur(gray,5)

                edges = cv2.adaptiveThreshold(
                    blur,255,
                    cv2.ADAPTIVE_THRESH_MEAN_C,
                    cv2.THRESH_BINARY,
                    9,9
                )

                color = cv2.bilateralFilter(img,9,300,300)
                output = cv2.bitwise_and(color,color,mask=edges)

            elif style == "Pencil Sketch (Color)":

                gray, color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
                output = color

            elif style == "Vintage":

                kernel = np.array([[0.272,0.534,0.131],
                                [0.349,0.686,0.168],
                                [0.393,0.769,0.189]])
                output = cv2.transform(img,kernel)

            elif style == "Pop Art":

                output = cv2.applyColorMap(img, cv2.COLORMAP_JET)

            elif style == "🤖 AI Anime Style":

                smooth = cv2.bilateralFilter(img,15,80,80)
                edges = cv2.Canny(smooth,100,200)
                edges = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
                output = cv2.addWeighted(smooth,0.9,edges,0.2,0)

            elif style == "🎨 Watercolor Painting":

                output = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

            elif style == "🖌 Comic Book Effect":

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray,80,150)
                edges = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
                color = cv2.bilateralFilter(img,9,200,200)
                output = cv2.bitwise_and(color,edges)

            col1,col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(image,use_container_width=True)

            with col2:
                st.subheader("Styled Image")
                st.image(output,use_container_width=True)

            result = cv2.imencode(".png", output)[1].tobytes()

            st.download_button(
                "⬇ Download Image",
                result,
                "toonify.png",
                "image/png"
            )

        except Exception as e:

            st.error("❌ Image processing failed.")
            st.warning("Possible reasons: corrupted image or unsupported format.")

# ============================================================
# LOGOUT PAGE
# ============================================================
elif st.session_state.page == "Logout":

    st.session_state.logged_in = False
    st.success("You have been logged out.")

    if st.button("Return to Home"):
        st.session_state.page = "Home"
