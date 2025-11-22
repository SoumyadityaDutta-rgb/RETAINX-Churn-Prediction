# 📊 RETAINX: Smart Churn Predictor & Advisor

**RETAINX** is an advanced analytics and prediction tool designed to help telecom companies reduce customer churn. By leveraging both traditional machine learning techniques and cutting-edge Large Language Models (LLMs), RETAINX not only predicts *who* will leave but also explains *why* and suggests *how* to keep them.

## 🚀 Features

- **🔮 Smart Churn Prediction**: Uses advanced algorithms and LLM reasoning to assess the likelihood of a customer leaving.
- **🧠 AI-Powered Insights**: Integrated with **Google Gemini Pro** to provide qualitative analysis and actionable business strategies tailored to specific customer profiles.
- **📊 Interactive Dashboard**: A user-friendly **Streamlit** web application for uploading datasets and testing individual customer scenarios.
- **📈 Comprehensive Data Analysis**: Includes a Jupyter Notebook (`RETAINX.ipynb`) for deep-dive Exploratory Data Analysis (EDA) and model training (XGBoost, CatBoost).
- **📉 Visual Analytics**: Includes a Power BI report (`datathon.pbix`) for business intelligence visualization.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Web Framework**: Streamlit
- **AI/LLM**: Google Gemini API (`gemini-2.5-pro` / `gemini-1.5-pro`)
- **Machine Learning**: XGBoost, CatBoost, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Power BI

## 📂 Project Structure

```
├── doc1.py                               # Main Streamlit application script
├── RETAINX.ipynb                         # Jupyter Notebook for EDA and Model Training
├── churn_model.pkl                       # Serialized Machine Learning Model
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Telco Customer Churn Dataset
├── datathon.pbix                         # Power BI Dashboard File
└── README.md                             # Project Documentation
```

## ⚡ Installation & Setup

1.  **Clone the repository**:
    ```bash
   git clone https://github.com/SoumyadityaDutta-rgb/RETAINX-Churn-Prediction.git
   cd RETAINX-Churn-Prediction

    ```

2.  **Install Dependencies**:
    Ensure you have Python installed. You can install the required libraries using pip:
    ```bash
    pip install streamlit pandas google-generativeai xgboost catboost scikit-learn matplotlib seaborn
    ```

3.  **Configure API Key**:
    - Open `doc1.py`.
    - Locate the line: `genai.configure(api_key="")`.
    - Insert your valid **Google Gemini API Key** inside the quotes.

## 🖥️ Usage

### Running the Web App
To launch the interactive prediction tool:

```bash
streamlit run doc1.py
```

1.  **Upload Dataset**: Upload the `WA_Fn-UseC_-Telco-Customer-Churn.csv` file to initialize the context.
2.  **Input Customer Details**: Use the sidebar/form to enter specific details about a customer (e.g., Tenure, Contract Type, Monthly Charges).
3.  **Get Predictions**: Click **"Predict Churn & Get Suggestions"**. The app will use Gemini to analyze the data and provide a churn probability along with 3 strategic retention suggestions.

### Exploring the Notebook
To view the data analysis and model training process:
1.  Open `RETAINX.ipynb` in Jupyter Notebook or Google Colab.
2.  Run the cells to see data visualization, preprocessing steps, and model performance metrics.

## 📊 Dataset
The project uses the **Telco Customer Churn** dataset, which includes information about:
-   **Customer Demographics**: Gender, Senior Citizen, Partner, Dependents.
-   **Services**: Phone, Internet, Online Security, Streaming, etc.
-   **Account Information**: Tenure, Contract, Payment Method, Monthly/Total Charges.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is open-source and available for educational and research purposes.


