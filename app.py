import streamlit as st
# # largest heading like h1
# st.title("Heart Disease Prediction")
# # larger heading 
# st.header("Patient Information")
# # large heading
# st.subheader("Enter the patient's details")
# # entering patient detail(taking input in num) Build-in validation of inputs
# # using min value and max value
# # this dont let users to enter above max and below min
# # we can display warning message for this using st.warning
# age = st.number_input("Enter Age",min_value=29,max_value=77)
# if age<29 or age>77:
#     st.warning("Please verify the entered values")
# # manual validation of inputs
# it accepts both integer and decimals 
# to have only integer specify it with value=0
# age = st.number_input("Enter Age",value=29)
# if age<29 or age>77:
#     st.error("Patient must be greater than 28 and less than 78")
# # arbitrary text(based on random choice rather than any logical system or reason)
# # here to enter gender,humans may type male Male MALE abc 123.now program has to handle all these possibilities
# # Gender = st.text_input("Enter Gender")
# # to overcome this we use selectbox.user can only choose given options
# # selectbox saves space and good when there are many options
# # sex = st.selectbox("Select Gender",["Female","Male"])
# # st.write("Selected: ",sex)
# # Radio button for choosing one option
# # radio shows all option immediatelu and good when there are only few options
# sex = st.radio("Select Gender",["Female","Male"])
# st.write("Selected: ",sex)
# # how to convert into numerics where model expects numerics
# # male is 1 and female is 0
# sex = 1 if sex == 'Male' else 0
# # button.It waits for a user to click it
# if st.button('Predict'):
#     st.write("Predicting....")
# # paragraph type 
# st.write("This application predicts whether a patient is likely to have heart disease")
import pandas as pd
import joblib
# import streamlit as st
model = joblib.load('heart_prediction.pkl')
st.markdown("<h1 style='text-align:center;'>Heart Disease Prediction</h1>",unsafe_allow_html=True) 
df = pd.read_csv("dataset/heart.csv")
x = df.drop('target',axis=1)
# print(x.columns)
# print(x.dtypes)
# print(df['thalach'].describe())
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