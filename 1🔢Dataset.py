import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", layout="wide")

@st.cache_data
def load_and_clean_data(file):
    df1 = pd.read_csv(file)
    return df1

st.title("Verisetinin ilk hali")

uploaded_file = st.file_uploader("Verisetini yükleyin", type=["csv"])

if uploaded_file is not None:
    df1 = load_and_clean_data(uploaded_file)

    st.subheader("İşlenmemiş Veri Önizlemesi")
    st.write(df1)