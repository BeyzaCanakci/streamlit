import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Metagenomik Uygulama",
    page_icon=":computer:",
    layout="wide"
)

st.title(":computer: Makine Öğrenmesi ile Hastalık Tahmini")
st.subheader("Hasta örneklerindeki mikrobiyal bolluk değerleri ile hastalık tahmini gerçekleştirebilirsiniz")
st.markdown("""
Vücudumuzda trilyonlarca farklı mikroorganizmalar bulunmaktadır. Bunlar bakteri, virüs ve arkelerden oluşmaktadır. 
Bu canlılar bağırsaklarımız başta olmak üzere birçok yerde koloniler kurarak birlikte yaşamaktadırlar.
Bazı bakteriler iyi huylu iken bazıları kötü huyludur. Her hastalıkta kötü bakterilerin sayısı arttığı bilinir ama hangi hastalıkta hangi bakterilerin sayısı artar?

Bu uygulama, halen araştırılmakta olan bu alanda, bağırsak mikrobiyotasına odaklanarak olası hastalıkları tahmin etmeyi amaçlamaktadır. 
Kişilerin örneklerindeki mikroorganizmaların bolluk düzeylerine dayanarak, mikrobiyal çeşitlilik ile hastalıklar arasındaki ilişkileri analiz eder ve buna göre tahminlerde bulunur.
""")

# Cache'li model yükleme
@st.cache_resource
def load_model():
    return joblib.load("model/RF-Metagenomic-data-analysis.pkl")

model = load_model()

# Dosya yükleme
uploaded_file = st.file_uploader("Bir CSV dosyası yükle", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Disease' in df.columns:
        df = df.drop(columns=['Disease'])  # Etiket varsa çıkar

    st.write("Yüklenen veri:")
    st.write(df.head())

    # Model ile tahmin
    if st.button("Model ile tahmin et"):
        prediction = model.predict(df)
        st.write("🔍 Tahmin Sonuçları:")
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
        st.write("Kodlarının Karşılık Geldiği Hastalıklar:")
        st.table(label_df)

    # Feature importance gösterimi
    if st.button("Feature Importance'ı Göster"):
        try:
            importances = model.feature_importances_
        except AttributeError:
            st.warning("Model feature importance desteklemiyor!")
        else:
            # Modelin eğitildiği veri ile uyumlu feature'lar
            try:
                train_df = pd.read_csv("/Users/beyzacanakci/Desktop/miuul/proje/final_df.csv")
                X_train = train_df.drop(columns=["disease"])
                features = X_train.columns
            except Exception as e:
                st.error(f"Feature isimleri alınırken hata oluştu: {e}")
                features = [f"Feature {i}" for i in range(len(importances))]

            feature_imp = pd.DataFrame({
                'Feature': features,
                'Importance': importances
            }).sort_values(by='Importance', ascending=False)

            st.subheader("📊 Feature Importance Grafiği")
            fig, ax = plt.subplots(figsize=(10, 12))
            sns.barplot(data=feature_imp.head(20), x='Importance', y='Feature', ax=ax, palette='viridis')
            st.pyplot(fig)

            st.subheader("İlk 20 Özelliğin Önem değerleri")
            st.dataframe(feature_imp.head(20))
