import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

# Title and description
st.title("❤️ Heart Disease Prediction App")
st.markdown("Enter the patient's details below to predict the likelihood of heart disease.")

# Input fields
st.header("Patient Data")

col1, col2 = st.columns(2)

with col1:
    # Age: Int
    age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
    
    # Sex: String (Male/Female) - Kept as requested
    sex = st.selectbox("Sex", ["Male", "Female"])
    
    # CP: Int (Check CSV: values like 1, 2, 3, 4)
    # User wanted "int form not like categorical", so using number_input
    cp = st.number_input("Chest Pain Type (1-4)", min_value=1, max_value=4, value=1, step=1)
    
    # Trestbps: Int
    trestbps = st.number_input("Resting Blood Pressure", min_value=0, value=120, step=1)
    
    # Chol: Int
    chol = st.number_input("Cholesterol", min_value=0, value=200, step=1)
    
    # FBS: Int (0 or 1)
    fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", min_value=0, max_value=1, value=0, step=1)
    
    # RestECG: Int (0, 1, 2)
    restecg = st.number_input("Resting ECG Results (0, 1, 2)", min_value=0, max_value=2, value=0, step=1)

with col2:
    # Thalach: Int
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, value=150, step=1)
    
    # Exang: Int (0 or 1)
    exang = st.number_input("Exercise Induced Angina (1=Yes, 0=No)", min_value=0, max_value=1, value=0, step=1)
    
    # Oldpeak: FLOAT (Check CSV: values like 2.3, 1.5)
    oldpeak = st.number_input("ST Depression (Oldpeak)", value=0.0, step=0.1, format="%.1f")
    
    # Slope: Int (1, 2, 3)
    slope = st.number_input("Slope of the Peak Exercise ST Segment (1-3)", min_value=1, max_value=3, value=1, step=1)
    
    # CA: Int (0-3)
    ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0, step=1)
    
    # Thal: Int (3, 6, 7)
    thal = st.number_input("Thalassemia (3=Normal, 6=Fixed, 7=Reversable)", value=3, step=1)


if st.button("Predict"):
    # Construct payload - sending explicit types as requested
    payload = {
        "age": int(age),
        "sex": sex, # Sends "Male" or "Female" string
        "cp": int(cp),
        "trestbps": int(trestbps),
        "chol": int(chol),
        "fbs": int(fbs),
        "restecg": int(restecg),
        "thalach": int(thalach),
        "exang": int(exang),
        "oldpeak": float(oldpeak),
        "slope": int(slope),
        "ca": int(ca),
        "thal": int(thal)
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if "error" in result:
                st.error(f"Backend Error: {result['error']}")
            else:
                prediction = result.get("Heart Disease Result")
                if prediction == "Presence":
                    st.error(f"Prediction: {prediction} of Heart Disease")
                else:
                    st.success(f"Prediction: {prediction} of Heart Disease")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")
