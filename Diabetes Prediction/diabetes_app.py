import pandas as pd 
import streamlit as st 
import pickle


#Load the model
with open('model.pkl','rb') as pkl:
    classifier = pickle.load(pkl)

def main():
    style = """<div style='background-color: #12345F; padding:10px'>
                <h1 style ='color:white'><Center>Diabetes Prediction</h1>
                </div> """
    st.markdown(style,unsafe_allow_html=True)
    left,right = st.columns((2,2))
    Pregnancies = left.number_input('Enter Preganancies as whole numbers', step = 1, value=0)
    Glucose     = right.number_input('Enter Glucose as whole numbers', step = 1, value=0)
    BloodPressure = left.number_input('Enter Blood Pressure as whole numbers', step = 1, value=0)
    SkinThickness = right.number_input('Enter Skin Thickness as whole numbers', step = 1, value=0)
    Insulin       = left.number_input('Enter Insulin as whole numbers', step = 1, value=0)
    BMI           = right.number_input('Enter BMI as decimal numbers', step = 1, value=0)
    DiabetesPedigreeFunction = left.number_input('Enter  DiabetesPedigreeFunction as decimal numbers', step = 1, value=0)
    Age  = right.number_input('Enter Age as whole numbers', step = 1, value=0)
    predict_button =st.button('Am I Diabetic ?')

    #When predict button is clicked
    if predict_button:

        res = classifier.predict([[Pregnancies,Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if res[0]==0:
            st.success("You are not Diabetic")
        else:
            st.success("You are Diabetic")
    









if __name__ == '__main__':
    main()
