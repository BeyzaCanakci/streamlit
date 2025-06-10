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

## Folder Structure

```
streamlit/
├── streamlit_app.py         # Main entry point for the Streamlit app
├── pages/
│   ├── 1📊Exploratory_Data_Analysis.py
│   ├── 2Microbial_Analysis.py
│   └── 3Disease_Prediction_with_Model.py
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

