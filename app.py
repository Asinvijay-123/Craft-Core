import streamlit as st

# Page configuration
st.set_page_config(page_title="Craft Core", layout="centered")

# Custom CSS for styling
def add_custom_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #fff7f0;
            color: #222222;
            font-family: 'Segoe UI', sans-serif;
        }

        h1 {
            color: #b85c38;
            text-align: center;
            font-size: 3em;
            margin-bottom: 0.2em;
        }

        h2, h3 {
            color: #b85c38;
        }

        a {
            color: #d35400 !important;
            text-decoration: none;
            font-weight: bold;
        }

        .stMarkdown {
            font-size: 1.1rem;
        }

        hr {
            border: none;
            border-top: 2px solid #b85c38;
            margin-top: 1em;
            margin-bottom: 1em;
        }

        .custom-subtitle {
            text-align: center;
            font-size: 1.3em;
            font-weight: bold;
            color: #444;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_styles()

# Main Title
st.markdown("<h1>🎁 Craft Core</h1>", unsafe_allow_html=True)
st.markdown('<div class="custom-subtitle">Your one-stop destination for handmade gifts, customized crafts & creative hobby classes 🌸</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Order Form
# Order Form Section (Enhanced)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='
        background-color: #fff0e6;
        border: 2px solid #b85c38;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: Segoe UI, sans-serif;
    '>
        <h2 style='color: #b85c38;'>📝 Join Our Hobby Classes or Place an Order</h2>
        <p style='font-size: 1.2em; color: #333333; margin: 10px 0 20px 0;'>
            Whether you're looking to <strong>explore your creativity</strong> or buy <strong>unique handmade gifts</strong>, we've got you covered! 💝
        </p>
        <a href='https://docs.google.com/forms/d/e/1FAIpQLScFqvbWrNsXStg7Hor6_4M0r7XadxxbAMujl_7ErwEkSZZ7Jg/viewform?usp=sharing&ouid=111322587025743213802' target='_blank' style='
            display: inline-block;
            background-color: #000000;
            color: #ffffff;
            padding: 12px 24px;
            font-size: 1.1em;
            font-weight: bold;
            border-radius: 10px;
            text-decoration: none;
            transition: background-color 0.3s;
        ' onmouseover="this.style.backgroundColor='#333333'" onmouseout="this.style.backgroundColor='#000000'">
            👉 Fill Out the Form
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Product Gallery
st.header("✨ Our Handmade Collection (Available for Sale & Display)")
st.markdown("Enjoy our handcrafted designs, made with love and creativity:")

# Display only the two uploaded images
images = [
    ("lippon_art.jpg", "Mandala Mirror Art"),
    ("double_evil_eye.jpg", "Double Evil Eye Decor"),
    ("blue_art.jpg", "Mandala Blue Art"),
    ("butterfly.jpg", "Black & White Butterfly Sketch"),
    ("chocalate_gft_box.jpg", "Chocolate Gift Box"),
    ("peacock.jpg", "Intricate Peacock Art"),
    ("pen_stand.jpg", "Handmade Pen Stand"),
    ("pink_booket.jpg", "Pink Rose Bouquet"),
    ("texture_art.jpg", "DIY Texture Art"),
    ("tower.jpg", "Handmade Explosion Box"),
    ("Wall_hanging_khusi.jpg", "Personalized Name Tag"),
    ("kit_kat_box.jpg", "KitKat Chocolate Gift Box"),
    ("rose_booket.jpg", "Blue & Red Rose Bouquet")
]

# Show in rows of 2
for i in range(0, len(images), 2):
    col1, col2 = st.columns(2)
    img1, cap1 = images[i]
    with col1:
        st.image(img1, caption=cap1, use_container_width=True)
    if i + 1 < len(images):
        img2, cap2 = images[i + 1]
        with col2:
            st.image(img2, caption=cap2, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Contact Section
# Contact Section
st.markdown("<hr>", unsafe_allow_html=True)

# Centered and Bold "Contact Us" title
st.markdown(
    """
    <h2 style='text-align: center; font-weight: bold;'>📩 Contact Us</h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='
        background-color: #ffe8d6;
        border: 2px solid #b85c38;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        font-family: Segoe UI, sans-serif;
    '>
        <p style='font-size: 1.4em; font-weight: bold; color: #b85c38; margin-bottom: 10px;'>
            📞 Reach Us At:
        </p>
        <p style='font-size: 1.6em; font-weight: bold; color: #000000;'>
            <a href='tel:+919352659602' style='text-decoration: none; color: #000000;'>+91 93526 59602</a>
        </p>
        <p style='font-size: 1em; color: #444444; margin-top: 10px;'>
            Feel free to call us for <strong>bulk orders</strong>, <strong>customized crafts</strong>, or <strong>hobby class registrations</strong>!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
