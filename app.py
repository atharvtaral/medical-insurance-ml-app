import streamlit as st
import pandas as pd
import joblib

# ------------------ Page Config ------------------1
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)

# ------------------ Custom CSS ------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .title {
        font-size:40px !important;
        font-weight:700;
        color:#1f77b4;
        text-align:center;
    }
    .subtext {
        text-align:center;
        color:gray;
        font-size:18px;
    }
    .stButton>button {
        background-color:#1f77b4;
        color:white;
        font-size:18px;
        border-radius:10px;
        padding:10px 24px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown("<p class='title'>💰 Insurance Premium Predictor</p>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Enter your details to estimate insurance cost</p>", unsafe_allow_html=True)

st.write("")

# ------------------ Load Model ------------------
model = joblib.load("lasso_regression.joblib")

# ------------------ User Inputs ------------------
age = st.slider("Select Age", 18, 100, 25)
sex = st.selectbox("Select Gender", ["Male", "Female"])
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=15, value=0)
smoker = st.selectbox("Smoker?", ["Yes", "No"])

# ------------------ Encoding ------------------
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

# ------------------ Prediction ------------------
if st.button("Predict Insurance Premium"):
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💵 Estimated Insurance Premium: ₹ {round(prediction, 2)}")
