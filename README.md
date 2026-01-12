# Heart Disease Prediction System ❤️

This project is a full-stack machine learning application that predicts the presence of heart disease based on patient health metrics. It features a robust **FastAPI** backend for serving the model and a modern **Streamlit** frontend for an interactive user experience.

## 🚀 Features
- **Machine Learning Integration**: Powered by a trained Scikit-learn model.
- **FastAPI Backend**: High-performance API with automatic Swagger documentation.
- **Streamlit Frontend**: User-friendly web interface for inputting patient data and viewing results.
- **Dockerized**: Containerized for easy deployment and consistency across environments.
- **Strict Validation**: Pydantic models ensure data integrity for all inputs.

## 🛠️ Technology Stack
- **Languages**: Python 3.13
- **Backend Framework**: FastAPI
- **Frontend Framework**: Streamlit
- **ML Libraries**: Pandas, Scikit-learn, Pickle
- **Containerization**: Docker

## 📋 Prerequisites
- Python 3.10+
- Docker (optional, for containerized execution)

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd heart-disease-prediction
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Backend**:
   ```bash
   uvicorn backend:app --reload
   ```
   The API will be available at `http://localhost:8000`. You can access the documentation at `http://localhost:8000/docs`.

4. **Run the Frontend**:
   ```bash
   streamlit run frontend.py
   ```
   The UI will open in your default browser at `http://localhost:8501`.

## 🐳 Running with Docker

1. **Build the image**:
   ```bash
   docker build -t heart-disease-app .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 heart-disease-app
   ```

## 📊 Data Mapping
The model expects the following features:
- **Age**: Patient's age (Int)
- **Sex**: "Male" or "Female"
- **Chest pain type**: Typical Angina, Atypical Angina, Non-anginal Pain, Asymptomatic (Int 1-4)
- **BP**: Resting blood pressure (Int)
- **Cholesterol**: Serum cholesterol in mg/dl (Int)
- **FBS over 120**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **EKG results**: Resting electrocardiographic results (Int 0-2)
- **Max HR**: Maximum heart rate achieved (Int)
- **Exercise angina**: Exercise induced angina (1 = yes; 0 = no)
- **ST depression**: ST depression induced by exercise relative to rest (Float)
- **Slope of ST**: The slope of the peak exercise ST segment (Int 1-3)
- **Number of vessels fluro**: Number of major vessels (0-3) colored by fluoroscopy
- **Thallium**: (3 = normal; 6 = fixed defect; 7 = reversable defect)

---
Developed with ❤️ for health awareness.
