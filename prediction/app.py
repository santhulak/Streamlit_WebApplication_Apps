import pandas as pd 
import streamlit as st 
import pickle


#Load the model
with open('model.pkl','rb') as pkl:
    classifier = pickle.load(pkl)

def main():
    style = """<div style='background-color: #12345F; padding:10px'>
                <h1 style ='color:white'><Center>Extra Marital Affair Prediction</h1>
                </div> """
    st.markdown(style,unsafe_allow_html=True)
    left,right = st.columns((2,2))
    rate_marriage = left.number_input('Marriage Rate', step = 1, value=0)
    age    = right.number_input('Age', step = 1, value=0)
    yrs_married = left.number_input('Years of Marriage', step = 1, value=0)
    children = right.number_input('No of Children', step = 1, value=0)
    religious       = left.number_input('Religious', step = 1, value=0)
    educ          = right.number_input('Education', step = 1, value=0)
    occupation = left.number_input('Occupation', step = 1, value=0)
    occupation_husb  = right.number_input('Occupation of Husband', step = 1, value=0)
    predict_button =st.button('Do Women have Extra Affair?')

    #When predict button is clicked
    if predict_button:

        res = classifier.predict([[rate_marriage,age,yrs_married,children,religious,educ,occupation,occupation_husb]])
        if res[0]==0:
            st.success("No, Women doesn't have Affair")
        else:
            st.success("Yes, Women have Affair")
  

if __name__ == '__main__':
    main()
