Heart Disease Prediction

A machine learning web application that predicts the possibility of heart disease based on patient health parameters.

Live Demo

"Click here to use the Heart Disease Prediction App" (https://heart-disease-prediction-cyrlc52khx6xmq3kfxjpso.streamlit.app/)

Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Joblib
- Streamlit

Project Features

- Data preprocessing and exploratory data analysis
- Machine learning model training and evaluation
- Saving the trained model using Joblib
- Interactive web application built with Streamlit
- Online deployment using Streamlit Community Cloud

Project Structure

heart-disease-prediction/
│
├── dataset/
│   └── heart.csv
├── app.py
├── heart.py
├── heart_prediction.pkl
├── requirements.txt
└── README.md

How to Run Locally

1. Clone the repository:
   
   "git clone https://github.com/sp-akshitha23/heart-disease-prediction.git"

2. Navigate to the project folder:
   
   "cd heart-disease-prediction"

3. Install the required libraries:
   
   "pip install -r requirements.txt"

4. Run the application:
   
   "python -m streamlit run app.py"

Disclaimer

This project is intended for educational purposes only. Its predictions are not a medical diagnosis or a substitute for professional medical advice.