import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import ttest_ind, mannwhitneyu
from statsmodels.stats.multitest import multipletests
from scipy.stats import mstats

def analyze_microbiome_disease(X_num, y_dis, disease, control_label="healthy", top_n=5):
    """
    Belirli bir hastalık için anlamlı mikroorganizmaları analiz eder ve görselleştirir.
    """

    # Adım 1: Verileri hazırlama (Log dönüşümü ve Winsorize)
    X_num_log = np.log1p(X_num)
    X_num_winsorized = X_num_log.apply(lambda col: mstats.winsorize(col, limits=[0.01, 0.01]))
    X_num_winsorized['disease'] = y_dis  

    # Adım 2: İstatistiksel testler
    disease_results = []
    for microbe in X_num_winsorized.columns:
        if microbe != "disease":
            healthy_group = X_num_winsorized[y_dis == control_label][microbe]
            disease_group = X_num_winsorized[y_dis == disease][microbe]

            if len(healthy_group) > 30 and len(disease_group) > 30:
                _, p_value = ttest_ind(healthy_group, disease_group)
            else:
                _, p_value = mannwhitneyu(healthy_group, disease_group)

            disease_results.append([microbe, p_value])

    # Adım 3: Çoklu karşılaştırma düzeltmesi
    disease_results_df = pd.DataFrame(disease_results, columns=["Microbe", "p_value"])
    disease_results_df["adjusted_p"] = multipletests(disease_results_df["p_value"], method="bonferroni")[1]

    # Adım 4: Anlamlı mikroorganizmaları bul
    significant_microbes = disease_results_df[disease_results_df["adjusted_p"] < 0.05]

    # Adım 5: En önemli mikroorganizmaları seç
    top_microbes = significant_microbes.sort_values(by="adjusted_p").head(top_n)

    # Adım 6: Görselleştirme
    if not top_microbes.empty:
        top_microbe_names = top_microbes["Microbe"].tolist()
        top_microbe_data = X_num_winsorized[top_microbe_names + ["disease"]]
        melted_data = pd.melt(top_microbe_data[top_microbe_data["disease"].isin([disease, control_label])],
                              id_vars=['disease'],
                              value_vars=top_microbe_names,
                              var_name='Microbe',
                              value_name='Abundance')

        plt.figure(figsize=(10, 6))
        sns.boxplot(data=melted_data, x="Microbe", y="Abundance", hue="disease", palette=["#FFCCE5", "#C1F8C1"])
        plt.xticks(rotation=45, ha="right")
        plt.title(f"Top {top_n} Significant Microbes for {disease} vs {control_label}")
        plt.tight_layout()
        st.pyplot(plt)  # Streamlit için görselleştirme

        return top_microbes
    else:
        st.error(f"No significant microbes found for {disease} vs {control_label}")
        return None

# Streamlit Uygulama
st.set_page_config(page_title="Mikrobiyom Hastalık Analizi", page_icon=":microscope:", layout="wide")
st.title("Microbiome Disease Analysis")
st.subheader("Hastalıkların biyobelirteç analizi")
st.markdown("Hasta örneklerinden elde edilen mikroorganizmaların analizini yapın ve hastalık ile sağlıklı grup arasındaki farkları inceleyin. Bu uygulama, mikroorganizmaların hastalıklarla ilişkisini anlamanıza yardımcı olacak ve hastalıkların biyobelirteçlerini analiz edebileceksiniz.")

# Verileri Yükleme
st.sidebar.header("Verilerinizi Yükleyin")
uploaded_file = st.sidebar.file_uploader("Hastalıklar içeren bir CSV dosyası yükleyin", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Kullanıcıdan hastalık ve kontrol grup seçimi
    disease = st.sidebar.selectbox("Hangi hastalığı analiz etmek istersiniz?", df['disease'].unique())
    control_label = "healthy"  # Sağlıklı grup sabit
    top_n = st.sidebar.slider("En önemli mikroorganizmaların sayısı", 1, 10, 5)

    # Verileri X_num ve y_dis olarak ayırma
    X_num = df.drop(columns=['disease'])
    y_dis = df['disease']
    
    # Hastalık için analiz yapma
    top_microbes_df = analyze_microbiome_disease(X_num, y_dis, disease, control_label, top_n)
    
    # Anlamlı mikroorganizmaları listele
    if top_microbes_df is not None:
        st.write("En anlamlı mikroorganizmalar:")
        st.dataframe(top_microbes_df)
