from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, Field, validator
import pickle
import pandas as pd

# Load model
try:
    with open("heart_disease_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None

app = FastAPI()

class HeartDisease(BaseModel):
    age: Annotated[int, Field(gt=0)]
    sex: str
    cp: Annotated[int, Field(description="Chest pain type of the patient")]
    trestbps: Annotated[int, Field(description="Resting blood pressure of the patient")]
    chol: Annotated[int, Field(description="Cholestrol of the patient")]
    fbs: Annotated[int, Field(description="Fasting blood sugar of the patient")] # removed gt=0 potentially if 0 is allowed
    restecg: Annotated[int, Field(description="Resting electrocardiographic results of the patient")]
    thalach: Annotated[int, Field(description="Maximum heart rate of the patient")]
    exang: Annotated[int, Field(description="Exercise-induced angina of the patient")]
    oldpeak: Annotated[float, Field(description="ST depression induced by exercise relative to rest of the patient")]
    slope: Annotated[int, Field(description="The slope of the peak exercise ST segment of the patient")]
    ca: Annotated[int, Field(description="Number of major vessels colored by fluoroscopy of the patient")]
    thal: Annotated[int, Field(description="Thalassemia of the patient")]

    @validator('sex')
    def encode_sex(cls, value):
        value = value.lower()
        if value == "male":
            return 1
        elif value == "female":
            return 0
        else:
            raise ValueError("sex must be 'Male' or 'Female'")

@app.post("/predict")
def predict_heart_disease(data: HeartDisease):
    if model is None:
        return {"error": "Model file not found"}


    
    df = pd.DataFrame({
        "Age": [data.age],
        "Sex": [data.sex], 
        "Chest pain type": [data.cp],
        "BP": [data.trestbps],
        "Cholesterol": [data.chol],
        "FBS over 120": [data.fbs],
        "EKG results": [data.restecg],
        "Max HR": [data.thalach],
        "Exercise angina": [data.exang],
        "ST depression": [data.oldpeak],
        "Slope of ST": [data.slope],
        "Number of vessels fluro": [data.ca],
        "Thallium": [data.thal]
    })
    
    
    df.index = [0]

    try:
        prediction = model.predict(df)[0]
        label_map = {0: "Absence", 1: "Presence"}
        result = label_map.get(prediction, str(prediction))
        
        return {"Heart Disease Result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return ["Heart Disease Prediction API"]


