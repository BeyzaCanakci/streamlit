import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Keşifçi Veri Analizi", layout="wide")

@st.cache_data
def load_and_clean_data(file):
    df1 = pd.read_csv(file)

    df = pd.concat([df1.iloc[:, [0]], df1.iloc[:, [3]], df1.iloc[:, [4]], df1.iloc[:, [9]], df1.iloc[:, 211:]], axis=1)

    df = df[df['bodysite'] == 'stool']
    df = df[df['disease'] != '-']
    df = df[df['pubmedid'] != '-']
    df = df[df['dataset_name'] != "Candela_Africa"]
    df = df[df['disease'] != ' -']
    df = df[df['disease'] != 'n_relative']
    df['disease'] = df['disease'].replace('n', 'healthy')

    header_part = df.iloc[:, [2]]
    species_cols = [col for col in df.columns[2:] if 's__' in str(col)]
    species_data = df[species_cols]
    new_col_names = [c.split('|')[-1] if 's__' in c else c for c in species_data.columns]
    species_data.columns = new_col_names
    species_data = species_data.loc[:, ~species_data.columns.str.contains('t__')]

    final_df = pd.concat([header_part, species_data], axis=1).reset_index(drop=True)
    final_df = final_df[final_df['disease'] != 'underweight']
    final_df['disease'] = final_df['disease'].replace('obese', 'obesity')
    final_df['disease'] = final_df['disease'].replace('cancer', 'CRC')
    return final_df

def cat_summary(dataframe, col_name):
    summary_df = pd.DataFrame({
        col_name: dataframe[col_name].value_counts(),
        "Ratio (%)": 100 * dataframe[col_name].value_counts() / len(dataframe)
    })
    st.subheader(f"{col_name} /hastalık dağılımı")
    st.dataframe(summary_df)

def remove_all_zero_microbes(dataframe):
    st.subheader("Sadece 0 Değerine Sahip Mikroorganizmaların Temizlenmesi")
    microbe_cols = [col for col in dataframe.columns if col.startswith('s__')]
    microbe_data = dataframe[microbe_cols]
    all_zero_cols = microbe_data.columns[(microbe_data == 0).all()]
    
    st.markdown(f"**Tamamen sıfır olan mikrobiyal kolon sayısı:** {len(all_zero_cols)}")
    if len(all_zero_cols) > 0:
        with st.expander("Bu kolonlar hangileri?"):
            for col in all_zero_cols:
                st.markdown(f"- {col}")
    
    cleaned_df = dataframe.drop(columns=all_zero_cols)
    return cleaned_df

def grab_col_names(dataframe):
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    return num_cols, cat_cols

def target_summary_with_num(dataframe, target, numerical_col):
    return dataframe.groupby(target).agg({numerical_col: "mean"}).reset_index()

# ----------------- APP BAŞLANGICI -----------------
st.title("Mikrobiyal Veri Analizi")

uploaded_file = st.file_uploader("Verisetini yükleyin", type=["csv"])

if uploaded_file is not None:
    df = load_and_clean_data(uploaded_file)

    st.subheader("İşlenmiş Veri Önizlemesi")
    st.write(df.head())

    st.subheader("Veri Kümesi Bilgisi")
    st.write("Satır ve sütun sayısı:", df.shape)
    st.write("Veri türleri:")
    st.write(df.dtypes)

    cat_summary(df, "disease")

    st.subheader("Veri Kümesi Başlıkları")
    st.write(df.columns)

    st.subheader("Veri Kümesi İstatistikleri")
    st.write(df.describe())

    st.subheader("Veri Kümesi Kayıp Değerler")
    st.write(df.isnull().sum())

    # Temizleme
    df = remove_all_zero_microbes(df)

    st.subheader("Temizlenmiş Veri Kümesi")
    st.write(df.head())

    st.subheader("Temizlenmiş Veri Kümesi Bilgisi")
    st.write("Satır ve sütun sayısı:", df.shape)

    # Kolon türlerini al
    numeric_cols, categoric_cols = grab_col_names(df)

    st.subheader(" Mikroorganizmaların Hastalık Gruplarına Göre Ortalaması")
    selected_col = st.selectbox("Bir mikroorganizma seç:", numeric_cols)

    if selected_col:
        summary_df = target_summary_with_num(df, "disease", selected_col)
        st.write(f"`{selected_col}` kolonunun `hastalık` değişkenine göre ortalaması:")
        st.dataframe(summary_df)

        # Opsiyonel: Barplot
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=summary_df, x="disease", y=selected_col, ax=ax)
        ax.set_title(f"{selected_col} Ortalamaları (Hastalık Gruplarına Göre)")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(fig)



        st.subheader("Kategorik Değişkenlerin Dağılımı")
        for col in categoric_cols:
            fig, ax = plt.subplots(figsize=(10, 4))  # Gerekirse boyutu büyüt
            sns.countplot(data=df, x=col, ax=ax)
            ax.set_title(f"{col} dağılımı")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            plt.tight_layout()
            st.pyplot(fig)

