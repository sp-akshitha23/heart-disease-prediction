import streamlit as st
import pandas as pd
import joblib
# import streamlit as st
model = joblib.load('heart_prediction.pkl')
st.markdown("<h1 style='text-align:center;'>Heart Disease Prediction</h1>",unsafe_allow_html=True) 
df = pd.read_csv("dataset/heart.csv")
x = df.drop('target',axis=1)
age = st.number_input("Enter Age",min_value=29,max_value=77)
sex = st.radio("Select Gender",['Female','Male'])
sex = 1 if sex == 'Male' else 0
cp = st.selectbox("Select Chest Pain Type",['Typical Angina','Atypical Angina','Non-anginal Pain','Asymptomatic'])
if cp == "Typical Angina":
    cp = 0
    st.warning("It is likely related to Heart Disease")
elif cp == 'Atypical Angina':
    cp = 1
elif cp == 'Non-anginal Pain':
    cp = 2
elif cp == 'Asymptomatic':
    cp = 3
trestbps = st.number_input("Enter Resting Blood Pressure",min_value=94,max_value=200)
chol = st.number_input("Enter cholesterol Levels",min_value=126,max_value=564)
if chol>=240:
    st.warning("High cholesterol")
fbs = st.number_input("Enter Fasting Blood Sugar:",value=0)
if fbs <= 120:
    fbs = 0
elif fbs > 120:
    fbs = 1
restecg = st.selectbox("Select Resting ECG(Electrocardiographic) Results",['Normal ECG','ST-T wave abnormality','Left ventricular hypertrophy'])
if restecg == 'Normal ECG':
    restecg = 0
elif restecg == 'ST-T wave abnormality':
    restecg = 1
else:
    restecg = 2
thalach = st.number_input("Enter Thalach",min_value=71,max_value=202)
exang = st.radio("Do patient has Exang(Exercise Induced Angina)",['No','Yes'])
exang = 0 if exang == 'No' else 1
oldpeak = st.number_input("Enter Oldpeak(ST depression)")
slope = st.selectbox("Select Slope",['Upsloping','Flat','Downsloping'])
if slope == 'Upsloping':
    slope = 0
elif slope == 'Flat':
    slope = 1
else:
    slope = 2
ca = st.selectbox("Number of Major vessels (CA)",[0,1,2,3,4])
# print(df['thal'].value_counts())
thal = st.selectbox("Select Thalassemia",['Normal','Fixed Defect','Reversible Defect','other'])
if thal == 'Normal':
    thal = 1
elif thal == 'Fixed Defect':
    thal = 2
elif thal == 'Reversible Defect':
    thal = 3
else:
    thal = 0
if st.button("Predict"):
    predict = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if predict == 0:
        st.markdown("<h1 style='text-align:center;'>No Heart Disease</h1>",unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align:center;'>You Have Heart Disease</h1>",unsafe_allow_html=True) 
        st.write("please consult doctor")  
