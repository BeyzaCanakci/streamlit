
import streamlit as st

st.set_page_config(
    page_title="Metagenomik Uygulama",
    page_icon="🧫",
    layout="wide"
)

st.title("Metagenomic Data Analysis Platform")
st.markdown("""
In this platform:
- 📊 **Discovery data analysis steps**
- 🧬 **You can visualize microbial diversity and abundance analysis**
- 🧠 **You can predict the disease with machine learning**



You can select pages from the menu on the left.
""")
from PIL import Image

image = Image.open("/streamlit/images/proje.webp")  # webp formatı destekleniyor
st.image(image, use_container_width=True)
