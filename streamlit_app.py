import streamlit as st
import joblib


# Load trained models
heart_disease_model = joblib.load(open("heart_disease_model.pkl", "rb"))
diabetes_model = joblib.load(open("trained_model.sav", "rb"))
student_alcohol_model = joblib.load(open("student_alcohol_model.pkl", "rb"))


# Define prediction functions
def predict_heart_disease(input_data):
    prediction = heart_disease_model.predict([input_data])
    return "Heart Disease" if prediction[0] == 1 else "No Heart Disease"


def predict_diabetes(input_data):
    prediction = diabetes_model.predict([input_data])
    return "Diabetic" if prediction[0] == 1 else "Non-Diabetic"


def predict_alcohol_consumption(input_data):
    prediction = student_alcohol_model.predict([input_data])
    return "High Consumption" if prediction[0] == 1 else "Low Consumption"


# Streamlit app interface
st.title("Multiple Disease Prediction App")

# Sidebar for choosing disease model
option = st.sidebar.selectbox("Choose Prediction Model",
                              ("Heart Disease", "Diabetes", "Student Alcohol Consumption"))

# User input forms based on model selection
if option == "Heart Disease":
    st.header("Heart Disease Prediction")
    age = st.number_input("Age", min_value=0, max_value=120, value=62)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", options=[0, 1])
    cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=140)
    chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=268)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)", options=[0, 1])
    restecg = st.selectbox("Resting Electrocardiographic Results (0-2)", options=[0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=200, value=160)
    exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", options=[0, 1])
    oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=3.6)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0-3)", options=[0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (0-3)", options=[0, 1, 2, 3])

    inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    if st.button("Predict"):
        result = predict_heart_disease(inputs)
        st.write("Prediction:", result)

elif option == "Diabetes":
    st.header("Diabetes Prediction")
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

    inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    if st.button("Predict"):
        result = predict_diabetes(inputs)
        st.write("Prediction:", result)

elif option == "Student Alcohol Consumption":
    st.header("Student Alcohol Consumption Prediction")
    age = st.slider('Age', 15, 22, 18)
    studytime = st.slider('Study Time (hours/week)', 1, 4, 2)
    health = st.slider('Health Status (1 = worst, 5 = best)', 1, 5, 3)
    absences = st.number_input('Number of School Absences', min_value=0, value=2)
    G1 = st.number_input('Grade 1 (out of 20)', min_value=0, max_value=20, value=12)
    G2 = st.number_input('Grade 2 (out of 20)', min_value=0, max_value=20, value=14)
    G3 = st.number_input('Grade 3 (out of 20)', min_value=0, max_value=20, value=14)
    inputs = [age, studytime, health, absences, G1, G2, G3]

    if st.button("Predict"):
        result = predict_alcohol_consumption(inputs)
        st.write("Prediction:", result)

# Run `streamlit run app.py` in your terminal to launch the app
