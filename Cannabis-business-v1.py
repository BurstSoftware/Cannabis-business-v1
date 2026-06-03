import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="Nicole's Garden | Cannabis & Living Soil",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0f1a0f; color: #e0f0e0; }
    .stButton>button { background-color: #4ade80; color: #0f1a0f; font-weight: bold; }
    .strain-card { background: #1a2a1a; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

st.title("🌱 Nicole's Garden")
st.subheader("Premium Cannabis • Regenerative Soil • Small Batch")

st.markdown("---")

col1, col2 = st.columns([3,2])
with col1:
    st.markdown("### Our Mission")
    st.write("""
    We grow **Nicole Kush** and **Lemon Haze Auto** using living soil methods. 
    We craft premium soil teas & amendments, sell healthy clones, and are pursuing our commissary license to offer artisanal edibles.
    """)

with col2:
    st.success("**Currently Available**\n\n• Nicole Kush Clones\n• Lemon Haze Auto Clones\n• Bloom Booster Tea\n• Super Soil Top-Dress")

st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Strains", "Amendments & Tea", "Clones", "Edibles (Soon)", "Shop"])

with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://picsum.photos/id/1015/800/500", caption="Nicole Kush")
        st.subheader("Nicole Kush")
        st.write("**Indica-Dominant** • Earthy, chocolate, pine • 22-26% THC")
    with col_b:
        st.image("https://picsum.photos/id/201/800/500", caption="Lemon Haze Auto")
        st.subheader("Lemon Haze Auto")
        st.write("**Sativa-Dominant** • Bright citrus & haze • 18-23% THC • Fast autoflower")

with tab2:
    st.subheader("Hand-Crafted Soil Amendments")
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Bloom Booster Tea", "$28 / gal", "Ships weekly")
    with c2:
        st.metric("Super Soil Top-Dress", "$35 / 5lb", "Organic blend")
    st.info("All products made with regenerative ingredients: worm castings, kelp, neem, crustacean meal, etc.")

with tab3:
    st.subheader("Clones For Sale")
    st.write("**Nicole Kush** — $25 each (min 4)")
    st.write("**Lemon Haze Auto** — $20 each (min 4)")
    if st.button("Reserve Clones"):
        st.success("Thank you! We'll contact you shortly for pickup/delivery details.")

with tab4:
    st.subheader("Commissary License In Progress")
    st.write("Coming soon: Lemon Haze Gummies, Nicole Kush Chocolate, Infused Honey & Tinctures")
    email = st.text_input("Get notified when edibles launch")
    if st.button("Sign Up"):
        st.balloons()
        st.success("You're on the list!")

with tab5:
    st.subheader("Shop Now")
    st.write("Pre-orders open for amendments and clones.")
    st.button("🛒 Go to Full Shop", type="primary")

st.markdown("---")
st.caption("Nicole's Garden © 2026 • Woman-led • Regenerative Cannabis Collective")
st.caption("Always follow your local laws and regulations.")
