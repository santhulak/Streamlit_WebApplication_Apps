import pandas as pd 
import streamlit as st 
import pickle


#Load the model
with open('model.pkl','rb') as pkl:
    classifier = pickle.load(pkl)
#classifier = pickle.load('model.pkl','rb')

def main():
    style = """<div style='background-color: #A74F3C; padding:10px'>
                <h1 style ='color:white'><Center>Heart Disease Prediction</h1>
                </div> """
    st.markdown(style,unsafe_allow_html=True)
    left,right = st.columns((2,2))
    Age = left.number_input('Enter Age in numbers ', step = 1, value=0)
    Sex     = right.selectbox('Choose Gender [0-male, 1-female]', (0,1))
    Chest_Pain = left.selectbox('Choose Number of times chest pain occurs', (0,1,2,3))
    Resting_Blood_Pressure = right.number_input('Enter Resting Blood Pressure', step = 1, value=0)
    Cholestoral       = left.number_input('Enter Cholestoral value', step = 1, value=0)
    Fasting_blood_sugar          = right.selectbox('Select Fasting blood sugar', (0,1))
    Resting_electrocardiographic = left.selectbox('Select Resting electrocardiographic',  (0,1,2))
    Max_heart_rate           = right.number_input('Enter Maximum Heart rate as whole numbers', step = 1, value=0)
    Exercise = left.selectbox('Choose whether you Exercise or not',(0,1))
    Old_peak           = right.number_input('Enter Old peak as decimal numbers', step = 1, value=0)
    Slope = left.selectbox('Choose the Slope' , (0,1,2))
    No_vessels           = right.selectbox('Select the no of vessels', (0,1,2,3,4))
    Thal = left.selectbox('Select Thal',(0,1,2,3))
    predict_button =st.button('Do I have Heart Disease ?')

    #When predict button is clicked
    if predict_button: 

        res = classifier.predict([[Age,Sex,Chest_Pain,Resting_Blood_Pressure,Cholestoral,Fasting_blood_sugar,Resting_electrocardiographic,Max_heart_rate,Exercise,Old_peak,Slope,No_vessels,Thal, ]])
        if res[0]==0:
            st.success("No, You do not have Heart Disease")
        else:
            st.success("Yes, You have Heart Disease")









if __name__ == '__main__':
    main()
