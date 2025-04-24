
import streamlit as st

st.set_page_config(
    page_title="Metagenomik Uygulama",
    page_icon="🧫",
    layout="wide"
)

st.title("Metagenomik Analiz Platformu")
st.markdown("""
Bu platformda:
- 🧠 **Makine öğrenmesi ile hastalık tahmini** yapabilirsiniz
- 🧬 **Mikrobiyal çeşitlilik ve bolluk analizlerini** görselleştirebilirsiniz.
- 📊 **Keşifçi veri analizi adımlarını** gerçekleştirebilirsiniz.

Soldaki menüden sayfaları seçebilirsiniz.
""")
from PIL import Image

image = Image.open("/Users/beyzacanakci/Desktop/miuul/proje/proje.webp")  # webp formatı destekleniyor
st.image(image, use_container_width=True)
