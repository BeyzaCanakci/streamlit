
import streamlit as st

st.set_page_config(
    page_title="Metagenomik Uygulama",
    page_icon="🧫",
    layout="wide"
)

st.title("Metagenomic Data Analysis Platform")
st.markdown("""
Bu platformda:
- 🧠 **You can predict the disease with machine learning**
- 🧬 **You can visualize microbial diversity and abundance analysis**
- 📊 **Discovery data analysis steps**

You can select pages from the menu on the left.
""")
from PIL import Image

image = Image.open("/Users/beyzacanakci/Desktop/miuul/proje/proje.webp")  # webp formatı destekleniyor
st.image(image, use_container_width=True)
