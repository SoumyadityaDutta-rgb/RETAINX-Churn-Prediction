import streamlit as st
import pandas as pd
import google.generativeai as genai

# ---------- GEMINI CONFIG ----------
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-pro")  # or gemini-1.5-pro

# ---------- STREAMLIT CONFIG ----------
st.set_page_config(page_title="RETAINX", page_icon="📊")
st.title("📊 RETAINX: Smart Churn Predictor & Advisor")

st.markdown("Upload your customer churn dataset and let RETAINX analyze it, predict churn for a user, and give actionable retention suggestions.")

# ---------- STEP 1: UPLOAD CSV ----------
uploaded_file = st.file_uploader("Upload your churn dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")
    st.dataframe(df.head())

    st.markdown("### Provide Customer Details")

    # ---------- STEP 2: FIXED INPUT OPTIONS ----------
    gender = st.selectbox("Gender (Male/Female)", ["Male", "Female"])
    senior = st.selectbox("SeniorCitizen (0 = No, 1 = Yes)", [0, 1])
    partner = st.selectbox("Partner (Yes/No)", ["Yes", "No"])
    dependents = st.selectbox("Dependents (Yes/No)", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", 0, 72, 8)
    phone = st.selectbox("PhoneService (Yes/No)", ["Yes", "No"])
    multiple = st.selectbox("MultipleLines (Yes/No/No phone service)", ["Yes", "No", "No phone service"])
    internet = st.selectbox("InternetService (DSL/Fiber optic/No)", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("OnlineSecurity (Yes/No/No internet service)", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("OnlineBackup (Yes/No/No internet service)", ["Yes", "No", "No internet service"])
    device_protect = st.selectbox("DeviceProtection (Yes/No/No internet service)", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("TechSupport (Yes/No/No internet service)", ["Yes", "No", "No internet service"])
    stream_tv = st.selectbox("StreamingTV (Yes/No/No internet service)", ["Yes", "No", "No internet service"])
    stream_movies = st.selectbox("StreamingMovies (Yes/No/No internet service)", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Contract (Month-to-month/One year/Two year)", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("PaperlessBilling (Yes/No)", ["Yes", "No"])
    payment = st.selectbox("PaymentMethod (Electronic check/Mailed check/Bank transfer/Credit card)", 
                           ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    monthly = st.number_input("MonthlyCharges (e.g. 75.35)", 0.0, 150.0, 67.0)
    total = st.number_input("TotalCharges (e.g. 3000.50)", 0.0, 10000.0, 5999.0)

    # ---------- STEP 3: COMPILE INPUT ----------
    user_data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protect,
        "TechSupport": tech_support,
        "StreamingTV": stream_tv,
        "StreamingMovies": stream_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    user_df = pd.DataFrame([user_data])
    st.write("#### 🧾 User Input Data")
    st.dataframe(user_df)

    # ---------- STEP 4: GEMINI ANALYSIS ----------
    if st.button("🔮 Predict Churn & Get Suggestions"):
        csv_preview = df.head(100).to_csv(index=False)

        prompt = f"""
        You are an expert telecom data analyst.
        Analyze the following churn dataset and the given customer details.
        Predict if the customer is likely to churn, and explain why.
        Then suggest 3 actionable business strategies to prevent churn.

        ### Dataset sample:
        {csv_preview}

        ### Customer details:
        {user_data}

        Respond with:
        1. Churn prediction (Yes/No)
        2. Confidence or reasoning
        3. 3 business retention suggestions (aligned with innovation and infrastructure ideas)
        """

        with st.spinner("Analyzing dataset and predicting..."):
            response = model.generate_content(prompt)

        st.markdown("### 🧠 Model Analysis")
        st.write(response.text)
