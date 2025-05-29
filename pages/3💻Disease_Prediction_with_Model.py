import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Metagenomic Application",
    page_icon=":computer:",
    layout="wide"
)

st.title(":computer: Disease prediction with machine learning")
st.subheader("You can make disease prediction with microbial abundance values ​​in patient samples.")
st.markdown("""
There are trillions of different microorganisms in our bodies. They consist of bacteria, viruses and archaea.
These creatures live together by establishing colonies in many places, especially in our intestines.
Some bacteria are benign, while others are malignant. It is known that the number of bad bacteria increases in every disease, but which bacteria increase in which disease?

This application aims to predict possible diseases by focusing on the intestinal microbiota in this area, which is still under research.
It analyzes the relationships between microbial diversity and diseases based on the abundance levels of microorganisms in people's samples and makes predictions accordingly.
""")

# Cache'li model yükleme
@st.cache_resource
def load_model():
    return joblib.load("model/RF-Metagenomic-data-analysis.pkl")

model = load_model()

# Dosya yükleme
uploaded_file = st.file_uploader("Upload data without label", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Disease' in df.columns:
        df = df.drop(columns=['Disease'])  # Etiket varsa çıkar

    st.write("Uploaded data:")
    st.write(df.head())

    # Model ile tahmin
    if st.button("Predict with model"):
        prediction = model.predict(df)
        st.write("🔍 Prediction results:")
        st.write(prediction)

        # Label karşılıklarını göster
        label_map = {
            0: "Colorectal Cancer",
            1: "Cirrhosis",
            2: "Healthy",
            3: "Ulcerative Colitis",
            4: "Leaness",
            5: "Obesity",
            6: "Type 2 Diabetes"
        }

        label_df = pd.DataFrame(list(label_map.items()), columns=["Kod", "Hastalık"])
        st.write("Diseases That Codes Correspond To:")
        st.table(label_df)

    # Showing Feature importance 
    if st.button("Feature Importance"):
        try:
            importances = model.feature_importances_
        except AttributeError:
            st.warning("Model doesn't support the feature importance!")
        else:
            # Features compatible with the data on which the model was trained
            try:
                train_df = pd.read_csv(uploaded_file)
                X_train = train_df.drop(columns=["disease"])
                features = X_train.columns
            except Exception as e:
                st.error(f"Error with feature names: {e}")
                features = [f"Feature {i}" for i in range(len(importances))]

            feature_imp = pd.DataFrame({
                'Feature': features,
                'Importance': importances
            }).sort_values(by='Importance', ascending=False)

            st.subheader("📊 Feature Importance Graph")
            fig, ax = plt.subplots(figsize=(10, 12))
            sns.barplot(data=feature_imp.head(20), x='Importance', y='Feature', ax=ax, palette='viridis')
            st.pyplot(fig)

            st.subheader("First 20 features with feature importance")
            st.dataframe(feature_imp.head(20))
