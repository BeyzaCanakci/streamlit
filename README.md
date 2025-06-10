# streamlit

## 🚀 Start app

Click the link below to run the application directly:


🔗 (https://str-microbial-analysis.streamlit.app/) 


---

# Streamlit Data Analysis Projects

This repository contains interactive data analysis projects built with Streamlit. All applications are organized as separate Python files inside the pages directory and are loaded through the main entry point streamlit_app.py.

## Features

- Interactive dashboards using Streamlit  
- Exploratory Data Analysis (EDA) tools  
- Visualizations with Python libraries (e.g., Matplotlib, Seaborn, Plotly)  
- User-friendly interface for exploring and understanding data  
- Modular project structure: each analysis as a separate script under pages/
Here is an example of a README (in English) for the file 2🧬Microbial_Analysis.py in your repo:

---

# Microbial Analysis Projects

This Streamlit app page (`2🧬Microbial_Analysis.py`) provides an interactive interface to analyze and visualize significant differences in microbial abundance between disease and healthy groups using user-uploaded data.

### Features

- **Data Upload:** Users can upload their own CSV files containing microbial abundance data with a `disease` column.
- **Statistical Analysis:** The script applies statistical tests (t-test or Mann-Whitney U test, depending on group sizes) to identify microbes significantly associated with a selected disease.
- **Multiple Testing Correction:** Bonferroni correction is applied to control for false positives.
- **Visualization:** The most significant microbes are visualized via boxplots to compare distributions between disease and healthy groups.
- **Customizable:** Users can select the disease group to analyze and the number of top significant microbes to display.

### How to Use

1. **Upload Data:**
   - The data file should be in CSV format and contain a column named `disease` indicating group labels (e.g., "healthy", "disease1", "disease2", etc.).
   - All other columns should represent the abundance of different microbes.

2. **Configure Analysis:**
   - Select which disease group to compare against the "healthy" control.
   - Choose how many of the top significant microbes you want to visualize.

3. **Interpret Results:**
   - The app will display a boxplot of the top significant microbes and a table listing them with their adjusted p-values.

### Example Data Format

| microbe1 | microbe2 | ... | disease  |
|----------|----------|-----|----------|
| 0.1      | 2.3      | ... | healthy  |
| 0.5      | 1.8      | ... | disease1 |
| ...      | ...      | ... | ...      |

### Main Functionality

- **analyze_microbiome_disease:** Core function for statistical testing and visualization.
- **Streamlit Interface:** Provides user controls for data upload, group selection, and result display.

### Requirements

- Python libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `streamlit`, `scipy`, `statsmodels`

### Usage

Run this page as part of your Streamlit application:
```bash
streamlit run pages/2🧬Microbial_Analysis.py
```

---
Here’s a sample README file in English for the file 3💻Disease_Prediction_with_Model.py in your repository. You can copy and adapt this as README.md, or place it in the /pages directory if you prefer a per-page README.

---

# Disease Prediction with Model

This script, `3💻Disease_Prediction_with_Model.py`, is part of a Streamlit application for predicting diseases using a machine learning model. The app provides a user-friendly interface for entering symptoms and outputs the probable disease based on the trained model.

## Features

- User input interface for symptoms.
- Machine learning-based disease prediction.
- Clean and interactive Streamlit UI.
- Easy to use for both technical and non-technical users.

## Usage

1. **Requirements**  
   Make sure you have installed the required Python libraries:
   - streamlit
   - pandas
   - scikit-learn
   - numpy


3. **How it works**  
   - The user enters symptoms into the web app.
   - The model processes the input and predicts the most likely disease.
   - The result is displayed instantly within the Streamlit app.

## File Location

- `pages/3💻Disease_Prediction_with_Model.py`

## Customization

- You can update the model or symptoms list by editing the script.
- For more advanced features, integrate additional models or data sources as needed.


---


## Folder Structure

```
streamlit/
├── streamlit_app.py         # Main entry point for the Streamlit app
├── pages/
│   ├── 1📊Exploratory_Data_Analysis.py
│   ├── 2🧬Microbial_Analysis.py
│   └── 3💻Disease_Prediction_with_Model.py
├── README.md
└── ...
```

- Run streamlit_app.py to launch the Streamlit interface.
- Each file in the pages/ directory represents a different data analysis project.

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/BeyzaCanakci/streamlit.git
   cd streamlit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
   Use the sidebar to navigate between different projects located in the pages/ directory.

## Requirements

- Python 3.7+
- Streamlit
- Other libraries as listed in requirements.txt (e.g., pandas, matplotlib, seaborn, plotly, etc.)

## Usage

- After starting the app, select a project from the sidebar to view its dashboard.
- Use the provided widgets to filter and explore the data.
- Visualize various aspects of the data using plots and tables.

## License

This project is licensed under the MIT License.

---

