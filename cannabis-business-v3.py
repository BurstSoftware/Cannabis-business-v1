import streamlit as st

st.set_page_config(page_title="Nicole's Garden", page_icon="🌱", layout="centered")

st.title("🌱 Nicole's Garden")

st.subheader("Premium Cannabis • Living Soil • Small Batch")

st.markdown("---")

st.success("**Currently Available**")

# Business Activities - Core Offerings
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌿 Strains We Grow")
    st.write("**Nicole Kush** — Indica-dominant flagship")
    st.write("**Lemon Haze Auto** — Fast sativa autoflower")

with col2:
    st.markdown("### 🧪 Soil Amendments & Tea")
    st.write("• Bloom Booster Compost Tea — $28/gal")
    st.write("• Super Soil Top-Dress Mix — $35/5lb")

st.markdown("---")

st.markdown("### 🌱 Clones For Sale")
st.write("**Nicole Kush Clones** — $25 each (min 4)")
st.write("**Lemon Haze Auto Clones** — $20 each (min 4)")

if st.button("Reserve Clones", type="primary", use_container_width=True):
    st.success("Thank you! We'll contact you soon.")

st.markdown("---")

st.markdown("### 🍫 Edibles (Coming Soon)")
st.write("Pursuing commissary license to sell:")
st.write("• Lemon Haze Gummies")
st.write("• Nicole Kush Chocolate Bars")
st.write("• Infused Honey & Tinctures")

email = st.text_input("Get notified when edibles launch", placeholder="your@email.com")
if st.button("Notify Me", type="primary", use_container_width=True):
    if email:
        st.balloons()
        st.success("You're on the list!")
    else:
        st.warning("Please enter an email.")

st.markdown("---")

st.caption("Woman-led • Regenerative Living Soil • Nicole's Garden © 2026")
st.caption("Always follow local cannabis laws")
