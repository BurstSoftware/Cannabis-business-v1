import streamlit as st

st.set_page_config(
    page_title="Nicole's Garden",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a nice cannabis/green theme
st.markdown("""
<style>
    .main { background-color: #0f1a0f; color: #e0f0e0; }
    h1, h2, h3 { color: #90ee90; }
    .stButton>button {
        background-color: #4ade80;
        color: #0f1a0f;
        font-weight: bold;
        border-radius: 8px;
    }
    .card {
        background-color: #1a2a1a;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🌱 Nicole's Garden")
st.subheader("Premium Cannabis • Living Soil • Small Batch")

st.markdown("---")

# Hero Section
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    **Woman-led regenerative cannabis collective**  
    Growing **Nicole Kush** & **Lemon Haze Auto** using living soil methods.  
    We make soil teas, sell clones, and are pursuing our commissary license for edibles.
    """)
with col2:
    st.success("**Now Available**\n\n• Clones\n• Soil Amendments")

st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🌿 Our Strains", "🧪 Amendments & Tea", "🌱 Clones", "🍫 Edibles (Soon)"])

with tab1:
    st.subheader("Signature Strains")
    c1, c2 = st.columns(2)
    
    with c1:
        st.image("https://picsum.photos/id/1015/600/400", use_container_width=True)
        st.markdown("**Nicole Kush**")
        st.caption("Indica-Dominant • Earthy, Chocolate, Pine • 22-26% THC")
        st.write("Our flagship strain. Dense buds, relaxing effects.")

    with c2:
        st.image("https://picsum.photos/id/201/600/400", use_container_width=True)
        st.markdown("**Lemon Haze Auto**")
        st.caption("Sativa-Dominant • Bright Lemon & Haze • 18-23% THC")
        st.write("Fast autoflower, great for daytime use.")

with tab2:
    st.subheader("Hand-Crafted Soil Amendments")
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("**Bloom Booster Tea**")
        st.write("Compost tea for flowering stage. Rich in microbes & phosphorus.")
        st.metric(label="", value="$28 / 1 gal")
    
    with c2:
        st.markdown("**Super Soil Top-Dress**")
        st.write("Organic blend: worm castings, kelp, neem & more.")
        st.metric(label="", value="$35 / 5 lb bag")

    st.info("All amendments are made in small batches using regenerative ingredients.")

with tab3:
    st.subheader("Clones For Sale")
    st.markdown("""
    **Nicole Kush Clones** — $25 each (minimum 4)  
    **Lemon Haze Auto Clones** — $20 each (minimum 4)
    """)
    
    if st.button("🛒 Reserve Clones Now", type="primary"):
        st.success("Thank you! We'll contact you soon with availability and pickup/delivery options.")

with tab4:
    st.subheader("Edibles — Commissary License In Progress")
    st.write("Coming soon: Gummies, Chocolate Bars, Infused Honey & Tinctures made with our own flower.")
    
    email = st.text_input("Email Address", placeholder="you@email.com")
    if st.button("Notify Me When Edibles Launch"):
        if email:
            st.balloons()
            st.success("You're on the list! We'll notify you when we launch.")
        else:
            st.warning("Please enter your email.")

st.markdown("---")

# Footer
st.markdown("""
**Nicole's Garden © 2026**  
Small-batch • Regenerative • Community Focused  

*Always comply with your local cannabis laws.*
""")

st.caption("Simplified & optimized for Streamlit Cloud")
